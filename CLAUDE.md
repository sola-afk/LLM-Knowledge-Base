# Project Communications Monitoring Agent
Build AI agents that monitor customer-facing communications and flag compliance breaches, quality issues, and cases that need human escalation.

Two channels, sharing one criteria ID space and one MCC register:
- **Calls** (live) — `/Evaluator` assesses Fireflies transcripts.
- **Email** (in design) — `/EmailEvaluator` assesses customer-facing mail. Blocked on mailbox access and lawful basis; see `Researcher/req-email-detection-criteria.md` § Dependencies.

## Workspaces
- /Researcher — Gathers regulations, monitoring criteria, failure examples, and the prioritised list of what the agents must detect. Serves both channels; the MCC register and AE source-of-truth are shared and channel-agnostic.
- /Designer — Owns the agents' prompts, output schema, decision rules, and tool integrations; iterates them in versioned files. Calibration rules R1–R7 live here and apply to both channels.
- /Evaluator — **Calls.** Pulls call transcripts from Fireflies for a given date, assesses them against detection criteria, and identifies breaches.
- /EmailEvaluator — **Email.** Pulls customer-facing mail for a given date, splits it into templated and bespoke lanes, and assesses the bespoke lane. Also runs the template-library audit.
- /AsanaQueueManager — Asana Call Monitoring Queue Manager. Receives flagged calls from the Evaluator and creates tasks in the Asana Call Monitoring project, routing to the correct department section and @-mentioning the relevant executive.
- /compliance-wiki — Existing Karpathy-style knowledge base of Irish/EU financial-services regulation; consult before researching anything new.

## Criterion IDs are shared across channels
`HF-01` means the same thing in an email as on a call. Every criterion carries `applies_to: call | email | both`. Channel is an attribute of the finding, not of the rule — so Compliance can query "all HF-01 breaches this quarter, all channels" without reconciling two taxonomies. Never redefine, renumber, or retire an existing ID.

## Routing
| Task | Go to | Read |
|------|-------|------|
| Define or update what the agent must detect (calls) | /Researcher | CONTEXT.md + req-detection-criteria.md |
| Define or update what the agent must detect (email) | /Researcher | CONTEXT.md + req-email-detection-criteria.md |
| Write or revise agent prompts and output schema | /Designer | CONTEXT.md |
| Pull Fireflies transcripts for a date and assess compliance | /Evaluator | CONTEXT.md |
| Pull email for a date and assess compliance | /EmailEvaluator | CONTEXT.md |
| Audit the email template library | /EmailEvaluator | CONTEXT.md § Template Library Audit |
| Create Asana tasks for flagged calls | /AsanaQueueManager | CONTEXT.md |
| Look up a regulation, regulator, or compliance concept | /compliance-wiki | CLAUDE.md |

## Naming conventions
- Research notes (Researcher): `research-<topic>.md` — e.g. `research-mifid-call-recording.md`
- Requirements docs (Researcher): `req-<area>.md` — e.g. `req-detection-criteria.md`
- Prompt files (Designer): `prompt-<component>-v<n>.md` — e.g. `prompt-classifier-v3.md`
- Agent specs (Designer): `spec-<component>.md` — e.g. `spec-output-schema.md`
- Test sets (Evaluator): `tests-<scenario>.jsonl` — e.g. `tests-mis-selling.jsonl`
- Eval reports (Evaluator): `eval-<YYYY-MM-DD>-daily.md`
- Eval reports (EmailEvaluator): `eval-email-<YYYY-MM-DD>-daily.md`
- Template audits (EmailEvaluator): `audit-templates-<YYYY-MM-DD>.md`
- Calibration notes: `calibration-<YYYY-MM-DD>-<topic>.md` — prefix email ones `calibration-<YYYY-MM-DD>-email-<topic>.md`
- Routing specs (AsanaQueueManager): `spec-<component>.md` — e.g. `spec-asana-task.md`
- All filenames: lowercase, kebab-case, no spaces.
