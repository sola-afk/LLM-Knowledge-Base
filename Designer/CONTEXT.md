# Current Project
Translate the Researcher's detection criteria into a working agent: a prompt (or chain of prompts), a strict output schema, decision rules for flag-vs-escalate, and tool integrations (transcript fetcher, regulatory lookup). Iterate prompt versions in numbered files so the Evaluator can compare runs side-by-side.

# What good looks like
* Every prompt change is a new versioned file (`prompt-classifier-v4.md`) — never overwrite an old version.
* The output schema is strict, machine-parseable JSON with required fields for criterion ID, severity, evidence quote, and recommended action.
* Each detection criterion maps to a clearly identified section of the prompt, so a reader can trace which prompt lines enforce which rule.
* Edge cases (ambiguity, missing audio, multi-language calls, partial transcripts) have explicit fallback behaviour defined.
* A short changelog at the top of each new prompt version explains what changed and why.
* **Timestamps are mandatory and precise**: every finding must report the exact timestamp from the Fireflies transcript sentence data in `MM:SS` or `HH:MM:SS` format. "Mid-call", "late-call", or approximate ranges are not acceptable. The Fireflies transcript returns sentence-level timestamps — use them directly.
* **Recording consent is excluded**: do not check for or flag the absence of a verbal recording disclosure at the start of a call. Pre-call consent is collected separately and is not a detection criterion. See `Researcher/req-detection-criteria.md` Conventions note.

# What to avoid
* Don't invent detection criteria the Researcher hasn't specified — push back and ask, don't paper over the gap.
* Don't ship a prompt without a defined output schema — unstructured outputs break the Evaluator.
* Don't delete or overwrite previous prompt versions; the Evaluator needs them for regression testing.
* Don't bake firm-specific identifiers, real client names, or live credentials into prompt files.
