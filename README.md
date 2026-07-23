# Claude Skill — Déclaration d'accessibilité RGAA

Skill [Claude Code](https://claude.com/claude-code) / [Claude Skills](https://www.anthropic.com/news/skills)
pour générer et mettre à jour une **déclaration d'accessibilité** conforme au
modèle officiel du [design system de l'État](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/),
au titre de l'article 47 de la loi n°2005-102 et du **RGAA** (Référentiel
Général d'Amélioration de l'Accessibilité).

Publié par l'[Institut du Numérique Responsable](https://institutnr.org/).

## Ce que fait ce skill

- Collecte les informations nécessaires (audit RGAA, taux de conformité,
  non-conformités, dérogations, environnements de test...).
- Génère une déclaration d'accessibilité complète, au format Markdown,
  reprenant scrupuleusement le modèle officiel — y compris les mentions
  légales et la procédure de recours auprès du Défenseur des droits.
- Signale les informations manquantes plutôt que d'inventer des résultats
  d'audit ou des taux de conformité.

## Installation

Copier le dossier [`skills/rgaa-declaration-accessibilite`](skills/rgaa-declaration-accessibilite)
dans le répertoire de skills de votre installation Claude (ex.
`~/.claude/skills/`), ou l'ajouter comme skill de projet.

## Utilisation

Dans Claude Code, invoquer le skill dès qu'une tâche concerne une déclaration
d'accessibilité, un audit RGAA à formaliser, ou un schéma pluriannuel
d'accessibilité. Voir [`SKILL.md`](skills/rgaa-declaration-accessibilite/SKILL.md)
pour le détail des champs attendus et du déroulé de génération.

## Mots-clés

RGAA, accessibilité numérique, déclaration d'accessibilité, article 47 loi
2005-102, WCAG, écoconception, numérique responsable, Claude Skill, Claude
Code, secteur public, service public numérique.

## Contribuer

Les contributions sont bienvenues via **pull request** — voir
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE)
