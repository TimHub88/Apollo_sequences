# 🏭 SÉQUENCE APOLLO : INDUSTRIELS VOSGES

## 📊 VUE D'ENSEMBLE

**Nom de la séquence :** "Industriels Vosges" (Spécialisée)  
**Cible :** Directeurs sites industriels, QHSE, DRH industrie  
**Timing :** Toute l'année  
**Durée totale :** 21 jours  
**Nombre de touchpoints :** 4 emails automatiques + 3 templates de réponse

---

## 🎯 ANGLE & POSITIONNEMENT

**Angle principal :** Sécurité + Cohésion + Local (Vosges)

**Proposition de valeur :**
- Réduction mesurable des accidents du travail (-35%)
- Diminution de l'absentéisme (-34%)
- Baisse du turnover (-39%)
- Formation QHSE par l'expérience (outdoor challengeant)
- Intervenants crédibles (champions sportifs + formateurs)

---

## 📅 STRUCTURE DE LA SÉQUENCE

### Step 1 - Email Initial (J0)
**Timing :** Immédiat à l'entrée du contact  
**Type :** A/B Test (2 variants)  
**Priorité :** High

#### Variant A - Compliance/Obligations QHSE
- **Subject :** `QHSE : formation cohésion équipe ?`
- **Angle :** Obligations légales bien-être + statistiques sécurité
- **Ton :** Professionnel, orienté conformité
- **CTA :** 15 min d'échange

#### Variant B - Pain Point Turnover
- **Subject :** `Turnover ouvriers : solution éprouvée`
- **Angle :** Problème émotionnel du turnover + cas client
- **Ton :** Humain, storytelling
- **CTA :** RDV téléphonique

---

### Step 2 - Solutions Outdoor Vosges (J+7)
**Timing :** 7 jours après Step 1  
**Condition :** Si pas de réponse au Step 1

- **Subject :** `Team building industriel : pas du paintball`
- **Contenu :** Présentation 3 formats d'activités
  1. VTT Descente avec Rémy Absalon
  2. Survie en équipe (Faire Face Formations)
  3. Renforcement mental (Maxime Laheurte)
- **CTA :** Répondre 1, 2 ou 3 par email
- **Ton :** Direct, accessible, décontracté

---

### Step 3 - ROI Mesurable Industrie (J+14)
**Timing :** 7 jours après Step 2  
**Condition :** Si pas de réponse

- **Subject :** `Absentéisme -30% : comment ?`
- **Contenu :** Données chiffrées avant/après + calcul ROI 1150%
- **Angle :** Rationnel, financier, preuves concrètes
- **Garantie :** Remboursement si pas de résultats en 6 mois
- **CTA :** Échange 20 min
- **Ton :** Corporate, professionnel, orienté décideurs

---

### Step 4 - Visite Site + Démo (J+21)
**Timing :** 7 jours après Step 3  
**Condition :** Si pas de réponse

- **Subject :** `Démo gratuite sur votre site ?`
- **Contenu :** Proposition intervention gratuite (1h30, 0€)
- **Format :** Mini-démo + Q&A + devis personnalisé
- **CTA :** Répondre avec 2-3 dates possibles
- **Ton :** Humble, généreux, sans pression
- **Permission to ignore :** Explicite

---

## 📧 EMAILS BONUS (AUTO-RÉPONSES)

### 1. Prospect Intéressé
- **Usage :** Réponse positive du prospect
- **Contenu :** Process en 3 étapes + CTA Calendly
- **Ton :** Enthousiaste, professionnel

### 2. Pas Intéressé
- **Usage :** Désintérêt clair du prospect
- **Contenu :** Remerciement + suppression de liste + porte ouverte
- **Ton :** Respectueux, humble, minimaliste

### 3. Pas Maintenant
- **Usage :** Timing non opportun
- **Contenu :** Proposition recontact dans 3-4 mois
- **Ton :** Compréhensif, patient

---

## 🔧 CONFIGURATION APOLLO.IO

### Tokens utilisés
- `{{contact.first_name}}` - Prénom du contact
- `{{account.name}}` - Nom de l'entreprise

### A/B Testing (Step 1)
- **Split :** 50/50
- **Metric :** Ouvertures + Réponses
- **Auto-optimisation :** Après 100 envois

