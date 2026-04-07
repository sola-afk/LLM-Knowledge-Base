# Compliance Knowledge Base — Schema

You are maintaining a compliance knowledge base for a compliance manager at a financial services firm based in Ireland. This wiki tracks regulatory requirements, policies, vendor due diligence, audit findings, risk assessments, and industry developments. The knowledge base is built on Andrej Karpathy's LLM Wiki pattern.

## Architecture

There are three layers:

1. **raw/** — Immutable source documents. Regulations, guidance notes, policies, audit reports, vendor assessments, articles, consultation papers. You read from here but never modify these files.
2. **wiki/** — LLM-maintained markdown files. Summaries, entity pages, concept pages, comparisons, regulatory trackers. You own this layer entirely. You create pages, update them when new sources arrive, maintain cross-references, and keep everything consistent.
3. **CLAUDE.md** (this file) — The schema. It tells you how the wiki is structured, what conventions to follow, and what workflows to use.

## Directory Structure

```
compliance-wiki/
├── CLAUDE.md              # This schema file
├── raw/                   # Immutable source documents
│   ├── assets/            # Images, diagrams downloaded locally
│   └── (source files)     # .md, .pdf, .txt, .html files
├── wiki/                  # LLM-maintained wiki
│   ├── index.md           # Master index of all wiki pages
│   ├── log.md             # Chronological activity log
│   ├── overview.md        # High-level synthesis / dashboard
│   ├── entities/          # Organisations, regulators, vendors, people
│   ├── concepts/          # Regulatory concepts, compliance topics
│   ├── sources/           # Summary pages for each ingested source
│   └── comparisons/       # Comparison tables, analyses, frameworks
└── output/                # Generated deliverables (slides, charts, reports)
```

## Page Conventions

### Frontmatter (YAML Properties)

Every wiki page MUST include YAML frontmatter:

```yaml
---
title: Page Title
created: 2026-04-07
updated: 2026-04-07
type: entity | concept | source | comparison | overview
tags:
  - compliance/gdpr
  - regulation/cbi
source_count: 3
status: draft | active | review | archived
---
```

### Tag Hierarchy

Use nested tags consistently:

- `regulation/` — Regulatory frameworks: `regulation/gdpr`, `regulation/dora`, `regulation/aml`, `regulation/mifid`, `regulation/solvency`, `regulation/cbi`, `regulation/eba`, `regulation/eiopa`
- `compliance/` — Compliance domains: `compliance/data-protection`, `compliance/outsourcing`, `compliance/fitness-probity`, `compliance/conduct`, `compliance/risk-management`, `compliance/complaints`
- `entity/` — Entity types: `entity/regulator`, `entity/vendor`, `entity/internal`, `entity/industry-body`
- `process/` — Processes: `process/audit`, `process/breach`, `process/incident`, `process/change-management`, `process/due-diligence`
- `status/` — Lifecycle: `status/in-force`, `status/consultation`, `status/upcoming`, `status/superseded`

### Internal Links

Use Obsidian wikilinks for all cross-references:

```markdown
See [[GDPR]] for the full regulatory framework.
This vendor is assessed under [[Outsourcing Policy]].
Related finding: [[Audit 2025-Q3#Finding 4]].
```

### Page Templates

#### Entity Page (wiki/entities/)

```markdown
---
title: Central Bank of Ireland
type: entity
tags:
  - entity/regulator
  - regulation/cbi
created: 2026-04-07
updated: 2026-04-07
---

# Central Bank of Ireland

## Overview
Brief description of the entity and its relevance to our compliance programme.

## Key Regulations & Guidance
- [[Individual Accountability Framework]]
- [[Fitness and Probity Standards]]

## Recent Developments
- Chronological list of recent actions, publications, enforcement.

## Impact on Our Firm
How this entity's actions affect our compliance obligations.

## Sources
- [[source-name-1]]
- [[source-name-2]]
```

#### Concept Page (wiki/concepts/)

```markdown
---
title: Outsourcing
type: concept
tags:
  - compliance/outsourcing
  - regulation/cbi
  - regulation/eba
created: 2026-04-07
updated: 2026-04-07
source_count: 0
---

# Outsourcing

## Definition
Clear definition of the concept in regulatory context.

## Regulatory Framework
Which regulations apply, with links to [[entity pages]] for each regulator.

## Key Requirements
The main compliance obligations, summarised clearly.

## Our Approach
How our firm addresses this — links to relevant [[policies]] and [[procedures]].

## Open Questions / Gaps
Areas of uncertainty or known gaps in our compliance.

## Sources
- [[source-name]]
```

#### Source Summary Page (wiki/sources/)

```markdown
---
title: "CBI Guidance on Outsourcing — 2025 Update"
type: source
tags:
  - regulation/cbi
  - compliance/outsourcing
created: 2026-04-07
updated: 2026-04-07
source_file: raw/cbi-outsourcing-guidance-2025.md
---

# CBI Guidance on Outsourcing — 2025 Update

## Key Takeaways
3–5 bullet points summarising the most important points.

## Detailed Summary
Longer summary in paragraphs. Focus on what matters for our compliance programme.

## Impact Assessment
What this means for us. What needs to change. What deadlines apply.

## Cross-References
Links to wiki pages updated as a result of this source:
- Updated: [[Outsourcing]]
- Updated: [[Central Bank of Ireland]]
- New page: [[Cloud Outsourcing Requirements]]

## Raw Source
Link to the file in raw/: `raw/cbi-outsourcing-guidance-2025.md`
```

## Operations

### 1. Ingest

When a new source is added to `raw/`:

1. Read the source document thoroughly.
2. Discuss key takeaways with the user — what matters most for our compliance programme.
3. Create a source summary page in `wiki/sources/`.
4. Update `wiki/index.md` — add the new page with a one-line summary.
5. Update relevant entity pages in `wiki/entities/` — add new developments, requirements.
6. Update relevant concept pages in `wiki/concepts/` — integrate new information, note contradictions.
7. Create new entity or concept pages if the source introduces topics not yet covered.
8. Update `wiki/overview.md` if the source materially changes the compliance landscape.
9. Append an entry to `wiki/log.md`.
10. Report back: what was created, what was updated, what questions arise.

A single source might touch 5–15 wiki pages. Take the time to update everything properly.

### 2. Query

When the user asks a question:

1. Read `wiki/index.md` to find relevant pages.
2. Read the relevant wiki pages.
3. Synthesise an answer with links to sources.
4. If the answer is valuable and reusable, offer to file it back into the wiki as a new page (e.g., a comparison, analysis, or regulatory summary).

Outputs can take different forms:
- A new wiki page (markdown)
- A comparison table
- A slide deck (Marp format) in `output/`
- A chart or visualisation in `output/`
- A briefing note for management

### 3. Lint (Health Check)

When asked to lint or health-check the wiki:

1. Check for contradictions between pages (e.g., two pages stating different deadlines for the same requirement).
2. Find stale information — regulatory developments that have been superseded.
3. Identify orphan pages with no inbound links.
4. Find important concepts mentioned but lacking their own page.
5. Check for missing cross-references.
6. Suggest new sources to look for (e.g., "The DORA deadline has passed — should we check for CBI enforcement guidance?").
7. Verify tag consistency — are tags used consistently across pages?
8. Check that all source summary pages link back to their raw file.
9. Update `wiki/log.md` with the lint results.

### 4. Regulatory Change Tracking

Special workflow for regulatory developments:

1. When a new regulation, consultation paper, or guidance note is ingested, assess:
   - Is this **in force**, **upcoming**, or **in consultation**?
   - What is the **effective date** or **response deadline**?
   - Does it **amend or supersede** existing requirements?
2. Update the relevant concept page with timeline information.
3. If it supersedes something, mark the old source/concept as `status/superseded`.
4. Flag any **action items** for the compliance team.

## Special Files

### index.md

The master index. Organised by section:

```markdown
# Compliance Wiki Index

## Entities
- [[Central Bank of Ireland]] — Irish financial regulator
- [[Data Protection Commission]] — Irish GDPR supervisory authority

## Concepts
- [[Outsourcing]] — EBA/CBI outsourcing requirements (3 sources)
- [[GDPR]] — Data protection regulation and compliance (5 sources)

## Sources
- [[CBI Outsourcing Guidance 2025]] — Updated outsourcing expectations
- [[DORA Implementation Guide]] — Digital operational resilience

## Comparisons
- [[GDPR vs DORA Data Requirements]] — Overlap analysis
```

Update this on every ingest. The LLM reads this first when answering queries to find relevant pages.

### log.md

Chronological, append-only. Each entry uses a consistent format:

```markdown
## [2026-04-07] ingest | CBI Outsourcing Guidance 2025
- Source: raw/cbi-outsourcing-guidance-2025.md
- Created: wiki/sources/cbi-outsourcing-guidance-2025.md
- Updated: wiki/concepts/outsourcing.md, wiki/entities/central-bank-of-ireland.md
- Notes: New cloud-specific requirements. Deadline Q3 2026.

## [2026-04-07] query | Overlap between DORA and existing CBI outsourcing rules
- Created: wiki/comparisons/dora-vs-cbi-outsourcing.md
- Filed back into wiki as reusable comparison.

## [2026-04-07] lint | Weekly health check
- Found: 2 orphan pages, 1 stale deadline, 3 missing cross-references.
- Fixed all issues. Details in lint report.
```

### overview.md

A living executive summary of the compliance landscape. Updated when material changes occur. Should answer: "What are the most important compliance priorities right now?"

## Compliance-Specific Conventions

### Regulatory References
Always include the full regulatory reference on first mention:
- "Regulation (EU) 2016/679 (GDPR)"
- "Regulation (EU) 2022/2554 (DORA)"
- "S.I. No. 60/2011 — Fitness and Probity Standards"

### Deadlines and Dates
Always note effective dates, transposition deadlines, and response deadlines. Use the callout format:

```markdown
> [!warning] Deadline
> DORA applies from **17 January 2025**. All ICT third-party arrangements must be compliant.
```

### Risk Ratings
When assessing impact, use: **High**, **Medium**, **Low** with brief justification.

### Confidentiality
Never include personal data, client names, or commercially sensitive information in the wiki unless explicitly approved. Use anonymised references where needed.

## Tips

- Use **Obsidian Web Clipper** to clip regulatory publications and articles directly to `raw/`.
- Use **Obsidian's graph view** to visualise how regulations, concepts, and entities connect.
- Use **Dataview** plugin to query pages by tag, status, or date (e.g., "show all upcoming regulatory deadlines").
- The wiki is a git repo — commit regularly for version history.
- Run a lint pass weekly to keep the wiki healthy.
- When in doubt about regulatory interpretation, flag it as an open question rather than stating it as fact.
