---
title: Activity Log
created: 2026-04-07
updated: 2026-04-07
type: overview
tags:
  - compliance/log
status: active
---

# Activity Log

## [2026-04-07] setup | Initial knowledge base creation
- Created: CLAUDE.md schema file
- Created: wiki/index.md, wiki/log.md, wiki/overview.md
- Created: Directory structure (raw/, wiki/entities/, wiki/concepts/, wiki/sources/, wiki/comparisons/, output/)
- Notes: Knowledge base initialised. Ready for source ingestion.

## [2026-04-07] ingest | Kota KYB Software Requirements
- Source: raw/kota-kyb-software-requirements.md (renamed from "Untitled document.md")
- Created: wiki/sources/kota-kyb-software-requirements.md
- Created: wiki/entities/kota.md, wiki/entities/central-bank-of-ireland.md, wiki/entities/fca.md, wiki/entities/complyadvantage.md
- Created: wiki/concepts/kyb.md, wiki/concepts/sanctions-and-pep-screening.md, wiki/concepts/ubo-identification.md, wiki/concepts/aml-compliance.md
- Updated: wiki/index.md, wiki/overview.md
- Notes: Comprehensive KYB vendor requirements for Kota's Platform and Embed verticals. Key gap identified: no dedicated KYB provider. ComplyAdvantage pain points documented.

## [2026-04-07] ingest | KYB Requirements by Product Type
- Source: raw/kyb-requirements-by-product.md (renamed from "KYB Requirements.md")
- Created: wiki/sources/kyb-requirements-by-product.md
- Updated: All concept and entity pages with product-specific matrix data
- Notes: Due diligence requirements vary significantly by product. PEPP risk assessment outstanding — director/UBO ID requirements unknown.

## [2026-04-07] ingest | Case Creation Workflow Notes
- Source: raw/case-creation-workflow-notes.md (renamed from "Conditions are mainly for case creation.md")
- Created: wiki/sources/case-creation-workflow-notes.md
- Notes: Brief internal notes on conditional logic for case creation workflows. Low priority — useful context for KYB platform configuration.

## [2026-04-07] research | KYB Provider Market Research — Top 10 Developer-Friendly Providers
- Source: Web research across multiple industry comparison guides and provider websites
- Created: wiki/sources/kyb-provider-research-2026-04.md
- Created: wiki/comparisons/kyb-provider-comparison.md
- Created: wiki/entities/sumsub.md, wiki/entities/signzy.md, wiki/entities/complycube.md, wiki/entities/ondato.md, wiki/entities/veriff.md, wiki/entities/idenfy.md, wiki/entities/aiprise.md, wiki/entities/persona.md, wiki/entities/alloy.md, wiki/entities/onfido.md
- Updated: wiki/index.md, wiki/overview.md
- Notes: Evaluated 10 KYB providers against Kota's requirements. Top 3 recommendations: Sumsub (best all-round), Persona (best DX), ComplyCube (best pricing transparency). Next steps: request demos, validate EU coverage, request security certifications.

## [2026-04-07] research | KYB Provider UX Research — Top 10 for User Experience & Simplistic Design
- Source: Web research across provider websites and industry guides
- Created: wiki/sources/kyb-provider-ux-research-2026-04.md
- Created: wiki/comparisons/kyb-provider-ux-comparison.md
- Created: wiki/entities/vespia.md, wiki/entities/spektr.md, wiki/entities/strise.md, wiki/entities/checkin-com.md, wiki/entities/shufti-pro.md, wiki/entities/compliancely.md, wiki/entities/middesk.md
- Updated: wiki/index.md, wiki/overview.md
- Notes: Evaluated 10 KYB providers on UX and design simplicity. Top 3 UX picks: Spektr (best compliance team UX), Vespia/Veriff (best onboarding UX), Persona (best combined DX+UX). Persona and Sumsub rank highly across both developer and UX dimensions.

## [2026-04-07] deliverable | KYB Provider Product Requirements Document
- Created: output/kyb-provider-product-requirements.md
- Notes: Formal PRD synthesising all knowledge base sources — functional requirements (40 items), technical requirements (20 items), security requirements (12 items), UX requirements (7 items), vendor requirements (8 items). Includes evaluation scorecard, shortlisted providers, decision framework (replace vs extend ComplyAdvantage), and 16-week implementation timeline.

## [2026-04-08] ingest | Q1 2026 Compliance Review — Embed Hubs
- Source: raw/Q1 2026 Compliance Review- Embed hubs.docx (converted to raw/q1-2026-compliance-review-embed-hubs.md)
- Notes: Terms of Reference for compliance audit of Embed Hubs — customer-facing information portals on kota.io subdomains. Scope: consumer protection, insurance distribution, data protection. Built on Lovable by Josh Ellwood.

