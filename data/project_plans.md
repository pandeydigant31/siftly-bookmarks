# Project Plans from Twitter Bookmarks
## Generated from AI Analysis | March 16, 2026

Based on your 103 Twitter/X bookmarks (58 AI & ML, 28 Dev Tools, 14 Startups & Business, 10 Science & Research, 5 Design & Product, 5 Productivity, 3 Health & Wellness, 3 Security & Privacy), here are actionable projects distilled from what you've been saving.

---

## Project 1: Multi-Agent Orchestration Framework

**Source bookmarks:**
- "Introducing autocontext: a recursive self-improving harness designed to help your agents succeed on any task" (@JayScambler)
- "autoresearch@home: Any agent on the internet can join and collaborate on AI/ML research" (@christinetyip)
- "Droids can now pursue goals autonomously over multi-day horizons... We call these Missions" (@FactoryAI)
- "Meet Hermes Agent, the open source agent that grows with you... multi-level memory system and persistent dedicated machine access" (@NousResearch)
- "New research on agent memory... real agents interact with databases, code executors, and web interfaces, generating machine-readable trajectories" (unknown)
- "Base44 just dropped Superagent: persistent memory, scheduled jobs, event triggers, browser sessions" (@cgtwts)

**What to build:**
A multi-agent orchestration system that goes beyond a single ReAct loop into coordinated agent teams:
1. **Agent Registry** -- define agent roles (Hunter, Skeptic, Referee -- inspired by the bug-finding trio from @danpeguine) with typed capabilities
2. **Trajectory-Based Memory** -- implement the research insight that agent memory should store machine-readable trajectories, not chatbot-style dialogue
3. **Multi-Day Mission Planner** -- like Factory's Droids, support long-horizon tasks where you approve a plan and come back to finished work
4. **Recursive Self-Improvement Loop** -- port autocontext's pattern: agents generate context files that make future iterations better
5. **Swarm Coordination Layer** -- inspired by autoresearch@home, let multiple agents explore a search space in parallel and merge discoveries

**Why this is worth doing:**
Your bookmarks show a clear fascination with agents that exceed single-turn interactions. Between Hermes Agent's persistent memory, Factory's multi-day missions, and autoresearch@home's swarm collaboration, the pattern is unmistakable: the next leap in AI tooling is orchestrated agent teams, not solo agents. Building this now positions you at the frontier.

**Effort:** 3-4 weekends (incremental -- each layer is independently useful)
**Stack:** Python, LangGraph or custom orchestration, SQLite for trajectory storage, Claude/local LLM backends
**First step:** Implement the Hunter/Skeptic/Referee bug-finding trio as a proof-of-concept multi-agent pipeline on one of your existing repos

---

## Project 2: Autoresearch-Powered Code Optimizer

**Source bookmarks:**
- "Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12 model. It found ~20 changes that improved the validation loss" (@karpathy)
- "Autoresearch works even better for optimizing any piece of software. make an auto folder, add program.md and bench script, make a branch and let it rip" (@tobi)
- "We've raised $6.5M to kill vector databases... Embeddings can't tell a Q3 renewal clause from a..." (@contextkingceo)
- "near-lossless geometric compression for all existing transformer architectures" (@tsotchke)

**What to build:**
An autoresearch harness adapted for your own codebases -- automated experimentation that discovers optimizations while you sleep:
1. **Bench Script Framework** -- standardized benchmark scripts for your key projects (Siftly query speed, dashboard load times, data pipeline throughput)
2. **Experiment Runner** -- follows Tobi Lutke's recipe: auto folder + program.md + bench script + branch, then let an agent iterate
3. **Change Tracker** -- like Karpathy's 276-experiment dashboard, visualize kept vs. discarded changes and running-best performance
4. **Transfer Validation** -- test whether improvements found on small configurations transfer to production-scale (Karpathy proved this with depth=12 to depth=24)

**Why this is worth doing:**
Karpathy ran 276 experiments and found 29 additive improvements that transferred to larger models. Tobi says this works even better for general software optimization. This is a force multiplier -- you set it up once and it discovers improvements autonomously over days.

