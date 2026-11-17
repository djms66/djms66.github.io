#!/usr/bin/env python3
"""Pages publiques d'Atelier Web (GitHub Pages) : accueil, assistance, confidentialité, mentions légales, FR + EN.
Lancer : python3 build.py — écrit les pages dans ce dossier."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIL = "contact@danielstreng.fr"
UPDATED = {"fr": "17 novembre 2026", "en": "November 17, 2026"}

# chemin de chaque page, par langue
PATHS = {
    "home":    {"en": "atelier-web/en/",          "fr": "atelier-web/"},
    "support": {"en": "atelier-web/en/support/",  "fr": "atelier-web/assistance/"},
    "privacy": {"en": "atelier-web/en/privacy/",  "fr": "atelier-web/confidentialite/"},
    "legal":   {"en": "atelier-web/en/legal/",    "fr": "atelier-web/mentions-legales/"},
}
NAV = {
    "en": [("home", "Atelier Web"), ("support", "Support"), ("privacy", "Privacy"), ("legal", "Legal notice")],
    "fr": [("home", "Atelier Web"), ("support", "Assistance"), ("privacy", "Confidentialité"), ("legal", "Mentions légales")],
}

CSS = """
:root{--ink:#16151c;--soft:#5b5866;--line:#e6e1d8;--bg:#faf7f2;--accent:#5538ff}
@media (prefers-color-scheme:dark){:root{--ink:#f2efe8;--soft:#aaa6b4;--line:#2e2c36;--bg:#14131a;--accent:#8f7dff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;-webkit-text-size-adjust:100%}
header,main,footer{max-width:760px;margin:0 auto;padding:0 24px}
header{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:baseline;padding-top:28px;padding-bottom:18px;border-bottom:1px solid var(--line)}
header .brand{font-weight:800;letter-spacing:.14em;text-transform:uppercase;font-size:15px;margin-right:auto;color:var(--ink);text-decoration:none}
header a{color:var(--soft);text-decoration:none;font-size:15px}
header a[aria-current]{color:var(--ink);font-weight:600}
header .lang{margin-left:8px;padding:2px 10px;border:1px solid var(--line);border-radius:999px}
main{padding-top:36px;padding-bottom:48px}
h1{font-size:40px;line-height:1.1;letter-spacing:-.02em;margin:0 0 12px}
h2{font-size:21px;margin:36px 0 8px}
h3{font-size:17px;margin:22px 0 4px}
p,li{color:var(--ink)}
.lead{font-size:20px;color:var(--soft);margin:0 0 8px}
.date{color:var(--soft);font-size:14px}
a{color:var(--accent)}
ul{padding-left:1.2em}
li{margin:6px 0}
.card{border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:18px 0}
footer{padding-top:18px;padding-bottom:40px;border-top:1px solid var(--line);color:var(--soft);font-size:14px}
"""

M = f'<a href="mailto:{MAIL}">{MAIL}</a>'

BODY = {
"home": {
"en": ("Atelier Web — website builder for Mac, iPad and iPhone", f"""
<h1>Atelier Web</h1>
<p class="lead">Lay out your website like a poster, on Mac, iPad and iPhone.</p>
<p>Text, images, shapes, galleries and sheet music go exactly where you want them: no blocks, no code.
Every page adapts to desktop, tablet and mobile, then goes online in one step: Netlify, your web host or your WordPress site.</p>
<div class="card"><strong>Try it, then buy once.</strong> Creating, editing and previewing are free and unlimited.
Publishing is included in the 7-day free trial, then in a one-time purchase for all your devices. No subscription.</div>
<p>Questions? See the <a href="support/">support page</a> or write to {M}.</p>
"""),
"fr": ("Atelier Web — création de sites pour Mac, iPad et iPhone", f"""
<h1>Atelier Web</h1>
<p class="lead">Composez votre site comme une affiche, sur Mac, iPad et iPhone.</p>
<p>Textes, images, formes, galeries et partitions se placent exactement où vous voulez : sans blocs, sans code.
Chaque page s'adapte à l'ordinateur, la tablette et le mobile, puis se met en ligne en un geste : Netlify, votre hébergeur ou votre WordPress.</p>
<div class="card"><strong>Essayez, puis achetez une fois.</strong> Créer, modifier et prévisualiser sont gratuits et sans limite.
La mise en ligne est comprise dans l'essai gratuit de 7 jours, puis dans un achat unique valable sur tous vos appareils. Aucun abonnement.</div>
<p>Une question ? Consultez la page <a href="assistance/">Assistance</a> ou écrivez à {M}.</p>
"""),
},
"support": {
"en": ("Support — Atelier Web", f"""
<h1>Support</h1>
<p class="lead">Answers to common questions, and how to reach us.</p>
<h2>Contact</h2>
<p>Write to {M}. To help us answer quickly, please mention your device (Mac, iPad or iPhone), the app version
(Options › About) and, if possible, a screenshot of the problem. We reply within a few working days.</p>
<h2>Frequently asked questions</h2>
<h3>What does each device do?</h3>
<p>Mac and iPad have the full design tools. iPhone is a companion: review your sites, fix text, replace images, preview and publish.</p>
<h3>Where are my pages stored?</h3>
<p>On your device, in the app's Documents folder. If you turn on sync, they also go through the folder you choose (iCloud Drive or another service).</p>
<h3>How do I put my site online?</h3>
<p>Tap “Publish”. The first time, choose where your site lives: Netlify, your web host (FTP), your WordPress site or files to upload yourself. Atelier Web remembers your choice.</p>
<h3>What is free, and what do I pay for?</h3>
<p>Creating, editing and previewing are free and unlimited. Publishing requires the one-time purchase “Atelier Web Full”, valid on every device signed in with the same Apple Account, or the 7-day free trial. There is no subscription, and the trial never charges you when it ends.</p>
<h3>I bought it on another device. How do I unlock it here?</h3>
<p>Open Options › Atelier Web Full and tap “Restore Purchases”, signed in with the same Apple Account.</p>
<h3>How do I get a refund?</h3>
<p>Purchases are handled by Apple: request a refund at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h3>Can I use any image, font or piece of music?</h3>
<p>Only what you have the right to use. The fonts, sounds and sample pieces included in the app are free to use (licences listed in Options › About). Imported scores must be in the public domain or yours.</p>
"""),
"fr": ("Assistance — Atelier Web", f"""
<h1>Assistance</h1>
<p class="lead">Les réponses aux questions courantes, et comment nous joindre.</p>
<h2>Nous contacter</h2>
<p>Écrivez à {M}. Pour une réponse rapide, précisez l'appareil (Mac, iPad ou iPhone), la version de l'appli
(Options › À propos) et, si possible, une capture d'écran du problème. Réponse sous quelques jours ouvrés.</p>
<h2>Questions fréquentes</h2>
<h3>À quoi sert chaque appareil ?</h3>
<p>Le Mac et l'iPad ont tous les outils de mise en page. L'iPhone accompagne : revoir ses sites, corriger un texte, remplacer une image, prévisualiser et publier.</p>
<h3>Où sont rangées mes pages ?</h3>
<p>Sur votre appareil, dans le dossier Documents de l'appli. Si vous activez la synchronisation, elles passent aussi par le dossier que vous choisissez (iCloud Drive ou un autre service).</p>
<h3>Comment mettre mon site en ligne ?</h3>
<p>Touchez « Mettre en ligne ». La première fois, choisissez où votre site doit vivre : Netlify, votre hébergeur (FTP), votre WordPress ou des fichiers à déposer vous-même. Atelier Web retient votre choix.</p>
<h3>Qu'est-ce qui est gratuit, et qu'est-ce qui est payant ?</h3>
<p>Créer, modifier et prévisualiser sont gratuits et sans limite. La mise en ligne demande l'achat unique « Atelier Web complet », valable sur tous les appareils liés au même identifiant Apple, ou l'essai gratuit de 7 jours. Aucun abonnement, et l'essai ne déclenche aucun paiement à son terme.</p>
<h3>J'ai acheté l'appli sur un autre appareil. Comment la débloquer ici ?</h3>
<p>Ouvrez Options › Atelier Web complet et touchez « Restaurer les achats », avec le même identifiant Apple.</p>
<h3>Comment obtenir un remboursement ?</h3>
<p>Les achats sont gérés par Apple : faites la demande sur <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h3>Puis-je utiliser n'importe quelle image, police ou musique ?</h3>
<p>Seulement ce que vous avez le droit d'utiliser. Les polices, sons et morceaux d'exemple fournis dans l'appli sont libres d'usage (licences dans Options › À propos). Les partitions importées doivent être libres de droit ou les vôtres.</p>
"""),
},
}

BODY["privacy"] = {
"en": ("Privacy policy — Atelier Web", f"""
<h1>Privacy policy</h1>
<p class="date">Last updated: {UPDATED['en']}</p>
<h2>In short</h2>
<p>Atelier Web collects no personal data. No account, no usage statistics, no advertising, no tracking. The publisher receives nothing you create.</p>
<h2>What stays on your device</h2>
<ul>
<li>Your pages, images, fonts and imported pieces (MIDI, MusicXML, ABC) are stored in the app's Documents folder, on your device.</li>
<li>Only the photos and files you choose yourself are read.</li>
<li>Your WordPress password and your Netlify or FTP credentials are kept encrypted in Apple's keychain and are only used to connect to those services.</li>
</ul>
<h2>Connections made by the app</h2>
<ul>
<li>Only to the addresses you give it: your WordPress site, your hosting (Netlify, FTP) and the web pages you choose to import. Those sites receive the usual information of a visit (IP address, device type) under their own rules.</li>
<li>Instrument sounds for sheet music are included in the app. They are only fetched online (GitHub) as a fallback, if missing.</li>
<li>Sync between your devices goes through the folder you choose (iCloud Drive or another service), under that service's terms.</li>
</ul>
<h2>Purchases</h2>
<p>The free trial and the full-version purchase are handled entirely by Apple's App Store. The publisher receives neither your name, nor your address, nor your payment details.</p>
<h2>Sites you publish</h2>
<p>Sites made with Atelier Web contain no tracker added by the app. If you add forms or third-party services, you are responsible for them towards your visitors.</p>
<h2>Children</h2>
<p>The app collects no data, including children's data.</p>
<h2>Your rights and contact</h2>
<p>Since no data about you is collected, there is nothing to access, correct or delete at the publisher's. Any question: {M}.</p>
"""),
"fr": ("Politique de confidentialité — Atelier Web", f"""
<h1>Politique de confidentialité</h1>
<p class="date">Dernière mise à jour : {UPDATED['fr']}</p>
<h2>En bref</h2>
<p>Atelier Web ne collecte aucune donnée personnelle. Pas de compte, pas de statistiques d'usage, pas de publicité, pas de pisteur. L'éditeur ne reçoit rien de ce que vous créez.</p>
<h2>Ce qui reste sur votre appareil</h2>
<ul>
<li>Vos pages, images, polices et morceaux importés (MIDI, MusicXML, ABC) sont rangés dans le dossier Documents de l'application, sur votre appareil.</li>
<li>Seules les photos et les fichiers que vous choisissez vous-même sont lus.</li>
<li>Le mot de passe de votre site WordPress, et vos accès Netlify ou FTP, sont gardés chiffrés dans le trousseau d'Apple et ne servent qu'à vous connecter à ces services.</li>
</ul>
<h2>Les connexions que fait l'application</h2>
<ul>
<li>Uniquement vers les adresses que vous lui indiquez : votre site WordPress, votre hébergement (Netlify, FTP) et les pages web que vous choisissez d'importer. Ces sites reçoivent les informations habituelles d'une visite (adresse IP, type d'appareil), selon leurs propres règles.</li>
<li>Les sons d'instrument des partitions sont livrés avec l'application. Ils ne sont demandés en ligne (GitHub) qu'en secours, s'ils manquent.</li>
<li>La synchronisation entre vos appareils passe par le dossier que vous désignez (iCloud Drive ou un autre service), selon les conditions de ce service.</li>
</ul>
<h2>Achats</h2>
<p>L'essai gratuit et l'achat de la version complète passent entièrement par l'App Store d'Apple. L'éditeur ne reçoit ni votre nom, ni votre adresse, ni vos coordonnées bancaires.</p>
<h2>Les sites que vous publiez</h2>
<p>Les sites créés avec Atelier Web n'intègrent aucun pisteur ajouté par l'application. Si vous y ajoutez des formulaires ou des services tiers, vous en êtes responsable vis-à-vis de vos visiteurs.</p>
<h2>Enfants</h2>
<p>L'application ne collecte aucune donnée, y compris celles des enfants.</p>
<h2>Vos droits et contact</h2>
<p>Aucune donnée vous concernant n'étant collectée, il n'y a rien à consulter, rectifier ou effacer chez l'éditeur. Pour toute question : {M}.</p>
"""),
}

BODY["legal"] = {
"en": ("Legal notice — Atelier Web", f"""
<h1>Legal notice</h1>
<h2>Publisher</h2>
<p>Atelier Web and this site are published by Daniel Streng, France. Contact: {M}. Publication director: Daniel Streng.</p>
<h2>Hosting</h2>
<p>GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States — <a href="https://pages.github.com">GitHub Pages</a>.</p>
<h2>Sale of the app</h2>
<p>The app is distributed and sold by Apple through the App Store, under Apple's standard licence agreement (EULA).</p>
<h2>Intellectual property</h2>
<p>The app, its texts and visuals are protected by copyright. Third-party fonts, sounds and libraries are used under their own licences, listed in the app (Options › About): SIL Open Font License, Apache License 2.0, MIT (abcjs), CC BY-SA 3.0 (MusyngKite sounds).</p>
<h2>Personal data</h2>
<p>See the <a href="../privacy/">privacy policy</a>: the app collects no personal data.</p>
"""),
"fr": ("Mentions légales — Atelier Web", f"""
<h1>Mentions légales</h1>
<h2>Éditeur</h2>
<p>Atelier Web et ce site sont édités par Daniel Streng, France. Contact : {M}. Directeur de la publication : Daniel Streng.</p>
<h2>Hébergement</h2>
<p>GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — <a href="https://pages.github.com">GitHub Pages</a>.</p>
<h2>Vente de l'application</h2>
<p>L'application est distribuée et vendue par Apple sur l'App Store, selon le contrat de licence standard d'Apple (EULA).</p>
<h2>Propriété intellectuelle</h2>
<p>L'application, ses textes et visuels sont protégés par le droit d'auteur. Les polices, sons et bibliothèques de tiers sont utilisés selon leurs propres licences, indiquées dans l'appli (Options › À propos) : SIL Open Font License, Apache License 2.0, MIT (abcjs), CC BY-SA 3.0 (sons MusyngKite).</p>
<h2>Données personnelles</h2>
<p>Voir la <a href="../confidentialite/">politique de confidentialité</a> : l'application ne collecte aucune donnée personnelle.</p>
"""),
}


def rel(src, dst):
    """Lien relatif d'une page (dossier) vers une autre."""
    return os.path.relpath(os.path.join(ROOT, dst), os.path.join(ROOT, src)).replace(os.sep, "/") + "/"


def page(key, lang):
    title, body = BODY[key][lang]
    here = PATHS[key][lang]
    other = "fr" if lang == "en" else "en"
    nav = []
    for k, label in NAV[lang]:
        cur = ' aria-current="page"' if k == key else ""
        cls = ' class="brand"' if k == "home" else ""
        nav.append(f'<a{cls} href="{rel(here, PATHS[k][lang])}"{cur}>{label}</a>')
    nav.append(f'<a class="lang" href="{rel(here, PATHS[key][other])}" hreflang="{other}" lang="{other}">'
               f'{"Français" if other == "fr" else "English"}</a>')
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="https://djms66.github.io/{PATHS[key][l]}">' for l in ("en", "fr"))
    foot = ("© 2026 Daniel Streng · Atelier Web" if lang == "en" else "© 2026 Daniel Streng · Atelier Web")
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{title}">
{alt}
<style>{CSS}</style></head>
<body><header>{''.join(nav)}</header>
<main>{body}</main>
<footer>{foot} · <a href="{rel(here, PATHS['legal'][lang])}">{'Legal notice' if lang == 'en' else 'Mentions légales'}</a></footer>
</body></html>
"""


for key in PATHS:
    for lang in ("en", "fr"):
        d = os.path.join(ROOT, PATHS[key][lang])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(page(key, lang))

# Racine : vers la page anglaise ou française selon la langue du navigateur.
open(os.path.join(ROOT, "index.html"), "w").write("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Atelier Web</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script>location.replace((navigator.language||'').toLowerCase().startsWith('fr')?'atelier-web/':'atelier-web/en/');</script>
</head><body><p><a href="atelier-web/en/">Atelier Web (English)</a> · <a href="atelier-web/">Atelier Web (Français)</a></p></body></html>
""")
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
print("pages écrites")
