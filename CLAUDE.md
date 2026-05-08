# Project Call Monitoring Agent
Build an AI agent that listens to customer-facing call transcripts and flags compliance breaches, quality issues, and cases that need human escalation.

## Workspaces
- /Researcher — Gathers regulations, monitoring criteria, failure examples, and the prioritised list of what the agent must detect.
- /Designer — Owns the agent's prompts, output schema, decision rules, and tool integrations; iterates them in versioned files.
- /Evaluator — Builds test sets of call transcripts, runs the agent against them, and reports precision, recall, and regressions.
- /Reviewer — Grades agent outputs as a human compliance reviewer would, tracks agreement over time, and recommends calibration changes.
- /compliance-wiki — Existing Karpathy-style knowledge base of Irish/EU financial-services regulation; consult before researching anything new.

## Routing
| Task | Go to | Read |
|------|-------|------|
| Define or update what the agent must detect | /Researcher | CONTEXT.md |
| Write or revise agent prompts and output schema | /Designer | CONTEXT.md |
| Build test sets, run evals, measure accuracy | /Evaluator | CONTEXT.md |
| Grade live outputs, calibrate thresholds | /Reviewer | CONTEXT.md |
| Look up a regulation, regulator, or compliance concept | /compliance-wiki | CLAUDE.md |

## Naming conventions
- Research notes (Researcher): `research-<topic>.md` — e.g. `research-mifid-call-recording.md`
- Requirements docs (Researcher): `req-<area>.md` — e.g. `req-detection-criteria.md`
- Prompt files (Designer): `prompt-<component>-v<n>.md` — e.g. `prompt-classifier-v3.md`
- Agent specs (Designer): `spec-<component>.md` — e.g. `spec-output-schema.md`
- Test sets (Evaluator): `tests-<scenario>.jsonl` — e.g. `tests-mis-selling.jsonl`
- Eval reports (Evaluator): `eval-<YYYY-MM-DD>-<run-name>.md` — e.g. `eval-2026-05-08-baseline.md`
- Review reports (Reviewer): `review-<YYYY-MM-DD>-batch-<NN>.md` — e.g. `review-2026-05-08-batch-01.md`
- Calibration notes (Reviewer): `calibration-<topic>.md`
- All filenames: lowercase, kebab-case, no spaces.
