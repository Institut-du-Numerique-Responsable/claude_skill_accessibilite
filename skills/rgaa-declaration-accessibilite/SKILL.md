---
name: rgaa-declaration-accessibilite
version: 2.0.0
description: Use when a user needs to draft, update, or review a French accessibility declaration (déclaration d'accessibilité) for a public-sector website, app, or intranet under RGAA 4.1.2 / article 47 of loi n°2005-102. Triggers on "déclaration d'accessibilité", "RGAA", "audit accessibilité conformité", or requests to fill the gouv.fr accessibility declaration template.
repository: https://github.com/Institut-du-Numerique-Responsable/claude_skill_accessibilite
tags: [accessibility, rgaa, french, government, compliance, declaration]
license: MIT
---

# RGAA Accessibility Declaration (RGAA 4.1.2)

## Overview

Generates a French public-sector accessibility declaration that **strictly follows** the
official RGAA 4.1.2 template published at:
- [Design system de l'État - Modèle de déclaration](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/)
- [Obligations légales - accessibilite.numerique.gouv.fr](https://accessibilite.numerique.gouv.fr/obligations/declaration-accessibilite/)

**Key compliance requirements enforced by this skill:**
- Targets **RGAA 4.1.2** explicitly (RGAA 5 is announced for end of 2026 but not yet applicable).
- **Distinguishes** between percentage of criteria respected and average conformity rate.
- **Requires** justification and accessible alternative for each disproportionate burden derogation.
- **Requires** links to the multi-year accessibility scheme (schéma pluriannuel) and action plan.
- Legal wording (article 47, Défenseur des droits procedure) stays **verbatim**.
- Signals missing information explicitly — **never invents** audit data.

## When to Use

- User wants to publish or update a `déclaration d'accessibilité` page for a public site/app.
- User has RGAA 4.1.2 audit results to turn into a legal declaration.
- User asks about the legal recourse section, disproportionate burden exemptions, or **Disproportionate burden** derogations.

**Not for:** General accessibility code fixes (WCAG/RGAA remediation) — that is a separate audit/dev task, not a declaration-drafting task.

**Not for:** Multi-year accessibility scheme (schéma pluriannuel) as a standalone deliverable — this skill only generates the declaration itself.

## Required Inputs

**Ask the user for whatever is missing before generating the declaration.**
**Validate coherence before output:**
- "totalement conforme" requires 100% compliance rate (Compliance rate)
- "partiellement conforme" requires >= 50% and < 100% compliance rate
- "non conforme" requires < 50% compliance rate

**Note:** Compliance level must match the compliance rate. The skill distinguishes between **percentage of criteria respected** and **average conformity rate**.

### Organisation and Service
| Field | Required | Example |
|---|---|---|
| Organisation name | ✅ | "Institut du Numérique Responsable" |
| Service name | ✅ | "Site web de l'INR" |
| Site/app URL | ✅ | "https://institutnr.org" |

### Audit Information
| Field | Required | Example |
|---|---|---|
| RGAA version | ✅ | "RGAA 4.1.2" (fixed) |
| Audit date | ✅ | "12/03/2026" |
| Auditor | ✅ | "Société Audit Accessibilité" |

### Conformity Status
| Field | Required | Example | Validation |
|---|---|---|---|
| Conformity level | ✅ | non conforme / partiellement conforme / totalement conforme | Must match rate |
| **Percentage of criteria respected** | ✅ | "72%" | Must be 0-100 |
| **Average conformity rate** | ✅ | "85%" | Must be 0-100 |

### Non-Conformities
| Field | Required | Example |
|---|---|---|
| Non-conformities list | ✅ | Each: title + description + remediation deadline |

### Disproportionate Burden Derogations
| Field | Required | Example | Validation |
|---|---|---|---|
| Derogation title | ✅ | "Vidéos pré-existantes" | |
| Derogation description | ✅ | "150 vidéos sans sous-titres" | |
| **Justification** | ✅ | "Coût estimé à 50 000€" | **Mandatory** |
| **Accessible alternative** | ⚠️ | "Transcripts disponibles sur demande" | Required if exists |

### Technical Context
| Field | Required | Example |
|---|---|---|
| Technologies used | ✅ | HTML5, CSS, JS, ARIA |
| Test environments | ✅ | Firefox + NVDA, Safari + VoiceOver |
| Evaluation tools | ✅ | Tanaguru, AccessiNum |
| Sample pages tested | ✅ | List of URLs |

### Strategy and Plans
| Field | Required | Example |
|---|---|---|
| **Accessibility strategy** | ✅ | "Formation annuelle des équipes, audits trimestriels..." |
| **Multi-year scheme URL** | ⚠️ | "https://exemple.gouv.fr/schema-pluriannuel" | Required if exists |
| **Action plan URL** | ⚠️ | "https://exemple.gouv.fr/plan-action" | Required if exists |

### Publication
| Field | Required | Example |
|---|---|---|
| Declaration establishment date | ✅ | "01/01/2026" |
| Declaration last update date | ✅ | "27/08/2026" |
| Contact method | ✅ | "accessibilite@exemple.gouv.fr" |

## Generation Steps

1. **Collect all required inputs** (ask concise follow-up questions for gaps only).
2. **Validate coherence:**
   - Conformity level must match both percentage rates
   - All derogations must have justification
   - All placeholders must be filled before output
3. **Check mandatory links:**
   - If multi-year scheme exists: require `lien_schema_pluriannuel`
   - If action plan exists: require `lien_plan_action`
4. Copy `template.md` and substitute all `{{placeholders}}`.
5. Keep the legal sections **unchanged word-for-word:**
   - Commitment intro: "article 47 de la loi n°2005-102 du 11 février 2005"
   - Recourse section: Défenseur des droits online form, regional delegates, postal address "Libre réponse 71120, 75342 Paris CEDEX 07"
6. Output as **Markdown** ready to publish.
7. If any required field is missing, **stop and ask** — do not generate incomplete declaration.
8. If the user has no audit yet, **say so explicitly** — do not invent compliance percentages or fabricate non-conformity lists.

## Common Mistakes

- ❌ Paraphrasing the legal recourse text — it **must stay exact**, it's a legal requirement.
- ❌ Inventing audit numbers when none were provided — **ask instead**.
- ❌ Omitting the disproportionate burden section when it doesn't apply — state "Sans objet".
- ❌ Confusing "percentage of criteria respected" with "average conformity rate" — these are **two distinct metrics**.
- ❌ Omitting justification for derogations — **justification is mandatory**.
- ❌ Generating declaration without links to multi-year scheme and action plan (when they exist).

## Reference

- Full template with placeholders: [template.md](template.md)
- Official RGAA 4.1.2 template: [design.numerique.gouv.fr](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/)
- Legal obligations: [accessibilite.numerique.gouv.fr](https://accessibilite.numerique.gouv.fr/obligations/declaration-accessibilite/)
- Article 47: [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031977820)
