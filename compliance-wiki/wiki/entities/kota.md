---
title: Kota
type: entity
tags:
  - entity/internal
  - regulation/cbi
  - regulation/fca
  - compliance/aml
  - compliance/kyb
created: 2026-04-07
updated: 2026-04-07
status: active
---

# Kota

## Overview
Kota is a CBI-regulated insurance intermediary operating two product verticals:

- **Platform** — Direct employer onboarding for group insurance products (Health, Pensions, Income Protection, PEPP).
- **Embed (Developer)** — API and UI component integrations enabling partner platforms (Remote, Employment Hero, Helios, Globalli) to create and manage employers through Kota's infrastructure.

Kota operates across EU/EEA markets and in the UK as an appointed representative of Innovative Risk Labs Ltd (FCA-regulated).

## Regulatory Status
- **Ireland**: Regulated by the [[Central Bank of Ireland]] as an insurance intermediary.
- **UK**: Appointed representative of Innovative Risk Labs Ltd, regulated by the [[FCA]].

## Products
| Product | KYB Tier | Notes |
|---------|----------|-------|
| Health | Light | Sanctions only, no PEP/UBO requirements |
| Pensions (Group) | Mid | Full screening, director/UBO ID for high risk only |
| Income Protection (Group) | Full | All identification and screening mandatory |
| PEPP | Full (TBC) | Risk assessment outstanding for director/UBO ID |

See [[KYB Requirements by Product Type]] for the full matrix.

## Current Compliance Stack
- **Sanctions/PEP screening**: [[ComplyAdvantage]] (Mesh interface, ~70–85% fuzzy matching)
- **KYB**: Gap — no dedicated KYB provider. Evaluation underway (see [[Kota KYB Software Requirements]]).

## Key Compliance Priorities
1. Select and implement a KYB software provider.
2. Complete PEPP product risk assessment.
3. Resolve ComplyAdvantage pain points (false positives, test data contamination).
4. Ensure Embed partner integrations meet AML/KYB obligations at both partner and employer level.

## Sources
- [[Kota KYB Software Requirements]]
- [[KYB Requirements by Product Type]]
- [[Case Creation Workflow Notes]]
