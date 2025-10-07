# 🔍 SÉQUENCE APOLLO : INVISIBLES SUR GOOGLE

## 📊 VUE D'ENSEMBLE

**Nom de la séquence :** "Invisibles sur Google" (Artisans/Commerçants)  
**Cible :** Artisans, commerçants sans site web ou avec site amateur  
**Timing :** Toute l'année (evergreen)  
**Durée totale :** 18 jours  
**Nombre de touchpoints :** 5 emails automatiques avec variants A/B

---

## 🎯 ANGLE & POSITIONNEMENT

**Angle principal :** Perte clients quotidienne + Concurrence visible = Urgence

**Proposition de valeur :**
- 73% des clients cherchent sur Google avant d'appeler
- Diagnostic gratuit offert (10-15 min)
- Agence locale Épinal (comprend enjeux locaux)
- Interlocuteur unique (pas perdu entre 10 personnes)
- Tarifs transparents adaptés TPE

---

## 📅 STRUCTURE DE LA SÉQUENCE

### Step 1 - Question Provocante (J0)
**Timing :** Immédiat à l'entrée du contact  
**Type :** A/B Test (2 variants)  
**Priorité :** High

#### Variant A - Statistique Choc
- **Subject :** `{{first_name}}, 73% de vos clients vous cherchent sur Google`
- **Angle :** Statistique locale + perte clients
- **Ton :** Direct, factuel
- **CTA :** Diagnostic gratuit 15 min

#### Variant B - Question Directe
- **Subject :** `Question rapide sur {{company}}`
- **Angle :** Question + exemple chiffré
- **Ton :** Convivial, interrogatif
- **CTA :** Diagnostic gratuit

---

### Step 2 - Cas Client Local (J+4)
**Timing :** 4 jours après Step 1  
**Condition :** Si pas de réponse au Step 1  
**Type :** A/B Test (2 variants)

#### Variant A - Avant/Après Chiffré
- **Subject :** `[Cas client] Plombier Épinal → +40% clients en 3 mois`
- **Contenu :** Résultats mesurables client local
- **Ton :** Professionnel, chiffré

#### Variant B - Storytelling Problème
- **Subject :** `Comment un artisan perd 200 clients/an sans le savoir`
- **Contenu :** Histoire vraie, identification
- **Ton :** Narratif, humain

---

### Step 3 - Diagnostic Gratuit (J+8)
**Timing :** 4 jours après Step 2  
**Condition :** Si pas de réponse  
**Type :** A/B Test (2 variants)

#### Variant A - Bénéfices Concrets
- **Subject :** `Diagnostic gratuit {{company}} → 3 opportunités`
- **Contenu :** Ce que contient le diagnostic
- **Ton :** Généreux, sans engagement

#### Variant B - Urgence Subtile
- **Subject :** `{{first_name}}, vos concurrents investissent (pas vous)`
- **Contenu :** Écart avec concurrence
- **Ton :** Urgence douce, réveiller

---

### Step 4 - Social Proof + Portfolio (J+12)
**Timing :** 4 jours après Step 3  
**Condition :** Si pas de réponse  
**Type :** A/B Test (2 variants)

#### Variant A - Portfolio Ciblé
- **Subject :** `3 exemples artisans Vosges (avant/après)`
- **Contenu :** 3 projets concrets + lien portfolio
- **Ton :** Preuve, crédibilité

#### Variant B - Témoignages Clients
- **Subject :** `Ce qu'ils disent après 6 mois`
- **Contenu :** 3 témoignages clients locaux
- **Ton :** Social proof, confiance

---

### Step 5 - Breakup Final (J+18)
**Timing :** 6 jours après Step 4  
**Condition :** Si pas de réponse  
**Type :** A/B Test (2 variants)

#### Variant A - Permission to Close
- **Subject :** `Dernier message (promis)`
- **Contenu :** Guide gratuit + porte ouverte
- **Ton :** Respectueux, humble

#### Variant B - Offre Dernière Chance
- **Subject :** `{{first_name}}, dernière opportunité`
- **Contenu :** Diagnostic approfondi gratuit si réponse avant vendredi
- **Ton :** Urgence finale

---

## 🔧 CONFIGURATION APOLLO.IO

### Tokens utilisés
- `{{first_name}}` - Prénom du contact
- `{{company}}` - Nom de l'entreprise
- `{{city}}` - Ville (si disponible)

### Custom Fields recommandés
- `website_url` - URL du site actuel
- `industry_fr` - Secteur en français
- `city` - Ville de l'entreprise

