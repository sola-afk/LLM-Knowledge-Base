---
title: Call Supervision Audit — Source Analysis 2025–2026
created: 2026-05-08
type: research
period_covered: June 2025 – March 2026
source: Notion ☎️ Call Supervision Audit (MCC Supervision)
---

# Call Supervision Audit — Source Analysis 2025–2026

## Scope

This note analyses the human compliance-reviewed call audit log covering **June 2025 through Q1 2026** — 13 calls reviewed in depth across the Sales and Customer Success teams, plus the audit log's own Pass/Pass-with-comments/Fail/Severe-Fail rubric.

Each entry is a Notion page containing: a Fireflies recording link, a 1–5 grade, free-text findings, timestamped excerpts, and the human reviewer's regulatory framing (typically CBI/FCA). The detection criteria the agent must enforce are derived **bottom-up** from the breaches the human reviewer actually flagged — not top-down from regulation alone.

Anonymisation: customer names and staff names are replaced with case IDs (e.g. `Q4-25-SF-01` = Q4 2025, Severe Fail #1).

## Distribution by grade and period

| Grade | Count | Notes |
|------|-------|-------|
| 5 — Severe Fail | 1 | Q1 2026: misled customer on firm capability/global coverage |
| 4 — Fail w/ referral | 1 | Q4 2025: repeated explicit recommendations across two calls |
| 3 — Fail | 1 | Q2 2025: cross-sold regulated products without authorisation |
| 2 — Pass with comments | ~6 | language and absolute-claim issues |
| 1 — Pass | ~4 | mostly operational / process calls |

The grade trend is roughly stable; severity of failures is concentrated in calls that touch **pension scheme design** and **firm capability claims**.

## Recurring breach themes (ordered by frequency)

### 1. Crossing the advice perimeter (≥9/13 calls flagged)
By far the dominant failure mode. Trigger phrases recur across reviewers:
- Explicit: "I recommend", "you should", "best thing to do", "what might be best for you"
- Comparative value judgements: "so superior", "much better than", "more advantageous", "real benefit"
- Configuration advice tied to a regulatory/financial outcome (e.g. "set a 1% minimum and they won't fall into the government scheme")
- Personal nudges to employees: "increase her percent when she gets a pay rise", "you could go to zero, but it's beneficial if you contribute more"
- Anchoring to social proof: "98% of clients do this"

The reviewers consistently cite **CBI Consumer Protection Code (CPC)**, **MiFID II conduct**, **FCA COBS 9 / PERG 8** as the regulatory frame, and Kota's internal rule that non-advised staff "may not give financial advice or a recommendation".

### 2. False or sloppy framing of firm role and capability (≥4 calls)
Two distinct sub-patterns:
- **Inflating role**: calling sales staff "qualified financial advisors"; describing capabilities the firm does not have ("we go to market for the most competitive quotes" when only one panel provider is used; "we are global" when EEA-only).
- **Misciting regulatory status**: e.g. "we record because we're regulated by central bank" — conflates being regulated with a lawful basis to record.

Severe Fail Q1-26 is in this category; misled the customer on geographic scope and on going-to-market-for-quotes.

### 3. Recording / consent disclosure failures (≥4 calls)
Either no opener at all, or implied/assumed consent ("I'm making the assumption that's all okay"), or the wrong basis (regulator status used instead of consent + purpose).

### 4. Absolutes and over-certainty in product/coverage claims (≥4 calls)
"Everything's covered", "full cover", "won't lose cover", "minuscule [premium impact]", "we can be certain". Insurance reviewers flag these against **clear, fair and not misleading** (IDD Art. 17(2), ICOBS 2.2.2R, CPC 2025 Part 3).

### 5. Cross-selling / arranging regulated products without authorisation (1 call but Fail-rated)
Q2-25-F-01: a CS rep introduced and offered to arrange quotes for Life Assurance and Income Protection. Reviewer cited **S.I. 229/2018** insurance distribution authorisation requirement and FCA general prohibition.

### 6. Tax and pensions-law guidance (≥3 calls)
Examples flagged: personal tax credits and marital sharing; auto-enrolment eligibility conclusions stated as fact ("she won't be included in auto-enrolment"); P11D oversimplifications. Reviewers explicitly mark these as outside non-advised scope.

### 7. Avoiding-the-regulator language (≥3 calls)
Configuration discussions framed around how to **prevent** employees being auto-enrolled into the state scheme (My Future Fund). Two reviewers also flagged "we're finding ways around" wording and "it's within the rules at the moment" hedging — both characterised as circumvention-adjacent.

### 8. Personal data / GDPR handoff (1 call, marked Red)
Q4-25-PII-01: vendor contact agreed to receive a spreadsheet of employee PPS numbers, DOB, salaries, addresses by email and re-upload on the customer's behalf. Flagged under **GDPR Art. 5/32**, DPA absence, and DPC quote-data guidance.

### 9. Inducement / commission disclosure (≥2 calls)
Commission discussed in promotional terms ("you can start to make some money") rather than as neutral remuneration disclosure under **IDR Reg. 23(1)(h)** / IDD Art. 19(1)(d)–(e).

### 10. Marketing/emotive framing in regulated comms (≥3 calls)
"Wild West", "good news story", "all good news", disparagement of competitor brokers ("traditional broker nature… can leave it open to mistakes"). Flagged against CPC 2025 Part 3 and CBI Standards for Business.

## What the agent can learn from the reviewers' rubric

- The 1–5 grade in the existing audit gives a usable severity signal: 5 = misled customer / capability misrepresentation; 4 = repeated explicit recommendations; 3 = unauthorised regulated activity; 2 = language hygiene and absolutes; 1 = no findings.
- Reviewers consistently quote the **exact transcript span** with timestamp before applying the regulatory frame — this is the format the agent's output schema should mirror so a human can re-listen to the same span.
- Reviewers separate **must-fix** (perimeter/capability/PII) from **should-fix** (language, tone) — the agent should preserve this split rather than collapsing into a single "flagged" label.
- "No findings" calls (Pass, grade 1) are mostly operational/admin — these define the **negative class** the agent must not over-flag.

## Cross-references in this knowledge base

The following pages already cover regulation cited by the reviewers:
- [[Insurance Distribution]] — S.I. 229/2018, IDD, CPC 2025, FCA PRIN 2A / ICOBS
- [[Product Governance]] — IDD Art. 25, Delegated Reg. 2017/2358, CPC 2025
- [[Data Retention]] — CPC 2025 retention, GDPR storage limitation, DPC guidance
- [[Kota]] — internal entity page (CBI-regulated intermediary, Platform & Embed)

Gaps the wiki does not yet cover that this project will need:
- **Advice perimeter** (CBI CPC Ch. 4; FCA PERG 8.24–8.30; QFA requirement) — no concept page
- **Insurance Distribution authorisation regime** (S.I. 229/2018 Reg. 5; FCA FSMA s. 19 general prohibition) at the activity-level — partially in [[Insurance Distribution]] but not from a "what an unauthorised person may not do on a call" angle
- **Auto-enrolment Retirement Savings Act 2024 (My Future Fund)** — no concept page; relevant to most pension calls
- **GDPR call-recording lawful basis & PII handoff** — no dedicated page; touched in [[Data Retention]] only

## Open questions for the Designer / Reviewer workspaces

1. Should the agent flag "Pass with comments" caliber issues (single absolute, light marketing tone) at all in v1, or only "Fail" caliber issues, to keep precision high?
2. The reviewers sometimes overrule a flagged risk on listening (see Q3-25-PC-01) — does the agent need an explicit "auto-overrule" path for known-benign phrases, or should we let the human reviewer continue to do that?
3. Multiple calls from the same staff member show repeating phrasing ("what we're seeing companies do", "you could keep that at 1%"). Should the agent surface staff-member-level patterns over time, or stay call-by-call in v1?
4. PII handling spans transcript and *out-of-call action* (e.g. emailing a spreadsheet). Is the agent's perimeter just the transcript, or also the call's stated action items?

## Source list

All 13 reviewed calls live as pages under the **☎️ Call Supervision Audit** Notion database (MCC Supervision teamspace). They are referenced here by case ID, not customer name.