**Effort:** 2 weekends (basic harness), then ongoing experimentation
**Stack:** Python, Git (branch-per-experiment), Claude Code in sandbox mode, custom benchmark scripts
**First step:** Pick one function in Siftly (e.g., the FTS5 search pipeline) and create a program.md + bench script, then run a 24-hour autoresearch loop

---

## Project 3: Claude Code Power-User Skill Library

**Source bookmarks:**
- "How I created the frontend slides skill: Get Claude Code to create a website, iterate, then turn the workflow into a skill" (unknown)
- "Beginner vibe coder... generates an AI slob and debugs endlessly. Not so beginner vibe coder: setup personal [tooling]" (unknown)
- "We just added /btw to Claude Code! Use it to have side chain conversations while Claude is working" (@trq212)
- "Today we're launching local scheduled tasks in Claude Code desktop" (@trq212)
- "New in Claude Code: Code Review. A team of agents runs a deep review on every PR" (@bcherny)
- "permanently switch to running Claude Code on the server mostly on bypass permissions mode... for the first time I've managed to outrun my todo list" (unknown)
- "/remote-control is now available to all Pro users!" (unknown)
- "gstack is available now... open source, MIT license, one paste to install it on your local Claude Code" (@garrytan)

**What to build:**
A curated library of Claude Code skills and workflows that encode your best practices:
1. **Analysis Skill** -- automate your standard data analysis workflow (query sensors, generate plots, run diagnostics)
2. **PR Review Skill** -- leverage Claude Code's new code review feature with custom review criteria for your repos
3. **Scheduled Health Checks** -- use the new scheduled tasks feature to run daily code quality and performance checks
4. **Frontend Generation Skill** -- encode the slides skill pattern with your own UI vocabulary (the "learn what UI components are called" advice)
5. **gstack Integration** -- install gstack for automated security review (it caught XSS vulnerabilities a CTO's team missed)
6. **Remote Workflow** -- configure /remote-control for phone-based code review while away from desk

**Why this is worth doing:**
The gap between beginner and advanced "vibe coders" is exactly this: personal tooling that compounds. You've bookmarked 8+ tweets about Claude Code features and workflows. Converting those into reusable skills means you stop re-explaining context every session. The bypass-permissions user reported outrunning their todo list for the first time.

**Effort:** 1 weekend per skill (start with the highest-leverage one)
**Stack:** Claude Code skills (Markdown-based), gstack (MIT license), your existing codebase
**First step:** Take the /btw + /remote-control + scheduled tasks features and set up a daily automated code review on your main repo

---

## Project 4: AI-Powered Knowledge Pipeline (Research + Bookmarks)

**Source bookmarks:**
- "Siftly runs a 4-stage AI pipeline on your bookmarks -- entity extraction, vision analysis, semantic tagging, categorization" (@RoundtableSpace)
- "Defuddle now returns YouTube transcripts! Paste a YouTube link to get a markdown transcript with timestamps" (@kepano)
- "Introducing Paperscrolling: Get the most trending research with key ideas, figures, and audio explanations" (@askalphaxiv)
- "9 insane Claude prompts that turn 40+ research papers into structured literature reviews, knowledge maps, and research gaps" (@aiwithjainam)
- "AI can now build RAG pipelines like Google Brain's retrieval research team" (unknown)
- "Anthropic dropped 12 FREE courses that teach you how to build with Claude -- ship tool-using agents, build full RAG pipelines" (unknown)
- "colleague who recently went through AI/ML interviews has published this study booklet... PPO RL, constrained LLM inference" (@WaleAkinfaderin)
- "Introducing Elements of AI Agents. Our first text-based AI course. FREE to enroll" (@omarsar0)

**What to build:**
A unified knowledge ingestion and synthesis pipeline that turns your scattered research sources into structured, queryable knowledge:
1. **Multi-Source Ingestion** -- pull from Twitter bookmarks (you already have 103), YouTube transcripts via Defuddle, arXiv papers via alphaXiv, and saved articles
2. **RAG Pipeline** -- follow the Anthropic free courses to build a retrieval pipeline over your ingested content using local embeddings (skip vector DBs -- the ContextKing bookmark explains why embeddings miss relevance)
3. **Literature Review Generator** -- use Claude's research prompts to auto-generate structured reviews across topics (e.g., "summarize everything I've saved about MoE architectures")
4. **Knowledge Gap Detector** -- identify topics you're bookmarking heavily but haven't built anything for yet
5. **Study Guide Generator** -- auto-create study materials from bookmarked ML papers (like the AI/ML interview booklet)

**Why this is worth doing:**
You have 103 bookmarks spanning AI agents, ML training, robotics, health, and business. Without a pipeline, most of this knowledge decays. The RAG + synthesis approach turns passive bookmarking into active knowledge building, and you already have the Siftly infrastructure to build on.

**Effort:** 2-3 weekends (incremental -- each source is a separate integration)
**Stack:** Python, Siftly as foundation, Defuddle API, ChromaDB or SQLite FTS, Claude API
**First step:** Follow Anthropic's 12 free courses to build a minimal RAG pipeline, then point it at your bookmarks.json as the first data source

---

## Project 5: AI-Assisted CAD & Physical Prototyping Pipeline

**Source bookmarks:**
- "MIT just dropped an AI model that converts photos into fully editable CAD programs... GenCAD" (@heygurisingh)
- "AI ASSISTED GARAGE MANUFACTURING IS ABOUT TO EXPLODE! CAD Drawings From Just A Picture!" (@BrianRoemmele)
- "People who've never set foot in a factory will never understand... robotics simulation has promised faster deployment" (@IlirAliu_)
- "Join the Physical AI team... build with NVIDIA Robotics stack... 60+ humanoids, arms, wheeled" (@r_turb0)
- "NVIDIA Nemotron 3 Super... 120B open model uses hybrid MoE architecture... 5x higher throughput" (@nvidianewsroom)

**What to build:**
A photo-to-prototype pipeline that leverages GenCAD and related tools for rapid physical design iteration:
1. **Photo-to-CAD Converter** -- integrate GenCAD (MIT, open) to turn photos of parts/assemblies into parametric CAD models
2. **Design Iteration Loop** -- use Claude to suggest modifications to generated CAD command sequences, then re-render
3. **Sim-to-Real Validator** -- address the factory pain point: build a simple comparison framework that checks simulation predictions against real-world measurements
4. **Parts Library** -- accumulate a library of parametric CAD primitives generated from photos of common parts

**Why this is worth doing:**
You bookmarked two separate tweets about MIT's photo-to-CAD research plus robotics simulation pain points. The convergence of AI-generated CAD with physical prototyping is a genuine frontier. If you have any hardware projects, this pipeline eliminates the manual CAD bottleneck.

**Effort:** 2-3 weekends (GenCAD setup + integration)
**Stack:** Python, GenCAD (MIT open source), NVIDIA Isaac Sim (optional), parametric CAD viewers
**First step:** Download GenCAD and run it on photos of 5 simple objects to validate the pipeline and understand its limitations

---

## Project 6: ML Training Accelerator Toolkit

**Source bookmarks:**
- "Trellis framework: 50x faster training, LoRA training, open-source ML" (@luke_drago_)
- "Simply adding Gaussian noise to LLMs (one step -- no iterations, no learning rate, no gradients)... RandOpt" (@yule_gan)
- "88 pages of gold for training MoEs" (@TheAhmadOsman)
- "We collaborated with NVIDIA to teach you about Reinforcement Learning and RL environments... GRPO and RL best practices" (@UnslothAI)
- "Synthetic Data Playbook: We generated over 1T tokens in 90 experiments with 100k+ GPUh" (@joelniklaus)
- "I fine-tuned an AI model with no knowledge of models, finetuning, weights etc... using Nebula AI and Modal" (@WinterArc2125)

**What to build:**
A personal toolkit that bundles the best training acceleration techniques from your bookmarks into reusable recipes:
1. **RandOpt Implementation** -- the paper shows Gaussian noise + ensembling matches GRPO/PPO on math, coding, and chemistry tasks with zero training. Implement this as a baseline improvement method
2. **Trellis Integration** -- set up the 50x faster post-training framework for LoRA fine-tuning
3. **RL Environment Templates** -- follow Unsloth/NVIDIA's guide to create reusable RL environments with verifiable rewards
4. **Synthetic Data Generator** -- apply lessons from the Synthetic Data Playbook (which tested across Gemma, Qwen, Llama, Falcon) to generate domain-specific training data
5. **One-Click Fine-Tuning** -- replicate the Nebula AI + Modal pattern for zero-expertise fine-tuning via API

**Why this is worth doing:**
The ML training landscape is moving fast -- RandOpt eliminates gradients entirely, Trellis offers 50x speedups, and the synthetic data playbook distills 90 experiments into actionable guidance. Having these techniques ready in a personal toolkit means you can rapidly experiment with model improvement.

**Effort:** 3 weekends (one per technique cluster)
**Stack:** Python, PyTorch, Unsloth, Modal (for GPU), Trellis framework, HuggingFace
**First step:** Implement RandOpt on a small model (it requires zero training infrastructure -- just noise injection and ensembling)

---

## Project 7: AI Eval & Interview Prep Framework

**Source bookmarks:**
- "If you're interviewing for AI PM roles... the ability to define eval dimensions, build a test dataset, write eval criteria, and set blocking thresholds separates you" (unknown)
- "the AI-native PM bar is rising... PMs getting hired at top AI companies have full tooling stacks: custom GPTs for PRD drafts, Claude Projects" (@aakashgupta)
- "advice for interviewing now that writing code is becoming the easy part" (unknown)
- "Socratic prompting technique... output quality went from 3/10 to 9.5/10" (unknown)
- "colleague who went through AI/ML interviews published this study booklet" (@WaleAkinfaderin)

**What to build:**
A portable AI evaluation framework that doubles as career preparation and a portfolio piece:
1. **Eval Dimensions Library** -- reusable scoring rubrics for accuracy, helpfulness, safety, format compliance, and domain-specific metrics
2. **Test Dataset Generator** -- tools to create balanced, representative test sets from real data
3. **Blocking Threshold System** -- define quality gates that prevent bad outputs from shipping
4. **AI PM Portfolio** -- package the eval framework as a demonstrable case study showing hands-on eval skills (not just conceptual knowledge)
5. **Socratic Prompting Integration** -- build the prompting technique into your eval workflow to improve prompt quality from 3/10 to 9.5/10
6. **Interview Prep Module** -- structured study paths using the ML interview booklet covering PPO RL, constrained LLM inference, and modern techniques

**Why this is worth doing:**
Multiple bookmarks converge on one message: the bar for AI roles is rising fast. Six months ago, knowing prompts was enough. Now hiring managers at OpenAI, Anthropic, Google, and Meta want people who can build eval pipelines. A portable eval framework is both immediately useful and a career differentiator.

**Effort:** 2 weekends to generalize, ongoing refinement
**Stack:** Python, your existing scoring infrastructure, Claude API for Socratic prompting
**First step:** Abstract one domain-specific eval pipeline into a domain-agnostic framework, then apply it to a second domain as proof of portability

---

## Project 8: Startup Idea Validation Engine

**Source bookmarks:**
- "If you want to start a company: Find a large incumbent that is weak and outdated. Find a segment of customers that is not their core target market" (@HarryStebbings)
- "anyone can get their first 100 users by doing this: post on hacker news, launch on product hunt, email everyone you know" (@askOkara)
- "Someone built a directory of 5,700+ failed YC startups with post mortems, deep analysis, and rebuild plans" (@Amank1412)
- "A 10-minute application for $100,000. A free, no-strings-attached prize for builders, scientists, operators. The Eigenprize" (@thewildstevenp)
- "AMI Labs just raised $1.03B. World Labs raised $1B... both are betting on world models" (@zhuokaiz)
- "Lucent is an AI that automatically watches your session replays and finds bugs and UX issues" (@ycombinator)
- "Parker from Perfectly is your AI career super-connector on iMessage and WhatsApp" (@ycombinator)

**What to build:**
A structured idea validation pipeline that combines the startup frameworks from your bookmarks:
1. **Incumbent Weakness Scanner** -- apply Harry Stebbings' framework: identify large weak incumbents, underserved segments, and what they can't provide
2. **Failed Startup Analyzer** -- query the 5,700+ failed YC startup database for ideas that failed due to timing (not concept) and are now viable with AI
3. **First 100 Users Playbook** -- codify the distribution checklist (HN, PH, build in public, free tools) into a structured launch plan
4. **Opportunity Tracker** -- monitor prizes (Eigenprize), funding rounds ($1B+ world model bets), and YC launches for patterns
5. **Validation Scorecard** -- score ideas on market size, timing, technical feasibility, and distribution advantage

**Why this is worth doing:**
You've bookmarked a complete toolkit for startup thinking: frameworks for finding ideas, databases of failed startups to learn from, distribution playbooks, and funding opportunities. Connecting these into a systematic pipeline turns scattered inspiration into actionable opportunity evaluation.

**Effort:** 1-2 weekends (it's mostly connecting existing resources)
**Stack:** Python, web scraping for the failed YC database, Notion/Markdown for tracking
**First step:** Run Harry Stebbings' 3-step framework against 3 industries you know well, and cross-reference with the failed YC startup database for timing-related failures

---

## Quick Wins (< 1 hour each)

| # | Action | Source Bookmark |
|---|--------|----------------|
| 1 | Try Socratic prompting on your next Claude session | "output quality went from 3/10 to 9.5/10" |
| 2 | Install gstack on your repos for automated security review | "gstack... open source, MIT license, one paste to install" (@garrytan) |
| 3 | Set up Claude Code /remote-control for mobile access | "/remote-control is now available to all Pro users" |
| 4 | Learn proper UI component names for better vibe coding | "10x your vibecoded frontends by learning what components are called" |
| 5 | Configure Claude Code scheduled tasks for daily checks | "local scheduled tasks in Claude Code desktop" (@trq212) |
| 6 | Try the /btw command for side conversations mid-task | "side chain conversations while Claude is working" (@trq212) |
| 7 | Sign up for Anthropic's 12 free Claude courses | "12 FREE courses -- build with Claude" |
| 8 | Enroll in Elements of AI Agents (free, audio available) | "Our first text-based AI course. FREE to enroll" (@omarsar0) |
| 9 | Bookmark the ML interview study guide for later review | "study booklet... PPO RL, constrained LLM inference" (@WaleAkinfaderin) |
| 10 | Explore alphaXiv Paperscrolling for research discovery | "trending research with key ideas, figures, and audio explanations" (@askalphaxiv) |

---

## Priority Matrix

| Project | Impact | Effort | Synergy with Existing Work | Recommended Order |
|---------|--------|--------|---------------------------|-------------------|
| P3: Claude Code Skills | High | Low | Direct (daily workflow) | **Start here** |
| P2: Autoresearch Optimizer | Very High | Medium | Direct (any codebase) | **Second** |
| P4: Knowledge Pipeline | High | Medium | Direct (Siftly, bookmarks) | **Third** |
| P1: Multi-Agent Framework | Very High | High | High (builds on P3 skills) | **Fourth** |
| P6: ML Training Toolkit | High | High | Medium (model experimentation) | **Fifth** |
| P7: Eval & Interview Prep | High | Medium | Direct (career + portfolio) | **Sixth** |
| P5: CAD/Prototyping Pipeline | Medium | Medium | Low (new domain) | **Seventh** |
| P8: Startup Validation | Medium | Low | Medium (idea generation) | **Eighth** |

---

*Generated from 103 Twitter/X bookmarks analyzed by Claude AI*