### A/B Testing (tous les steps)
- **Split :** 50/50 sur chaque step
- **Metric :** Taux de réponse (priorité) puis ouverture
- **Auto-optimisation :** Après 100-150 envois

### Conditions d'envoi
- **Step 2** : Si pas de réponse à Step 1 après 4 jours
- **Step 3** : Si pas de réponse à Step 2 après 4 jours
- **Step 4** : Si pas de réponse à Step 3 après 4 jours
- **Step 5** : Si pas de réponse à Step 4 après 6 jours

### Sortie de séquence
Un contact sort automatiquement si :
- Il répond à un email
- Il clique sur diagnostic/portfolio
- Il se désabonne

---

## 📂 STRUCTURE DES FICHIERS

```
sequence_invisibles_google/
├── README.md (ce fichier)
│
├── step_1_question_provocante/
│   ├── template_variant_a.html
│   ├── prompts_variant_a.md
│   ├── template_variant_b.html
│   └── prompts_variant_b.md
│
├── step_2_cas_client_local/
│   ├── template_variant_a.html
│   ├── prompts_variant_a.md
│   ├── template_variant_b.html
│   └── prompts_variant_b.md
│
├── step_3_diagnostic_gratuit/
│   ├── template_variant_a.html
│   ├── prompts_variant_a.md
│   ├── template_variant_b.html
│   └── prompts_variant_b.md
│
├── step_4_social_proof_portfolio/
│   ├── template_variant_a.html
│   ├── prompts_variant_a.md
│   ├── template_variant_b.html
│   └── prompts_variant_b.md
│
└── step_5_breakup_final/
    ├── template_variant_a.html
    ├── prompts_variant_a.md
    ├── template_variant_b.html
    └── prompts_variant_b.md
```

---

## 🎨 CHARTE GRAPHIQUE HEZIDA

### Couleurs principales
- **Bleu/Violet principal :** `#6366F1`
- **Bleu/Violet foncé :** `#4F46A5`
- **Bleu/Violet clair :** `#A5B4FC`
- **Gris texte :** `#374151`
- **Gris clair :** `#F9FAFB`

### Composants clés
- **Badges :** Pills arrondis (border-radius: 20px)
- **Boxes :** Border-radius 10-12px
- **Boutons CTA :** Gradient bleu/violet, border-radius 10px
- **Logo :** 48px

---

## 📈 KPIs À SUIVRE

### Métriques par email
- **Taux d'ouverture** : Objectif >28%
- **Taux de clic** : Objectif >12%
- **Taux de réponse** : Objectif >4%

### Métriques globales séquence
- **Diagnostics demandés** : Objectif 8-15 pour 200 contacts
- **Devis envoyés** : Objectif 3-6
- **Clients signés** : Objectif 1-2

### Optimisations continues
- Tester nouveaux subject lines
- Ajuster timings entre steps
- Varier les preuves sociales
- Tester différents CTAs

---

## 🎯 SEGMENT CIBLE

### Critères de qualification
- **Taille entreprise :** 1-10 salariés
- **Secteur :** Artisanat, commerce, services
- **Localisation :** Vosges puis Lorraine
- **Site web :** Absent ou très amateur

### Liste idéale (Apollo filters)
```
Company Size: 1-10 employees
Location: Vosges (88), puis Meurthe-et-Moselle, Moselle
Industry: Construction, Retail, Services, Automotive
Job Title: Owner, Gérant, Propriétaire
```

---

## 💡 BONNES PRATIQUES

### ✅ À FAIRE
- Vérifier manuellement présence site web
- Personnaliser avec ville/secteur
- Répondre sous 2h aux intéressés
- Envoyer diagnostic promis même jour
- Documenter objections récurrentes

### ❌ À ÉVITER
- Cibler entreprises avec site moderne
- Jargon technique (UX, SEO, etc.)
- Vendre dès email 1
- Ignorer demandes de diagnostic
- Relancer trop vite

---

## 📞 CONTACT & SUPPORT

**Hezida**  
Vivien Geoffroy  
📞 06 72 05 87 44  
🌐 hezida.fr  
📧 contact@hezida.fr

---

## 📝 NOTES & MISES À JOUR

**Version :** 1.0  
**Date création :** Octobre 2025  
**Dernière mise à jour :** Octobre 2025

### Historique des modifications
- **v1.0 (Oct 2025)** : Création initiale
  - 5 steps automatiques
  - 2 variants A/B par step (10 emails total)
  - Focus artisans/commerçants Vosges

---

*Pour toute question ou optimisation, contacter Hezida.*
