# LLM Knowledge Base

Project workspace for building communications monitoring agents — calls (live), sales email (in design), and customer service / CX (in design) — plus a compliance knowledge base they draw on.

Monitoring focus is the customer-facing functions: sales, customer service, customer success. BenOps / Embed is out of scope.

## Root files
- `CLAUDE.md` — Project goal, workspace map, routing table, and naming conventions. Claude reads this first.
- `README.md` — This file.

## Workspaces
- `Researcher/` — Defines what the agents must detect. Produces research notes, regulatory citations, and prioritised detection criteria. Serves both channels: `req-detection-criteria.md` (calls) and `req-email-detection-criteria.md` (email). The MCC register and AE source-of-truth are shared and channel-agnostic — read-only from the channel workspaces, never forked.
- `Designer/` — Builds the agents. Produces versioned prompts, output schemas, and decision rules. Calibration rules R1–R7 live here and apply to both channels.
- `Evaluator/` — **Calls.** Pulls customer-facing call transcripts from Fireflies for a given date and assesses each call against the detection criteria; produces a daily eval report.
- `EmailEvaluator/` — **Email.** Pulls customer-facing mail for a given date, splits it into templated (Lane 1) and bespoke (Lane 2) populations, and assesses Lane 2 against the email criteria. Also runs the template-library audit. **Not yet runnable** — blocked on domain-scope mailbox access and a documented lawful basis.
- `IntercomEvaluator/` — **Customer Service / CX.** Pulls CX conversations for a given date — in-app chat plus mail to `support@kota.io` — splits them into Fin / macro / bespoke lanes, and assesses each. Owns complaints-handling detection (HF-23/24) and automated-agent conduct (HF-25/26, currently dormant), plus the help-centre content audit. **Access already works** — app-level integration, not a mailbox grant — so this channel is unblocked where sales email is not. Excludes BenOps / Embed.
- `AsanaQueueManager/` — Routes flagged calls into the Asana Call Monitoring project, applying section/assignee routing and writing structured custom fields plus a full task body.
- `compliance-wiki/` — Existing Karpathy-style wiki of Irish/EU financial-services regulation. Has its own `CLAUDE.md` and an internal `raw/`, `wiki/`, `output/` layout. Used as a research source by the Researcher workspace.

Human grading and calibration of agent outputs sits with the Compliance team (Sola Olaniyan + Trevor Gardiner) on the Asana tasks themselves, not as a separate workspace.

Each workspace contains a `CONTEXT.md` that defines its current focus, quality bar, and anti-patterns.

## Channel model

Criterion IDs are a single shared space. `HF-01` means the same thing in an email as on a call; each criterion carries `applies_to: call | email | both`. Channel is an attribute of the finding, not of the rule — so Compliance can query one taxonomy across both channels.

The two evaluators run independently and share their criteria space, MCC register, and AE source-of-truth. The email pipeline differs from the call pipeline in three structural ways: a two-lane split (templates are assessed once at approval, not per send), mandatory preprocessing (quoted history and signatures stripped before assessment), and per-thread state (a thread is re-read every run, unlike a call, which is seen once).
