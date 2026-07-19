# -*- coding: utf-8 -*-
import os, urllib.parse

BASE = "https://www.saveursmaghrebines.com"
WA = "33619257588"
OUT = os.path.dirname(os.path.abspath(__file__))

PRODUCTS = [
 dict(slug="patate-douce", nom="Patate douce", origine="Égypte", flag="🇪🇬",
   variete="Beauregard", dispo="disponible",
   desc="Patate douce Beauregard d'Égypte, chair orange, sucrée et régulière. Tous calibres, qualité export contrôlée au départ.",
   photos=[("photos/patate-recolte.jpg","Récolte en cours — origine Égypte"),
           ("photos/patate-calibre.jpg","Calibrage et conditionnement export")],
   specs=[("Origine","Égypte"),("Variété","Beauregard"),
          ("Calibres","S · M · L1 · L2 · XL · Jumbo"),
          ("Conditionnement","Carton 6 kg"),
          ("Saisonnalité","Août → Mars"),
          ("Incoterm proposé","CIF Marseille / Anvers"),
          ("Délai indicatif","≈ 15 jours"),
          ("Certifications","Phytosanitaire · Origine · GlobalG.A.P.")]),
 dict(slug="oignon-rouge", nom="Oignon rouge", origine="Égypte", flag="🇪🇬",
   variete="Rouge", dispo="disponible",
   desc="Oignon rouge d'Égypte, coloration intense, bonne conservation. Filets ou cartons selon votre besoin.",
   photos=[("photos/oignon-rouge.jpg","Oignon rouge — qualité export"),
           ("photos/oignon-transit.jpg","Chargement conteneur reefer au départ")],
   specs=[("Origine","Égypte"),
          ("Conditionnement","Filets 25 kg ou cartons"),
          ("Calibres","40/60 · 60/80 · 80+"),
          ("Saisonnalité","Mars → Septembre"),
          ("Incoterm proposé","CIF Marseille / Anvers"),
          ("Délai indicatif","≈ 15 jours"),
          ("Certifications","Phytosanitaire · Origine")]),
 dict(slug="mangue-kent", nom="Mangue Kent", origine="Sénégal", flag="🇸🇳",
   variete="Kent", dispo="disponible",
   desc="Mangue Kent du Sénégal, sans fibre, très demandée à Rungis. Départ avion pour l'ultra-frais ou bateau pour le volume.",
   photos=[],
   specs=[("Origine","Sénégal"),("Variété","Kent"),
          ("Conditionnement","Carton 4 kg"),
          ("Logistique","Avion (48h) ou bateau"),
          ("Saisonnalité","Mai → Septembre"),
          ("Certifications","Phytosanitaire · Origine")]),
 dict(slug="pitaya", nom="Pitaya — Fruit du dragon", origine="Vietnam / Équateur", flag="🐉",
   variete="Chair blanche, rouge ou jaune", dispo="bientot",
   desc="Fruit du dragon chair blanche, rouge ou jaune. Sourcing en cours de finalisation auprès d'origines vérifiées.",
   photos=[],
   specs=[("Origines","Vietnam · Équateur"),
          ("Variétés","Chair blanche · rouge · jaune"),
          ("Conditionnement","Cartons ventilés 5 / 10 kg"),
          ("Logistique","Maritime reefer, 16–25 jours"),
          ("Statut","Ouverture prochaine — pré-commandes possibles")]),
 dict(slug="fruit-de-la-passion", nom="Fruit de la passion", origine="Colombie", flag="🇨🇴",
   variete="Purple Passion Fruit", dispo="bientot",
   desc="Purple passion fruit de Colombie, calibre régulier, forte demande GMS et grossistes. Sourcing en cours de finalisation.",
   photos=[],
   specs=[("Origine","Colombie"),
          ("Variété","Purple Passion Fruit"),
          ("Logistique","Maritime reefer ou avion"),
          ("Statut","Ouverture prochaine — pré-commandes possibles")]),
]

