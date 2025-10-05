# 📧 REQUIREMENTS COMPLÈTES - TEMPLATES EMAIL SEMINARY

## 🎯 CONTEXTE DU PROJET

**Entreprise :** Seminary  
**Secteur :** Organisation de séminaires d'entreprise sur-mesure dans les Vosges  
**Plateforme :** Apollo.io (séquences d'emails automatisées)  
**Cible :** dépend de la demande (PME, Indudtriels, Startup...)
**Contact :** Benoit Timéo | 06 75 63 06 60 | goseminary.com | tim@goseminary.com (Geoffroy Vivien est un nom d'emprunt pour SEMINARY à remplacer par les vrais infos de contact)

---
## CONTRAINTES ORGANISATIONNELS 

- Pour chaque nouvelle séquence créer un dossier dans ce repo "SEQUENCES_EMAIL_APOLLO" ou nous nous trouvons, un dossier nommé "sequence" + nom de la séquence par rapport à sa cible ou quoi 
- Créer ensuite des sous dossiers dans ce dossier créer pour chaque Step, chaque étape
- dans chaque step insérer les templates html liés à la step + les prompts d'illustrations associés (format md pour les prompts, un seul fichier md pour un meme template donc un fichier markdown peut contenir plusieurs prompts d'images si le template auquel il est associé doit contenir plusieurs images, le fichier markdown doit aussi contenir le Subject du template/mail) (donc une seule step peut contenir plusieurs fichiers markdown mais un seul fichier markdown par template/mail)


## 🚨 CONTRAINTES TECHNIQUES CRITIQUES (APOLLO.IO)

### ⚠️ RÈGLE #1 : FORMAT HTML POUR APOLLO
**IMPÉRATIF :** Ne fournis **QUE** le code HTML de la balise `<body>`. 

**❌ INTERDIT :**
- Balises `<head>`
- Balises `<style>` 
- Balises `<link>`
- Media queries `@media`
- Classes CSS
- Pseudo-sélecteurs (`:hover`, `:before`, `:after`)

**✅ OBLIGATOIRE :**
- CSS 100% **inline** via attribut `style="..."`
- Structure en **tables HTML** (`<table>`, `<tr>`, `<td>`)
- Propriétés CSS simples et universelles
- Compatibilité maximum clients email

### 📝 RÈGLE #2 : TOKENS APOLLO.IO

**Tokens standards disponibles :** (si besoin)
```
{{contact.first_name}}       → Prénom du contact
{{account.name}}          → Nom de l'entreprise
{{account.primary_industry}}         → Secteur d'activité
{{account.number_of_employees}}   → Nombre d'employés
{{account.city}}            → Ville de l'entreprise
```

BONNES PRATIQUES TOKENS : essaye de les placer le plus souvent possible, par exemple lors d'un template d'exemple d'une situation par exemple "PME INDUSTRIELLE, 60 personnes" pour évoquer un cas d'étude, tu peux remplacer le secteur d'industrie et le nombre d'employés par celui de la personne en question pour qu'elle se sente encore plus concerné. 
Dans d'autres cas il est vraiment utile d'utiliser ces tokens car ils personnalisent le mail bien plus qu'on le pense, sois ingénieux pour les intégrer.

**⚠️ IMPORTANT : Pas de fallbacks conditionnels complexes !**

Apollo.io **N'INTERPRÈTE PAS** les syntaxes suivantes :
- ❌ `{{first_name | fallback: 'Bonjour'}}`
- ❌ `{{#if company}}{{company}}{{else}}votre entreprise{{/if}}`

**✅ SOLUTION :**
- Utiliser **uniquement** `{{first_name}}` et `{{company}}` (les plus fiables)
- Pour les autres champs : utiliser des **valeurs génériques** dans le texte
- Exemple : "PME industrielle · 50 salariés · Vosges" (valeurs par défaut intégrées)

### 📌 RÈGLE #3 : STRUCTURE HTML COMPATIBLE EMAIL

**Template de base obligatoire :**
```html
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #fafafa;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0">
                    <!-- Contenu ici -->
                </table>
            </td>
        </tr>
    </table>
</body>
```

---

## 🎨 CHARTE GRAPHIQUE SEMINARY

### 🔤 TYPOGRAPHIE

**Police principale :** Arial, sans-serif (fallback compatible email)
*Note : Poppins souhaité mais non supporté dans emails, utiliser Arial*

**Graisses (font-weight) :**
- Normal : `400`
- Medium : `500`
- Semi-gras : `600`
- Gras : `700`
- Extra-gras : `800`

**Couleurs de texte :**
```css
color: #374151;  /* Texte principal */
color: #4B5563;  /* Texte secondaire */
color: #111827;  /* Titres */
color: #6B7280;  /* Footer/texte discret */
```

### 🎨 PALETTE COULEURS

**Couleurs primaires (violet) :**
```css
background: #7E22CE;  /* Violet principal */
background: #5B21B6;  /* Violet hover/foncé */
```

**Gradients violets :**
```css
background: linear-gradient(135deg, #7E22CE 0%, #5B21B6 100%);  /* Header */
background: linear-gradient(135deg, #F8F5FC 0%, #F3E8FF 100%);  /* Sections claires */
```

**Couleurs de fond :**
```css
background-color: #fafafa;  /* Fond page */
background-color: #fff;     /* Fond container */
background-color: #F3E8FF;  /* Fond accent violet clair */
background-color: #F8F5FC;  /* Fond accent violet très clair */
background-color: #F9FAFB;  /* Fond accent gris clair */
```

**Couleurs d'urgence/erreur :**
```css
background-color: #EF4444;  /* Rouge urgence */
background-color: #FEF2F2;  /* Fond rouge clair */
border-color: #DC2626;      /* Bordure rouge */
```

**Couleurs succès/gratuit :**
```css
background-color: #10B981;  /* Vert succès */
background-color: #FFFBEB;  /* Fond jaune attention */
border-color: #F59E0B;      /* Bordure orange */
```

**Bordures :**
```css
border: 1px solid #E5E7EB;  /* Bordure standard */
```

### 📐 FORMES ET STYLES

**Bordures arrondies :**
```css
border-radius: 12px;   /* Containers et sections */
border-radius: 10px;   /* Boutons et images */
border-radius: 20px;   /* Badges/tags "kicker" (effet pilule) */
border-radius: 50%;    /* Badges circulaires numérotés */
```

**Bordures d'accentuation :**
```css
border-left: 4px solid #7E22CE;  /* Citation/mise en avant */
```

**Ombres (à utiliser avec parcimonie dans emails) :**
```css
/* Note : éviter les ombres complexes, peu supportées */
```

### 🖼️ IMAGES

**Logo Seminary :**
```
https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2F11d96a0e7e946a6d02eea1b59ed8995d.cdn.bubble.io%2Ff1738937103143x452387340290872700%2FSans%2520titre-1%2520%25281%2529.png?w=64&h=64&auto=compress&dpr=1&fit=max
```

**Dimensions recommandées :**
- Logo header : 42-48px
- Images illustration : max-width 520px

**Images (Priorité sur la mise en place d'image)
Génerer pour chaque template le prompt d'illustration exacte en anglais permettant à une IA de géneration d'images de géneré l'image adéquat à la situation/sujet évoqué dans le template, afin de parfaitement l'illustrer, puis insérer dans le fichier markdown lié au template
Exemple : " A photorealistic image, no text. A close-up, high-end shot of a minimalist and elegant business card or a small, branded notepad. The card simply says 'Seminary' with a subtle logo. It is resting on a natural surface, like a rustic wooden table or a smooth stone, next to a stylish pen and a warm cup of coffee. In the background, beautifully blurred (bokeh effect), is a serene and majestic landscape of the Vosges mountains, perhaps a lake or a forest in autumn. The overall feeling is professional, understated, and helpful. It visually represents the idea of 'keeping something in mind' or 'having a contact handy for the future' " 

**Images d'illustration libres de droits (Pexels) :** (mettre en place meme si peu utile car géneration d'images par IA, juste pour mettre à l'avance des images en place dans le template)

*Team Building & Collaboration :*
- `https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=600`
- `https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=600`
- `https://images.pexels.com/photos/1181298/pexels-photo-1181298.jpeg?auto=compress&cs=tinysrgb&w=600`

*Paysages Vosges :*
- `https://images.pexels.com/photos/167699/pexels-photo-167699.jpeg?auto=compress&cs=tinysrgb&w=600`
- `https://images.pexels.com/photos/534164/pexels-photo-534164.jpeg?auto=compress&cs=tinysrgb&w=600`
- `https://images.pexels.com/photos/2310641/pexels-photo-2310641.jpeg?auto=compress&cs=tinysrgb&w=600`

**Style image :**
```html
<img src="..." width="520" style="max-width: 100%; height: auto; border-radius: 10px; display: block;">
```

---

## 📝 COMPOSANTS RÉUTILISABLES

### 🎯 BADGES / KICKERS

**Badge standard (violet) :**
```html
<span style="display: inline-block; background-color: #7E22CE; color: #ffffff; padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
    🎯 TEXTE ICI
</span>
```

**Badge urgence (rouge) :**
```html
<span style="display: inline-block; background-color: #EF4444; color: #ffffff; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">
    ⏰ TEXTE ICI
</span>
```

**Badge gratuit (vert) :**
```html
<span style="display: inline-block; background-color: #10B981; color: #ffffff; padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
    🎁 GRATUIT
</span>
```

### 📦 BOX / CONTAINERS

**Box problème (rouge) :**
```html
<td style="background-color: #FEF2F2; border-left: 4px solid #DC2626; padding: 24px; border-radius: 10px;">
    <!-- Contenu -->
</td>
```

**Box solution (violet) :**
```html
<td style="background: linear-gradient(135deg, #F8F5FC 0%, #F3E8FF 100%); border: 2px solid #7E22CE; padding: 28px; border-radius: 12px;">
    <!-- Contenu -->
</td>
```

**Box neutre (grise) :**
```html
<td style="background-color: #F9FAFB; padding: 20px; border-radius: 10px; border-left: 4px solid #9CA3AF;">
    <!-- Contenu -->
</td>
```

**Box attention (jaune) :**
```html
<td style="background-color: #FFFBEB; border-left: 4px solid #F59E0B; padding: 20px; border-radius: 10px;">
    <!-- Contenu -->
</td>
```

### 🔘 BOUTONS CTA

**CTA principal (violet) :**
```html
<a href="https://calendly.com/goseminary/decouverte-seminary" style="display: inline-block; background: linear-gradient(135deg, #7E22CE 0%, #5B21B6 100%); color: #ffffff; text-decoration: none; padding: 16px 40px; border-radius: 10px; font-weight: 700; font-size: 16px;">
    📅 Texte bouton
</a>
```

**CTA urgence (rouge) :**
```html
<a href="..." style="display: inline-block; background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%); color: #ffffff; text-decoration: none; padding: 18px 56px; border-radius: 10px; font-weight: 800; font-size: 17px; text-transform: uppercase;">
    ✉️ TEXTE BOUTON
</a>
```

**CTA gratuit (vert) :**
```html
<a href="#" style="display: inline-block; background: linear-gradient(135deg, #10B981 0%, #059669 100%); color: #ffffff; text-decoration: none; padding: 16px 48px; border-radius: 10px; font-weight: 700; font-size: 16px;">
    📥 Texte bouton
</a>
```

### 🔢 BADGES NUMÉROTÉS

**Badge circulaire (pour étapes) :**
```html
<div style="width: 32px; height: 32px; background: linear-gradient(135deg, #7E22CE 0%, #5B21B6 100%); border-radius: 50%; color: #ffffff; font-weight: 700; font-size: 16px; text-align: center; line-height: 32px;">
    1
</div>
```

### ✅ CHECKMARKS / POINTS

**Liste avec flèches violettes :**
```html
<table>
    <tr>
        <td width="18" valign="top" style="color: #7E22CE; font-weight: 700; font-size: 16px;">→</td>
        <td style="padding: 6px 0;">
            <p style="font-size: 15px; color: #374151; margin: 0;">Texte item</p>
        </td>
    </tr>
</table>
```

**Checkmark vert circulaire :**
```html
<div style="width: 24px; height: 24px; background-color: #10B981; border-radius: 50%;">
    <span style="color: #ffffff; font-weight: 700; font-size: 14px; line-height: 24px; text-align: center; display: block;">✓</span>
</div>
```

---

## 🏗️ STRUCTURE TYPE D'UN EMAIL

### 📋 ANATOMIE COMPLÈTE

```html
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #fafafa; color: #374151; line-height: 1.6;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #fafafa; padding: 20px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden;">
                    
                    <!-- 1. HEADER AVEC LOGO -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #7E22CE 0%, #5B21B6 100%); padding: 24px 40px; text-align: center;">
                            <img src="[LOGO_URL]" alt="Seminary Logo" width="48" height="48" style="display: block; margin: 0 auto;">
                        </td>
                    </tr>
                    
                    <!-- 2. HERO SECTION -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #F8F5FC 0%, #F3E8FF 100%); padding: 32px 40px; text-align: center; border-bottom: 1px solid #E5E7EB;">
                            <!-- Badge + Titre + Sous-titre -->
                        </td>
                    </tr>
                    
                    <!-- 3. CONTENU PRINCIPAL -->
                    <tr>
                        <td style="padding: 40px;">
                            <!-- Greeting + Corps du message + CTA -->
                        </td>
                    </tr>
                    
                    <!-- 4. FOOTER -->
                    <tr>
                        <td style="background-color: #F9FAFB; padding: 20px 40px; text-align: center; border-top: 1px solid #E5E7EB;">
                            <p style="font-size: 11px; color: #6B7280; margin: 0;">© 2025 Seminary · Tous droits réservés</p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
```

### 📝 SIGNATURE STANDARD

**Version complète :**
```html
<tr>
    <td style="border-top: 1px solid #E5E7EB; padding-top: 24px;">
        <p style="font-size: 16px; font-weight: 700; color: #111827; margin: 0 0 2px 0;">Benoit Timéo</p>
        <p style="font-size: 13px; font-weight: 500; color: #7E22CE; margin: 0 0 6px 0;">Seminary · Séminaires sur-mesure Vosges</p>
        <p style="font-size: 12px; color: #6B7280; margin: 0;">
            🌐 <a href="https://goseminary.com" style="color: #7E22CE; text-decoration: none; font-weight: 600;">goseminary.com</a> · 📞 06 75 63 06 60
        </p>
    </td>
</tr>
```

**Version courte (breakup/finale) :**
```html
<tr>
    <td style="border-top: 1px solid #E5E7EB; padding-top: 24px;">
        <p style="font-size: 16px; font-weight: 700; color: #111827; margin: 0 0 2px 0;">Timéo</p>
        <p style="font-size: 13px; font-weight: 500; color: #7E22CE; margin: 0 0 6px 0;">Seminary</p>
        <p style="font-size: 12px; color: #6B7280; margin: 0;">📞 06 75 63 06 60 · 🌐 goseminary.com</p>
    </td>
</tr>
```

---

## ✍️ RÈGLES DE COPYWRITING

### 🎯 TON & VOIX

**Caractéristiques :**
- **Direct et concret** : Pas de blabla, aller droit au but
- **Local et authentique** : Ancrage Vosges, proximité
- **Professionnel mais accessible** : Pas corporate, humain
- **Orienté solution** : Focus sur bénéfices, pas features
- **Respectueux** : Jamais pushy, toujours permission-based

**À FAIRE :**
- ✅ Phrases courtes et impactantes
- ✅ Chiffres concrets (12k€, 48h, 50 salariés)
- ✅ Verbes d'action (bloquer, réserver, organiser)
- ✅ Exemples réels (PME 40p, VTT Rémy Absalon)
- ✅ Questions rhétoriques ("Deal ?", "Intéressé(e) ?")

**À ÉVITER :**
- ❌ Jargon marketing ("solutions innovantes", "écosystème")
- ❌ Superlatifs excessifs ("le meilleur", "unique au monde")
- ❌ Phrases trop longues (>25 mots)
- ❌ Langage corporate froid
- ❌ Pression commerciale agressive

### 📊 STRUCTURE NARRATIVE EFFICACE

**Email de prospection (format court) :**
1. **Hook** (1 phrase) : Problème ou opportunité
2. **Contexte** (2-3 phrases) : Situation actuelle
3. **Solution** (box structurée) : Ce que Seminary fait
4. **Social proof** (optionnel) : Exemples clients
5. **CTA clair** (1 action) : Prendre RDV / Répondre

**Email de valeur/éducation :**
1. **Cadeau** (ressource gratuite)
2. **Contenu** (liste bénéfices)
3. **Encouragement** (bienveillance)
4. **Rappel dispo** (porte ouverte)

**Email d'urgence :**
1. **Scarcity** (places limitées)
2. **Timeline** (dates précises)
3. **Justification** (pourquoi urgence)
4. **2 options claires** (OUI ou ignorer)

### 🎭 PSYCHOLOGIE PERSUASIVE

**Leviers utilisés :**
- **Aversion à la perte** : "Combien ça coûte quand ça rate ?"
- **Scarcity** : "3 derniers créneaux"
- **Social proof** : "PME locales réservent en masse"
- **Réciprocité** : Checklist gratuite
- **Autorité** : Exemples concrets, partenaires nommés
- **Simplicité** : "Répondez OUI", "Deal ?"

---

## 📅 TYPES D'EMAILS DE LA SÉQUENCE

### 📧 EMAIL 1 - INITIAL OUTREACH (Jour 0)

**Objectifs :**
- Présenter Seminary en 30 secondes
- Identifier le problème (organisation = 20h de recherche)
- Proposer la solution tout-en-un
- CTA : Réserver 15 min

**Éléments clés :**
- Badge focus ("Fin d'année", "Direct/Problème")
- Problème encadré en rouge
- Solution en 4 points (→ Lieux, → Activités, → Prestataires, → Gestion)
- 1 image team-building
- CTA Calendly

**Tokens :** `{{first_name}}`, `{{company}}`

---

### 📧 EMAIL 2 - FOLLOW-UP STORYTELLING (Jour +3)

**Objectifs :**
- Apporter de la valeur via exemple concret
- Montrer expertise et références
- Créer identification (cas client similaire)
- CTA : Échange 15 min pour propositions sur-mesure

**Éléments clés :**
- Badge "Follow-up"
- Cas client structure (Client / Besoin / Solution / Résultat)
- Utilisation de valeurs génériques (50 salariés, Épinal, industrielle)
- 2 images (team + paysage Vosges)
- Process en 3 options sur-mesure

**Tokens :** `{{first_name}}`, `{{company}}`

---

### 📧 EMAIL 3A - BREAKUP SOFT (Jour +7)

**Objectifs :**
- Nettoyer la liste (permission to close)
- Respecter le temps du prospect
- Laisser porte ouverte pour le futur
- Action minimale (répondre "intéressé")

**Éléments clés :**
- Badge gris "Dernier message"
- 2 box distinctes (ignorer vs répondre)
- Question simple "Deal ?"
- P.S. stratégique (garder sous le coude)
- Ton humble et respectueux

**Tokens :** `{{first_name}}`, `{{company}}`

---

### 📧 EMAIL 3B - VALEUR FINALE (Jour +7) 

**Objectifs :**
- Apporter valeur sans demande (lead magnet)
- Positionner comme expert généreux
- Créer réciprocité via ressource gratuite
- Rester top-of-mind

**Éléments clés :**
- Badge vert "Gratuit"
- Checklist avec 4 bénéfices concrets
- CTA vert téléchargement
- Message encourageant ("Bonne organisation en interne")
- Signature courte "Timéo"

**Tokens :** `{{first_name}}`

---

### 📧 EMAIL 4 - OFFRE SPÉCIALE URGENCE (Jour +14)

**Objectifs :**
- Créer urgence réelle (places limitées)
- Dates précises fin novembre / début décembre
- Action immédiate (répondre OUI)
- Justifier rareté (PME locales réservent)

**Éléments clés :**
- Header + badge rouge (urgence)
- 3 créneaux avec checkmarks verts
- Box jaune urgence (10 jours)
- 2 options claires (OUI box violette / Ignorer box grise)
- CTA rouge imposant "RÉPONDRE OUI"

**Tokens :** `{{first_name}}`, `{{company}}`

---

## 🔗 LIENS IMPORTANTS

**Calendly (RDV découverte) :**
```
https://calendly.com/goseminary/decouverte-seminary
```

**Site web :**
```
https://goseminary.com
```

**Email contact :**
```
contact@goseminary.com
```

**Téléphone :**
```
06 75 63 06 60
```

---

## ✅ CHECKLIST VALIDATION EMAIL

Avant de valider un template, vérifier :

### Structure technique
- [ ] Uniquement balise `<body>` (pas de `<head>`, `<style>`, `<link>`)
- [ ] CSS 100% inline
- [ ] Structure en tables HTML
- [ ] Width="600" sur container principal
- [ ] Attributs cellpadding="0" cellspacing="0" border="0"

### Tokens Apollo
- [ ] Utilisation uniquement de `{{first_name}}` et `{{company}}`
- [ ] Pas de syntaxe conditionnelle complexe
- [ ] Valeurs par défaut intégrées dans le texte si nécessaire

### Design Seminary
- [ ] Logo Seminary présent (bonne URL)
- [ ] Couleurs violettes (#7E22CE, #5B21B6)
- [ ] Gradients appliqués correctement
- [ ] Border-radius (12px containers, 10px boutons, 20px badges)
- [ ] Images avec border-radius: 10px

### Contenu
- [ ] Greeting personnalisé avec `{{first_name}}`
- [ ] Message clair et concis (< 200 mots hors signature)
- [ ] 1 CTA principal évident
- [ ] Signature complète (nom, entreprise, contact)
- [ ] Footer avec copyright

### Copywriting
- [ ] Ton direct et authentique
- [ ] Pas de jargon marketing
- [ ] Verbes d'action
- [ ] Chiffres concrets si pertinent
- [ ] Question ou CTA clair en fin

### Responsive
- [ ] Width="600" avec max-width via style
- [ ] Images avec max-width: 100%
- [ ] Padding adaptatif (40px → 20px si besoin)

---

## 🚀 EXEMPLES DE VARIATIONS À CRÉER

Si tu dois créer de nouveaux templates, voici des variations possibles :

### Par industrie
- PME industrielles (métallurgie, plasturgie)
- Secteur tertiaire (bureaux d'études, cabinets)
- Commerce / Retail
- Tech / Startups

### Par taille d'entreprise
- TPE (10-20 salariés)
- PME (20-100 salariés)
- ETI (100-250 salariés)

### Par timing
- Séminaire de fin d'année (Q4)
- Team-building printemps
- Séminaire de rentrée (septembre)
- Événement one-shot urgent

### Par objectif événement
- Cohésion d'équipe
- Kick-off commercial
- Formation management
- Célébration résultats

---

## RESPONSIVE MOBILE (telephone, tablette)
- Point primordial : tous les templates doivent pouvoir etre efficacement lisible sur un télephone de nimporte quel types, les élements doivent être autant clair et précis, avec le même déroulé, que sur le format ordinateur
- Cela ne doit pas impacter le responsive laptop/ordinateur qui doit rester intact et impeccable dans sa présentation
-ATTENTION : aux images qui sont le coeur du responsive et qui doivent elles aussi être bien responsive mobile pour une efficacité et agréabilité visuelle optimale

## 💡 CONSEILS FINAUX

1. **Simplicité avant tout** : Un email = 1 message = 1 CTA
2. **Respect du prospect** : Toujours donner option de sortie
3. **Valeur réelle** : Chaque email doit apporter quelque chose
4. **Tests A/B** : Varier sujets, hooks, longueurs
5. **Mesure** : Tracker ouvertures, clics, réponses

**Signature :**
Pour toute question : Benoit Timéo | Seminary | goseminary.com | 06 75 63 06 60

---

*Document de référence complet pour la création de templates email Seminary compatibles Apollo.io - Version 1.0 - Octobre 2025*