## [2026-04-08] deliverable | Embed Hub Sampling Review Template
- Created: output/embed-hub-sampling-review-template.md
- Notes: 30-item checklist across 7 categories (clear presentation, product information, disclosures, IPIDs, data protection, consistency, governance) with regulatory references down to section/subsection level. Covers CBI Consumer Protection Code 2025, S.I. No. 229/2018, IDD, FCA Consumer Duty (PRIN 2A), ICOBS, GDPR.

## [2026-04-08] wiki | Product Governance and Insurance Distribution concept pages
- Created: wiki/concepts/product-governance.md
- Created: wiki/concepts/insurance-distribution.md
- Updated: wiki/index.md
- Notes: Product governance covers IDR Reg.38 manufacturer and distributor obligations, IDD Art.25, CPC 2025 Standards for Business, FCA PRIN 2A.3. Insurance distribution covers disclosures (Reg.23), pre-contractual info (Reg.26), IPIDs (Reg.27), CPC 2025 Parts 3–4, ICOBS, and FCA Consumer Duty.

## [2026-04-08] ingest | Product governance framework articles (4 sources)
- Sources: Skyjed, ESMA/A&L Goodbody, Ruleguard, KPMG Ireland (all adapted from MiFID II to insurance distribution)
- Created: raw/product-governance-framework-skyjed.md, raw/product-governance-target-market-esma-alg.md, raw/product-governance-quality-assessment-ruleguard.md, raw/product-governance-manufacturer-distributor-kpmg.md
- Created: wiki/sources/ pages for all 4
- Updated: wiki/concepts/product-governance.md — added lifecycle phases, five target market categories, feedback loop, self-assessment checklist, expanded open questions
- Updated: wiki/index.md

## [2026-04-08] research | EU product governance regulatory framework
- Sources: Delegated Regulation (EU) 2017/2358 (EUR-Lex), EIOPA POG Peer Review 2023, EU Retail Investment Strategy (Dec 2025)
- Created: raw/eu-delegated-regulation-2017-2358-pog.md, raw/eiopa-pog-peer-review-2023.md, raw/eu-retail-investment-strategy-pog-2025.md
- Created: wiki/sources/ pages for all 3
- Updated: wiki/concepts/product-governance.md — added Delegated Regulation 2017/2358 articles (product approval, target market, testing, monitoring, corrective action), EIOPA peer review findings, upcoming Retail Investment Strategy (value-for-money, undue costs)
- Updated: wiki/index.md
- Notes: Delegated Reg. 2017/2358 is the foundational EU regulation — Articles 4-8 (manufacturers) and 10 (distributors). EIOPA peer review found target markets too broad, product testing inconsistent, distributor feedback loops weak. RIS introduces value-for-money assessments (~2028).

## [2026-04-08] research | CPC 2025 quote data retention and deletion
- Source: S.I. 81/2025, DPC guidance, Insurance Ireland guidance, industry briefings
- Created: raw/cpc-2025-quote-data-retention.md
- Created: wiki/sources/cpc-2025-quote-data-retention.md
- Created: wiki/concepts/data-retention.md
- Updated: wiki/index.md
- Notes: CPC 2025 sets 12-month retention for non-customer records (quote-only) — reduced from 6 years. 6 years retained for active customers. 12 months is consent-based. GDPR Art.5(1)(e) overlay — DPC suggests ~21-day cooling-off for abandoned quotes. Effective 24 March 2026.

## [2026-08-21] monitoring | Email monitoring — Intercom — Week 34 (17–21 Aug 2026)
- Applied the Call Monitoring programme's assessment criteria (Call Monitoring 2026 sheet + Call Supervision Audit Notion DB) to customer-facing email in Intercom.
- Criteria carried across unchanged; Recording Consent remapped to Regulatory Disclosure (no email analogue). Grades 1-5 and categories (CPC / MCC / Data Protection) unchanged.
- Created: output/intercom-email-monitoring-2026-W34.md
- Sample: 9 customer-facing threads, risk-weighted, from a population of 434 email conversations.
- Grades: 3x Pass, 4x Pass with comments, 2x Fail.
- Fail 1 - Ctrl Alt: five statutory auto-enrolment questions answered as settled fact, no caveat or referral. Comparable to the Q1 call finding logged as an MCC breach. Same handler qualified an near-identical query correctly two days earlier.
- Fail 2 - Healthcare Renewal campaign: promotional outbound with no regulatory footer, financial promotion approval status unconfirmed, and sent to a client with no Irish employees since June.
- Other themes: footer applied on BenOps outbound but missing from CX platform and campaign email; benefit levels quoted without reference to the table of cover; snoozing used in place of responding; special category health data processed pre-enrolment without documented basis.
- Escalations raised to HOB/GM, IRL, Support ops and DPO.

