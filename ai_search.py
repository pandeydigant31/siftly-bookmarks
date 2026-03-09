"""Claude Haiku semantic search for bookmarks. Capped at 20 calls/session."""

import json
import os
import time

CACHE_TTL_SECONDS = 300  # 5 minutes
MAX_AI_SEARCHES = 20
MODEL = "claude-haiku-4-5-20251001"

SEARCH_PROMPT = """You are a bookmark search assistant. Given a user's query and a list of Twitter bookmarks, return the tweetIds of bookmarks that best match semantically.

Return ONLY valid JSON: {"matches": ["tweetId1", "tweetId2", ...], "reason": "one sentence explaining your selection"}
If nothing matches, return {"matches": [], "reason": "No matching bookmarks found."}
Return at most 10 matches, ordered by relevance."""


def get_api_key() -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    try:
        import streamlit as st
        key = st.secrets.get("ANTHROPIC_API_KEY")
        if key:
            os.environ["ANTHROPIC_API_KEY"] = key
            return key
    except Exception:
        pass
    return None


def _raw_search(query: str, bookmarks: list[dict]) -> dict:
    """Call Claude Haiku with the full bookmark corpus."""
    import anthropic

    digest = "\n".join(
        f"- [{b['tweetId']}] {b['text'][:200]} "
        f"(categories: {', '.join(c['name'] for c in b.get('categories', []))})"
        for b in bookmarks
    )

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system=SEARCH_PROMPT,
        messages=[{"role": "user", "content": f"Query: {query}\n\nBookmarks:\n{digest}"}],
    )

    raw = resp.content[0].text.strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(raw)


def cached_ai_search(query: str, bookmarks: list[dict], session_state: dict) -> dict | None:
    """AI search with session caching and rate limiting.

    Returns {"matches": [...], "reason": str} or None if limit reached / no key.
    """
    if "ai_cache" not in session_state:
        session_state["ai_cache"] = {}
    if "ai_search_count" not in session_state:
        session_state["ai_search_count"] = 0

    cache = session_state["ai_cache"]
    now = time.time()
    cache_key = query.lower().strip()

    # Check cache
    if cache_key in cache:
        entry = cache[cache_key]
        if now - entry["ts"] < CACHE_TTL_SECONDS:
            return entry["result"]

    # Check rate limit
    if session_state["ai_search_count"] >= MAX_AI_SEARCHES:
        return None

    # Check API key
    if not get_api_key():
        return None

    result = _raw_search(query, bookmarks)

    cache[cache_key] = {"result": result, "ts": now}
    session_state["ai_search_count"] += 1

    return result


def remaining_searches(session_state: dict) -> int:
    return MAX_AI_SEARCHES - session_state.get("ai_search_count", 0)
