# Sécurité

Ce document décrit la politique de sécurité du projet **claude_skill_accessibilite** et explique comment signaler des vulnérabilités.

## Signalement des vulnérabilités

Si vous découvrez une vulnérabilité de sécurité dans ce projet, **ne créez pas d'issue publique**. À la place :

1. **Envoyez un e-mail** à : `security@institutnr.org`
2. **Incluez** dans votre message :
   - Une description claire de la vulnérabilité
   - Les étapes pour la reproduire
   - L'impact potentiel
   - Les versions affectées (le cas échéant)

L'équipe de l'Institut du Numérique Responsable accusera réception dans les **48 heures** et fournira une estimation du délai de correction.

## Champ d'application

Cette politique s'applique à :
- Le code source du skill `rgaa-declaration-accessibilite`
- Le template de déclaration d'accessibilité
- La page publique (GitHub Pages)
- La documentation

## Engagement

Nous nous engageons à :
- Accuser réception de votre signalement sous 48 heures
- Traiter les vulnérabilités critiques sous 7 jours
- Maintenir la confidentialité jusqu'à la publication d'un correctif
- Créditer les découvreurs (si désiré) dans les notes de version

## Déploiement

Ce projet est un dépôt public statique. Il n'y a pas :
- De backend ou de serveur à exploiter
- De base de données
- De dépendances externes (le skill utilise uniquement Python 3 standard library)
- De collecte de données utilisateur

Les seules surfaces d'attaque potentielles sont :
- Le contenu généré (déclarations d'accessibilité) - vérifiez toujours les sorties
- La page GitHub Pages - hébergée par GitHub avec leurs propres protections

## Bonnes pratiques

- **Validez toujours** les déclarations générées avant publication
- **Ne partagez pas** de données sensibles avec le skill
- **Vérifiez** que vos entrées RGAA sont correctes avant génération
- **Signalez** toute activité suspecte à security@institutnr.org

## Exclusions

Les problèmes suivants ne sont **pas** considérés comme des vulnérabilités de sécurité :
- Problèmes de conformité RGAA dans les déclarations générées (c'est la responsabilité de l'utilisateur de fournir des données d'audit correctes)
- Fautes d'orthographe ou erreurs de documentation
- Fonctionnalités manquantes (utilisez les issues GitHub)

---

*Dernière mise à jour : 27 août 2026*