## [2026-08-21] setup | Email Monitoring Asana project created
- Created Asana project "Email Monitoring" (gid 1217717281350976) in the Compliance team, mirroring the Call Monitoring project (gid 1213240137041729).
- Sections mirror call monitoring: Go-to-Market, Customer Success, Benefits, Escalated, Resolved/False Positives. Added "Embed" as a sixth - it is a live Intercom queue with no call-channel equivalent.
- Seeded with the 9 assessed threads from the week 34 review. 2 in Escalated (Ctrl Alt MCC, Healthcare Renewal campaign), 4 across team sections, 3 in Resolved/False Positives.
- Each task body carries the full assessment in the call monitoring column order: date, Kota staff, prospect/client, email purpose, regulatory disclosure, grade, requirement breached, Intercom conversation link, issues, training gap, action, response from management.
- Outstanding manual steps (Asana API cannot do these): attach the 7 existing workspace custom fields (Grade, Issues, Requirement Breached, Kota Staff, Prospect/Client, Call Purpose, Recording Link); delete the auto-created empty section; reorder sections; confirm privacy (created as Private/owner-only, Call Monitoring is private to team).
- Grade mapping from the Notion 1-5 scale to the Asana triage scale: 1 Pass = no grade + Resolved; 2 Pass with comments = Minor Correction; 3 Fail = Fail; 4 Fail with referral = Fail + Escalated; 5 Severe Fail = Severe Fail.

## [2026-08-21] cross-reference | Escalated email findings vs approved product scripts
- Checked both escalated week 34 items against approved content: Intercom Help Centre art. 14470927 "How to manage your Irish pension scheme on Kota", Notion "AutoEnrolment in Ireland", "Health Insurance Renewals SOP", "Renewals checklist", and the Notion approved script library under MCC Supervision.
- Ctrl Alt: answers are NOT on script. Of five, one directly contradicts approved content (13-week look-back vs the documented "re-enrolled every 2 years"), one rests on a premise art. 14470927 contradicts (Deirdre earns EUR 18,000, below the EUR 20,000 auto-exempt threshold, never mentioned), two are unsourced mechanics, one is unverifiable. The approved answer that did exist - the 1.5%/3.5% exemption thresholds and the "Allow Kota to keep you exempt" toggle - was not used. Grade upgraded 3 to 4.
- Surfaced an unresolved substantive question: does the EUR 20,000 AE threshold apply per employment or to aggregate earnings? Neither approved source covers multi-employment. Art. 14470927 needs updating either way.
- Healthcare Renewal: on script for timing (33 days vs 30 required) and channel, off script for content. SOP requires the email to state "the new prices"; it does not. SOP frames it as informational, "a reply is not required"; the email pushes a booking CTA. Kota's own Renewals checklist lists "Clear disclaimer that the policy auto-renews unless actioned" as a compliance requirement, unticked, and the email omits it while telling the customer changes can only be made before renewal.
- Because the SOP instructs staff to duplicate template 42771939 and keep the copy unchanged, the defect is likely in the template rather than the sender, and would affect every ILH renewal customer this year. Not yet verified against the template - flagged as the first action.
- Noted the SOP is marked "In progress" with the UK (Freedom) and IPMI (Allianz) sections unfinished, and risk level set to Low.
- Discovered the Notion MCC Supervision page already holds a "Email Audit" database with the same schema as Call Supervision Audit, plus a "Documentation Audit" database. Overlaps with the new Asana project - the record of truth needs deciding.

## [2026-08-21] update | Email Monitoring Asana simplified to two sections
- Reworked every task to lead with a clickable "Open this conversation in Intercom" link at the top of the description (html_notes), so each email can be reviewed directly from the task.
- Collapsed the workflow to two sections per request: Escalated and Resolved/False Positives.
- Placement: 2 in Escalated (Ctrl Alt MCC, Definely renewal template); 7 in Resolved/False Positives.
- Three of the resolved items carry open actions noted in their descriptions and flagged to move back to Escalated if needed: Nory (customer still unanswered, FRT missed), Remote/Anthropic (pre-enrolment special category data, lawful basis undocumented), Flatpay (whether an opt-out triggers a consequences-of-cancellation disclosure).
- Asana API cannot delete or reorder sections, so Go-to-Market, Customer Success, Benefits, Embed and the auto-created untitled section are now empty and need deleting in the UI. There is also no update_project endpoint exposed, so the project description still describes the original six-section structure and needs editing by hand.