CSS = """
:root{--vert:#0F3D2E;--vert2:#1B4332;--accent:#2D8A5F;--or:#C9A227;--creme:#FAF8F4;--txt:#25302B;--wa:#25D366;}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',-apple-system,Segoe UI,Roboto,sans-serif;background:var(--creme);color:var(--txt);line-height:1.55}
a{text-decoration:none;color:inherit}
.wrap{max-width:680px;margin:0 auto;padding:0 18px}
header.top{background:linear-gradient(135deg,var(--vert) 0%,var(--vert2) 100%);color:#fff;padding:14px 0}
header.top .wrap{display:flex;align-items:center;justify-content:space-between}
.logo{font-family:Georgia,'Times New Roman',serif;font-size:1.25rem;font-weight:700;letter-spacing:.3px}
.logo span{color:var(--or)}
.tag{font-size:.7rem;opacity:.85;letter-spacing:.14em;text-transform:uppercase}
.hero{background:linear-gradient(160deg,var(--vert) 0%,var(--vert2) 70%,#245B41 100%);color:#fff;padding:38px 0 44px;text-align:center}
.hero h1{font-family:Georgia,serif;font-size:1.7rem;line-height:1.25;margin-bottom:10px}
.hero p{opacity:.9;font-size:.95rem;max-width:480px;margin:0 auto}
.hero .pills{margin-top:18px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.pill{border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:5px 14px;font-size:.75rem}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:26px 0 10px}
@media(max-width:430px){.grid{grid-template-columns:1fr}}
.card{background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 6px 24px rgba(15,61,46,.10);transition:transform .15s}
.card:active{transform:scale(.98)}
.card .ph{height:150px;background-size:cover;background-position:center;position:relative}
.card .ph.nophoto{display:flex;align-items:center;justify-content:center;font-size:3rem;background:linear-gradient(135deg,#E8F3EC,#D2E7DA)}
.badge{position:absolute;top:10px;left:10px;font-size:.66rem;font-weight:600;padding:4px 10px;border-radius:999px;color:#fff;background:var(--accent)}
.badge.soon{background:var(--or)}
.card .in{padding:12px 14px 14px}
.card h3{font-size:.98rem;color:var(--vert)}
.card .or{font-size:.78rem;color:#6b7a72;margin-top:2px}
.section-t{font-family:Georgia,serif;color:var(--vert);font-size:1.25rem;margin:26px 0 4px}
.gal{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;padding:18px 0 6px;-webkit-overflow-scrolling:touch}
.gal img{scroll-snap-align:center;border-radius:16px;width:86%;flex:none;box-shadow:0 8px 26px rgba(15,61,46,.16)}
.cap{font-size:.75rem;color:#6b7a72;font-style:italic;margin-bottom:8px}
.nophoto-hero{margin:18px 0;border-radius:18px;padding:44px 20px;text-align:center;background:linear-gradient(135deg,#E8F3EC,#D2E7DA);color:var(--vert)}
.nophoto-hero .e{font-size:3.4rem}
.nophoto-hero p{font-size:.85rem;margin-top:8px}
.specs{background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 6px 24px rgba(15,61,46,.08);margin:14px 0}
.specs .row{display:flex;justify-content:space-between;gap:14px;padding:11px 16px;border-bottom:1px solid #F0EEE8;font-size:.86rem}
.specs .row:last-child{border-bottom:none}
.specs .k{color:#6b7a72}
.specs .v{font-weight:600;text-align:right;color:var(--vert2)}
.note{font-size:.8rem;color:#6b7a72;margin:12px 2px 90px}
.wa-btn{display:flex;align-items:center;justify-content:center;gap:10px;background:var(--wa);color:#fff;font-weight:700;border-radius:999px;padding:15px 22px;font-size:.95rem;box-shadow:0 8px 22px rgba(37,211,102,.4)}
.wa-fixed{position:fixed;left:16px;right:16px;bottom:14px;z-index:50;max-width:648px;margin:0 auto}
.wa-ico{width:22px;height:22px}
.crumb{font-size:.75rem;color:#6b7a72;padding:14px 0 0}
.crumb a{color:var(--accent);font-weight:600}
h1.pt{font-family:Georgia,serif;color:var(--vert);font-size:1.55rem;margin-top:6px}
.sub{color:#6b7a72;font-size:.9rem;margin-top:2px}
.desc{margin:12px 0 0;font-size:.92rem}
footer{background:var(--vert2);color:#fff;padding:26px 0 100px;margin-top:40px;font-size:.8rem}
footer .wrap{display:flex;flex-direction:column;gap:6px}
footer a{color:#BFDCCB}
.exclu{display:inline-block;background:var(--or);color:#fff;font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:4px 12px;border-radius:999px;margin-bottom:12px}
.contact-card{background:#fff;border-radius:18px;box-shadow:0 6px 24px rgba(15,61,46,.08);padding:22px;margin:20px 0;text-align:center}
.contact-card .big{font-size:1.1rem;font-weight:700;color:var(--vert)}
"""

