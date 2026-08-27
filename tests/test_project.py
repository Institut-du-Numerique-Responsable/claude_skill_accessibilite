#!/usr/bin/env python3
"""
Tests de conformité pour le projet claude_skill_accessibilite.

Ces tests vérifient :
- La structure obligatoire du modèle RGAA (rubriques réglementaires)
- La cohérence entre état de conformité et taux de conformité
- Les métadonnées SEO (canonical, Open Graph, JSON-LD)
- Les liens officiels (Défenseur des droits, RGAA, etc.)
- L'absence d'attribution IA dans l'historique Git
- L'absence de placeholders dans les fichiers publics
- La validité HTML, JSON-LD, XML, Markdown
"""

import json
import os
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


class TestRGAAConformity(unittest.TestCase):
    """Tests liés à la conformité RGAA 4.1.2."""

    def setUp(self):
        self.repo_root = Path(__file__).parent.parent
        self.skill_dir = self.repo_root / "skills" / "rgaa-declaration-accessibilite"
        self.docs_dir = self.repo_root / "docs"
        self.template_path = self.skill_dir / "template.md"
        self.skill_path = self.skill_dir / "SKILL.md"
        self.readme_path = self.repo_root / "README.md"
        self.index_path = self.docs_dir / "index.html"
        self.llms_path = self.docs_dir / "llms.txt"
        self.robots_path = self.docs_dir / "robots.txt"
        self.sitemap_path = self.docs_dir / "sitemap.xml"

    # =========================================================================
    # TESTS 1 : STRUCTURE OBLIGATOIRE DU MODÈLE RGAA
    # =========================================================================

    def test_template_exists(self):
        """Le modèle template.md doit exister."""
        self.assertTrue(self.template_path.exists(),
                       f"Fichier {self.template_path} introuvable")

    def test_template_required_sections(self):
        """Le modèle doit contenir toutes les rubriques réglementaires RGAA 4.1.2."""
        required_sections = [
            "Engagement et stratégie",
            "État de conformité",
            "Résultats des tests",
            "Contenus non accessibles",
            "Établissement",
            "Environnement de test",
            "Outils",
            "Échantillon",
            "Contact",
            "Voies de recours",
        ]
        
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        
        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, content,
                             f"Section obligatoire '{section}' manquante dans template.md")

    def test_template_legal_mentions(self):
        """Le modèle doit contenir les mentions légales exactes."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        
        # Engagement article 47
        self.assertIn("article 47 de la loi n°2005-102 du 11 février 2005", content,
                     "Mention de l'article 47 manquante ou incorrecte")
        
        # Défenseur des droits (adresse postale officielle)
        self.assertIn("Libre réponse 71120", content,
                     "Adresse postale du Défenseur des droits manquante")
        self.assertIn("75342 Paris CEDEX 07", content,
                     "Code postal du Défenseur des droits manquant")

    def test_template_rgaa_version(self):
        """Le modèle doit cibler explicitement le RGAA 4.1.2."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        
        # Doit mentionner RGAA 4.1.2 (et non pas juste RGAA 4 ou 4.1)
        self.assertIn("RGAA 4.1.2", content,
                     "Version RGAA 4.1.2 non mentionnée explicitement")

    # =========================================================================
    # TESTS 2 : COHÉRENCE ÉTAT/TAUX
    # =========================================================================

    def test_readme_conformity_examples(self):
        """Les exemples dans README.md doivent respecter les seuils de conformité."""
        if not self.readme_path.exists():
            self.skipTest("README.md introuvable")
        
        content = self.readme_path.read_text()
        
        # Chercher les exemples de conformité dans les blocs de code ou exemples concrets
        # On cherche des phrases où l'état et le taux apparaissent dans la même ligne
        # EXCLURE les lignes de documentation (tableaux avec |, titres, listes à puces)
        lines = content.split('\n')
        
        for line in lines:
            # Ignorer les lignes qui ressemblent à de la documentation (tableaux, listes, titres)
            if line.strip().startswith(('|', '-', '#', '##', '**', '✅', '❌', '⚠️')):
                continue
            if not line.strip():
                continue
            
            # Chercher dans les lignes qui contiennent à la fois un état et un pourcentage
            state_pattern = r'(partiellement conforme|totalement conforme|non conforme)'
            rate_pattern = r'(\d+%|\d+,\d+%)'
            
            state_match = re.search(state_pattern, line, re.IGNORECASE)
            rate_match = re.search(rate_pattern, line)
            
            if state_match and rate_match:
                state = state_match.group(1).lower()
                rate_str = rate_match.group(1).replace('%', '').replace(',', '.')
                
                try:
                    rate = float(rate_str)
                except ValueError:
                    continue
                
                # Vérification des seuils
                if 'totalement conforme' in state:
                    self.assertEqual(rate, 100.0,
                                   f"État 'totalement conforme' avec taux {rate}% (doit être 100%) dans: {line.strip()}")
                elif 'partiellement conforme' in state:
                    self.assertGreaterEqual(rate, 50.0,
                                         f"État 'partiellement conforme' avec taux {rate}% (doit être >= 50%) dans: {line.strip()}")
                    self.assertLess(rate, 100.0,
                                 f"État 'partiellement conforme' avec taux {rate}% (doit être < 100%) dans: {line.strip()}")
                elif 'non conforme' in state:
                    self.assertLess(rate, 50.0,
                                 f"État 'non conforme' avec taux {rate}% (doit être < 50%) dans: {line.strip()}")

    def test_template_conformity_rates_distinction(self):
        """Le modèle doit distinguer pourcentage de critères respectés et taux moyen de conformité."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        
        # Doit mentionner les deux concepts distincts
        self.assertIn("pourcentage de critères respectés", content.lower(),
                     "Mention 'pourcentage de critères respectés' manquante")
        self.assertIn("taux moyen de conformité", content.lower(),
                     "Mention 'taux moyen de conformité' manquante")

    # =========================================================================
    # TESTS 3 : LIENS OFFICIELS
    # =========================================================================

    def test_template_official_links(self):
        """Le modèle doit contenir les liens officiels obligatoires."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        
        # Liens obligatoires
        required_links = [
            "accessibilite.numerique.gouv.fr",
            "formulaire.defenseurdesdroits.fr",
            "design.numerique.gouv.fr",
        ]
        
        for link in required_links:
            with self.subTest(link=link):
                self.assertIn(link, content,
                             f"Lien officiel {link} manquant dans template.md")

    def test_readme_official_links(self):
        """Le README doit contenir les références officielles."""
        if not self.readme_path.exists():
            self.skipTest("README.md introuvable")
        
        content = self.readme_path.read_text()
        
        required_links = [
            "https://accessibilite.numerique.gouv.fr/",
            "https://design.numerique.gouv.fr/outils/exemple-declaration-accessibilite/",
            "https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031977820",
        ]
        
        for link in required_links:
            with self.subTest(link=link):
                self.assertIn(link, content,
                             f"Lien officiel {link} manquant dans README.md")

    def test_skill_official_links(self):
        """Le SKILL.md doit référencer les sources officielles."""
        if not self.skill_path.exists():
            self.skipTest("SKILL.md introuvable")
        
        content = self.skill_path.read_text()
        
        self.assertIn("design.numerique.gouv.fr", content,
                     "Référence au design system de l'État manquante dans SKILL.md")

    # =========================================================================
    # TESTS 4 : MÉTADONNÉES SEO
    # =========================================================================

    def test_index_html_canonical(self):
        """La page publique doit avoir une URL canonique."""
        if not self.index_path.exists():
            self.skipTest("index.html introuvable")
        
        content = self.index_path.read_text()
        
        self.assertIn('rel="canonical"', content,
                     "Balise canonical manquante dans index.html")

    def test_index_html_open_graph(self):
        """La page publique doit avoir des métadonnées Open Graph."""
        if not self.index_path.exists():
            self.skipTest("index.html introuvable")
        
        content = self.index_path.read_text()
        
        required_og = [
            'property="og:title"',
            'property="og:description"',
            'property="og:url"',
            'property="og:type"',
        ]
        
        for og_tag in required_og:
            with self.subTest(tag=og_tag):
                self.assertIn(og_tag, content,
                             f"Métadonnée Open Graph {og_tag} manquante")

    def test_index_html_json_ld(self):
        """La page publique doit avoir des données structurées JSON-LD."""
        if not self.index_path.exists():
            self.skipTest("index.html introuvable")
        
        content = self.index_path.read_text()
        
        # Chercher le bloc JSON-LD
        json_ld_pattern = r'<script type="application/ld\+json">(.*?)</script>'
        matches = re.findall(json_ld_pattern, content, re.DOTALL)
        
        self.assertTrue(len(matches) > 0,
                       "Aucun bloc JSON-LD trouvé dans index.html")
        
        # Vérifier que le JSON-LD est valide
        for json_str in matches:
            json_str = json_str.strip()
            if json_str:
                try:
                    json.loads(json_str)
                except json.JSONDecodeError as e:
                    self.fail(f"JSON-LD invalide : {e}")

    def test_index_html_title(self):
        """La page publique doit avoir un titre conforme."""
        if not self.index_path.exists():
            self.skipTest("index.html introuvable")
        
        content = self.index_path.read_text()
        
        # Le titre doit être "Créez une déclaration d’accessibilité RGAA conforme"
        self.assertIn("Créez une déclaration d’accessibilité RGAA conforme", content,
                     "Titre de la page non conforme (doit être 'Créez une déclaration d’accessibilité RGAA conforme')")

    # =========================================================================
    # TESTS 5 : ABSENCE D'ATTRIBUTION IA
    # =========================================================================

    def test_no_ai_coauthored_by(self):
        """L'historique Git ne doit pas contenir de trailers Co-authored-by: Claude."""
        import subprocess
        
        try:
            # Chercher spécifiquement dans les messages de commit et trailers (pas dans les diffs)
            result = subprocess.run(
                ["git", "log", "--all", "--format=%H %s%n%b%n---TRAILERS---"],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Vérifier qu'aucune ligne NE contient "Co-authored-by: Claude" dans les messages/trailers
            # (exclure les diffs qui pourraient contenir des faux positifs)
            output_lines = (result.stdout + result.stderr).split('\n')
            
            for line in output_lines:
                # Arrêter la vérification après ---TRAILERS--- pour éviter les diffs
                if line.startswith('---TRAILERS---'):
                    break
                if 'Co-authored-by: Claude' in line:
                    self.fail(
                        f"Historique Git contient des trailers Co-authored-by: Claude dans : {line}"
                    )
        except subprocess.TimeoutExpired:
            self.skipTest("Commande git timeout")
        except FileNotFoundError:
            self.skipTest("Git non disponible")

    def test_no_ai_author_mentions(self):
        """Les fichiers ne doivent pas créditer Claude comme auteur ou co-auteur."""
        # Fichiers à vérifier
        files_to_check = [
            self.readme_path,
            self.template_path,
            self.skill_path,
            self.index_path,
        ]
        
        for file_path in files_to_check:
            if file_path.exists():
                content = file_path.read_text()
                
                # Chercher les mentions d'auteurs IA
                ai_author_patterns = [
                    r'Auteur.*Claude',
                    r'Co-auteur.*Claude',
                    r'Contributeur.*Claude',
                    r'Generated by.*Claude',
                    r'Co-Authored-By:.*Claude',
                ]
                
                for pattern in ai_author_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    self.assertEqual(len(matches), 0,
                                   f"Fichier {file_path} contient des mentions d'auteurs IA: {matches}")

    # =========================================================================
    # TESTS 6 : ABSENCE DE PLACEHOLDERS
    # =========================================================================

    def test_no_placeholders_in_public_files(self):
        """Les fichiers publics ne doivent pas contenir de placeholders non remplacés."""
        public_files = [
            self.index_path,
            self.docs_dir / "llms.txt",
            self.docs_dir / "robots.txt",
            self.docs_dir / "sitemap.xml",
        ]
        
        for file_path in public_files:
            if file_path.exists():
                content = file_path.read_text()
                
                # Chercher les placeholders {{...}}
                placeholders = re.findall(r'\{\{[^}]+\}\}', content)
                self.assertEqual(len(placeholders), 0,
                               f"Fichier {file_path} contient des placeholders non remplacés: {placeholders}")

    # =========================================================================
    # TESTS 7 : VALIDITÉ DES FICHIERS
    # =========================================================================

    def test_sitemap_xml_valid(self):
        """Le sitemap.xml doit être valide."""
        if not self.sitemap_path.exists():
            self.skipTest("sitemap.xml introuvable")
        
        try:
            ET.parse(self.sitemap_path)
        except ET.ParseError as e:
            self.fail(f"sitemap.xml invalide : {e}")

    def test_sitemap_has_lastmod(self):
        """Le sitemap.xml doit contenir une date de dernière modification."""
        if not self.sitemap_path.exists():
            self.skipTest("sitemap.xml introuvable")
        
        content = self.sitemap_path.read_text()
        
        self.assertIn('<lastmod>', content,
                     "Balise <lastmod> manquante dans sitemap.xml")

    def test_robots_txt_valid(self):
        """Le robots.txt doit être valide et simple."""
        if not self.robots_path.exists():
            self.skipTest("robots.txt introuvable")
        
        content = self.robots_path.read_text()
        
        # Doit contenir au minimum User-agent et Sitemap
        self.assertTrue(
            'User-agent:' in content or 'user-agent:' in content,
            "User-agent manquant dans robots.txt"
        )
        self.assertIn("Sitemap:", content,
                     "Sitemap manquant dans robots.txt")

    def test_llms_txt_valid(self):
        """Le llms.txt doit être valide et contenir les liens essentiels."""
        if not self.llms_path.exists():
            self.skipTest("llms.txt introuvable")
        
        content = self.llms_path.read_text()
        
        # Doit contenir des liens vers : skill, modèle, README, sources officielles
        required_llms_links = [
            "claude_skill_accessibilite",
            "SKILL.md",
            "template.md",
            "README.md",
            "accessibilite.numerique.gouv.fr",
        ]
        
        for link in required_llms_links:
            with self.subTest(link=link):
                self.assertIn(link, content,
                             f"Lien essentiel {link} manquant dans llms.txt")

    # =========================================================================
    # TESTS 8 : CONTRÔLES SPÉCIFIQUES DU SKILL
    # =========================================================================

    def test_skill_trigger_keywords(self):
        """Le SKILL.md doit contenir les mots-clés de déclenchement."""
        if not self.skill_path.exists():
            self.skipTest("SKILL.md introuvable")
        
        content = self.skill_path.read_text()
        
        required_triggers = [
            "déclaration d'accessibilité",
            "RGAA",
            "schéma pluriannuel",
        ]
        
        for trigger in required_triggers:
            with self.subTest(trigger=trigger):
                self.assertIn(trigger, content,
                             f"Mot-clé de déclenchement '{trigger}' manquant dans SKILL.md")

    def test_skill_required_inputs(self):
        """Le SKILL.md doit documenter les champs requis."""
        if not self.skill_path.exists():
            self.skipTest("SKILL.md introuvable")
        
        content = self.skill_path.read_text()
        
        required_inputs = [
            "Organisation",
            "Site/app",
            "RGAA version",
            "Audit date",
            "Compliance level",
            "Compliance rate",
            "Non-conformities",
            "Disproportionate burden",
            "Technologies",
            "Test environments",
            "Sample pages",
            "Contact",
        ]
        
        for input_field in required_inputs:
            with self.subTest(input=input_field):
                self.assertIn(input_field, content,
                             f"Champ requis '{input_field}' non documenté dans SKILL.md")


class TestAuditorFieldDistinction(unittest.TestCase):
    """Tests pour la distinction entre percentage de critères respectés et taux moyen de conformité."""

    def setUp(self):
        self.template_path = Path(__file__).parent.parent / "skills" / "rgaa-declaration-accessibilite" / "template.md"

    def test_distinct_mentions(self):
        """Le modèle doit clairement distinguer les deux métriques."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        
        # Compter les occurrences
        criteria_respected_count = len(re.findall(
            r'pourcentage de critères respectés', content, re.IGNORECASE
        ))
        avg_conformity_count = len(re.findall(
            r'taux moyen de conformité', content, re.IGNORECASE
        ))
        
        self.assertGreater(criteria_respected_count, 0,
                         "Mention 'pourcentage de critères respectés' manquante")
        self.assertGreater(avg_conformity_count, 0,
                         "Mention 'taux moyen de conformité' manquante")


class TestTemplateRequiredFields(unittest.TestCase):
    """Tests pour vérifier que le template exige tous les champs obligatoires."""

    def setUp(self):
        self.template_path = Path(__file__).parent.parent / "skills" / "rgaa-declaration-accessibilite" / "template.md"

    def test_template_has_audit_date_placeholder(self):
        """Le template doit exiger la date de l'audit."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        self.assertIn("{{date_audit}}", content,
                     "Placeholder pour la date de l'audit manquant dans template.md")

    def test_template_has_auditor_placeholder(self):
        """Le template doit exiger l'auditeur."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        self.assertIn("{{auditeur}}", content,
                     "Placeholder pour l'auditeur manquant dans template.md")

    def test_template_has_rgaa_version_placeholder(self):
        """Le template doit exiger la version du RGAA."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        # Le template doit cibler RGAA 4.1.2 explicitement
        self.assertIn("RGAA 4.1.2", content,
                     "RGAA 4.1.2 non mentionné explicitement dans template.md")

    def test_template_has_contact_placeholder(self):
        """Le template doit exiger un contact accessible."""
        if not self.template_path.exists():
            self.skipTest("template.md introuvable")
        
        content = self.template_path.read_text()
        # Vérifier qu'il y a des placeholders pour les contacts
        self.assertTrue(
            "{{contact}}" in content or "{{moyen_contact}}" in content or "{{contacts}}" in content,
            "Aucun placeholder pour le contact trouvé dans template.md"
        )


