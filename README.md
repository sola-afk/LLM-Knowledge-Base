# LLM Knowledge Base

Project workspace for building a call monitoring agent, plus a compliance knowledge base it draws on.

## Root files
- `CLAUDE.md` — Project goal, workspace map, routing table, and naming conventions. Claude reads this first.
- `README.md` — This file.

## Workspaces
- `Researcher/` — Defines what the agent must detect. Produces research notes, regulatory citations, and prioritised detection criteria.
- `Designer/` — Builds the agent. Produces versioned prompts, output schemas, and decision rules.
- `Evaluator/` — Tests the agent. Produces labelled test sets and eval reports with precision/recall and regression analysis.
- `Reviewer/` — Grades agent outputs as a human compliance reviewer. Produces review reports, calibration notes, and a rolling agreement-rate tracker.
- `compliance-wiki/` — Existing Karpathy-style wiki of Irish/EU financial-services regulation. Has its own `CLAUDE.md` and an internal `raw/`, `wiki/`, `output/` layout. Used as a research source by the Researcher workspace.

Each workspace contains a `CONTEXT.md` that defines its current focus, quality bar, and anti-patterns.
