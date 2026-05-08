# Project Call Monitoring Agent
Build an AI agent that listens to customer-facing call transcripts and flags compliance breaches, quality issues, and cases that need human escalation.

## Workspaces
- /Researcher — Gathers regulations, monitoring criteria, failure examples, and the prioritised list of what the agent must detect.
- /Designer — Owns the agent's prompts, output schema, decision rules, and tool integrations; iterates them in versioned files.
- /Evaluator — Pulls call transcripts from Fireflies for a given date, assesses them against detection criteria, and identifies breaches.
- /Router — Receives flagged calls from the Evaluator and creates tasks in the Asana Call Monitoring project, routing to the correct department section and @-mentioning the relevant executive.
- /compliance-wiki — Existing Karpathy-style knowledge base of Irish/EU financial-services regulation; consult before researching anything new.

## Routing
| Task | Go to | Read |
|------|-------|------|
| Define or update what the agent must detect | /Researcher | CONTEXT.md |
| Write or revise agent prompts and output schema | /Designer | CONTEXT.md |
| Pull Fireflies transcripts for a date and assess compliance | /Evaluator | CONTEXT.md |
| Create Asana tasks for flagged calls | /Router | CONTEXT.md |
| Look up a regulation, regulator, or compliance concept | /compliance-wiki | CLAUDE.md |

## Naming conventions
- Research notes (Researcher): `research-<topic>.md` — e.g. `research-mifid-call-recording.md`
- Requirements docs (Researcher): `req-<area>.md` — e.g. `req-detection-criteria.md`
- Prompt files (Designer): `prompt-<component>-v<n>.md` — e.g. `prompt-classifier-v3.md`
- Agent specs (Designer): `spec-<component>.md` — e.g. `spec-output-schema.md`
- Test sets (Evaluator): `tests-<scenario>.jsonl` — e.g. `tests-mis-selling.jsonl`
- Routing specs (Router): `spec-<component>.md` — e.g. `spec-asana-task.md`
- All filenames: lowercase, kebab-case, no spaces.