WA_SVG = '<svg class="wa-ico" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.4 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6-.5.5c-.2.2-.3.4-.1.7.2.3.8 1.4 1.8 2.2 1.2 1.1 2.3 1.4 2.6 1.6.3.1.5.1.7-.1l1-1.2c.2-.3.4-.2.7-.1l2.1 1c.3.1.5.2.6.4 0 .1 0 .8-.3 1.4Z"/></svg>'

def wa_link(product=None):
    if product:
        msg = f"Bonjour, je suis intéressé par : {product} (vu sur saveursmaghrebines.com). Pouvez-vous m'envoyer le prix du jour ?"
    else:
        msg = "Bonjour, je vous contacte depuis saveursmaghrebines.com."
    return f"https://wa.me/{WA}?text={urllib.parse.quote(msg)}"

def page(title, desc, canonical, ogimg, body, waproduct=None):
    wa = wa_link(waproduct)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimg}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header class="top"><div class="wrap">
<a href="/"><div class="logo">Saveurs <span>Maghrébines</span></div>
<div class="tag">Sourcing F&L · Rungis</div></a>
</div></header>
{body}
<a class="wa-btn wa-fixed" href="{wa}" target="_blank" rel="noopener">{WA_SVG} Demander prix / échantillon</a>
<footer><div class="wrap">
<div><strong>Saveurs Maghrébines</strong> — Sourcing international Fruits & Légumes</div>
<div>Basé à Rungis · Origines vérifiées · Qualité contrôlée au départ</div>
<div>WhatsApp : +33 6 19 25 75 88 · <a href="mailto:contact@flash-jour.com">contact@flash-jour.com</a></div>
<div style="opacity:.6;margin-top:8px">© 2026 Saveurs Maghrébines — <a href="/contact/">Contact</a></div>
</div></footer>
</body></html>"""

# ---------- index ----------
cards = ""
for p in PRODUCTS:
    if p["photos"]:
        ph = f'<div class="ph" style="background-image:url(/{p["photos"][0][0]})">'
    else:
        emo = {"mangue-kent":"🥭","pitaya":"🐉","fruit-de-la-passion":"💜"}.get(p["slug"],"🍃")
        ph = f'<div class="ph nophoto">{emo}'
    badge = '<span class="badge">Disponible</span>' if p["dispo"]=="disponible" else '<span class="badge soon">Bientôt</span>'
    cards += f"""<a class="card" href="/{p['slug']}/">{ph}{badge}</div>
