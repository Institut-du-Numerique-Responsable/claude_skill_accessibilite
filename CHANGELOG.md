# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère à la [sémantique de version 2.0.0](https://semver.org/).

## [Non publié]

### Ajouté
- Ajout des tests de conformité RGAA 4.1.2 (`tests/test_project.py`)
- Intégration continue GitHub Actions (`.github/workflows/quality.yml`)
- Mise à jour complète du template pour RGAA 4.1.2 avec distinction entre pourcentage de critères respectés et taux moyen de conformité
- Ajout des liens vers schéma pluriannuel et plan d'action dans le template
- Exigence de justification et alternative accessible pour les dérogations
- Refonte de la page publique (`docs/index.html`) avec design accessible et parcours utilisateur en 3 étapes
- Métadonnées SEO complètes (canonical, Open Graph, JSON-LD)
- Mise à jour de `docs/llms.txt` avec liens directs vers les ressources

### Modifié
- `SKILL.md` : Mise à jour pour RGAA 4.1.2 avec champs requis détaillés et validations de cohérence
- `template.md` : Structure conforme au modèle officiel RGAA 4.1.2
- `README.md` : Exemples corrigés et documentation mise à jour
- `docs/sitemap.xml` : Ajout de la date de dernière modification

## [1.0.0] - 2026-07-23

### Ajouté
- Première version du skill `rgaa-declaration-accessibilite`
- Génération de déclarations d'accessibilité conformes au modèle officiel gouv.fr
- Page publique GitHub Pages
- Documentation complète (README, CONTRIBUTING)
- Modèle de déclaration d'accessibilité

[Non publié]: https://github.com/Institut-du-Numerique-Responsable/claude_skill_accessibilite/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Institut-du-Numerique-Responsable/claude_skill_accessibilite/releases/tag/v1.0.0
