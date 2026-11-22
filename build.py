#!/usr/bin/env python3
"""Pages publiques d'Atelier Web (GitHub Pages) : accueil, assistance, confidentialité, mentions légales, FR + EN.
Lancer : python3 build.py — écrit les pages dans ce dossier."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIL = "contact@danielstreng.fr"
UPDATED = {"fr": "18 novembre 2026", "en": "November 18, 2026"}

# chemin de chaque page, par langue
PATHS = {
    "home":    {"en": "en/",          "fr": "fr/"},
    "support": {"en": "en/support/",  "fr": "fr/assistance/"},
    "privacy": {"en": "en/privacy/",  "fr": "fr/confidentialite/"},
    "legal":   {"en": "en/legal/",    "fr": "fr/mentions-legales/"},
}
SITE = "https://atelier-web.danielstreng.fr/"
# Logo Atelier Web (logo_atelier_web.svg) : en tête de page, il tourne lentement autour de son centre de symétrie.
LOGO_PATH = "M1000.44,992.099l-288.739,-981.713l236.22,-0l236.22,708.661l236.22,-561.024l236.052,0l236.22,561.024l236.22,-708.661l236.22,0l-288.479,981.713l994.256,240.728l-118.11,204.573l-731.829,-149.758l367.75,485.085l-118.026,204.427l-603.971,-75.939l495.609,558.904l-118.11,204.573l-705.652,-740.868l-705.944,740.941l-118.11,-204.573l495.609,-558.904l-603.971,75.939l-118.026,-204.427l367.75,-485.085l-731.829,149.758l-118.11,-204.573l994.558,-240.801Zm537.948,576.132l-0,-0.031l0.062,0.016l0.062,-0.016l0,0.031l275.961,69.053l151.772,-262.876l-197.899,-204.54l-78.187,-273.655l-303.543,0l-78.199,273.697l-197.929,204.571l151.772,262.876l276.128,-69.126Zm-812.102,203.32l340.1,-60.072l-118.026,-204.427l-222.074,264.499Zm812.102,-1406.602l-118.026,324.571l236.052,-0l-118.026,-324.571Zm812.06,1406.529l-222.074,-264.499l-118.026,204.427l340.1,60.072Z"
# Anciennes adresses (djms66.github.io/atelier-web/…) : redirigées vers les nouvelles.
OLD = {"atelier-web/": "fr/", "atelier-web/en/": "en/",
       "atelier-web/assistance/": "fr/assistance/", "atelier-web/en/support/": "en/support/",
       "atelier-web/confidentialite/": "fr/confidentialite/", "atelier-web/en/privacy/": "en/privacy/",
       "atelier-web/mentions-legales/": "fr/mentions-legales/", "atelier-web/en/legal/": "en/legal/"}

NAV = {
    "en": [("home", "Atelier Web"), ("support", "Support"), ("privacy", "Privacy"), ("legal", "Legal notice")],
    "fr": [("home", "Atelier Web"), ("support", "Assistance"), ("privacy", "Confidentialité"), ("legal", "Mentions légales")],
}

CSS = """
:root{color-scheme:dark;--bg:#10141b;--panel:#1a2029;--ink:#f6f5f1;--muted:#bac1cb;--accent:#ad9bff;--hair:#333c48}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:100%}
a{color:inherit}
a:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
.brand .logo{width:1.2em;height:1.15em;vertical-align:-.2em;margin-right:.35em;fill:currentColor;
  transform-origin:50.11% 48.88%;animation:tourne 26s linear infinite}
@keyframes tourne{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.brand .logo{animation:none}}
.site-header,.site-main,.site-footer{width:min(100% - 56px,1200px);margin:0 auto}
.site-header{min-height:78px;display:flex;align-items:center;gap:24px;border-bottom:1px solid var(--hair)}
.site-header .brand{font-size:22px;font-weight:700;letter-spacing:-.045em;margin-right:auto;text-decoration:none;white-space:nowrap}
.site-nav{display:flex;align-items:center;gap:clamp(14px,2.2vw,34px)}
.site-nav a,.site-header .lang{font-size:14px;color:var(--muted);text-decoration:none;white-space:nowrap}
.site-nav a[aria-current]{color:var(--accent)}
.site-nav a:hover,.site-header .lang:hover{color:var(--ink)}
.site-header .lang{padding:5px 10px;border-left:1px solid var(--hair);margin-left:0}
.site-main{padding-top:50px;padding-bottom:84px;min-height:calc(100vh - 160px)}
.site-main:not(.home){max-width:900px}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:500}
h1{font-size:clamp(42px,6vw,74px);line-height:1.04;letter-spacing:-.045em;margin:0 0 18px}
h2{font-size:30px;line-height:1.2;margin:54px 0 13px;padding-top:26px;border-top:1px solid var(--hair)}
h3{font-size:19px;margin:30px 0 5px}
p,li{color:var(--ink)}
.lead{font-size:clamp(19px,2.2vw,25px);line-height:1.45;color:#d7dbe2;margin:0 0 16px}
.date{color:var(--muted);font-size:14px}
.site-main a:not(.action){color:#c9bcff;text-underline-offset:3px}
ul{padding-left:1.2em}
li{margin:9px 0}
.site-footer{padding:22px 0 36px;border-top:1px solid var(--hair);color:#a5adb8;font-size:13px;display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap}
.footer-links{display:flex;gap:20px;flex-wrap:wrap}
.site-footer a{color:var(--muted);text-decoration:none}
.site-footer a:hover{color:var(--ink)}
.home-hero{display:grid;grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);align-items:center;gap:clamp(36px,6vw,84px);padding:42px 0 70px}
.home-copy h1{max-width:700px}
.home-copy .lead{max-width:610px}
.home-copy p:not(.lead){max-width:590px;color:var(--muted)}
.home-image{margin:0;min-width:0}
.home-image img{display:block;width:100%;aspect-ratio:1.42;object-fit:cover;object-position:center;border:1px solid var(--hair);border-radius:14px}
.home-image figcaption{color:var(--muted);font-size:12px;margin-top:9px}
.actions{display:flex;align-items:center;gap:24px;flex-wrap:wrap;margin-top:28px}
.action{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 20px;background:var(--accent);color:#10141b;text-decoration:none;font-weight:650}
.action-secondary{color:var(--ink);text-decoration:underline;text-underline-offset:5px}
.offer{display:grid;grid-template-columns:minmax(230px,.7fr) 1.3fr;gap:42px;padding:34px 0;border-top:1px solid var(--hair)}
.offer h2{border:0;padding:0;margin:0;font-size:clamp(28px,3.3vw,40px)}
.offer p{margin:0;color:var(--muted);max-width:700px}
@media(max-width:760px){.site-header,.site-main,.site-footer{width:min(100% - 36px,1200px)}.site-header{min-height:0;padding:16px 0 13px;display:grid;grid-template-columns:1fr auto;gap:14px}.site-header .brand{font-size:20px}.site-nav{grid-column:1/-1;grid-row:2;gap:0;justify-content:space-between;overflow-x:auto;padding-bottom:2px}.site-nav a{font-size:12px}.site-header .lang{grid-column:2;grid-row:1;border-left:1px solid var(--hair)}.site-main{padding-top:27px;padding-bottom:58px}.home-hero{grid-template-columns:1fr;gap:28px;padding:15px 0 46px}.home-copy h1{font-size:clamp(44px,12vw,66px)}.home-image{order:-1}.home-image img{aspect-ratio:1.55}.offer{grid-template-columns:1fr;gap:12px;padding:26px 0}.site-footer{padding-top:18px}.footer-links{gap:12px 18px}}
@media(max-width:390px){.site-header,.site-main,.site-footer{width:min(100% - 28px,1200px)}.site-nav{gap:12px;justify-content:flex-start}.site-nav a{font-size:11px}.home-copy h1{font-size:43px}.actions{gap:16px}}
"""

M = f'<a href="mailto:{MAIL}">{MAIL}</a>'

BODY = {
"home": {
"en": ("Atelier Web — website builder for Mac, iPad and iPhone", f"""
<section class="home-hero"><div class="home-copy">
<h1>Lay out your website like a poster.</h1>
<p class="lead">On Mac, iPad and iPhone.</p>
<p>Text, images, shapes, galleries and sheet music go exactly where you want them: no blocks, no code. Every page adapts to desktop, tablet and mobile, then goes online in one step: Netlify, your web host or your WordPress site.</p>
<div class="actions"><a class="action" href="../press/">Watch the demonstrations</a><a class="action-secondary" href="support/">Get support</a></div>
</div><figure class="home-image"><img src="../press/assets/preview-en.jpg" alt="Atelier Web editor with a visual page composition and editing tools"><figcaption>Compose freely on Mac, iPad and iPhone.</figcaption></figure></section>
<section class="offer"><h2>Try it, then buy once.</h2><p>Start a free 7-day trial to create and edit; publishing stays locked. When it ends, your existing sites remain available in preview. One purchase unlocks creating, editing and publishing on all your devices. No subscription.</p></section>
<p>Questions? Write to {M} or visit our <a href="support/">support page</a>.</p>
"""),
"fr": ("Atelier Web — création de sites pour Mac, iPad et iPhone", f"""
<section class="home-hero"><div class="home-copy">
<h1>Composez votre site comme une affiche.</h1>
<p class="lead">Sur Mac, iPad et iPhone.</p>
<p>Textes, images, formes, galeries et partitions se placent exactement où vous voulez : sans blocs, sans code. Chaque page s'adapte à l'ordinateur, la tablette et le mobile, puis se met en ligne en un geste : Netlify, votre hébergeur ou votre WordPress.</p>
<div class="actions"><a class="action" href="../press/">Voir les démonstrations</a><a class="action-secondary" href="assistance/">Besoin d’aide ?</a></div>
</div><figure class="home-image"><img src="../press/assets/preview-fr.jpg" alt="Éditeur Atelier Web avec une composition visuelle et les outils de mise en page"><figcaption>Composez librement sur Mac, iPad et iPhone.</figcaption></figure></section>
<section class="offer"><h2>Essayez, puis achetez une fois.</h2><p>Commencez l'essai gratuit de 7 jours pour créer et modifier ; la mise en ligne reste bloquée. À la fin, vos sites restent consultables en aperçu. Un achat unique débloque la création, la modification et la mise en ligne sur tous vos appareils. Aucun abonnement.</p></section>
<p>Une question ? Écrivez à {M} ou consultez l’<a href="assistance/">assistance</a>.</p>
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
<p>Start the 7-day free trial to create and edit; publishing stays locked. After the trial, your existing sites remain available in preview, while creating, editing and publishing require the one-time purchase “Atelier Web Full”, valid on every device signed in with the same Apple Account. There is no subscription, and the trial ends without a charge. The price is shown on the App Store and in the app (Options › Atelier Web Full), in your country's currency.</p>
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
<p>Commencez l'essai gratuit de 7 jours pour créer et modifier ; la mise en ligne reste bloquée. À la fin de l'essai, vos sites existants restent consultables en aperçu ; créer, modifier et mettre en ligne demandent l'achat unique « Atelier Web complet », valable sur tous les appareils liés au même identifiant Apple. Aucun abonnement, et l'essai se termine sans paiement. Le prix est indiqué sur l'App Store et dans l'appli (Options › Atelier Web complet), dans la monnaie de votre pays.</p>
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
<li>A local timestamp helps calculate the 7-day trial and prevents changing the device clock from extending it. It stays on your device and is not sent to the publisher.</li>
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
<li>Un horodatage local sert à calculer les 7 jours d'essai et empêche qu'un changement d'horloge prolonge l'essai. Il reste sur votre appareil et n'est pas envoyé à l'éditeur.</li>
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
    home_label = "Atelier Web"
    home_cur = ' aria-current="page"' if key == "home" else ""
    brand = (f'<a class="brand" href="{rel(here, PATHS["home"][lang])}"{home_cur}>'
             f'<img class="logo" src="/logo.svg?v=3" alt="" width="28" height="28">{home_label}</a>')
    nav = []
    for k, label in NAV[lang][1:]:
        cur = ' aria-current="page"' if k == key else ""
        nav.append(f'<a href="{rel(here, PATHS[k][lang])}"{cur}>{label}</a>')
    press_label = "Press" if lang == "en" else "Presse"
    nav.append(f'<a href="{rel(here, "press/")}">{press_label}</a>')
    lang_link = f'<a class="lang" href="{rel(here, PATHS[key][other])}" hreflang="{other}" lang="{other}">{"FR" if other == "fr" else "EN"}</a>'
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{PATHS[key][l]}">' for l in ("en", "fr"))
    foot = "© 2026 Daniel Streng · Atelier Web"
    footer_labels = [
        ("Support" if lang == "en" else "Assistance", PATHS["support"][lang]),
        ("Privacy" if lang == "en" else "Confidentialité", PATHS["privacy"][lang]),
        ("Legal notice" if lang == "en" else "Mentions légales", PATHS["legal"][lang]),
        ("Press" if lang == "en" else "Presse", "press/"),
    ]
    footer_links = "".join(f'<a href="{rel(here, dst)}">{label}</a>' for label, dst in footer_labels)
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#10141b">
<title>{title}</title>
<meta name="description" content="{title}">
{alt}
<link rel="icon" href="/logo.svg?v=3" type="image/svg+xml"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=3"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png?v=3"><link rel="shortcut icon" href="/favicon.ico?v=3"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=3">
<style>{CSS}</style></head>
<body><header class="site-header">{brand}<nav class="site-nav" aria-label="{'Main navigation' if lang == 'en' else 'Navigation principale'}">{''.join(nav)}</nav>{lang_link}</header>
<main class="site-main {key}">{body}</main>
<footer class="site-footer"><span>{foot}</span><nav class="footer-links" aria-label="{'Footer navigation' if lang == 'en' else 'Navigation de pied de page'}">{footer_links}</nav></footer>
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
<link rel="icon" href="/logo.svg?v=3" type="image/svg+xml"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=3"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png?v=3"><link rel="shortcut icon" href="/favicon.ico?v=3"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=3">
<script>location.replace((navigator.language||'').toLowerCase().startsWith('fr')?'fr/':'en/');</script>
</head><body><p><a href="en/">Atelier Web (English)</a> · <a href="fr/">Atelier Web (Français)</a></p></body></html>
""")
for old, new in OLD.items():
    d = os.path.join(ROOT, old)
    os.makedirs(d, exist_ok=True)
    url = SITE + new
    open(os.path.join(d, "index.html"), "w").write(f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Atelier Web</title>
<meta http-equiv="refresh" content="0; url={url}"><link rel="canonical" href="{url}">
</head><body><p><a href="{url}">{url}</a></p></body></html>
""")
open(os.path.join(ROOT, "CNAME"), "w").write("atelier-web.danielstreng.fr\n")
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
print("pages écrites")
