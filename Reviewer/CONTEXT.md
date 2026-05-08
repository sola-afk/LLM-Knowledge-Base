# Current Project
Sample agent outputs from production-like runs and grade them as a human compliance reviewer would. Identify systematic false positives and false negatives, propose threshold or prompt adjustments to the Designer, and track agent-vs-human agreement over time so we can see whether quality is improving or drifting.

# What good looks like
* Every reviewed output is graded as Correct, False Positive, False Negative, or Borderline with a one-sentence rationale.
* Findings are aggregated by criterion so patterns — not one-off mistakes — drive recommendations.
* Recommendations to the Designer are specific and actionable: which criterion, which prompt section, what change is suggested.
* Agent-vs-reviewer agreement is tracked in a single rolling table across batches; trend matters more than any single batch.
* Borderline cases are escalated to a named human SME with a clear, written question — not silently resolved.

# What to avoid
* Don't propose prompt rewrites — recommend changes, but the Designer owns the prompt.
* Don't grade in bulk without reading the full transcript span the agent flagged.
* Don't change grading criteria mid-batch; if criteria need updating, finish the batch first and revise for the next one.
* Don't review or file outputs containing identifiable customer data without anonymising first.
