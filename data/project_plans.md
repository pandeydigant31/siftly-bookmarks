# Project Plans from Twitter Bookmarks
## Generated from AI Analysis | March 9, 2026

Based on your 25 Twitter/X bookmarks (14 AI & ML, 9 Dev Tools, 3 Business, 2 Design), here are actionable projects distilled from what you've been saving.

---

## Project 1: Build Your Own AI Agent Framework (from Scratch)

**Source bookmarks:**
- "For people who keep asking what to build in AI Engineering > Build your own Reasoner, Agent loop, Inference Server, Transformer..."
- "New research on agent memory — real agents interact with databases, code executors, and web interfaces"
- "Wolfram Foundation Tool for LLM systems — inject reliable computation into any AI or agent system"

**What to build:**
A modular AI agent framework with these components built from first principles:
1. **Chain-of-Thought Reasoner** — implement structured thinking with step-by-step reasoning
2. **ReAct Agent Loop** — observation/thought/action cycle that connects to real tools
3. **Agent Memory System** — based on the research paper, build trajectory-based memory (not chatbot-style) that stores structured interactions with tools, databases, and code executors
4. **Wolfram Tool Integration** — connect Wolfram's Foundation Tool API for reliable computation

**Why this is worth doing:**
You already have the CSH2 domain-specific LLM project (csh2-llm). This agent framework could become the backbone for your Phase 3+ work — a tool-augmented inference loop that uses your 10 domain tools (CoolProp, Sensor Lookup, Pump Calculator, etc.).

**Effort:** 2-3 weekends
**Stack:** Python, your existing Qwen3-4B setup, Wolfram API (free tier)
**First step:** Implement a minimal ReAct loop that can call CoolProp and your sensor lookup tool

---

## Project 2: RAG Pipeline for Your Own Data

**Source bookmarks:**
- "AI can now build RAG pipelines like Google Brain's retrieval research team (for free) — 12 Claude prompts"
- "Anthropic dropped 12 FREE courses that teach you how to build with Claude — ship tool-using agents, build full RAG pipelines"

**What to build:**
A personal RAG (Retrieval-Augmented Generation) pipeline that indexes your own data sources:
1. **Document ingestion** — index your CSH2 analysis docs, physics reference, sensor tag maps
2. **Embedding + vector store** — use local embeddings (no API cost) with ChromaDB or FAISS
3. **Retrieval chain** — semantic search + reranking over your knowledge base
4. **Query interface** — natural language queries like "what's the diagnostic signature for DCV leak?"

**Why this is worth doing:**
Your murphy_feb18 directory has extensive docs (tag_map.md, analysis_protocol.md, physics_reference.md, calibration results). A RAG pipeline would let you query all of this conversationally, and it directly feeds into the csh2-llm project's tool-augmented architecture.

**Effort:** 1-2 weekends (basic pipeline), ongoing refinement
**Stack:** Python, ChromaDB/FAISS, sentence-transformers, Claude API
**First step:** Follow the Anthropic free courses to build a minimal RAG pipeline, then point it at your murphy_feb18/docs/ directory

---

## Project 3: "Vibe Coding" Workflow System with Claude Code Skills

**Source bookmarks:**
- "How I created the frontend slides skill — get Claude Code to create a website, iterate, then turn the workflow into a skill"
- "Beginner vs not-so-beginner vibe coder — setup personal [tooling/workflow]"
- "Most powerful vibe coding prompt — ship SEO websites, Claude apps, personal dashboards in <5 minutes"
- "10x your vibecoded frontends by learning what UI components are called"
- "Claude Code Remote Control now available to all Pro users"

**What to build:**
A personal Claude Code skill library that encodes your best workflows:
1. **CSH2 Analysis Skill** — a skill that automates your standard Murphy analysis workflow (query BigFive sensors, generate time-series plots, run diagnostics D1-D8)
2. **Frontend Dashboard Skill** — encode the "good slides/dashboard" criteria and UI component vocabulary into a reusable skill
3. **Remote Code Review Skill** — use Claude Code's /remote-control feature to review and iterate on code from any device
4. **Data Pipeline Skill** — automate your common data workflows (CSV export, CoolProp validation, sensor data quality checks)

