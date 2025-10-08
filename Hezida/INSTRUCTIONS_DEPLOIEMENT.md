# 🚀 INSTRUCTIONS DE DÉPLOIEMENT - HEZIDA

**Guide rapide pour lancer vos séquences sur Apollo.io**

---

## ⚡ DÉMARRAGE RAPIDE (30 MIN)

### Étape 1 : Vérification Préalable ✅

Avant de commencer, assurez-vous d'avoir :
- [ ] Compte Apollo.io actif
- [ ] Email warmup effectué (14-21 jours minimum)
- [ ] Liste de contacts qualifiés (200+ par segment)
- [ ] Calendly configuré et accessible
- [ ] Google Analytics prêt pour tracking UTM

---

## 📋 DÉPLOIEMENT SÉQUENCE PAR SÉQUENCE

### 🔍 SÉQUENCE 1 : "Invisibles sur Google"

**Cible :** Artisans, commerçants sans site web

#### Configuration Apollo

1. **Créer nouvelle séquence**
   - Nom : "Hezida - Invisibles Google - Artisans"
   - Type : Email Sequence
   - Daily limit : 40-50 emails

2. **Ajouter les 5 steps**

**Step 1 (J0) - Question Provocante**
- Type : Automatic Email
- Delay : Immediate
- A/B Test : ON (50/50)
- **Variant A :**
  - Subject : `{{first_name}}, 73% de vos clients vous cherchent sur Google`
  - Body : Copier depuis `step_1_question_provocante/template_variant_a.html`
- **Variant B :**
  - Subject : `Question rapide sur {{company}}`
  - Body : Copier depuis `step_1_question_provocante/template_variant_b.html`

**Step 2 (J+4) - Cas Client Local**
- Type : Automatic Email
- Delay : 4 days after Step 1
- Condition : If no reply
- A/B Test : ON (50/50)
- **Variant A :**
  - Subject : `[Cas client] Plombier Épinal → +40% clients en 3 mois`
  - Body : Copier depuis `step_2_cas_client_local/template_variant_a.html`
- **Variant B :**
  - Subject : `Comment un artisan perd 200 clients/an sans le savoir`
  - Body : Copier depuis `step_2_cas_client_local/template_variant_b.html`

**Step 3 (J+8) - Objections & Preuve**
- Type : Automatic Email
- Delay : 4 days after Step 2
- Condition : If no reply
- A/B Test : ON (50/50)
- **Variant A :**
  - Subject : `{{first_name}}, diagnostic gratuit site {{company}}`
  - Body : Copier depuis `step_3_objections_preuve/template_variant_a.html`
- **Variant B :**
  - Subject : `{{first_name}}, vos concurrents investissent (pas vous)`
  - Body : Copier depuis `step_3_objections_preuve/template_variant_b.html`

**Step 4 (J+12) - Breakup Soft**
- Type : Automatic Email
- Delay : 4 days after Step 3
- Condition : If no reply
- Subject : `Dernier message (promis)`
- Body : Copier depuis `step_4_breakup_soft/template.html`

**Step 5 (J+18) - Offre Finale**
- Type : Automatic Email
- Delay : 6 days after Step 4
- Condition : If no reply
- Subject : `{{first_name}}, dernière opportunité`
- Body : Copier depuis `step_5_offre_finale/template.html`

#### Paramètres Séquence 1
```
Daily Send Limit: 40-50 emails
Time Zone: Europe/Paris
Sending Window: 9h-12h ET 14h-18h
Weekend Sending: OFF
Auto-pause on reply: ON
Auto-pause on bounce: ON
A/B Test Winner: Auto-select after 100 sends
```

#### Contacts à Importer
- Artisans Vosges/Lorraine
- Commerçants locaux
- Taille : 1-10 employés
- Secteurs : BTP, commerce, services

---

### 🔄 SÉQUENCE 2 : "Refonte Site Obsolète"

**Cible :** PME avec site web 2010-2015

#### Configuration Apollo

1. **Créer nouvelle séquence**
   - Nom : "Hezida - Refonte Site - PME"
   - Type : Email Sequence
   - Daily limit : 35-45 emails

2. **Ajouter les 6 steps**

**Step 1 (J0) - Diagnostic Site 2010**
- A/B Test : ON
- **Variant A :** `Score site {{company}} : audit en 60 secondes`
- **Variant B :** `{{company}} vs vos concurrents : analyse rapide`

**Step 2 (J+4) - Avant/Après**
- Delay : 4 days
- A/B Test : ON
- **Variant A :** `{{first_name}}, PME métallurgie Épinal : +142% leads en 4 mois`
- **Variant B :** `Coût réel de garder votre site actuel`

**Step 3 (J+8) - ROI Refonte**
- Delay : 4 days
- A/B Test : ON
- **Variant A :** `Site moderne 2025 vs site 2012 : la différence`
- **Variant B :** `Google pénalise les sites comme le vôtre`

**Step 4 (J+12) - Cas Client PME**
- Delay : 4 days
- A/B Test : ON
- **Variant A :** `[Cas client] PME Nancy : résultats 6 mois post-refonte`
- **Variant B :** `"Pourquoi j'ai attendu 3 ans..." (regret DG)`

**Step 5 (J+16) - Offre Audit**
- Delay : 4 days
- A/B Test : ON
- **Variant A :** `Audit approfondi gratuit {{company}} (valeur 300€)`
- **Variant B :** `Refonte 2025 : anticiper maintenant`

**Step 6 (J+21) - Final Touch**
- Delay : 5 days
- A/B Test : ON
- **Variant A :** `Vidéo : avant/après refonte (2 min)`
- **Variant B :** `Dernier message + guide gratuit`

