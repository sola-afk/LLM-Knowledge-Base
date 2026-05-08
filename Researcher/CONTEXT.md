# Current Project
Map out everything the call monitoring agent must detect: compliance triggers required by Irish/EU regulation (Consumer Protection Code, MiFID II, IDD, AML), quality issues that erode customer outcomes, and escalation cases that need a human reviewer. Output a prioritised list of detection criteria the Designer can build prompts against.

# What good looks like
* Every detection criterion cites a specific regulation, internal policy, or documented incident — no detections without a source.
* Cross-check `/compliance-wiki` (its `wiki/index.md`) before adding new criteria so we reuse existing entries instead of duplicating them.
* Each criterion includes one short positive and one short negative example so the Designer can write prompts that disambiguate.
* Criteria are prioritised High/Medium/Low by regulatory and customer-harm risk, with a one-sentence justification per rating.
* Hard rules (always flag) are clearly separated from soft signals (escalate only if multiple co-occur).

# What to avoid
* Don't propose a detection from assumed regulation — verify against `/compliance-wiki` or the source text first.
* Don't write detection logic, prompts, or pseudocode — that's the Designer's job; describe behaviour in plain English.
* Don't flatten priority — labelling everything "High" defeats the point of prioritisation.
* Don't include personal data, real client names, or recording excerpts that could identify a real customer.
