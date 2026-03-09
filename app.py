"""Bookmarks — AI-organized Twitter bookmark dashboard."""

import json
import html as html_lib
import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

from ai_search import cached_ai_search, remaining_searches, get_api_key, MAX_AI_SEARCHES

# ── Config ────────────────────────────────────────────────────────────────────

DATA_DIR = Path(__file__).parent / "data"

st.set_page_config(
    page_title="Bookmarks",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Data loading ──────────────────────────────────────────────────────────────


@st.cache_data
def load_bookmarks() -> list[dict]:
    with open(DATA_DIR / "bookmarks.json") as f:
        return json.load(f)


@st.cache_data
def load_project_plans() -> str:
    return (DATA_DIR / "project_plans.md").read_text()


# ── Helpers ───────────────────────────────────────────────────────────────────


def relative_time(iso_str: str) -> str:
    """Convert ISO timestamp to relative time string."""
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        delta = datetime.now(timezone.utc) - dt
        days = delta.days
        if days < 1:
            return "today"
        if days == 1:
            return "yesterday"
        if days < 7:
            return f"{days}d ago"
        if days < 30:
            return f"{days // 7}w ago"
        if days < 365:
            return f"{days // 30}mo ago"
        return f"{days // 365}y ago"
    except Exception:
        return ""


def text_filter(bookmarks: list[dict], query: str) -> list[dict]:
    """Case-insensitive substring match across text, author, categories."""
    q = query.lower()
    return [
        b for b in bookmarks
        if q in b.get("text", "").lower()
        or q in b.get("authorHandle", "").lower()
        or q in b.get("authorName", "").lower()
        or any(q in c.get("name", "").lower() for c in b.get("categories", []))
    ]


def category_filter(bookmarks: list[dict], slugs: set[str]) -> list[dict]:
    if not slugs:
        return bookmarks
    return [
        b for b in bookmarks
        if any(c.get("slug") in slugs for c in b.get("categories", []))
    ]


def media_filter(bookmarks: list[dict], mode: str) -> list[dict]:
    if mode == "All":
        return bookmarks
    if mode == "With media":
        return [b for b in bookmarks if b.get("mediaItems")]
    return [b for b in bookmarks if not b.get("mediaItems")]


def sort_bookmarks(bookmarks: list[dict], order: str) -> list[dict]:
    reverse = order == "Newest"
    return sorted(
        bookmarks,
        key=lambda b: b.get("tweetCreatedAt", "") or "",
        reverse=reverse,
    )


def bookmarks_to_csv(bookmarks: list[dict]) -> str:
    rows = []
    for b in bookmarks:
        rows.append({
            "tweetId": b.get("tweetId", ""),
            "text": b.get("text", ""),
            "author": b.get("authorHandle", ""),
            "categories": "; ".join(c["name"] for c in b.get("categories", [])),
            "date": b.get("tweetCreatedAt", ""),
            "media": "; ".join(m["url"] for m in b.get("mediaItems", [])),
            "url": f"https://x.com/i/status/{b.get('tweetId', '')}",
        })
    return pd.DataFrame(rows).to_csv(index=False)


def get_all_categories(bookmarks: list[dict]) -> list[dict]:
    """Extract unique categories with counts, sorted by count desc."""
    counts: Counter = Counter()
    cat_info: dict = {}
    for b in bookmarks:
        for c in b.get("categories", []):
            slug = c.get("slug", "")
            counts[slug] += 1
            if slug not in cat_info:
                cat_info[slug] = {"name": c["name"], "slug": slug, "color": c.get("color", "#64748b")}
    return [
        {**cat_info[slug], "count": count}
        for slug, count in counts.most_common()
    ]


# ── Styling ───────────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

.stApp { background-color: #101010; }

.brand {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600; font-size: 1.2rem;
    letter-spacing: 0.08em; color: #c8c8c8;
    margin-bottom: 0.1rem;
}
.brand-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem; color: #6b6b6b;
    margin-bottom: 1rem;
}

.bookmark-card {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    padding: 1rem 1.15rem;
    margin-bottom: 0.7rem;
    transition: background 0.15s;
}
.bookmark-card:hover { background: #222222; }

.bookmark-text {
    color: #d4d4d4;
    font-size: 0.88rem;
    line-height: 1.65;
    white-space: pre-wrap;
    word-break: break-word;
}

.bookmark-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem; color: #6b6b6b;
    margin-top: 0.5rem;
}
.bookmark-meta a { color: #9a9a9a; text-decoration: none; }
.bookmark-meta a:hover { text-decoration: underline; color: #b0b0b0; }

.cat-badge {
    display: inline-block;
    padding: 2px 9px;
    border-radius: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    margin-right: 4px;
    margin-top: 0.45rem;
}

.ai-counter {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
}

.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem; color: #6b6b6b;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.ai-match-reason {
    background: #1e1e1e;
    border-left: 3px solid #7a7a7a;
    padding: 0.6rem 1rem;
    margin-bottom: 0.8rem;
    font-size: 0.82rem;
    color: #9a9a9a;
    border-radius: 0 6px 6px 0;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── Render bookmark card ──────────────────────────────────────────────────────


def render_card(b: dict):
    """Render a single bookmark as an HTML card + optional image."""
    text = b.get("text", "")
    truncated = text[:300] + ("..." if len(text) > 300 else "")
    safe_text = html_lib.escape(truncated)

    badges = ""
    for c in b.get("categories", []):
        color = c.get("color", "#64748b")
        badges += (
            f'<span class="cat-badge" '
            f'style="background:{color}22; color:{color};">'
            f'{html_lib.escape(c["name"])}</span>'
        )

    rel = relative_time(b.get("tweetCreatedAt", ""))
    handle = html_lib.escape(b.get("authorHandle", "unknown"))
    tweet_url = f"https://x.com/i/status/{b.get('tweetId', '')}"

    card_html = f"""<div class="bookmark-card">
<div class="bookmark-text">{safe_text}</div>
<div>{badges}</div>
<div class="bookmark-meta">
@{handle} &middot; {rel} &middot;
<a href="{tweet_url}" target="_blank">View on X ↗</a>
</div>
</div>"""

    media_items = b.get("mediaItems", [])
    photos = [m for m in media_items if m.get("type") == "photo"]

    if photos:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(card_html, unsafe_allow_html=True)
        with col2:
            try:
                st.image(photos[0]["url"], use_container_width=True)
            except Exception:
                st.markdown("🖼️", unsafe_allow_html=True)
    else:
        st.markdown(card_html, unsafe_allow_html=True)


# ── Load data ─────────────────────────────────────────────────────────────────

all_bookmarks = load_bookmarks()
project_plans = load_project_plans()
all_categories = get_all_categories(all_bookmarks)

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown('<div class="brand">BOOKMARKS</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="brand-sub">{len(all_bookmarks)} tweets &middot; '
        f'{len(all_categories)} categories</div>',
        unsafe_allow_html=True,
    )

    # Free-text search
    search_query = st.text_input(
        "Search", placeholder="Filter bookmarks...", label_visibility="collapsed"
    )

    # AI Search
    st.markdown("---")
    has_key = get_api_key() is not None
    remaining = remaining_searches(st.session_state)

    if has_key:
        ai_query = st.text_input(
            "AI Search", placeholder="Semantic search with Haiku...", key="ai_input"
        )
        ai_clicked = st.button("🔍 Search with AI", use_container_width=True, disabled=remaining <= 0)
        color = "#6b6b6b" if remaining > 5 else ("#999999" if remaining > 0 else "#b0b0b0")
        st.markdown(
            f'<div class="ai-counter" style="color:{color};">'
            f'{remaining}/{MAX_AI_SEARCHES} AI searches remaining</div>',
            unsafe_allow_html=True,
        )
    else:
        st.info("Add `ANTHROPIC_API_KEY` to Streamlit secrets for AI search.")
        ai_query = ""
        ai_clicked = False

    # Categories
    st.markdown("---")
    st.markdown('<div class="stat-label">Categories</div>', unsafe_allow_html=True)
    selected_slugs: set[str] = set()
    for cat in all_categories:
        if st.checkbox(
            f"{cat['name']} ({cat['count']})",
            value=True,
            key=f"cat_{cat['slug']}",
        ):
            selected_slugs.add(cat["slug"])

    # Media filter
    st.markdown("---")
    media_mode = st.radio("Media", ["All", "With media", "Text only"], horizontal=True)

    # Sort
    sort_order = st.radio("Sort", ["Newest", "Oldest"], horizontal=True)

    # Export
    st.markdown("---")


# ── Apply filters ─────────────────────────────────────────────────────────────

filtered = all_bookmarks

# AI search takes priority if activated
ai_result = None
if has_key and ai_clicked and ai_query and ai_query.strip():
    ai_result = cached_ai_search(ai_query.strip(), all_bookmarks, st.session_state)

if ai_result and ai_result.get("matches"):
    match_ids = set(ai_result["matches"])
    filtered = [b for b in all_bookmarks if b.get("tweetId") in match_ids]
else:
    if search_query:
        filtered = text_filter(filtered, search_query)
    filtered = category_filter(filtered, selected_slugs)
    filtered = media_filter(filtered, media_mode)

filtered = sort_bookmarks(filtered, sort_order)

# CSV download (in sidebar, after filters applied)
with st.sidebar:
    csv_data = bookmarks_to_csv(filtered)
    st.download_button(
        "📥 Download CSV",
        csv_data,
        "bookmarks_export.csv",
        "text/csv",
        use_container_width=True,
    )

# ── Tabs ──────────────────────────────────────────────────────────────────────

tab_bookmarks, tab_plans, tab_stats = st.tabs(["📑 Bookmarks", "🗂️ Project Plans", "📊 Stats"])

# ── Tab 1: Bookmarks ─────────────────────────────────────────────────────────

with tab_bookmarks:
    if ai_result and ai_result.get("reason"):
        st.markdown(
            f'<div class="ai-match-reason">🤖 {html_lib.escape(ai_result["reason"])}</div>',
            unsafe_allow_html=True,
        )

    st.caption(f"Showing {len(filtered)} of {len(all_bookmarks)} bookmarks")

    if not filtered:
        st.info("No bookmarks match your filters.")
    else:
        for b in filtered:
            render_card(b)

# ── Tab 2: Project Plans ─────────────────────────────────────────────────────

with tab_plans:
    st.markdown(project_plans)

# ── Tab 3: Stats ──────────────────────────────────────────────────────────────

with tab_stats:
    total = len(all_bookmarks)
    with_media = sum(1 for b in all_bookmarks if b.get("mediaItems"))
    num_cats = len(all_categories)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Bookmarks", total)
    c2.metric("Categories", num_cats)
    c3.metric("With Media", with_media)
    c4.metric("Text Only", total - with_media)

    st.markdown("---")
    st.subheader("Category Distribution")

    cat_df = pd.DataFrame([
        {"Category": c["name"], "Count": c["count"], "Color": c["color"]}
        for c in all_categories
    ])
    if not cat_df.empty:
        st.bar_chart(cat_df.set_index("Category")["Count"], horizontal=True, color="#8a8a8a")

    st.markdown("---")
    st.subheader("Timeline")
    dates = []
    for b in all_bookmarks:
        ts = b.get("tweetCreatedAt", "")
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                dates.append(dt.date())
            except Exception:
                pass
    if dates:
        date_counts = Counter(dates)
        timeline_df = pd.DataFrame(
            [{"Date": d, "Bookmarks": c} for d, c in sorted(date_counts.items())]
        )
        st.bar_chart(timeline_df.set_index("Date"), color="#8a8a8a")
