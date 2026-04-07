---
title: "Case Creation Workflow Notes"
type: source
tags:
  - process/case-management
  - compliance/kyb
created: 2026-04-07
updated: 2026-04-07
source_file: raw/case-creation-workflow-notes.md
status: draft
---

# Case Creation Workflow Notes

## Key Takeaways
- Conditions (rules/triggers) are used for **case creation**, not for portal configuration.
- Question fields should **dynamically appear** based on conditions (conditional logic).
- Portals are a separate configuration layer.
- Workflows can be **reviewed and adjusted** based on conditions.

## Detailed Summary
Brief internal notes on how the case management or compliance platform should handle conditional logic:

1. **Conditions for case creation** — Rules and conditions drive when and how cases are created in the compliance workflow. These are backend/process rules, not portal-facing.
2. **Dynamic question fields** — Fields should pop up (show/hide) based on conditions, enabling a guided workflow where analysts see only relevant questions.
3. **Portals** — Separate from conditions. Portal configuration is its own layer.
4. **Workflow review** — Existing workflows can be reviewed and modified based on condition logic.

## Impact Assessment
**Risk rating:** **Low** — These are implementation notes for platform configuration, not regulatory requirements. Useful context when configuring the case management module of the selected [[KYB (Know Your Business)]] provider.

## Cross-References
- Concept: [[KYB (Know Your Business)]]
- Source: [[Kota KYB Software Requirements]]

## Raw Source
`raw/case-creation-workflow-notes.md`
