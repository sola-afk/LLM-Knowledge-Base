# Current Project
Translate the Researcher's detection criteria into a working agent: a prompt (or chain of prompts), a strict output schema, decision rules for flag-vs-escalate, and tool integrations (transcript fetcher, regulatory lookup). Iterate prompt versions in numbered files so the Evaluator can compare runs side-by-side.

# What good looks like
* Every prompt change is a new versioned file (`prompt-classifier-v4.md`) — never overwrite an old version.
* The output schema is strict, machine-parseable JSON with required fields for criterion ID, severity, evidence quote, and recommended action.
* Each detection criterion maps to a clearly identified section of the prompt, so a reader can trace which prompt lines enforce which rule.
* Edge cases (ambiguity, missing audio, multi-language calls, partial transcripts) have explicit fallback behaviour defined.
* A short changelog at the top of each new prompt version explains what changed and why.
* **Verbatim quote is the search key, not the timestamp**: the Fireflies MCP tools do not expose per-sentence `start_time`, so timestamps are unreliable for navigating to a moment. Compliance pastes the exact transcript quote into the Fireflies search bar instead — the player jumps to that sentence. Every finding must therefore include the **EXACT verbatim transcript quote** that triggered the criterion. Do not paraphrase, summarise, or "clean up" the transcript. If the Fireflies transcriber wrote "Boop" for "BUPA" or "Booba" for "BUPA", preserve that rendering — it's what the search will match.
  * Optional: add a `~MM:SS` anchor from `fireflies_get_summary` action-items / topic ranges when one maps cleanly. This is a hint, not the search key. Never estimate timestamps by sentence position.
* **Recording consent is excluded — pre-call booking form**: Kota collects recording consent via a booking form when prospects and customers schedule the call. The agent must **not** flag any transcript-level recording-consent pattern: absence of an opener, implied consent ("I'm assuming that's okay"), or any "rep didn't request permission to record" line. There is no HF-06/HF-07 for recording disclosure — consent is a pre-call form artefact, not a transcript event. See `Researcher/req-detection-criteria.md` Conventions note.
* **HF-00 scope — "regulated activity" means product talk, not call attendance**: only flag an unqualified speaker if they are actually discussing **product features, quotes, pricing, comparisons, benefits/drawbacks, cover details, excesses, underwriting, recommendations, or arranging** of a retail financial product (pension, PMI, life, income protection). A BDR or AE asking discovery questions about the prospect's own structure, describing Kota's company/team/process/platform, scheduling, or making small talk is **not** regulated activity even if it happens on a call where a qualified colleague will later discuss products. Org chart, platform features, billing, HRIS, payroll integration → not retail financial products under MCC. Calibration source: Riot Games (2026-05-07) call was incorrectly graded Fail because Katie's BDR discovery question was misread as regulated activity.

## Calibration rules (R1–R5) — derived from false-positive analysis 2026-05-15

See `Evaluator/calibration-2026-05-15-false-positives.md` for the full analysis. Five rules apply on every eval run:

* **R1 — Speaker-content binding (always)**: Every finding must name **the specific speaker who said the specific quote**, and the quote must contain the regulated product content. Do not flag a qualified colleague's presence on the call. Do not flag a speaker for being on a call where regulated products were mentioned by someone else. Format: `[Criterion]: [Speaker X] said "[verbatim quote about product Y]"`.

* **R2 — Charitable-interpretation pass on AE quotes**: Before tagging HF-05 on an Irish auto-enrolment statement, compare the speaker's quote against **all** relevant gov.ie sections in `Researcher/source-of-truth-ae-myfuturefund.md`:
  * Section 3 (eligibility)
  * Section 4 (contribution rates + Year 1–3 split)
  * Section 5 (contribution base + €80k cap)
  * The "minimum-contribution standards for existing occupational schemes" subsection (Pensions Authority 3.5% exemption standard)
  * Section 7 (opt-out and suspension)

  If **any** section makes the statement correct under a reasonable reading, do not flag. Only flag when no section supports the statement. The "3.5% with 1.5% employer minimum" framing is a particularly common ambiguity — it can refer to either the AE Year 1–3 total OR the Pensions Authority occupational exemption standard.

* **R3 — HF-05 severity ladder**: Distinguish:
  * **HF-05 confirmed** — wrong number, wrong rule, wrong eligibility threshold, wrong phasing year. The customer has been told a specific fact that contradicts gov.ie. Escalation to Simon Ellis if the breach meets the spec criteria.
  * **HF-05 light** — right principle, wrong terminology (e.g. "taxable income" vs "gross earnings"); minor inaccuracy on a mechanic that doesn't change the customer's takeaway. Documented for coaching but doesn't auto-escalate on its own.

* **R4 — Kota's actual processes are NOT transcript findings**: These happen outside the call and must not be flagged from the transcript:
  * Recording consent — collected on the booking form.
  * Broker-of-record paperwork — signed separately.
  * Internal Slack BDR-to-AE handoff — happens in Slack.

  If the agent sees these patterns missing from the transcript, that is **not** a finding.

* **R5 — Track withdrawn findings explicitly**: Every eval report must include a "Findings withdrawn after reassessment" section listing any false positives surfaced during compliance review. Empty section is fine on a clean run, but the section must be there. Format:

  ```
  | Call | Original finding | Why withdrawn | Reassessment date |
  |---|---|---|---|
  ```

  This tracks the agent's false-positive rate explicitly and feeds the next calibration round.

# What to avoid
* Don't invent detection criteria the Researcher hasn't specified — push back and ask, don't paper over the gap.
* Don't ship a prompt without a defined output schema — unstructured outputs break the Evaluator.
* Don't delete or overwrite previous prompt versions; the Evaluator needs them for regression testing.
* Don't bake firm-specific identifiers, real client names, or live credentials into prompt files.