#### Paramètres Séquence 2
```
Daily Send Limit: 35-45 emails
Time Zone: Europe/Paris
Sending Window: 9h-12h ET 14h-17h
Weekend Sending: OFF
Auto-pause on reply: ON
```

#### Contacts à Importer
- PME Vosges/Lorraine
- Taille : 5-50 employés
- Site web existant mais obsolète
- Secteurs : Services B2B, industrie, BTP

---

### 🚀 SÉQUENCE 3 : "Nouveaux Entrepreneurs"

**Cible :** Créateurs d'entreprise (0-12 mois)

#### Configuration Apollo

1. **Créer nouvelle séquence**
   - Nom : "Hezida - Pack Création - Nouveaux"
   - Type : Email Sequence
   - Daily limit : 30-40 emails

2. **Ajouter les 4 steps**

**Step 1 (J0) - Félicitations**
- A/B Test : ON
- **Variant A :** `Félicitations pour {{company}} 🎉`
- **Variant B :** `{{company}} : communication prête pour le lancement ?`

**Step 2 (J+4) - Checklist/Exemples**
- Delay : 4 days
- A/B Test : ON
- **Variant A :** `Checklist lancement : 7 éléments indispensables`
- **Variant B :** `3 questions avant de lancer {{company}}`

**Step 3 (J+9) - Breakup Respectueux**
- Delay : 5 days
- A/B Test : ON
- **Variant A :** `{{first_name}}, timing pas bon ?`
- **Variant B :** `Vous accompagner quand vous serez prêt`

**Step 4 (J+15) - Offre Urgente**
- Delay : 6 days
- A/B Test : ON
- **Variant A :** `Pack Création Complet {{company}} + Bonus`
- **Variant B :** `Accompagnement personnalisé lancement`

#### Paramètres Séquence 3
```
Daily Send Limit: 30-40 emails
Time Zone: Europe/Paris
Sending Window: 9h-12h ET 15h-18h
Weekend Sending: OFF
Auto-pause on reply: ON
```

#### Contacts à Importer
- Nouvelles entreprises (0-12 mois)
- Taille : 1-5 employés
- Tous secteurs
- Source : CCI, Infogreffe, LinkedIn

---

## 📊 MÉTRIQUES À SUIVRE

### KPIs Critiques

**Semaine 1-2 :**
- Taux d'ouverture : >26%
- Taux de clic : >5%
- Taux de réponse : >3%

**Semaine 3-4 :**
- Taux d'ouverture : >32%
- Taux de clic : >8%
- Taux de réponse : >5%

**Objectifs Mensuels :**
- Diagnostics demandés : 15-30
- Devis envoyés : 8-15
- Clients signés : 3-6

### Dashboard Apollo à Consulter Quotidiennement

1. Sequence Performance
2. Email Open Rates (par variant)
3. Reply Rates (par step)
4. A/B Test Results
5. Unsubscribe Rate (<0.5%)

---

## ⚠️ BONNES PRATIQUES

### À FAIRE ✅
- Warmup email 14-21 jours AVANT lancement
- Tester sur 5-10 contacts d'abord
- Répondre aux prospects <4h
- Noter objections fréquentes
- Ajuster templates basés retours réels
- Célébrer chaque conversion !

### À NE PAS FAIRE ❌
- Envoyer sans warmup = spam immédiat
- Dépasser 60 emails/jour au début
- Ignorer les réponses négatives
- Modifier trop vite (attendre 100+ envois)
- Oublier de suivre les leads chauds

---

## 🆘 DÉPANNAGE RAPIDE

### Problème : Taux d'ouverture <20%
**Solutions :**
- Vérifier warmup email actif
- Tester nouveaux subjects
- Vérifier réputation expéditeur
- Réduire volume quotidien

### Problème : Taux de réponse <2%
**Solutions :**
- Améliorer personnalisation
- Raccourcir emails (60-80 mots)
- Renforcer CTA
- Tester nouveaux angles

### Problème : Beaucoup d'unsubscribe
**Solutions :**
- Vérifier ciblage (ICP correct ?)
- Adoucir ton des emails
- Espacer les touchpoints
- Améliorer valeur offerte

---

## 📞 CONTACT & SUPPORT

**En cas de question :**
- Email : contact@hezida.fr
- Téléphone : 06 72 05 87 44
- Documentation : Consultez les fichiers README.md de chaque séquence

---

## ✅ CHECKLIST AVANT LANCEMENT

**Technique :**
- [ ] Warmup email actif depuis 14+ jours
- [ ] Templates copiés dans Apollo
- [ ] UTM tracking vérifié
- [ ] Calendly fonctionnel
- [ ] Signature email configurée

**Contenu :**
- [ ] Portfolio Hezida à jour
- [ ] Cas clients documentés
- [ ] Templates réponses préparés
- [ ] Process diagnostic défini

**Commercial :**
- [ ] 200+ contacts importés par segment
- [ ] CRM configuré (Notion/Sheets)
- [ ] Calendrier bloqué pour RDV
- [ ] Pricing clair et assumé

---

## 🎯 OBJECTIF 30 JOURS

**Résultats Attendus Mois 1 :**
- 400-600 contacts approchés (mix 3 segments)
- 10-20 diagnostics demandés
- 4-8 devis envoyés
- 1-3 clients signés
- 3-10k€ CA généré

**Si objectifs atteints = SCALER Mois 2 !**

---

🎉 **Bonne chance avec vos campagnes Hezida !**

*Tous les templates sont prêts. Il ne reste plus qu'à lancer !*

