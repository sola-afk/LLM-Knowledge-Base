# Current Project
Build representative test sets of call transcripts (synthetic or anonymised) covering each detection criterion plus negatives and edge cases, run the Designer's latest prompt against them, and report precision, recall, and per-criterion failure modes. Reports go back to the Designer to drive the next prompt iteration.

# What good looks like
* Every test case is labelled with the expected criterion ID(s) and a one-line rationale for why that label is correct.
* Test sets cover positives, hard negatives (looks similar but isn't), and edge cases — not just easy positives.
* Eval reports include per-criterion precision/recall, a confusion matrix, and at least three concrete failure examples with the transcript span and the agent's exact output.
* Re-run the previous prompt version alongside the new one so regressions are visible — change one variable at a time.
* Save raw model outputs alongside the report so failures can be re-examined without re-running.

# What to avoid
* Don't hand-pick easy cases that inflate scores — the Designer can't improve what isn't measured honestly.
* Don't change the test set in the same run as a prompt change; vary one thing at a time.
* Don't use real, identifiable customer transcripts — anonymise thoroughly or synthesise.
* Don't summarise failures without quoting the exact transcript span and the model's exact output.