## [2026-08-21] blocked | Email Monitoring Asana custom field columns
- Requested: clickable conversation link as a column, and the Kota employee as a column, matching Call Monitoring's "Recording Link" and "Kota Staff" fields.
- BLOCKED at the API. The Asana MCP server exposes no endpoint to create a custom field or attach an existing workspace field to a project. Confirmed empirically: writing a value returns "Custom field with ID 1214635377742250 is not on given object" - a field must be on the project before any value can be set.
- Interim mitigation applied: renamed all 9 tasks to lead with the Kota employee, format "Employee - Client - Purpose (date)", so the author is visible in the list row without a column and survives truncation. The Intercom link remains a clickable link at the top of each task description.
- Awaiting the manual UI step: add the existing workspace fields Kota Staff (1214635377742250), Recording Link (1213240170325738, relabel to Conversation Link), Grade (1213240170325716), Issues (1213240170325728), Requirement Breached (1213240170325733), Prospect/Client (1214635377742252), Call Purpose (1213240170325723, relabel to Email Purpose). Once attached, all 9 tasks can be populated in a single call - values already held.
- Decision (21 Aug): use the existing Kota Staff workspace field rather than repurposing Assignee. Assignee would have given a native column immediately but would notify each employee and place an adverse finding in their My Tasks ahead of management review. Both columns therefore wait on the UI step; values are prepared.

## [2026-08-21] update | Email Monitoring Asana columns populated
- Fields added in the UI by Sola: Link (text) and Grade (enum: False Positive / Severe Fail / Fail / Minor Correction). Note this is a new project-specific Grade field, not the shared Call Monitoring one, so cross-channel reporting on a single Grade field is not available.
- Populated all 9 tasks: Link on all 9 (Intercom conversation permalinks), Grade on 6.
- Grade mapping applied: Fail x2 (Ctrl Alt, Definely); Minor Correction x4 (Imvizar, LearnUpon, Nory, Remote/Anthropic); the 3 passes left blank, since the enum is exception-based and has no Pass option, matching Call Monitoring.
- Caveat: the enum has no "Fail with referral" option, so Ctrl Alt displays as "Fail". The upgrade to Fail with referral, and the reasoning for it, sit in the task description.
- No Kota Staff field was added; the employee remains at the front of each task name.

## [2026-08-28] monitoring | Email monitoring — Intercom — Week 35 (24–28 Aug 2026)
- Second run of the email supervision programme. Criteria unchanged from Call Monitoring.
- Population: 594 email conversations, full sweep (6 pages, matches Intercom's count). Up 37% on week 34's 434.
- Created: output/intercom-email-monitoring-2026-W35.md. 5 threads assessed and added to the Email Monitoring Asana with Link and Grade populated.
- Grades: 1 Fail with referral, 1 Fail, 2 Pass with comments, 1 Pass.
- ESCALATION 1 (Data Protection): a health scheme renewal letter for Trevor Gardiner, Kota personnel, was posted to Ramp Network's Ireland office. Handled as a "mailing error", snoozed twice, no breach assessment, no DPO escalation, no Article 33 clock. Kota has precedent for this (Notion "Mixed employees data incident", Dec 2025) and a written commitment on the Cybersecurity page - neither applied. Recognition failure rather than knowledge gap. Letter contents not inspected; grading between 4 and 5 depends on that.
- ESCALATION 2 (CPC): employee pension transfer-in query received 26 Aug, no reply at all, both SLA targets breached, still open. Cross-reference shows an approved Help Centre article (9145103) answers the question almost verbatim - Fin escalated it out rather than serving the article and it sat unassigned. A Fin configuration and triage finding, not a handler one.
- Second renewal-communication defect in two consecutive weeks (W34: campaign email to an offboarded client; W35: letter to the wrong company). Widens the W34 recommendation from suppression rules to the mailing file itself.
- Onboard Retail: employer states the employee "has no recollection of enrolling in the health plan" and asks to reverse charges - a possible mis-enrolment/consent and redress issue processed as a routine cancellation, not flagged to Compliance.
- Ineffable Intelligence: possible platform defect enforcing an under-18 dependant age rule that may not match Bupa's policy, potentially refusing eligible dependants. Tier 1 (1h) SLA answered in 15 hours.
- SLA week on week: overall miss 58% to 55%; Embed P0 83% to 69%; Urgent 74% to 80%; P3 SME 19% to 30%. Misrouting 20% to 23%.
- Carried over unresolved from W34: opt-out consequences-of-cancellation disclosure question, and the missing regulatory footer on CX Platform outbound.
- Noted: the W34 Ctrl Alt item, graded 4 by Compliance, now shows as Minor Correction in Asana. Left as amended - the management view belongs in that column.
