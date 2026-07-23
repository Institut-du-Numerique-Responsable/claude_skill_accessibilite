# Claude Skill — Déclaration d'accessibilité RGAA

[![Licence MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)
[![RGAA 4](https://img.shields.io/badge/RGAA-4-005AEE.svg)](https://accessibilite.numerique.gouv.fr/)
[![Page publique](https://img.shields.io/badge/page-en%20ligne-brightgreen.svg)](https://institut-du-numerique-responsable.github.io/claude_skill_accessibilite/)
[![PR bienvenues](https://img.shields.io/badge/PR-bienvenues-orange.svg)](CONTRIBUTING.md)

Skill [Claude Code](https://claude.com/claude-code) / [Claude Skills](https://www.anthropic.com/news/skills)
pour générer et mettre à jour une **déclaration d'accessibilité** conforme au
modèle officiel du [design system de l'État](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/),
au titre de l'article 47 de la loi n°2005-102 et du **RGAA** (Référentiel
Général d'Amélioration de l'Accessibilité).

Publié par l'[Institut du Numérique Responsable](https://institutnr.org/).
Page publique du projet : https://institut-du-numerique-responsable.github.io/claude_skill_accessibilite/

## Sommaire

- [Pourquoi ce skill](#pourquoi-ce-skill)
- [Ce qu'il fait](#ce-quil-fait)
- [Ce qu'il ne fait pas](#ce-quil-ne-fait-pas)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple](#exemple)
- [Structure du dépôt](#structure-du-dépôt)
- [Champs attendus](#champs-attendus)
- [Contribuer](#contribuer)
- [Sécurité et fiabilité](#sécurité-et-fiabilité)
- [Ressources officielles](#ressources-officielles)
- [Mots-clés](#mots-clés)
- [Licence](#licence)

## Pourquoi ce skill

Toute entité publique (État, collectivités, établissements publics,
organismes délégataires de service public...) doit publier une déclaration
d'accessibilité conforme à un modèle officiel strict, incluant des mentions
légales exactes (article 47 de la loi n°2005-102, procédure de recours
Défenseur des droits). Rédiger cette déclaration à la main est répétitif et
source d'erreurs : oubli de section, reformulation involontaire du texte
légal, taux de conformité incohérents avec l'audit. Ce skill structure la
collecte des données d'audit et génère la déclaration à partir du modèle
officiel, sans jamais inventer de résultat.

## Ce qu'il fait

- Recueille les données nécessaires : audit RGAA, taux de conformité,
  non-conformités avec échéances, dérogations pour charge disproportionnée,
  environnements de test, technologies utilisées, pages vérifiées.
- Génère une déclaration d'accessibilité complète en Markdown, à partir de
  [`template.md`](skills/rgaa-declaration-accessibilite/template.md).
- Conserve **mot pour mot** les mentions légales : engagement au titre de
  l'article 47, procédure de recours auprès du Défenseur des droits.
- Signale explicitement les informations manquantes plutôt que de les
  deviner.

## Ce qu'il ne fait pas

- Ne réalise pas l'audit RGAA lui-même (utiliser un outil d'audit dédié ou un
  auditeur RGAA qualifié).
- Ne corrige pas le code pour rendre un site accessible — c'est un skill de
  **rédaction de déclaration**, pas de remédiation technique.
- N'invente pas de taux de conformité ni de liste de non-conformités : sans
  audit fourni, il le dit et s'arrête.

## Installation

Copier le dossier du skill dans le répertoire de skills Claude :

```bash
cp -r skills/rgaa-declaration-accessibilite ~/.claude/skills/
```

Ou l'ajouter comme skill de projet en le plaçant dans
`.claude/skills/` à la racine d'un projet.

## Utilisation

Dans Claude Code, invoquer le skill dès qu'une tâche concerne :

- une déclaration d'accessibilité à créer ou mettre à jour,
- un audit RGAA à formaliser en déclaration légale,
- un schéma pluriannuel d'accessibilité.

Claude pose les questions nécessaires pour les champs manquants (voir
[Champs attendus](#champs-attendus)), puis génère la déclaration. Le détail
du déroulé est documenté dans
[`SKILL.md`](skills/rgaa-declaration-accessibilite/SKILL.md).

## Exemple

**Demande :**

> Génère la déclaration d'accessibilité pour www.exemple.gouv.fr. Audit RGAA
> 4.1 du 12/03/2026, 72% de conformité, non-conforme sur les formulaires
> (échéance T3 2026), pas de dérogation. Contact via formulaire en ligne.

**Sortie (extrait) :**

```markdown
## État de conformité

www.exemple.gouv.fr est partiellement conforme avec le référentiel général
d'amélioration de l'accessibilité (RGAA 4.1), en raison des non-conformités
et des dérogations énumérées ci-dessous.

Résultats des tests : l'audit de conformité réalisé le 12/03/2026 révèle
que 72% des critères RGAA sont respectés.

## Contenus non accessibles

### Non-conformités

- Formulaires : erreurs de saisie non annoncées aux lecteurs d'écran.
  Échéance de mise en conformité : T3 2026.

### Dérogations pour charge disproportionnée

Sans objet.
```

Les champs non fournis (technologies, environnements de test, pages
vérifiées...) sont demandés avant génération, pas inventés.

## Structure du dépôt

```
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   └── index.html                 # page publique (GitHub Pages)
└── skills/
    └── rgaa-declaration-accessibilite/
        ├── SKILL.md                # déclencheurs, champs, étapes de génération
        └── template.md             # modèle officiel avec {{placeholders}}
```

## Champs attendus

| Champ | Exemple |
|---|---|
| Organisation | Institut du Numérique Responsable |
| Site/app + URL | www.exemple.gouv.fr |
| Version RGAA | RGAA 4.1 |
| Date de l'audit | 12/03/2026 |
| Niveau de conformité | non / partiellement / totalement conforme |
| Taux de conformité | 72% |
| Non-conformités | contenu + échéance |
| Dérogations | contenu + justification |
| Technologies | HTML5, CSS, JS, ARIA... |
| Environnements de test | Firefox + NVDA, Safari + VoiceOver |
| Pages vérifiées | liste d'URLs |
| Contact | formulaire, email, responsable |

Détail complet dans [`SKILL.md`](skills/rgaa-declaration-accessibilite/SKILL.md#required-inputs).

## Contribuer

Contributions bienvenues via **pull request** — pas de push direct sur
`main` (branche protégée, revue requise). Voir
[CONTRIBUTING.md](CONTRIBUTING.md). Toute modification du texte légal
(engagement article 47, procédure de recours) doit être justifiée par un
écart avéré avec le modèle officiel gouv.fr, pas une reformulation de style.

## Sécurité et fiabilité

- Le skill ne fabrique jamais de résultat d'audit : en l'absence de données,
  il pose la question plutôt que de compléter arbitrairement.
- Les sections légales (recours Défenseur des droits, engagement article 47)
  sont fixes et ne doivent pas être paraphrasées.
- Signaler tout écart entre `template.md` et le modèle officiel via une
  [issue](../../issues).

## Ressources officielles

- [Modèle officiel de déclaration d'accessibilité](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/) — design system de l'État
- [RGAA — Référentiel Général d'Amélioration de l'Accessibilité (version 4)](https://accessibilite.numerique.gouv.fr/) — déclinaison française des WCAG, référentiel applicable en France
- [WCAG — Web Content Accessibility Guidelines (W3C)](https://www.w3.org/WAI/standards-guidelines/wcag/) — norme internationale dont le RGAA est la transposition réglementaire française
- [Article 47 de la loi n°2005-102 du 11 février 2005](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031977820) — obligation légale d'accessibilité
- [Obligation de déclaration d'accessibilité (accessibilite.numerique.gouv.fr)](https://accessibilite.numerique.gouv.fr/obligations/) — qui est concerné, contenu obligatoire, sanctions
- [Défenseur des droits — formulaire de saisine](https://formulaire.defenseurdesdroits.fr/)

## Mots-clés

RGAA, accessibilité numérique, déclaration d'accessibilité, article 47 loi
2005-102, WCAG, écoconception, numérique responsable, Claude Skill, Claude
Code, secteur public, service public numérique.

## Licence

[MIT](LICENSE) — Institut du Numérique Responsable
