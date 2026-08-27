# Créez une déclaration d’accessibilité RGAA conforme

[![Licence MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)
[![RGAA 4.1.2](https://img.shields.io/badge/RGAA-4.1.2-005AEE.svg)](https://accessibilite.numerique.gouv.fr/)
[![Page publique](https://img.shields.io/badge/page-en%20ligne-brightgreen.svg)](https://institut-du-numerique-responsable.github.io/claude_skill_accessibilite/)
[![PR bienvenues](https://img.shields.io/badge/PR-bienvenues-orange.svg)](CONTRIBUTING.md)

**Skill Claude Code** pour générer une **déclaration d’accessibilité RGAA 4.1.2** conforme au modèle officiel de l’État, au titre de l’**article 47 de la loi n°2005-102**.

Publié par l’[Institut du Numérique Responsable](https://institutnr.org/).
Page publique : [institut-du-numerique-responsable.github.io/claude_skill_accessibilite](https://institut-du-numerique-responsable.github.io/claude_skill_accessibilite/)

---

## Publics prioritaires

| Public | Description |
|--------|-------------|
| **Responsables accessibilité** | Dans les administrations publiques (État, collectivités, établissements publics) |
| **Secteur public** | Organismes délégataires de service public |
| **Développeurs** | Équipes techniques en charge de la conformité accessibilité |

---

## Pourquoi ce skill

Toute entité publique doit publier une **déclaration d’accessibilité** conforme à un modèle officiel strict.

Rédiger ce document manuellement est **source d’erreurs** :
- Oubli de sections obligatoires
- Taux de conformité incohérents avec l’audit
- Reformulation involontaire du texte légal
- Confusion entre les deux métriques (pourcentage de critères respectés vs taux moyen de conformité)

Ce skill **structure la collecte des données d’audit** et génère la déclaration à partir du [modèle officiel du design system de l’État](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/), **sans jamais inventer de résultat**.

---

## Parcours éditorial

### 1️⃣ Audit RGAA
Réalisez un audit complet avec un outil qualifié (Tanaguru, AccessiNum) ou un auditeur certifié.
Notez :
- Les non-conformités relevées
- Les dérogations pour charge disproportionnée
- Les taux de conformité (pourcentage de critères respectés ET taux moyen)

### 2️⃣ Données vérifiées
Le skill collecte vos données et **valide leur cohérence** :
- Niveau de conformité (totalement/partiellement/non conforme) doit matcher les taux
- Toute dérogation doit avoir une justification **et** une alternative accessible
- Tous les champs obligatoires sont présents

### 3️⃣ Déclaration prête à publier
Génération automatique d’une **déclaration Markdown conforme**, prête à être publiée.
Tous les liens officiels (Défenseur des droits, modèle gouv.fr) sont inclus.

---

## Ce qu’il fait

✅ **Collecte** les données nécessaires :
- Audit RGAA 4.1.2 (date, auditeur)
- **Pourcentage de critères respectés** et **taux moyen de conformité** (deux métriques distinctes)
- Non-conformités avec échéances de correction
- Dérogations avec justification **et alternative accessible**
- Technologies, environnements de test, pages vérifiées
- Liens vers le **schéma pluriannuel** et le **plan d’action** (quand ils existent)

✅ **Génère** une déclaration d’accessibilité complète en Markdown, à partir de [`template.md`](skills/rgaa-declaration-accessibilite/template.md).

✅ **Conserve mot pour mot** les mentions légales :
- Engagement au titre de l’**article 47 de la loi n°2005-102 du 11 février 2005**
- Procédure de recours auprès du **Défenseur des droits**

✅ **Signale explicitement** les informations manquantes plutôt que de les deviner.

---

## Ce qu’il ne fait pas

❌ **Ne réalise pas** l’audit RGAA lui-même (utiliser un outil d’audit dédié ou un auditeur RGAA qualifié).

❌ **Ne corrige pas** le code pour rendre un site accessible — c’est un skill de **rédaction de déclaration**, pas de remédiation technique.

❌ **N’invente pas** de taux de conformité ni de liste de non-conformités : sans audit fourni, il le signale et s’arrête.

❌ **Ne traite pas** le schéma pluriannuel comme un livrable autonome — ce skill génère uniquement la déclaration.

---

## Installation

Copiez le dossier du skill dans votre répertoire de skills Claude :

```bash
cp -r skills/rgaa-declaration-accessibilite ~/.claude/skills/
```

Ou placez-le dans `.claude/skills/` à la racine d’un projet pour l’activer uniquement sur ce projet.

---

## Utilisation

Dans **Claude Code**, invoquez le skill dès qu’une tâche concerne :
- Une déclaration d’accessibilité à créer ou mettre à jour
- Un audit RGAA à formaliser en déclaration légale

Claude pose les questions nécessaires pour les **champs manquants** (voir [Champs attendus](#champs-attendus)), puis génère la déclaration.
Le détail du déroulé est documenté dans [`SKILL.md`](skills/rgaa-declaration-accessibilite/SKILL.md).

---

## Exemple

**Demande :**

> Génère la déclaration d’accessibilité pour www.exemple.gouv.fr. 
> Audit RGAA 4.1.2 du 12/03/2026, partiellement conforme, 
> 72% de critères respectés, taux moyen de conformité 85%, 
> non-conformité sur les formulaires (échéance T3 2026), 
> dérogation pour les vidéos (justification : coût de 50 000€, alternative : transcripts disponibles).

**Sortie (extrait) :**

```markdown
## État de conformité

www.exemple.gouv.fr est partiellement conforme avec le référentiel général
d’amélioration de l’accessibilité (RGAA 4.1.2), en raison des non-conformités
et des dérogations énumérées ci-dessous.

**Résultats des tests** :
- **Pourcentage de critères respectés** : 72%
- **Taux moyen de conformité** des critères applicables : 85%

## Contenus non accessibles

### Non-conformités
- **Formulaires** : erreurs de saisie non annoncées aux lecteurs d’écran.
  Échéance de mise en conformité : T3 2026.

### Dérogations pour charge disproportionnée
- **Vidéos pré-existantes** : 150 vidéos sans sous-titres.
  **Justification** : Coût estimé à 50 000€.
  **Alternative accessible** : Transcripts disponibles sur demande.
```

Les champs non fournis sont **demandés avant génération**, jamais inventés.

---

## Champs attendus

| Champ | Obligatoire | Exemple |
|-------|-------------|---------|
| Organisation | ✅ | Institut du Numérique Responsable |
| Service | ✅ | Site web de l’INR |
| URL du site/app | ✅ | https://institutnr.org |
| Version RGAA | ✅ | RGAA 4.1.2 (fixe) |
| Date de l’audit | ✅ | 12/03/2026 |
| Auditeur | ✅ | Société Audit Accessibilité |
| Niveau de conformité | ✅ | non / partiellement / totalement conforme |
| **Pourcentage de critères respectés** | ✅ | 72% |
| **Taux moyen de conformité** | ✅ | 85% |
| Non-conformités | ✅ | titre + description + échéance |
| Dérogations | ✅ | titre + description + justification + **alternative accessible** |
| Schéma pluriannuel (URL) | ⚠️ | https://exemple.gouv.fr/schema-pluriannuel |
| Plan d’action (URL) | ⚠️ | https://exemple.gouv.fr/plan-action |
| Stratégie d’accessibilité | ✅ | Formation annuelle, audits trimestriels… |
| Technologies | ✅ | HTML5, CSS, JS, ARIA… |
| Environnements de test | ✅ | Firefox + NVDA, Safari + VoiceOver |
| Outils d’évaluation | ✅ | Tanaguru, AccessiNum |
| Pages vérifiées | ✅ | Liste d’URLs |
| Date établissement déclaration | ✅ | 01/01/2026 |
| Date dernière mise à jour | ✅ | 27/08/2026 |
| Contact | ✅ | accessibilite@exemple.gouv.fr |

> ⚠️ = Requis si applicable. Le skill signale explicitement les champs manquants.

Détail complet dans [`SKILL.md`](skills/rgaa-declaration-accessibilite/SKILL.md).

---

## Validations automatiques

Le skill **valide la cohérence** des données avant génération :

| Règle | Condition |
|-------|-----------|
| Niveau = Totalement conforme | Doit avoir **100%** pour les deux taux |
| Niveau = Partiellement conforme | Doit avoir **>= 50%** et **< 100%** pour les deux taux |
| Niveau = Non conforme | Doit avoir **< 50%** pour les deux taux |
| Dérogation | Doit avoir une **justification** |
| Dérogation avec alternative | Doit inclure l’**alternative accessible** si elle existe |

---

## Structure du dépôt

```
.
├── README.md                    # Documentation principale
├── CONTRIBUTING.md             # Règles de contribution
├── LICENSE                     # Licence MIT
├── CHANGELOG.md                # Historique des modifications
├── SECURITY.md                 # Politique de sécurité
├── docs/
│   ├── index.html              # Page publique (GitHub Pages)
│   ├── llms.txt                # Résumé pour les assistants IA
│   ├── robots.txt              # Directives d’exploration
│   └── sitemap.xml             # Plan du site
└── skills/
    └── rgaa-declaration-accessibilite/
        ├── SKILL.md             # Déclencheurs, champs, étapes
        └── template.md          # Modèle RGAA 4.1.2 avec placeholders

└── tests/
    └── test_project.py          # Tests de conformité (23 tests)

└── .github/
    ├── workflows/
    │   └── quality.yml          # Intégration continue
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        └── bug.yml
```

---

## Contribuer

Les contributions sont bienvenues via **pull request** — pas de push direct sur `main` (branche protégée, revue requise).

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

**Règles spécifiques :**
- Toute modification du **texte légal** (engagement article 47, procédure de recours) doit être justifiée par un écart avéré avec le modèle officiel gouv.fr, **pas une reformulation de style**.
- Les tests doivent **tous passer** avant fusion.
- Les commits ne doivent **jamais** créditer une IA comme auteur ou co-auteur.

---

## Sécurité et fiabilité

✅ **Le skill ne fabrique jamais** de résultat d’audit : en l’absence de données, il pose la question plutôt que de compléter arbitrairement.

✅ **Les sections légales** (recours Défenseur des droits, engagement article 47) sont **fixes** et ne doivent pas être paraphrasées.

✅ **Signaler tout écart** entre `template.md` et le modèle officiel via une [issue](../../issues).

---

## Ressources officielles

| Ressource | Description |
|-----------|-------------|
| [Modèle officiel](https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/) | Design system de l’État — modèle à suivre |
| [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) | Référentiel officiel applicable en France |
| [Obligations légales](https://accessibilite.numerique.gouv.fr/obligations/declaration-accessibilite/) | Qui est concerné, contenu obligatoire, sanctions |
| [Article 47](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031977820) | Obligation légale (loi n°2005-102) |
| [Défenseur des droits](https://formulaire.defenseurdesdroits.fr/) | Formule de saisine en ligne |

---

## Limites

⚠️ **Le skill ne réalise pas l’audit** : un audit RGAA 4.1.2 pré-existant est **obligatoire**.

⚠️ **Les résultats générés dépendent de la qualité des données fournies** : le skill valide la cohérence formelle, pas l’exactitude des audits.

⚠️ **Pour les schémas pluriannuels** : ce skill génère uniquement la déclaration. Le schéma pluriannuel est un document séparé.

---

## Mots-clés

RGAA 4.1.2, accessibilité numérique, déclaration d’accessibilité, article 47 loi 2005-102, WCAG, écoconception, numérique responsable, secteur public, service public numérique, responsable accessibilité.

---

## Licence

[MIT](LICENSE) — Institut du Numérique Responsable
