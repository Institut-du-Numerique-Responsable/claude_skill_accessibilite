---
name: rgaa-declaration-accessibilite
description: Use when a user needs to draft, update, or review a French accessibility declaration (déclaration d'accessibilité) for a public-sector website, app, or intranet under RGAA / article 47 of loi n°2005-102. Triggers on "déclaration d'accessibilité", "RGAA", "schéma pluriannuel", "audit accessibilité conformité", or requests to fill the gouv.fr accessibility declaration template.
---

# RGAA Accessibility Declaration

## Overview

Generates a French public-sector accessibility declaration that follows the
official template published at
https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/.
The legal wording (commitment statement, article 47 reference, recourse
procedure with the Défenseur des droits) must stay verbatim — only the
variable fields are filled in from user-provided facts.

## When to Use

- User wants to publish or update a `déclaration d'accessibilité` page for a
  public site/app.
- User has RGAA audit results (conformity %, non-conformities) to turn into
  a legal declaration.
- User asks about the legal recourse section, disproportionate burden
  exemptions, or multi-year accessibility scheme (schéma pluriannuel).

Not for: general accessibility code fixes (WCAG/RGAA remediation) — that is
a separate audit/dev task, not a declaration-drafting task.

## Required Inputs

Ask the user for whatever is missing before generating the declaration:

| Field | Example |
|---|---|
| Organisation name | "Institut du Numérique Responsable" |
| Site/app name + URL | "www.exemple.gouv.fr" |
| RGAA version used | "RGAA 4.1" |
| Audit date | "12/03/2026" |
| Compliance level | non conforme / partiellement conforme / totalement conforme |
| Compliance rate | e.g. "72%" |
| Non-conformities list | content + remediation deadline |
| Disproportionate burden items | content + justification |
| Technologies used | HTML5, CSS, JS, ARIA... |
| Test environments | e.g. Firefox + NVDA, Safari + VoiceOver |
| Sample pages tested | list of URLs |
| Contact method | form/email to reach the responsable |

## Generation Steps

1. Collect inputs above (ask concise follow-up questions for gaps only).
2. Copy `template.md` and substitute `{{placeholders}}`.
3. Keep the legal sections unchanged word-for-word:
   - Commitment intro citing "article 47 de la loi n°2005-102 du 11 février 2005"
   - Recourse section (Défenseur des droits: online form, regional delegates,
     postal address "Libre réponse 71120, 75342 Paris CEDEX 07")
4. Output as Markdown (or HTML if the target site needs it) ready to publish.
5. If the user has no audit yet, say so explicitly — do not invent compliance
   percentages or fabricate non-conformity lists.

## Common Mistakes

- Paraphrasing the legal recourse text — it must stay exact, it's a legal
  requirement, not marketing copy.
- Inventing audit numbers when none were provided — ask instead.
- Omitting the disproportionate burden section when it doesn't apply — state
  "Sans objet" rather than deleting the heading, so the declaration stays
  auditable against the standard structure.

## Reference

Full template with placeholders: [template.md](template.md)
