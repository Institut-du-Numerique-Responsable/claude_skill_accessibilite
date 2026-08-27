# Déclaration d'accessibilité

## Engagement et stratégie

{{organisation}} s'engage à rendre {{service}} accessible conformément à l'article 47 de la loi n°2005-102 du 11 février 2005.

À cette fin, {{organisation}} met en œuvre la stratégie et les actions suivantes :
{{strategie_accessibilite}}

Cette déclaration d'accessibilité s'applique à **{{nom_site}}** ({{url_site}}).

> [Voir le schéma pluriannuel d'accessibilité de {{organisation}}]({{lien_schema_pluriannuel}})
> [Voir le plan d'action associé]({{lien_plan_action}})

## État de conformité

**{{nom_site}}** est **{{niveau_conformite}}** avec le référentiel général d'amélioration de l'accessibilité (RGAA 4.1.2), en raison des non-conformités et des dérogations énumérées ci-dessous.

**Résultats des tests** :
- **Pourcentage de critères respectés** : l'audit de conformité réalisé le {{date_audit}} par {{auditeur}} révèle que **{{pourcentage_criteres_respectes}}%** des critères RGAA sont respectés.
- **Taux moyen de conformité** des critères applicables : **{{taux_moyen_conformite}}%**. 

## Contenus non accessibles

### Non-conformités

{{#chaque_non_conformite}}
- **{{titre}}** : {{description}}. Échéance de mise en conformité : {{echeance}}.
{{/chaque_non_conformite}}

### Dérogations pour charge disproportionnée

{{#chaque_derogation}}
- **{{titre}}** : {{description}}. 
  **Justification** : {{justification}}.
  {{#alternative_accessible}}**Alternative accessible** : {{alternative_accessible}}{{/alternative_accessible}}
{{/chaque_derogation}}

<!-- Si aucune dérogation ne s'applique, indiquer "Sans objet". -->

### Contenus non soumis à l'obligation d'accessibilité

{{contenus_hors_obligation}}
<!-- Ex : contenus tiers non contrôlés, fichiers bureautiques antérieurs au 23/09/2018, etc. -->

## Établissement de cette déclaration d'accessibilité

Cette déclaration a été établie le {{date_etablissement}}.
Elle a été mise à jour le {{date_maj}}.

**Technologies utilisées pour la réalisation de {{service}} :**

{{#technologies}}
- {{technologie}}
{{/technologies}}

**Environnement de test** :
Les vérifications de restitution de contenus ont été réalisées sur la base de la combinaison fournie par {{organisation}}, avec les technologies d'assistance suivantes :

{{#environnements_test}}
- {{navigateur}} et {{lecteur_ecran}}
{{/environnements_test}}

**Outils d'évaluation utilisés :**

{{#outils_evaluation}}
- {{outil}}
{{/outils_evaluation}}

**Échantillon :**

{{#pages_verifiees}}
- [{{page}}]({{url_page}})
{{/pages_verifiees}}

## Retour d'information et contact

Si vous n'arrivez pas à accéder à un contenu ou à un service, vous pouvez contacter le responsable de {{service}} pour être orienté vers une alternative accessible ou obtenir le contenu sous une autre forme.

{{#contacts}}
- {{contact}}
{{/contacts}}

## Voies de recours

Cette procédure est à utiliser dans le cas suivant : vous avez signalé au responsable du site internet un défaut d'accessibilité qui vous empêche d'accéder à un contenu ou à un des services du portail et vous n'avez pas obtenu de réponse satisfaisante.

Vous pouvez :

- [Écrire un message au Défenseur des droits](https://formulaire.defenseurdesdroits.fr/)
- [Contacter le délégué du Défenseur des droits dans votre région](https://www.defenseurdesdroits.fr/saisir/delegues)
- Envoyer un courrier par la poste (gratuit, ne pas mettre de timbre) :

  ```
  Défenseur des droits
  Libre réponse 71120
  75342 Paris CEDEX 07
  ```

Pour en savoir plus sur les obligations légales : [Obligation de déclaration d'accessibilité](https://accessibilite.numerique.gouv.fr/obligations/declaration-accessibilite/)

---

*Cette déclaration a été générée à partir du [modèle officiel du design system de l'État](https://design.numerique.gouv.fr/outils/exemple-de-declaration-accessibilite/).*
