---
title: Weekly Call Eval — Scheduled Routine
created: 2026-09-30
type: spec
status: created — BLOCKED on connector attachment
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

> [!warning] BLOCKED — the Routine has no connectors attached
> The Routine was created successfully and **will fire**, but the sessions it starts carry **no
> connector tools** — no Fireflies, no Asana, no Slack. As it stands it will fail at step 3, when
> it tries to pull transcripts.
>
> Connectors could not be attached programmatically: passing them through from this session is
> disabled for this organization. **They must be attached to the Routine from the claude.ai
> Routines UI** before the first run.
>
> Required: **Fireflies** (pull transcripts), **Asana** (file Grade 3/4/5), **Slack** (notify
> Compliance).
>
> Until that is done the schedule produces failures, not coverage. A Routine that fires and fails
> is worse than no Routine, because the calendar entry implies the work is happening.

## What it does

1. **Period** — previous Mon–Fri, computed at run time.
2. **Reads** the run spec, criteria, MCC register, AE source-of-truth, script register, the R1–R7
   calibration rules, and the two most recent weekly reports (for repeat patterns).
3. **Pulls and triages** via `fireflies_get_transcripts` → `tools/extract.py triage`. Payloads are
   never pasted into context; the tool projects fields.
4. **Assesses** in risk order using `extract.py speakers` and `extract.py scan`, with an explicit
   instruction to include newer and unrecognised sales staff.
5. **Reports** to `Evaluator/eval-<from>-to-<to>-weekly.md`, including the mandatory R5 withdrawn-
   findings section.
6. **Files** every Grade 3/4/5 to Asana per `AsanaQueueManager/spec-asana-task.md`.
7. **Slacks** Sola Olaniyan (`U09CME6LKEU`) with a phone-readable summary.
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