<div class="in"><h3>{p['nom']}</h3><div class="or">{p['flag']} Origine {p['origine']}</div></div></a>\n"""

index_body = f"""
<div class="hero"><div class="wrap">
<span class="exclu">Réservé aux professionnels</span>
<h1>Le catalogue direct producteur,<br>dans votre poche.</h1>
<p>Fruits & légumes d'import sourcés en direct des origines. Photos réelles, specs complètes, prix du jour sur WhatsApp.</p>
<div class="pills"><span class="pill">📍 Rungis</span><span class="pill">🌍 4 continents</span><span class="pill">✅ Qualité contrôlée</span></div>
</div></div>
<div class="wrap">
<h2 class="section-t">Nos produits</h2>
<div class="grid">
{cards}
</div>
<p class="note">Les prix se communiquent en direct — demandez le prix du jour sur WhatsApp, réponse rapide. Photos et vidéos supplémentaires sur demande.</p>
</div>"""

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT,"index.html"),"w",encoding="utf-8") as f:
    f.write(page("Saveurs Maghrébines — Catalogue import Fruits & Légumes | Rungis",
        "Catalogue B2B : patate douce, oignon rouge, mangue Kent, pitaya, fruit de la passion. Sourcing direct origine, base Rungis. Prix du jour sur WhatsApp.",
        f"{BASE}/", f"{BASE}/photos/patate-recolte.jpg", index_body))

# ---------- product pages ----------
for p in PRODUCTS:
    d = os.path.join(OUT, p["slug"]); os.makedirs(d, exist_ok=True)
    if p["photos"]:
        imgs = "".join(f'<img src="/{src}" alt="{alt}">' for src,alt in p["photos"])
        gal = f'<div class="gal">{imgs}</div><div class="cap">Photos réelles de nos lots — glissez pour voir la suite →</div>'
        og = f"{BASE}/{p['photos'][0][0]}"
    else:
        emo = {"mangue-kent":"🥭","pitaya":"🐉","fruit-de-la-passion":"💜"}.get(p["slug"],"🍃")
        gal = f'<div class="nophoto-hero"><div class="e">{emo}</div><p><strong>Photos & vidéos des lots en cours sur demande</strong><br>Envoyées directement sur WhatsApp.</p></div>'
        og = f"{BASE}/photos/patate-recolte.jpg"
    rows = "".join(f'<div class="row"><span class="k">{k}</span><span class="v">{v}</span></div>' for k,v in p["specs"])
    badge = '<span class="badge" style="position:static">Disponible</span>' if p["dispo"]=="disponible" else '<span class="badge soon" style="position:static">Bientôt disponible</span>'
    body = f"""
<div class="wrap">
<div class="crumb"><a href="/">Catalogue</a> / {p['nom']}</div>
<h1 class="pt">{p['nom']}</h1>
<div class="sub">{p['flag']} Origine {p['origine']} · {p['variete']} &nbsp;{badge}</div>
<p class="desc">{p['desc']}</p>
{gal}
<div class="specs">{rows}
<div class="row"><span class="k">Prix</span><span class="v" style="color:var(--or)">Prix du jour sur WhatsApp</span></div>
</div>
<p class="note">Échantillons possibles avant toute commande. Aucun prix public : chaque cotation est ajustée au jour, au volume et à l'incoterm.</p>
</div>"""
    title = f"{p['nom']} origine {p['origine']} — import grossiste Rungis | Saveurs Maghrébines"
    with open(os.path.join(d,"index.html"),"w",encoding="utf-8") as f:
        f.write(page(title, p["desc"], f"{BASE}/{p['slug']}/", og, body, p["nom"]))

# ---------- contact ----------
d = os.path.join(OUT,"contact"); os.makedirs(d, exist_ok=True)
body = f"""
<div class="wrap">
<div class="crumb"><a href="/">Catalogue</a> / Contact</div>
<h1 class="pt">Contact</h1>
<div class="contact-card">
<div class="big">Saveurs Maghrébines</div>
<p style="margin:6px 0 14px;color:#6b7a72">Sourcing international Fruits & Légumes — Basé à Rungis</p>
<p><strong>WhatsApp :</strong> +33 6 19 25 75 88</p>
<p><strong>Email :</strong> <a style="color:var(--accent)" href="mailto:contact@flash-jour.com">contact@flash-jour.com</a></p>
</div>
<p class="note">Réponse rapide en journée. Photos, vidéos et cotations envoyées directement sur WhatsApp.</p>
</div>"""
with open(os.path.join(d,"index.html"),"w",encoding="utf-8") as f:
    f.write(page("Contact — Saveurs Maghrébines | Rungis",
        "Contactez Saveurs Maghrébines : sourcing fruits et légumes import, base Rungis. WhatsApp +33 6 19 25 75 88.",
        f"{BASE}/contact/", f"{BASE}/photos/patate-recolte.jpg", body))

# ---------- robots + sitemap ----------
with open(os.path.join(OUT,"robots.txt"),"w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
urls = [f"{BASE}/"] + [f"{BASE}/{p['slug']}/" for p in PRODUCTS] + [f"{BASE}/contact/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls: sm += f"  <url><loc>{u}</loc></url>\n"
sm += "</urlset>\n"
with open(os.path.join(OUT,"sitemap.xml"),"w") as f: f.write(sm)

os.makedirs(os.path.join(OUT,"assets"),exist_ok=True)
with open(os.path.join(OUT,"assets","style.css"),"w",encoding="utf-8") as f: f.write(CSS)
print("OK - pages generated")
