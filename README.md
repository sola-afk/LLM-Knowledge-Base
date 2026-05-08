# LLM Knowledge Base

Project workspace for building a call monitoring agent, plus a compliance knowledge base it draws on.

## Root files
- `CLAUDE.md` — Project goal, workspace map, routing table, and naming conventions. Claude reads this first.
- `README.md` — This file.

## Workspaces
- `Researcher/` — Defines what the agent must detect. Produces research notes, regulatory citations, and prioritised detection criteria.
- `Designer/` — Builds the agent. Produces versioned prompts, output schemas, and decision rules.
- `Evaluator/` — Pulls customer-facing call transcripts from Fireflies for a given date and assesses each call against the detection criteria; produces a daily eval report.
- `AsanaQueueManager/` — Routes flagged calls into the Asana Call Monitoring project, applying section/assignee routing and writing structured custom fields plus a full task body.
- `compliance-wiki/` — Existing Karpathy-style wiki of Irish/EU financial-services regulation. Has its own `CLAUDE.md` and an internal `raw/`, `wiki/`, `output/` layout. Used as a research source by the Researcher workspace.

Human grading and calibration of agent outputs sits with the Compliance team (Sola Olaniyan + Trevor Gardiner) on the Asana tasks themselves, not as a separate workspace.

Each workspace contains a `CONTEXT.md` that defines its current focus, quality bar, and anti-patterns.