### Conditions d'envoi
- **Step 2** : Si pas de réponse à Step 1 après 7 jours
- **Step 3** : Si pas de réponse à Step 2 après 7 jours supplémentaires
- **Step 4** : Si pas de réponse à Step 3 après 7 jours supplémentaires

### Sortie de séquence
Un contact sort automatiquement de la séquence si :
- Il répond à un email
- Il clique sur le lien Calendly
- Il ouvre 3 emails sans répondre (configurable)

---

## 📂 STRUCTURE DES FICHIERS

```
sequence_industriels_vosges/
├── README.md (ce fichier)
│
├── step_1_email_initial/
│   ├── template_variant_a.html
│   ├── prompts_variant_a.md
│   ├── template_variant_b.html
│   └── prompts_variant_b.md
│
├── step_2_solutions_outdoor/
│   ├── template.html
│   └── prompts.md
│
├── step_3_roi_mesurable/
│   ├── template.html
│   └── prompts.md
│
├── step_4_visite_demo/
│   ├── template.html
│   └── prompts.md
│
└── bonus_auto_replies/
    ├── template_interesse.html
    ├── template_pas_interesse.html
    ├── template_pas_maintenant.html
    └── prompts.md
```

---

## 🎨 CHARTE GRAPHIQUE

### Couleurs principales
- **Violet principal :** `#7E22CE`
- **Violet foncé :** `#5B21B6`
- **Vert succès :** `#10B981`
- **Rouge urgence :** `#EF4444`
- **Orange attention :** `#F59E0B`

### Composants clés
- **Badges :** Pills arrondis (border-radius: 20px)
- **Boxes :** Border-radius 10-12px, bordure gauche 4px
- **Boutons CTA :** Gradient violet, border-radius 10px
- **Logo :** 48px (emails), 42px (auto-réponses courtes)

---

## 📈 KPIs À SUIVRE

### Métriques par email
- **Taux d'ouverture** : Objectif >30%
- **Taux de clic** : Objectif >5%
- **Taux de réponse** : Objectif >3%

### Métriques globales séquence
- **Taux de conversion** : Objectif 5-8% (RDV booké)
- **Meilleur variant** (Step 1) : À analyser après 100 envois
- **Step le plus efficace** : Identifier pour optimiser

### Optimisations continues
- Tester nouveaux subject lines
- Ajuster timings entre steps
- Tester différentes images
- Varier les CTAs

---

## 🎯 SEGMENT CIBLE

### Critères de qualification
- **Taille entreprise :** 50-500 salariés
- **Secteur :** Industrie (métallurgie, plasturgie, mécanique, agroalimentaire)
- **Localisation :** Vosges + départements limitrophes (Grand Est)
- **Fonction :** Directeur site, QHSE, DRH, Responsable production

### Liste idéale (Apollo filters)
```
Industry: Manufacturing
Employees: 50-500
Location: Vosges, Meurthe-et-Moselle, Moselle, Haut-Rhin, Bas-Rhin
Job Title: Director, QHSE, HR, Production Manager
```

---

## 💡 BONNES PRATIQUES

### ✅ À FAIRE
- Personnaliser au maximum avec les tokens
- Laisser 7 jours entre chaque touchpoint
- Suivre les réponses manuellement et rapidement
- Utiliser les auto-réponses pour gagner du temps
- Analyser les KPIs chaque semaine

### ❌ À ÉVITER
- Envoyer à des prospects hors cible
- Réduire les délais entre emails (spam risk)
- Ignorer les demandes de désinscription
- Négliger les réponses positives
- Continuer d'envoyer après une réponse

---

## 📞 CONTACT & SUPPORT

**Seminary**  
Benoit Timéo  
📞 06 75 63 06 60  
🌐 goseminary.com  
📧 tim@goseminary.com

---

## 📝 NOTES & MISES À JOUR

**Version :** 1.0  
**Date création :** Octobre 2025  
**Dernière mise à jour :** Octobre 2025

### Historique des modifications
- **v1.0 (Oct 2025)** : Création initiale de la séquence Industriels Vosges
  - 4 steps automatiques
  - 2 variants A/B pour step 1
  - 3 templates d'auto-réponse
  - Documentation complète

---

*Pour toute question ou optimisation, contacter l'équipe Seminary.*