class TestHTMLMarkdownValidation(unittest.TestCase):
    """Tests pour la validation HTML et Markdown."""

    def setUp(self):
        self.index_path = Path(__file__).parent.parent / "docs" / "index.html"
        self.readme_path = Path(__file__).parent.parent / "README.md"

    def test_index_html_basic_structure(self):
        """La page publique doit avoir une structure HTML de base valide."""
        if not self.index_path.exists():
            self.skipTest("index.html introuvable")
        
        content = self.index_path.read_text()
        
        # Vérifier les éléments HTML de base
        self.assertIn("<!doctype html>", content.lower(),
                     "Doctype HTML manquant")
        self.assertIn("<html", content.lower(),
                     "Balise <html> manquante")
        self.assertIn("<head>", content.lower(),
                     "Balise <head> manquante")
        self.assertIn("<body>", content.lower(),
                     "Balise <body> manquante")
        self.assertIn("<title>", content.lower(),
                     "Balise <title> manquante")
        
        # Vérifier que les balises sont fermées
        self.assertIn("</html>", content.lower(),
                     "Balise </html> manquante")
        self.assertIn("</head>", content.lower(),
                     "Balise </head> manquante")
        self.assertIn("</body>", content.lower(),
                     "Balise </body> manquante")

    def test_readme_markdown_structure(self):
        """Le README doit avoir une structure Markdown valide."""
        if not self.readme_path.exists():
            self.skipTest("README.md introuvable")
        
        content = self.readme_path.read_text()
        
        # Vérifier qu'il y a un titre principal
        self.assertTrue(content.startswith("# "),
                       "Le README doit commencer par un titre principal (#)")
        
        # Vérifier qu'il y a des sections (##)
        self.assertIn("## ", content,
                     "Le README doit contenir des sections (##)")
        
        # Vérifier qu'il y a des listes
        self.assertTrue("- " in content or "* " in content,
                       "Le README doit contenir des listes")


if __name__ == '__main__':
    unittest.main()
