---
title: Weekly Call Eval — Scheduled Routine
created: 2026-09-30
type: spec
status: active — Fireflies + Asana attached; Slack missing
trigger_id: trig_01MpWuUjHQZgdX2EQ1gZh5yY
---

# Weekly Call Eval — Scheduled Routine

The call monitoring agent runs on a schedule. This file records what the Routine does, so the
behaviour is reviewable in the repo rather than living only in the scheduler.

| | |
|---|---|
| **Trigger ID** | `trig_01MpWuUjHQZgdX2EQ1gZh5yY` |
| **Name** | Weekly Call Compliance Eval (Kota) |
| **Schedule** | `0 7 * * 1` — Mondays 07:00 UTC |
| **Session** | Fresh session per fire (no accumulated context) |
| **First run** | 2026-10-05 |
| **Notifications** | Push to the owner on completion |
| **Branch** | `claude/call-monitoring-agent-foa9cs` |

> [!note] Verified 2026-09-30 — live, with one gap
> Connectors were attached manually and confirmed present on the trigger:
>
> | Connector | Status | Used for |
> |---|---|---|
> | **Fireflies** | ✅ attached | Pull transcripts (steps 3–4) |
> | **Asana** | ✅ attached | File Grade 3/4/5 (step 7) |
> | **Slack** | ❌ **not attached** | DM Compliance (step 8) |
>
> Also confirmed: `enabled: true`, fresh session per fire (`persist_session: false`), next run
> **2026-10-05 07:00 UTC**, and the tool allowlist includes Bash / Read / Write / Edit — so the
> session can run `extract.py` and push to git.
>
> **The Slack gap does not break the run.** Step 8 now degrades gracefully: with no Slack tool the
> session writes the same summary into the report under a "Summary for Compliance" heading and says
> explicitly in its final message that the DM could not be sent. Push notification to the owner is
> on regardless, so a run is never silent.
>
> Attach Slack from the claude.ai Routines UI to close it.

## What it does

1. **Period** — the most recent complete Mon–Fri *ending before today*, computed from the actual
   day-of-week at run time.
2. **Reads** the run spec, criteria, MCC register, AE source-of-truth, script register, the R1–R7
   calibration rules, and the two most recent weekly reports (for repeat patterns).
3. **Pulls and triages** via `fireflies_get_transcripts` → `tools/extract.py triage`. Payloads are
   never pasted into context; the tool projects fields.
4. **Assesses** in risk order using `extract.py speakers` and `extract.py scan`, with an explicit
   instruction to include newer and unrecognised sales staff.
5. **Reports** to `Evaluator/eval-<from>-to-<to>-weekly.md`, including the mandatory R5 withdrawn-
   findings section.
6. **Files** every Grade 3/4/5 to Asana per `AsanaQueueManager/spec-asana-task.md`.
7. **Notifies Compliance** — DMs Sola (`U09CME6LKEU`) if Slack is available; otherwise writes the
   summary into the report and says so, rather than skipping silently.
8. **Commits and pushes** to the working branch.

## Guards carried in the prompt

Every known defect from the 2026-09-07 → 2026-09-15 runs is written into the Routine prompt, so a
fresh session inherits them without having to rediscover them:

| Guard | Why |
|---|---|
| **Stale register** — an unrecognised speaker is *"verify with Compliance"*, never *"not on the register"* | The May 2026 snapshot produced a false HF-00 against Mark Fitzgibbon in a live Asana task on 2026-09-15. The finding is still raised; unregistered status is just not asserted as fact |
| **Alias check before HF-00** | "Dan" vs register "Daniel" caused a false positive against a qualified speaker |
| **Step 3.5 script carve-out** | Group-life 2x/4x multiples are approved scripted content. Arranging, renewals, comparisons, pricing and member-specific circumstances are not, regardless of script |
| **Spec drift warnings** | HF-06 vs HF-09 for GDPR/PII, and the two conflicting ES-03 definitions |
| **R1 — customer speech is never a finding** | Including the note that `yonder.app` addresses are Kota-side |
| **Coverage honesty** | "If you assessed 3 of 50, say 3 of 50. Never report unassessed calls as passes." |

## Known limitations

- **Coverage stays partial by design.** A week is ~50 calls; one run assesses a handful in risk
  order. The rest are reported as *not assessed*, never as passes. Daily runs would be more
  tractable (~10/day) — worth revisiting if partial coverage proves unsatisfactory.
- **DST drift.** The cron is UTC. Ireland leaves IST on 25 October 2026, after which 07:00 UTC is
  07:00 local rather than 08:00. Harmless for a Monday-morning job; noted so it is not a surprise.
- **Date arithmetic is day-of-week independent** *(fixed 2026-09-30)*. The first version said
  "7 days ago through 3 days ago", which is only correct on a Monday — a manual fire or a retry on
  any other day would have silently assessed a Wed–Sun window and labelled it a working week. The
  prompt now computes the last complete Mon–Fri and verifies the day-of-week before proceeding.
- **The register guard is a mitigation, not a fix.** Refreshing
  `Researcher/research-mcc-fitness-probity.md` from the Google Drive source removes the underlying
  failure mode. Until then every run carries the caveat.

## Maintenance

- Change the schedule or prompt with `update_trigger` on `trig_01MpWuUjHQZgdX2EQ1gZh5yY` — do not
  delete and recreate, which loses run history.
- **When the register is refreshed, edit the prompt** to remove the stale-snapshot guard. Leaving
  a stale warning in place trains the reader to ignore warnings.
- Review the guard table above whenever a new calibration rule is added, and keep this file in step
  with the live prompt.
