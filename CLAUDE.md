# Project Communications Monitoring Agent
Build AI agents that monitor customer-facing communications and flag compliance breaches, quality issues, and cases that need human escalation.

Three channels, sharing one criteria ID space and one MCC register:
- **Calls** (live) — `/Evaluator` assesses Fireflies transcripts.
- **Sales email** (in design) — `/EmailEvaluator` assesses GTM / sales mail. Blocked on mailbox access and lawful basis; see `Researcher/req-email-detection-criteria.md` § Dependencies.
- **Customer Service / CX** (in design, unblocked) — `/IntercomEvaluator` assesses Intercom conversations: in-app chat and mail to `support@kota.io`. Access already works; gated on complaints-deadline research, register coverage, and the CX team list. See `Researcher/req-intercom-detection-criteria.md` § Dependencies.

Monitoring focus is the **customer-facing functions**: sales, customer service, customer success. **BenOps / Embed is out of scope** — it is the larger Intercom population but a specialist operations function dealing with partner support desks.

Note: `support@kota.io` routes into Intercom, not Gmail. Customer service email is therefore the Intercom channel, and `/EmailEvaluator` is effectively sales/GTM only.

## Workspaces
- /Researcher — Gathers regulations, monitoring criteria, failure examples, and the prioritised list of what the agents must detect. Serves all channels; the MCC register and AE source-of-truth are shared and channel-agnostic.
- /Designer — Owns the agents' prompts, output schema, decision rules, and tool integrations; iterates them in versioned files. Calibration rules R1–R7 live here and apply to all channels.
- /Evaluator — **Calls.** Pulls call transcripts from Fireflies for a given date, assesses them against detection criteria, and identifies breaches.
- /EmailEvaluator — **Sales / GTM email.** Pulls customer-facing mail for a given date, splits it into templated and bespoke lanes, and assesses the bespoke lane. Also runs the template-library audit.
- /IntercomEvaluator — **Customer Service / CX.** Pulls CX conversations for a given date (chat + `support@kota.io`), splits them into Fin / macro / bespoke lanes, and assesses each. Owns complaints-handling detection, plus the help-centre content audit. Excludes BenOps.
- /AsanaQueueManager — Asana Call Monitoring Queue Manager. Receives flagged calls from the Evaluator and creates tasks in the Asana Call Monitoring project, routing to the correct department section and @-mentioning the relevant executive.
- /compliance-wiki — Existing Karpathy-style knowledge base of Irish/EU financial-services regulation; consult before researching anything new.

## Criterion IDs are shared across channels
`HF-01` means the same thing in an email as on a call. Every criterion carries `applies_to: call | email | intercom | both`. Channel is an attribute of the finding, not of the rule — so Compliance can query "all HF-01 breaches this quarter, all channels" without reconciling three taxonomies. Never redefine, renumber, or retire an existing ID.

Allocation so far: **HF-00–HF-15** base (calls), **HF-16–HF-22** email-only, **HF-23–HF-26** Intercom-only, **SF-10–SF-15** base, **SF-16–SF-17** email, **SF-18–SF-20** Intercom, **ES-01–ES-03** base, **ES-04–ES-05** cross-channel, **LIB-01–LIB-06** email template library, **LIB-07–LIB-12** Intercom content layer. Continue the sequence; never reuse.

## Routing
| Task | Go to | Read |
|------|-------|------|
| Define or update what the agent must detect (calls) | /Researcher | CONTEXT.md + req-detection-criteria.md |
| Define or update what the agent must detect (email) | /Researcher | CONTEXT.md + req-email-detection-criteria.md |
| Define or update what the agent must detect (Intercom) | /Researcher | CONTEXT.md + req-intercom-detection-criteria.md |
| Write or revise agent prompts and output schema | /Designer | CONTEXT.md |
| Pull Fireflies transcripts for a date and assess compliance | /Evaluator | CONTEXT.md |
| Pull email for a date and assess compliance | /EmailEvaluator | CONTEXT.md |
| Audit the email template library | /EmailEvaluator | CONTEXT.md § Template Library Audit |
| Pull Intercom conversations for a date and assess compliance | /IntercomEvaluator | CONTEXT.md |
| Audit help-centre Articles and Fin content sources | /IntercomEvaluator | CONTEXT.md § Content Governance Audit |
| Check complaints handling (recognition, logging, timelines) | /IntercomEvaluator | CONTEXT.md + req-intercom-detection-criteria.md § Complaints |
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
- Eval reports (IntercomEvaluator): `eval-intercom-<YYYY-MM-DD>-daily.md`
- Template audits (EmailEvaluator): `audit-templates-<YYYY-MM-DD>.md`
- Content audits (IntercomEvaluator): `audit-content-<YYYY-MM-DD>.md`
- Calibration notes: `calibration-<YYYY-MM-DD>-<topic>.md` — prefix non-call ones with the channel, e.g. `calibration-<YYYY-MM-DD>-email-<topic>.md`, `calibration-<YYYY-MM-DD>-intercom-<topic>.md`
- Routing specs (AsanaQueueManager): `spec-<component>.md` — e.g. `spec-asana-task.md`
- All filenames: lowercase, kebab-case, no spaces.