**Why this is worth doing:**
You already use Claude Code extensively. Encoding your best workflows as skills means you stop re-explaining context every session. The "beginner vs advanced vibe coder" distinction is exactly this — setup personal tooling that compounds.

**Effort:** 1 weekend per skill
**Stack:** Claude Code skills (Markdown-based), your existing codebase
**First step:** Take your most common Murphy analysis workflow and turn it into a Claude Code skill file

---

## Project 4: AI Eval Framework (Career Investment)

**Source bookmarks:**
- "Interviewing for AI PM roles — the ability to define eval dimensions, build test datasets, write eval criteria, and set blocking thresholds separates you"
- "Socratic prompting technique — output quality went from 3/10 to 9.5/10"

**What to build:**
A portable AI evaluation framework you can showcase:
1. **Eval dimensions library** — reusable scoring rubrics for different AI tasks (accuracy, helpfulness, safety, format compliance)
2. **Test dataset generator** — tools to create balanced, representative test sets
3. **Scoring pipeline** — automated evaluation with human-in-the-loop review
4. **Blocking threshold system** — define quality gates that prevent bad outputs from shipping

**Why this is worth doing:**
You've already built benchmark scoring infrastructure for csh2-llm (283 benchmark questions, score_benchmark.py, expert subset selection). Package this as a general-purpose eval framework and you have a portfolio piece for AI PM/engineering roles at frontier labs.

**Effort:** 2 weekends to generalize your existing csh2-llm eval code
**Stack:** Python, your existing score_benchmark.py as foundation
**First step:** Abstract your csh2-llm scoring pipeline into a domain-agnostic eval framework, apply it to a second domain as proof

---

## Project 5: Personal Knowledge Dashboard

**Source bookmarks:**
- "Silicon Valley reading list — what texts shaped tech leaders' thinking"
- Multiple article bookmarks (7 x.com/i/article links you saved but haven't read)
- Your existing Situation Monitor / Briefing App

**What to build:**
Extend your existing Situation Monitor into a full personal knowledge dashboard:
1. **Twitter bookmark integration** — pipe categorized bookmark data into your briefing app
2. **Article queue** — those 7 article bookmarks you saved as bare URLs need a read-later + summarization pipeline
3. **Reading list tracker** — track books/articles from the SV reading list tweet, with progress and notes
4. **Cross-source synthesis** — combine RSS feeds (your existing 40 feeds) + Twitter bookmarks + saved articles into a unified knowledge stream

**Why this is worth doing:**
You already have the Situation Monitor (situation_monitor_v0.1/briefing) with RSS scraping, Claude scoring, and Streamlit deployment. Adding Twitter bookmarks as another input source is incremental work that dramatically increases the value of the system.

**Effort:** 1 weekend (bookmark integration), 2-3 weekends (full dashboard)
**Stack:** Python, Streamlit, your existing briefing pipeline
**First step:** Write a script that feeds categorized bookmarks into your briefing.db

---

## Quick Wins (< 1 hour each)

| # | Action | Source Bookmark |
|---|--------|----------------|
| 1 | Try Socratic prompting technique on your next Claude session | "Socratic prompting — 3/10 to 9.5/10" |
| 2 | Set up Claude Code /remote-control for mobile access | "Remote Control now available to Pro users" |
| 3 | Learn proper UI component names for better vibe coding | "10x frontends by learning component names" |
| 4 | Run through Anthropic's 12 free courses | "12 FREE courses — build with Claude" |
| 5 | Try the "most powerful vibe coding prompt" on a side project | "Ship anything in <5 minutes" |

---

## Priority Matrix

| Project | Impact | Effort | Synergy with Existing Work | Recommended Order |
|---------|--------|--------|---------------------------|-------------------|
| P3: Claude Code Skills | High | Low | Direct (daily workflow) | **Start here** |
| P2: RAG Pipeline | High | Medium | Direct (csh2-llm, murphy_feb18) | **Second** |
| P1: Agent Framework | Very High | High | Direct (csh2-llm tools) | **Third** |
| P4: Eval Framework | High | Medium | Direct (csh2-llm scoring) | **Fourth** |
| P5: Knowledge Dashboard | Medium | Medium | Direct (briefing app) | **Fifth** |

---

*Generated from 25 Twitter/X bookmarks analyzed by Claude AI*
