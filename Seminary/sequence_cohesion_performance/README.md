# 🎯 SÉQUENCE EMAIL APOLLO : "COHÉSION & PERFORMANCE"

## 📋 INFORMATIONS GÉNÉRALES

**Nom de la séquence :** Cohésion & Performance (Evergreen)  
**Cible principale :** DRH, Managers, CEO PME / Industriels Vosges  
**Secteurs prioritaires :** Industrie, manufacturing, logistique (50-500 salariés)  
**Durée totale :** 18 jours  
**Nombre de touchpoints :** 4 emails automatiques  
**Type :** Séquence evergreen (utilisable toute l'année)

---

## 🎯 OBJECTIFS DE LA SÉQUENCE

### Objectif principal
Générer des RDV découverte avec des décideurs RH/Direction pour présenter les services de team building et séminaires Seminary dans les Vosges.

### Objectifs secondaires
- Positionner Seminary comme expert en cohésion d'équipe avec ROI mesurable
- Démontrer l'impact concret via données chiffrées et témoignages
- Qualifier les prospects selon leur timing (court/moyen/long terme)
- Proposer une visite concrète des lieux pour créer engagement

---

## 📧 STRUCTURE DE LA SÉQUENCE

### **STEP 1 - Email Initial (Jour 0)**
**Type :** Automatic Email  
**A/B Testing :** ✅ OUI (2 variants)

#### Variant A - Pain Point Direct
- **Subject :** Question : engagement de vos équipes ?
- **Preheader :** 78% des salariés se disent désengagés (étude 2025)
- **Angle :** Statistique choc + solution concrète
- **Template :** `step_1_email_initial/template_variant_a.html`
- **Prompts :** `step_1_email_initial/prompts_variant_a.md`

#### Variant B - Storytelling Problem
- **Subject :** Vos équipes se parlent vraiment ?
- **Preheader :** Le déclic d'un DRH face aux silos en entreprise
- **Angle :** Cas client concret avec résultats mesurés
- **Template :** `step_1_email_initial/template_variant_b.html`
- **Prompts :** `step_1_email_initial/prompts_variant_b.md`

**Configuration Apollo :**
- Send After : Immediately when contact enters
- Priority : High
- A/B Split : 50/50
- Metric : Track opens + replies

---

### **STEP 2 - Follow-up Bénéfices (Jour +5)**
**Type :** Automatic Email  
**A/B Testing :** ✅ OUI (2 variants)  
**Condition :** If no reply to Step 1

#### Variant A - ROI Chiffré
- **Subject :** ROI team building : vrais chiffres
- **Preheader :** Données mesurées sur 25 PME clientes (2024-2025)
- **Angle :** Data-driven avec comparaison avant/après
- **Template :** `step_2_follow_up_benefices/template_variant_a.html`
- **Prompts :** `step_2_follow_up_benefices/prompts_variant_a.md`

#### Variant B - Témoignages
- **Subject :** Ce qu'un DRH dit de Seminary
- **Preheader :** "Je ne m'attendais pas à un tel impact" - Sophie M., DRH
- **Angle :** Social proof avec témoignage détaillé
- **Template :** `step_2_follow_up_benefices/template_variant_b.html`
- **Prompts :** `step_2_follow_up_benefices/prompts_variant_b.md`

**Configuration Apollo :**
- Send After : 5 days after Step 1
- Condition : If no reply
- A/B Split : 50/50

---

### **STEP 3 - Social Proof + Urgence Douce (Jour +12)**
**Type :** Automatic Email  
**A/B Testing :** ❌ NON (1 seul template)  
**Condition :** If no reply to Step 2

- **Subject :** Dernière question : timing
- **Preheader :** A, B ou C ? (réponse simple)
- **Angle :** Permission to close avec choix clairs (A/B/C)
- **Template :** `step_3_social_proof/template.html`
- **Prompts :** `step_3_social_proof/prompts.md`

**Configuration Apollo :**
- Send After : 7 days after Step 2 (Jour +12 total)
- Condition : If no reply

**Options proposées :**
- **Option A :** Dans les 2-3 prochains mois → Proposition cette semaine
- **Option B :** Plus tard (2026) → Recontact début 2026
- **Option C :** Pas prévu → Fin de séquence

---

### **STEP 4 - Invitation Découverte (Jour +18)**
**Type :** Automatic Email  
**A/B Testing :** ❌ NON (1 seul template)  
**Condition :** If no reply to Step 3

- **Subject :** Visite guidée : nos lieux dans les Vosges
- **Preheader :** Venez découvrir Gérardmer, Épinal, La Bresse - sans engagement
- **Angle :** Invitation concrète avec dates spécifiques
- **Template :** `step_4_invitation_decouverte/template.html`
- **Prompts :** `step_4_invitation_decouverte/prompts.md`

**Configuration Apollo :**
- Send After : 6 days after Step 3 (Jour +18 total)
- Condition : If no reply

**Dates proposées (à adapter) :**
- Mercredi 16 octobre - 14h
- Jeudi 24 octobre - 10h
- Mardi 29 octobre - 15h

---

## 🎨 A/B TESTING : MODE D'EMPLOI

### Configuration dans Apollo.io

1. **Step 1 :**
   - Cliquer sur "Add Test" dans l'email step
   - Variant A : Pain Point Direct
   - Variant B : Storytelling
   - Split : 50/50
   - Metric : Opens + Replies

2. **Step 2 :**
   - Cliquer sur "Add Test" dans l'email step
   - Variant A : ROI Chiffré
   - Variant B : Témoignages
   - Split : 50/50
   - Metric : Opens + Replies

### Analyse des résultats

**Après 100 envois minimum :**
- Apollo choisit automatiquement le meilleur variant
- Analyser : Taux d'ouverture, taux de réponse, taux de clic
- Conserver le variant gagnant pour la suite

**Métriques clés à tracker :**
- Open Rate : >25% = bon
- Reply Rate : >5% = excellent
- Click Rate (CTA) : >3% = bon
- Conversion RDV : >2% = excellent

---

## 🔧 TOKENS APOLLO UTILISÉS

**Tokens standards dans cette séquence :**
```
{{contact.first_name}}       → Prénom du contact
{{account.name}}              → Nom de l'entreprise
```

**⚠️ Important :**
- Utiliser UNIQUEMENT ces tokens (les plus fiables sur Apollo)
- Pas de syntaxe conditionnelle complexe
- Valeurs génériques intégrées dans le texte quand nécessaire

---

## 📊 PAIN POINTS ADRESSÉS

### Pour DRH / Managers
- ✅ Engagement équipe en baisse
- ✅ Turnover élevé
- ✅ Silos entre services
- ✅ Communication difficile (remote/présentiel)
- ✅ Manque de cohésion après croissance rapide
- ✅ Besoin de ROI mesurable sur team building

### Solutions apportées par Seminary
- ✅ Activités challengeantes (VTT avec Rémy Absalon)
- ✅ Formations survie/cohésion en nature
- ✅ Leadership avec athlètes haut niveau
- ✅ Lieux authentiques Vosges (Gérardmer, Épinal, La Bresse)
- ✅ ROI démontré : -45% turnover, +36% engagement

---

## 📈 RÉSULTATS ATTENDUS

### Benchmarks séquence email B2B 2025
- **Open Rate :** 22-30%
- **Reply Rate :** 3-7%
- **Taux RDV pris :** 1-3%
- **Cycle de vente :** 30-60 jours après 1er contact

### KPIs à tracker dans Apollo
1. Nombre de contacts entrés dans la séquence
2. Taux d'ouverture par step
3. Taux de réponse par step
4. Nombre de RDV bookés
5. Nombre de visites guidées confirmées
6. Taux de conversion RDV → Client

---

## 🎯 PERSONNALISATION RECOMMANDÉE

### Avant de lancer la séquence

**1. Adapter les dates (Step 4)**
- Remplacer les dates d'exemple par des dates réelles
- Proposer 3 créneaux espacés de 3-5 jours

**2. Vérifier les images**
- Les URL Pexels sont temporaires
- Remplacer par images générées via prompts fournis
- Héberger sur CDN stable

**3. Segmentation**
- **Segment A :** PME industrielles 50-150 pers
- **Segment B :** PME industrielles 150-500 pers
- **Segment C :** Secteur tertiaire (adapter wording)

**4. Timing d'envoi optimal**
- **Jours :** Mardi, Mercredi, Jeudi
- **Heures :** 8h-10h ou 14h-16h
- **Éviter :** Lundi matin, Vendredi après 15h, Week-end

---

## ✅ CHECKLIST AVANT LANCEMENT

### Technique
- [ ] Tous les templates HTML importés dans Apollo
- [ ] Tokens `{{contact.first_name}}` et `{{account.name}}` testés
- [ ] Liens Calendly fonctionnels
- [ ] Email tim@goseminary.com configuré comme reply-to
- [ ] Images chargées et affichées correctement

### Contenu
- [ ] A/B tests configurés sur Step 1 et Step 2
- [ ] Subject lines optimisés (4-7 mots)
- [ ] Preheaders rédigés (complètent le subject)
- [ ] Dates Step 4 actualisées
- [ ] Numéro téléphone correct (06 75 63 06 60)

### Configuration Apollo
- [ ] Séquence activée
- [ ] Conditions "If no reply" configurées
- [ ] Délais entre steps respectés (J0, J+5, J+12, J+18)
- [ ] Désactivation auto si réponse reçue
- [ ] Analytics activés

---

## 🚀 BONNES PRATIQUES

### ✅ À FAIRE
- Tester l'envoi sur une petite liste pilote (50 contacts)
- Monitorer les réponses quotidiennement
- Répondre aux réponses dans les 4h max
- Analyser les variants après 100 envois
- Ajuster le timing selon les résultats

### ❌ À ÉVITER
- Envoyer sans tester les liens
- Ignorer les demandes de désinscription
- Relancer manuellement ceux qui ont répondu NON
- Modifier la séquence pendant un A/B test
- Envoyer le vendredi après 15h

---

## 📞 CONTACTS SEMINARY

**Email principal :** tim@goseminary.com  
**Téléphone :** 06 75 63 06 60  
**Site web :** https://goseminary.com  
**Calendly :** https://calendly.com/goseminary/decouverte-seminary

---

## 📝 NOTES ADDITIONNELLES

### Prochaines optimisations possibles
1. Créer variant Step 3 avec offre spéciale (scarcity)
2. Ajouter un Step 5 "dernière tentative" si besoin
3. Tester video thumbnail dans Step 1
4. Créer séquence LinkedIn en parallèle
5. Segmenter par taille entreprise (50-150 vs 150-500)

### Variantes sectorielles à créer
- Séquence Tech/Startups (angle innovation)
- Séquence Retail/Commerce (angle performance commerciale)
- Séquence Services/Bureaux d'études (angle créativité)

---

*Document créé le : Octobre 2025*  
*Version : 1.0*  
*Dernière mise à jour : 04/10/2025*
