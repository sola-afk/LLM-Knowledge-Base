# Current Project
Translate the Researcher's detection criteria into a working agent: a prompt (or chain of prompts), a strict output schema, decision rules for flag-vs-escalate, and tool integrations (transcript fetcher, regulatory lookup). Iterate prompt versions in numbered files so the Evaluator can compare runs side-by-side.

# What good looks like
* Every prompt change is a new versioned file (`prompt-classifier-v4.md`) — never overwrite an old version.
* The output schema is strict, machine-parseable JSON with required fields for criterion ID, severity, evidence quote, and recommended action.
* Each detection criterion maps to a clearly identified section of the prompt, so a reader can trace which prompt lines enforce which rule.
* Edge cases (ambiguity, missing audio, multi-language calls, partial transcripts) have explicit fallback behaviour defined.
* A short changelog at the top of each new prompt version explains what changed and why.
* **Timestamps are mandatory and precise**: every finding must report the exact timestamp from the Fireflies transcript sentence data in `MM:SS` or `HH:MM:SS` format. "Mid-call", "late-call", or approximate ranges are not acceptable. The Fireflies transcript returns sentence-level timestamps — use them directly.
  * **Important**: the `mcp__...__fireflies_get_transcript` tool returns sentence text and speaker only — `start_time` is not exposed in the current MCP wrapper. To anchor findings, also call `mcp__...__fireflies_get_summary` and use the timestamps embedded in `Action Items` (per-action) and `Shorthand Bullet` (per-topic-section). These give ~±30s accuracy and are tied to specific moments in the call. Map each finding's transcript span to the nearest action-item or topic-section anchor. Never estimate timestamps by sentence position — that drifts by minutes.
* **Recording consent is excluded — pre-call booking form**: Kota collects recording consent via a booking form when prospects and customers schedule the call. The agent must **not** flag any transcript-level recording-consent pattern: absence of an opener, implied consent ("I'm assuming that's okay"), or any "rep didn't request permission to record" line. There is no HF-06/HF-07 for recording disclosure — consent is a pre-call form artefact, not a transcript event. See `Researcher/req-detection-criteria.md` Conventions note.
* **HF-00 scope — "regulated activity" means product talk, not call attendance**: only flag an unqualified speaker if they are actually discussing **product features, quotes, pricing, comparisons, benefits/drawbacks, cover details, excesses, underwriting, recommendations, or arranging** of a retail financial product (pension, PMI, life, income protection). A BDR or AE asking discovery questions about the prospect's own structure, describing Kota's company/team/process/platform, scheduling, or making small talk is **not** regulated activity even if it happens on a call where a qualified colleague will later discuss products. Org chart, platform features, billing, HRIS, payroll integration → not retail financial products under MCC. Calibration source: Riot Games (2026-05-07) call was incorrectly graded Fail because Katie's BDR discovery question was misread as regulated activity.

# What to avoid
* Don't invent detection criteria the Researcher hasn't specified — push back and ask, don't paper over the gap.
* Don't ship a prompt without a defined output schema — unstructured outputs break the Evaluator.
* Don't delete or overwrite previous prompt versions; the Evaluator needs them for regression testing.
* Don't bake firm-specific identifiers, real client names, or live credentials into prompt files.
