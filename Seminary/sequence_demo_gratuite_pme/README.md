# 🎁 SÉQUENCE APOLLO : DÉMO GRATUITE PME VOSGES

## 📋 INFORMATIONS GÉNÉRALES

**Nom de la séquence :** Démo Gratuite PME (Evergreen)  
**Cible principale :** DG, DRH, Responsables Formation PME Vosges  
**Secteurs prioritaires :** Tous secteurs (PME 20-250 salariés)  
**Durée totale :** 21 jours  
**Nombre de touchpoints :** 5 emails automatiques  
**Type :** Séquence evergreen (utilisable toute l'année)

---

## 🎯 OBJECTIFS DE LA SÉQUENCE

### Objectif principal
Obtenir des inscriptions à des démos gratuites (1h) d'interventions Seminary pour les PME vosgiennes, avec conversion ultérieure en séminaires/formations complètes.

### Objectifs secondaires
- Faire découvrir le catalogue d'interventions Seminary
- Créer une relation de proximité avec les PME locales
- Qualifier l'intérêt pour des formations/séminaires sur-mesure
- Générer des recommandations et du bouche-à-oreille

### Proposition de valeur unique
- ✅ **100% gratuit** : Aucun frais pour la démo d'1h
- ✅ **Sur-mesure** : Le prospect choisit l'intervention qui l'intéresse
- ✅ **Local** : Intervenants qui se déplacent dans les Vosges
- ✅ **Sans engagement** : Possibilité de recontacter uniquement si intéressé

---

## 📧 STRUCTURE DE LA SÉQUENCE

### **STEP 1 - Email Initial Invitation (Jour 0)**
**Type :** Automatic Email  
**A/B Testing :** ✅ OUI (2 variants)

#### Variant A - Bénéfices Directs
- **Subject :** Démo gratuite 1h : formation pour {{account.name}} ?
- **Preheader :** Choisissez l'intervention qui vous intéresse · 0€ · Sans engagement
- **Angle :** Proposition directe avec bénéfices clairs
- **Template :** `step_1_invitation_demo/template_variant_a.html`
- **Prompts :** `step_1_invitation_demo/prompts_variant_a.md`

#### Variant B - Question Curiosité
- **Subject :** {{first_name}}, quelle formation intéresserait {{account.name}} ?
- **Preheader :** On vous offre 1h avec l'intervenant de votre choix · Gratuit
- **Angle :** Question engageante + curiosité sur le catalogue
- **Template :** `step_1_invitation_demo/template_variant_b.html`
- **Prompts :** `step_1_invitation_demo/prompts_variant_b.md`

**Configuration Apollo :**
- Send After : Immediately when contact enters
- Priority : High
- A/B Split : 50/50
- Metric : Track opens + replies + clicks

---

### **STEP 2 - Cas Client + Détails Pratiques (Jour +4)**
**Type :** Automatic Email  
**A/B Testing :** ✅ OUI (2 variants)  
**Condition :** If no reply to Step 1

#### Variant A - Témoignage PME Locale
- **Subject :** Ce qu'une PME vosgienne dit de nos démos
- **Preheader :** "On a testé avant de se lancer" - DG PME 45 pers.
- **Angle :** Social proof local + storytelling
- **Template :** `step_2_cas_client_details/template_variant_a.html`
- **Prompts :** `step_2_cas_client_details/prompts_variant_a.md`

#### Variant B - Résultats Chiffrés
- **Subject :** 87% des PME testent avant d'acheter
- **Preheader :** Comment 23 PME vosgiennes ont choisi leur formation
- **Angle :** Data-driven + preuve sociale par les chiffres
- **Template :** `step_2_cas_client_details/template_variant_b.html`
- **Prompts :** `step_2_cas_client_details/prompts_variant_b.md`

**Configuration Apollo :**
- Send After : 4 days after Step 1
- Condition : If no reply
- A/B Split : 50/50

---

### **STEP 3 - Catalogue Interventions (Jour +9)**
**Type :** Automatic Email  
**A/B Testing :** ❌ NON (1 seul template)  
**Condition :** If no reply to Step 2

- **Subject :** Nos 15 interventions disponibles (demo gratuite)
- **Preheader :** VTT, leadership, cohésion, survie, mental... Laquelle pour vous ?
- **Angle :** Présentation concrète du catalogue avec exemples
- **Template :** `step_3_catalogue_interventions/template.html`
- **Prompts :** `step_3_catalogue_interventions/prompts.md`

**Configuration Apollo :**
- Send After : 5 days after Step 2 (Jour +9 total)
- Condition : If no reply

**Contenu clé :**
- Liste de 5-6 interventions phares du catalogue Seminary
- Format : Nom intervenant + thème + durée démo (1h)
- CTA : Répondre avec le numéro de l'intervention qui intéresse

---

### **STEP 4 - Breakup Soft avec Options (Jour +15)**
**Type :** Automatic Email  
**A/B Testing :** ❌ NON (1 seul template)  
**Condition :** If no reply to Step 3

- **Subject :** {{first_name}}, timing pas bon ?
- **Preheader :** A, B ou C ? (réponse simple)
- **Angle :** Permission to close avec choix clairs (A/B/C) respectueux
- **Template :** `step_4_breakup_options/template.html`
- **Prompts :** `step_4_breakup_options/prompts.md`

**Configuration Apollo :**
- Send After : 6 days after Step 3 (Jour +15 total)
- Condition : If no reply

**Options proposées :**
- **Option A :** Intéressé bientôt (1-2 mois) → Proposition cette semaine
- **Option B :** Intéressé plus tard (fin 2025) → Recontact T3/T4
- **Option C :** Pas intéressé → Arrêt de la séquence

---

### **STEP 5 - Dernière Chance (Jour +21)**
**Type :** Automatic Email  
**A/B Testing :** ❌ NON (1 seul template)  
**Condition :** If no reply to Step 4

- **Subject :** Dernier message : démo gratuite {{account.name}}
- **Preheader :** 3 créneaux dispo cette semaine · Puis j'arrête de vous embêter
- **Angle :** Urgence douce + dernière opportunité concrète
- **Template :** `step_5_derniere_chance/template.html`
- **Prompts :** `step_5_derniere_chance/prompts.md`

**Configuration Apollo :**
- Send After : 6 days after Step 4 (Jour +21 total)
- Condition : If no reply
- Automatic exit after this email

**Dates proposées (à adapter) :**
- Mercredi [date] - 10h ou 14h
- Jeudi [date] - 9h ou 15h
- Vendredi [date] - 10h

---

## 🎨 A/B TESTING : MODE D'EMPLOI

### Configuration dans Apollo.io

1. **Step 1 :**
   - Cliquer sur "Add Test" dans l'email step
   - Variant A : Bénéfices Directs
   - Variant B : Question Curiosité
   - Split : 50/50
   - Metric : Opens + Replies + Clicks

2. **Step 2 :**
   - Cliquer sur "Add Test" dans l'email step
   - Variant A : Témoignage Local
   - Variant B : Résultats Chiffrés
   - Split : 50/50
   - Metric : Opens + Replies

### Analyse des résultats

**Après 100 envois minimum :**
- Apollo choisit automatiquement le meilleur variant
- Analyser : Taux d'ouverture, taux de réponse, taux de clic
- Conserver le variant gagnant pour la suite

**Métriques clés à tracker :**
- Open Rate : >28% = bon (offre gratuite)
- Reply Rate : >6% = excellent (offre gratuite)
- Click Rate (lien catalogue) : >4% = bon
- Conversion Démo : >3% = excellent

---

## 🔧 TOKENS APOLLO UTILISÉS

**Tokens standards dans cette séquence :**
```
{{contact.first_name}}       → Prénom du contact (utilisé dans tous)
{{account.name}}              → Nom de l'entreprise (utilisé dans tous)
```

**⚠️ Important :**
- Utiliser UNIQUEMENT ces tokens (les plus fiables sur Apollo)
- Pas de syntaxe conditionnelle complexe
- Valeurs génériques intégrées dans le texte quand nécessaire

---

## 📊 PAIN POINTS ADRESSÉS

### Pour DG / DRH PME Vosges
- ✅ Budget formation limité (offre gratuite = test sans risque)
- ✅ Incertitude sur ROI formation (démo permet de tester avant)
- ✅ Manque de temps pour chercher prestataires (catalogue clé en main)
- ✅ Besoin de proximité locale (intervenants se déplacent Vosges)
- ✅ Peur de s'engager sans connaître (0€ + sans engagement)

### Solutions apportées par Seminary
- ✅ Démo gratuite 1h (0€) pour tester sans risque
- ✅ Catalogue varié (VTT, leadership, cohésion, survie, mental...)
- ✅ Intervenants de prestige (Rémy Absalon, Maxime Laheurte...)
- ✅ Format flexible (demi-journée, journée complète, séminaire)
- ✅ Local Vosges (déplacement sur site possible)

---

## 📈 RÉSULTATS ATTENDUS

### Benchmarks séquence email offre gratuite 2025
- **Open Rate :** 28-35% (offre gratuite = meilleur taux)
- **Reply Rate :** 5-10% (offre gratuite = plus engageant)
- **Taux Démo bookée :** 3-6%
- **Conversion Démo → Client :** 30-40% (benchmark démos gratuites)

### KPIs à tracker dans Apollo
1. Nombre de contacts entrés dans la séquence
2. Taux d'ouverture par step
3. Taux de réponse par step
4. Nombre de démos bookées
5. Interventions les plus demandées (pour optimiser catalogue)
6. Taux de conversion Démo → Séminaire/Formation payante

---

## 🎯 PERSONNALISATION RECOMMANDÉE

### Avant de lancer la séquence

**1. Adapter les dates (Step 5)**
- Remplacer les dates d'exemple par des dates réelles
- Proposer 3 créneaux sur la semaine à venir
- Format : Jour + date + 2 horaires

**2. Mettre à jour le catalogue (Step 3)**
- Sélectionner 5-6 interventions phares du moment
- Vérifier disponibilité des intervenants
- Adapter selon saison (VTT été, cohésion indoor hiver...)

**3. Segmentation**
- **Segment A :** PME 20-50 pers (format demi-journée privilégié)
- **Segment B :** PME 50-150 pers (format journée privilégié)
- **Segment C :** PME 150-250 pers (format séminaire 2 jours)

**4. Timing d'envoi optimal**
- **Jours :** Mardi, Mercredi, Jeudi
- **Heures :** 8h-10h ou 14h-16h
- **Éviter :** Lundi matin (inbox saturée), Vendredi après 15h, Week-end

---

## ✅ CHECKLIST AVANT LANCEMENT

### Technique
- [ ] Tous les templates HTML importés dans Apollo
- [ ] Tokens `{{contact.first_name}}` et `{{account.name}}` testés
- [ ] Lien catalogue Seminary fonctionnel (https://goseminary.com/formations/)
- [ ] Email tim@goseminary.com configuré comme reply-to
- [ ] Pas d'images (templates texte seul pour meilleur délivrabilité)

### Contenu
- [ ] A/B tests configurés sur Step 1 et Step 2
- [ ] Subject lines optimisés (max 50 caractères)
- [ ] Preheaders rédigés (complètent le subject)
- [ ] Dates Step 5 actualisées
- [ ] Numéro téléphone correct (06 75 63 06 60)
- [ ] Interventions catalogue à jour

### Configuration Apollo
- [ ] Séquence activée
- [ ] Conditions "If no reply" configurées
- [ ] Délais entre steps respectés (J0, J+4, J+9, J+15, J+21)
- [ ] Désactivation auto si réponse reçue
- [ ] Analytics activés
- [ ] Exit auto après Step 5

---

## 🚀 BONNES PRATIQUES

### ✅ À FAIRE
- Tester l'envoi sur une petite liste pilote (30 contacts)
- Monitorer les réponses quotidiennement
- Répondre aux réponses dans les 2h max (offre gratuite = réactivité)
- Analyser les variants après 100 envois
- Tracker quelles interventions sont les plus demandées

### ❌ À ÉVITER
- Envoyer sans tester les liens
- Ignorer les demandes de désinscription
- Relancer manuellement ceux qui ont répondu NON
- Modifier la séquence pendant un A/B test
- Envoyer en période de vacances scolaires (cible PME = moins réactif)

---

## 📞 CONTACTS SEMINARY

**Email principal :** tim@goseminary.com  
**Téléphone :** 06 75 63 06 60  
**Site web :** https://goseminary.com  
**Catalogue formations :** https://goseminary.com/formations/  
**Contact direct :** Benoit Timéo

---

## 📝 NOTES ADDITIONNELLES

### Prochaines optimisations possibles
1. Créer variant Step 3 avec focus sur 3 interventions top (vs catalogue complet)
2. Ajouter un Step 6 "Offre spéciale" si pas de réponse après Step 5
3. Tester différentes durées de démo (30min vs 1h)
4. Créer séquence LinkedIn en parallèle
5. Segmenter par secteur d'activité (industrie vs services vs commerce)

### Variantes sectorielles à créer
- Séquence Industrie (focus sécurité + cohésion)
- Séquence Commerce (focus performance commerciale + motivation)
- Séquence Tech/Startups (focus innovation + agilité)

### Points de vigilance
- ⚠️ **Gratuité = valeur perçue** : Bien insister sur la qualité des intervenants pour éviter perception "démo bas de gamme"
- ⚠️ **Local = proximité** : Toujours mentionner "Vosges" pour créer ancrage géographique
- ⚠️ **Sans engagement** : Rassurer explicitement qu'aucune pression après la démo

---

*Document créé le : Octobre 2025*  
*Version : 1.0*  
*Dernière mise à jour : 25/10/2025*
*Basé sur les meilleures pratiques de prospection B2B 2025*

