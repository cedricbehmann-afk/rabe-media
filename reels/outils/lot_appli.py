# Lot « utilisation de l'app » du vendredi 6 nov. 2026 — demande de Cédric : montrer les AUTRES choses de l'app
# (pas les questions au chat, déjà montrées), avec Mr. Bob et Capitaine Rab. Moteur v3 + couche « vie » + carte de fin L2.
# Format poussé par les stats du 6/11 : question large à UNE réponse (pas de choix numérotés).
# Usage : python3 lot_appli.py video <clé>   (ou « stills »)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import vie
from vie import *
_av = sys.argv[:]
sys.argv = [sys.argv[0], 'stills', '__aucun__']
from lot_6nov import *
sys.argv = _av
from ile_ref import ILE

QUI = sys.argv[2] if len(sys.argv) > 2 else 'tout'
def go(n): return QUI in ('tout', n)
O4, O5 = O.replace('"7"', '"4"'), O.replace('"7"', '"5"')

# ---------------------------------------------------------------- nouvelles formes de Rab (yeux + houppe toujours)
def micro_rab():  # micro de l'app : la grille porte ses yeux, ondes de part et d'autre
    s = f'<path d="M-80,40 C-80,120 80,120 80,40" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>'
    s += f'<path d="M0,112 V160 M-50,160 H50" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>'
    s += f'<rect x="-56" y="-120" width="112" height="190" rx="56" fill="#f08566" {O}/>'
    s += ''.join(f'<path d="M-40,{y} H40" stroke="#d9674c" stroke-width="5" stroke-linecap="round"/>' for y in (30, 48))
    s += f'<g transform="translate(0,-48)">{yeux(0,0,rx=17,ry=21,gap=40)}</g>'
    for k in (1, -1):
        s += ''.join(f'<path d="M{k*(100+22*i)},{-50-14*i} Q{k*(124+30*i)},0 {k*(100+22*i)},{50+14*i}" fill="none" stroke="#5cc3bf" stroke-width="9" stroke-linecap="round"/>' for i in range(2))
    return s + houppe(0, -124, .85)

def hautparleur_rab():  # bulle sonore : Rab répond à voix haute
    s = f'<path d="M-120,-50 H-60 L10,-120 V120 L-60,50 H-120 Z" fill="#5cc3bf" {O}/>'
    s += ''.join(f'<path d="M{40+34*i},{-60-18*i} Q{80+46*i},0 {40+34*i},{60+18*i}" fill="none" stroke="#c4648c" stroke-width="10" stroke-linecap="round"/>' for i in range(3))
    s += f'<g transform="translate(-60,-2)">{yeux(0,0,rx=14,ry=17,gap=32)}</g>'
    return s + houppe(-20, -124, .8)

def oeil(cx, cy, rx=18, ry=22, look=(4, 2)):  # un seul œil du kit (blanc, iris turquoise, pupille, reflet)
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#ffffff" {O5}/>'
            f'<circle cx="{cx+look[0]}" cy="{cy+look[1]+3}" r="{rx*0.5}" fill="#2f9c97"/>'
            f'<circle cx="{cx+look[0]}" cy="{cy+look[1]+3}" r="{rx*0.26}" fill="{INK}"/>'
            f'<circle cx="{cx+look[0]+3}" cy="{cy+look[1]-1}" r="{rx*0.11}" fill="#ffffff"/>')

def bulle_txt(txt, size=54):  # (remplace celle du kit dans ce lot) : yeux plus haut, texte plus bas — ils ne se touchent plus
    s = f'<path d="M-170,-100 H170 C190,-100 200,-90 200,-70 V50 C200,70 190,80 170,80 H-20 L-70,130 L-60,80 H-170 C-190,80 -200,70 -200,50 V-70 C-200,-90 -190,-100 -170,-100 Z" fill="#ffffff" {O}/>'
    s += f'<text x="0" y="38" text-anchor="middle" font-family="JostX" font-size="{min(size, 56)}" fill="#c4648c">{txt}</text>'
    s += f'<g transform="translate(0,-46)">{yeux(0,0,rx=16,ry=19,gap=40)}</g>'
    return s + houppe(0, -104, .9)

def soleil_rab(c='#f6c84c'):  # (remplace celle du kit dans ce lot) : aucun rayon à midi, la houppe ne le traverse plus
    s = ''.join(f'<path d="M0,-150 L18,-112 L-18,-112 Z" fill="{c}" {O4} transform="rotate({a})"/>' for a in range(18, 360, 36))
    s += f'<circle r="100" fill="{c}" {O}/>' + yeux(0, -6, rx=22, ry=27, gap=46)
    return s + houppe(0, -100, .9)

def photo_rab():  # appareil photo : Rab a ses deux yeux sur le boîtier, l'objectif au centre
    s = f'<rect x="-60" y="-118" width="80" height="40" rx="10" fill="#3a3336" {O}/>'
    s += f'<rect x="-170" y="-90" width="340" height="210" rx="34" fill="#1e1a1c" {O}/>'
    s += f'<rect x="-170" y="-40" width="340" height="40" fill="#f08566"/><path d="M-170,-40 H170 M-170,0 H170" stroke="{INK}" stroke-width="5"/>'
    s += f'<circle cx="40" cy="22" r="76" fill="#ffffff" {O}/><circle cx="40" cy="22" r="54" fill="#2f9c97" {O5}/>'
    s += f'<circle cx="40" cy="22" r="25" fill="{INK}"/><circle cx="51" cy="11" r="9" fill="#ffffff"/>'
    s += f'<circle cx="138" cy="-62" r="12" fill="#f6c84c" {O4}/>'
    s += oeil(-128, 66, 17, 21) + oeil(-84, 66, 17, 21)
    s += ''.join(f'<path d="M{x},{y} l{dx},{dy}" stroke="#f6c84c" stroke-width="8" stroke-linecap="round"/>' for x, y, dx, dy in [(160, -110, 24, -24), (190, -76, 34, -6), (128, -128, 6, -34)])
    return s + houppe(-20, -122, .85)

def fleur_rab():  # fleur tropicale générique (5 pétales) : ce qu'on prend en photo
    s = ''.join(f'<ellipse cx="0" cy="-84" rx="54" ry="86" transform="rotate({a})" fill="#ffffff" {O}/>' for a in (0, 72, 144, 216, 288))
    s += ''.join(f'<ellipse cx="0" cy="-62" rx="22" ry="40" transform="rotate({a})" fill="#f6c84c"/>' for a in (0, 72, 144, 216, 288))
    s += f'<circle cx="0" cy="0" r="56" fill="#f6c84c" {O}/>'
    s += yeux(0, 0, rx=17, ry=21, gap=40)
    return s + houppe(0, -160, .8)

def carte_rab():  # la vraie silhouette de Saint-Barth ; toutes les épingles plantées SUR l'île ; Rab = l'épingle principale
    xs = [p[0] for p in ILE]; ys = [p[1] for p in ILE]
    w = 400; h = w * (max(ys) - min(ys)) / (max(xs) - min(xs))
    X = lambda x: (x - .5) * w; Y = lambda y: (y - (min(ys) + max(ys)) / 2) * h / (max(ys) - min(ys))
    d = 'M' + ' L'.join(f'{X(x):.1f},{Y(y):.1f}' for x, y in ILE) + ' Z'
    s = f'<rect x="-250" y="-220" width="500" height="440" rx="34" fill="#bfe6e2" {O}/>'
    s += f'<path d="{d}" fill="#f2e2c0" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    for (x, y, c) in [(0.25, 0.62, '#5cc3bf'), (0.62, 0.62, '#f6c84c'), (0.82, 0.70, '#5cc3bf')]:
        s += f'<g transform="translate({X(x):.0f},{Y(y):.0f})"><path d="M0,0 C-16,-22 -20,-36 -20,-46 A20,20 0 1 1 20,-46 C20,-36 16,-22 0,0 Z" fill="{c}" {O5}/><circle cx="0" cy="-46" r="7" fill="#ffffff"/></g>'
    s += f'<g transform="translate({X(0.45):.0f},{Y(0.60):.0f})"><path d="M0,0 C-40,-46 -54,-80 -54,-102 A54,54 0 1 1 54,-102 C54,-80 40,-46 0,0 Z" fill="#c4648c" {O}/>'
    s += f'<g transform="translate(0,-104)">{yeux(0,0,rx=14,ry=17,gap=32)}</g>{houppe(0,-158,.75)}</g>'
    return s

def planning_rab():  # la journée composée : 3 lignes d'horaires centrées sur la fiche, Rab sur l'en-tête
    s = f'<rect x="-190" y="-170" width="380" height="330" rx="30" fill="#ffffff" {O}/>'
    s += f'<path d="M-190,-90 V-140 a30,30 0 0 1 30,-30 H160 a30,30 0 0 1 30,30 V-90 Z" fill="#5cc3bf" {O}/>'
    s += f'<g transform="translate(0,-130)">{yeux(0,0,rx=15,ry=18,gap=36)}</g>'
    for i, (h, txt, c) in enumerate([('9 h', 'Plage', '#5cc3bf'), ('13 h', 'Déj', '#f6c84c'), ('17 h', 'Sunset', '#f08566')]):
        y = -28 + i * 72
        s += f'<circle cx="-130" cy="{y}" r="14" fill="{c}" {O4}/>'
        s += f'<text x="-104" y="{y+14}" font-family="JostX" font-size="40" fill="#1f2a2c">{h}</text>'
        s += f'<text x="20" y="{y+14}" font-family="Jost" font-size="40" fill="#1f2a2c">{txt}</text>'
    return s + houppe(0, -174, .85)

def dossier_rab():  # classeur de dossiers à onglets ; Rab (yeux + houppe) centré sur la chemise de devant
    s = ''
    for i, (lab, c) in enumerate([('École', '#f6c84c'), ('Plombier', '#5cc3bf'), ('Carte grise', '#f08566')]):
        y = -120 + i * 44; x0 = -170 + i * 22
        s += f'<path d="M{x0},{y} H{x0+110} L{x0+130},{y-40} H{x0+318} L{x0+334},{y} H{x0+340} V{y+250} H{x0} Z" fill="{c}" {O}/>'
        s += f'<text x="{x0+226}" y="{y-9}" text-anchor="middle" font-family="JostB" font-size="28" fill="#1f2a2c">{lab}</text>'
    cx = -126 + 170   # centre de la chemise de devant (x0 = -126, largeur 340)
    s += f'<g transform="translate({cx},96)">{yeux(0,0,rx=24,ry=30,gap=58)}</g>'
    return s + houppe(cx, 36, .95)

def maison_rab():  # case créole (toit rouge) : un œil de Rab à chaque fenêtre, clé à côté
    s = f'<rect x="-150" y="-40" width="300" height="190" fill="#ffffff" {O}/>'
    s += f'<path d="M-188,-28 L0,-170 L188,-28 Z" fill="#d9573f" {O}/>'
    s += f'<rect x="-32" y="48" width="64" height="102" fill="#5cc3bf" {O5}/><circle cx="18" cy="104" r="6" fill="{INK}"/>'
    s += f'<rect x="-128" y="-4" width="76" height="74" fill="#bfe6e2" {O5}/><rect x="52" y="-4" width="76" height="74" fill="#bfe6e2" {O5}/>'
    s += oeil(-90, 33, 22, 27) + oeil(90, 33, 22, 27)
    s += f'<g transform="translate(212,96) rotate(-30)"><circle cx="0" cy="0" r="26" fill="#f6c84c" {O5}/><circle cx="0" cy="0" r="9" fill="#ffffff"/><path d="M24,0 H86 M66,0 V22 M80,0 V16" stroke="{INK}" stroke-width="10" stroke-linecap="round"/></g>'
    return s + houppe(0, -172, .9)

def ecran_rab():  # écran d'accueil d'un téléphone (générique) : l'icône Rab prend sa place dans la grille, bouton « + » en bas
    s = f'<rect x="-130" y="-200" width="260" height="400" rx="40" fill="#1e1a1c" {O}/>'
    s += '<rect x="-112" y="-178" width="224" height="356" rx="24" fill="#bfe6e2"/>'
    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1): continue
            s += f'<rect x="{-96+j*68}" y="{-156+i*72}" width="56" height="56" rx="14" fill="{["#f6c84c","#ffffff","#f28fb8"][(i+j)%3]}" {O4}/>'
    s += f'<g transform="translate(0,-56)"><rect x="-38" y="-38" width="76" height="76" rx="19" fill="#c4648c" {O5}/>{yeux(0,4,rx=12,ry=15,gap=28)}</g>'
    s += f'<g transform="translate(0,112)"><circle cx="0" cy="0" r="40" fill="#5cc3bf" {O}/><path d="M0,-20 V20 M-20,0 H20" stroke="#ffffff" stroke-width="10" stroke-linecap="round"/></g>'
    return s + houppe(0, -204, .8)

def reseau_rab():  # barres de réseau barrées… et Rab (le rond « ✓ ») répond quand même
    s = ''.join(f'<rect x="{-190+i*56}" y="{40-i*46}" width="38" height="{60+i*46}" rx="8" fill="#3a4a72" {O}/>' for i in range(4))
    s += f'<path d="M-200,-98 L24,106" stroke="#d9573f" stroke-width="16" stroke-linecap="round"/>'
    s += f'<g transform="translate(134,-6)"><circle cx="0" cy="0" r="78" fill="#5cc3bf" {O}/>'
    s += f'<path d="M-30,34 L-10,52 L28,14" fill="none" stroke="#ffffff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
    s += f'<g transform="translate(0,-18)">{yeux(0,0,rx=16,ry=19,gap=38)}</g></g>'
    return s + houppe(134, -82, .8)

# Règle « le pouf ne touche jamais un visage » : le pouf du téléphone de Bob (pfT) est décalé vers sa main et réduit.
import gabarit as _GB
_rendre_av = _GB.rendre
def _rendre_appli(nom, svg, js, duree, stills=(0.0,)):
    svg = svg.replace('<g transform="translate(655,1165)"><g id="pfT"', '<g transform="translate(683,1175)"><g id="pfT"')
    js = js.replace("pouf('pfT',t,t0-0.04,0.5)", "pouf('pfT',t,t0-0.04,0.28)").replace("pouf('pfT',t,duree-0.58,0.5)", "pouf('pfT',t,duree-0.58,0.28)")
    # le 1er objet (lancé depuis la main de Bob) grandit pendant son vol : il ne passe jamais par-dessus la tête de Bob
    js = js.replace("const F=fit(k), kk=F.s*spr('ok'+k,1,dt,3.5,0.55);", "const F=fit(k), kk=F.s*spr('ok'+k,1,dt,3.5,0.55)*(k===0?(0.3+0.7*Math.pow(eo(cl((t-a)/0.38)),2)):1);")
    return _rendre_av(nom, svg, js, duree, stills)
_GB.rendre = _rendre_appli

FIN = lambda fr1, en: (fr1, '→ abonne-toi', en)
_R = R
def R(*a, **k):
    k.setdefault('hmax', 300); k.setdefault('wmax', 560)
    _R(*a, **k)

# ================================================================= 8 REELS « UTILISATION »
if go('a_voix'):        # parler à l'app (micro) + réponse à voix haute
    R('reel-app-1-parle-lui', FIN('Ta 1re question ?', 'Your first question? · follow'), plage(),
      [(0, 'tA', 'Pas envie de taper ?', 'Parle-lui !', 'Too lazy to type? Just talk to it'),
       (2.1, 'tB', 'Un appui', 'sur le micro…', 'Tap the mic and ask out loud'),
       (4.0, 'tC', '… et Rab répond', 'à voix haute', 'Rab answers out loud'),
       (5.8, 'tD', 'Ta 1re question,', 'en un mot ?', 'Your first question, in one word?')],
      None,
      [('tom', 'T', 200), ('lea', 'L', 868)],
      [(0.65, 2.0, bulle_txt('Allô ?', 60), 1.0), (2.15, 3.9, micro_rab(), 0.95), (4.05, 5.7, hautparleur_rab(), 0.95), (5.85, 7.45, bulle_txt('1 mot ?', 56), 1.0)],
      tenues={'tom': TENUES['plage']['tom'] if 'tom' in TENUES['plage'] else TENUES['saison']['tom'], 'lea': TENUES['plage']['lea'], 'B': TENUES['plage']['B']})

if go('a_photo'):       # « c'est quoi ça ? » en photo
    R('reel-app-2-c-est-quoi-ca', FIN('Ta photo mystère ?', 'Your mystery photo? · follow'), plage(),
      [(0, 'tA', 'C’est quoi,', 'cette fleur ?', 'What is this flower? Snap it'),
       (2.1, 'tB', 'Une photo…', '… et Rab te dit', 'One photo, Rab tells you what it is'),
       (4.0, 'tC', 'Plante, poisson,', 'lézard, coquillage', 'Plant, fish, lizard or shell'),
       (5.8, 'tD', 'Envoie-le à', 'ton pote curieux', 'Send it to your curious friend')],
      None,
      [('jess', 'J', 200), ('malik', 'M', 868)],
      [(0.65, 2.0, fleur_rab(), 0.9), (2.15, 3.9, photo_rab(), 0.95), (4.05, 5.7, poisson_rab(), 0.9), (5.85, 7.45, avion_papier(), 0.8)],
      tenues={'jess': TENUES['touriste']['jess'], 'malik': TENUES['plage']['malik'], 'B': TENUES['plage']['B']})

if go('a_carte'):       # la carte de l'île
    R('reel-app-3-la-carte', FIN('Ton coin préféré ?', 'Your favourite spot? · follow'), port_gustavia(),
      [(0, 'tA', 'C’est où,', 'ce commerce ?', 'Where is that shop? Check the map'),
       (2.1, 'tB', 'Toute l’île', 'sur une carte', 'The whole island on one map'),
       (4.0, 'tC', 'Commerces,', 'services, plages', 'Shops, services, beaches'),
       (5.8, 'tD', 'Envoie-le à celui', 'qui se perd', 'Send it to the one who always gets lost')],
      None,
      [('lea', 'L', 200), ('malik', 'M', 868)],
      [(0.65, 2.0, bulle_txt('C’est où ?', 52), 1.0), (2.15, 5.7, carte_rab(), 0.95), (5.85, 7.45, avion_papier(), 0.8)],
      tenues={'lea': TENUES['sortie']['lea'], 'malik': TENUES['plage']['malik'], 'B': TENUES['sortie']['B']})

if go('a_journee'):     # « organise-moi ma journée »
    R('reel-app-4-ma-journee', FIN('Ta journée parfaite ?', 'Your perfect day? · follow'), plage(),
      [(0, 'tA', 'Ta journée,', 'en 1 question', 'Your whole day in one question'),
       (2.1, 'tB', '« Organise-moi', 'ma journée »', '“Plan my day”'),
       (4.0, 'tC', 'Plage, déj,', 'sunset… à côté', 'Beach, lunch, sunset, all close by'),
       (5.8, 'tD', 'Ta journée', 'parfaite ? 1 mot', 'Your perfect day? One word')],
      None,
      [('jess', 'J', 200), ('tom', 'T', 868)],
      [(0.65, 2.0, bulle_txt('Et aujourd’hui ?', 38), 1.0), (2.15, 3.9, planning_rab(), 0.9), (4.05, 5.7, soleil_rab('#f08a24'), 1.0), (5.85, 7.45, bulle_txt('1 mot ?', 56), 1.0)],
      tenues={'jess': TENUES['touriste']['jess'], 'tom': TENUES['saison']['tom'], 'B': TENUES['plage']['B']})

if go('a_dossiers'):    # Mes dossiers (résidents)
    R('reel-app-5-mes-dossiers', FIN('Ta pire démarche ?', 'Your worst errand? · follow'), port_gustavia(),
      [(0, 'tA', 'Tes démarches,', 'bien rangées', 'Your errands, neatly filed'),
       (2.1, 'tB', 'Carte grise,', 'plombier, école…', 'Car papers, plumber, school…'),
       (4.0, 'tC', 'Tu reprends où', 'tu en étais', 'Pick up right where you left off'),
       (5.8, 'tD', 'Tague ton coloc', 'désorganisé', 'Tag your messiest roommate')],
      None,
      [('malik', 'M', 205), ('lea', 'L', 868)],
      [(0.65, 2.0, bulle_txt('J’en étais où ?', 40), 1.0), (2.15, 3.9, dossier_rab(), 0.85), (4.05, 5.7, bulle_txt('Reprendre', 50), 1.0), (5.85, 7.45, avion_papier(), 0.8)],
      tenues={'malik': TENUES['sortie']['malik'], 'lea': TENUES['sortie']['lea'], 'B': TENUES['sortie']['B']})

if go('a_annonces'):    # Aide à la vie de Saint-Barth : emploi · logement · vente
    R('reel-app-6-aide-a-la-vie', FIN('Tu cherches quoi ?', 'Job, room or sale? · follow'), port_gustavia(),
      [(0, 'tA', 'Job, logement,', 'à vendre ?', 'Job, room or for sale in St Barth?'),
       (2.1, 'tB', 'Les annonces', 'de l’île', 'All the island’s ads in one place'),
       (4.0, 'tC', 'Gratuit,', 'sans compte', 'Free, no account needed'),
       (5.8, 'tD', 'Tague celui qui', 'cherche un toit', 'Tag the friend looking for a room')],
      None,
      [('tom', 'T', 200), ('jess', 'J', 868)],
      [(0.65, 2.0, bulle_txt('Je cherche…', 44), 1.0), (2.15, 3.9, maison_rab(), 0.9), (4.05, 5.7, bulle_txt('Gratuit !', 52), 1.0), (5.85, 7.45, avion_papier(), 0.8)],
      tenues={'tom': TENUES['saison']['tom'], 'jess': TENUES['sortie']['jess'] if 'jess' in TENUES['sortie'] else TENUES['touriste']['jess'], 'B': TENUES['sortie']['B']})

if go('a_langues'):     # 4 langues
    R('reel-app-7-quatre-langues', FIN('Tu parles quoi ?', 'Which language? · follow'), plage(),
      [(0, 'tA', 'Tu parles quoi ?', '1 seul mot', 'Which language do you speak? One word'),
       (2.1, 'tB', 'Rab répond en', 'français, English…', 'Rab answers in French, English…'),
       (4.0, 'tC', '… español', 'et português', '… Spanish and Portuguese'),
       (5.8, 'tD', 'Envoie-le à ton', 'pote étranger', 'Send it to your friend from abroad')],
      None,
      [('jess', 'J', 200), ('malik', 'M', 868)],
      [(0.65, 2.0, bulle_txt('Bonjour !', 54), 1.0), (2.15, 3.9, bulle_txt('Hello!', 60), 1.0), (4.05, 4.85, bulle_txt('¡Hola!', 60), 1.0), (4.9, 5.7, bulle_txt('Olá!', 60), 1.0), (5.85, 7.45, avion_papier(), 0.8)],
      tenues={'jess': TENUES['touriste']['jess'], 'malik': TENUES['plage']['malik'], 'B': TENUES['plage']['B']})

if go('a_installer'):   # sur l'écran d'accueil, sans App Store
    R('reel-app-8-ecran-d-accueil', FIN('Tu l’as installée ?', 'Installed it? · follow'), plage(),
      [(0, 'tA', 'Une app sans', 'App Store ?', 'An app without the App Store?'),
       (2.1, 'tB', 'Partager → « Sur', 'l’écran d’accueil »', 'Share → “Add to Home Screen”'),
       (4.0, 'tC', 'Et elle répond', 'même sans réseau', 'And it answers even with no signal'),
       (5.8, 'tD', 'Envoie-le à ton', 'pote sans 4G', 'Send it to your friend with no signal')],
      None,
      [('lea', 'L', 200), ('tom', 'T', 868)],
      [(0.65, 2.0, bulle_txt('App Store ?', 48), 1.0), (2.15, 3.9, ecran_rab(), 0.85), (4.05, 5.7, reseau_rab(), 0.9), (5.85, 7.45, avion_papier(), 0.8)],
      tenues={'lea': TENUES['plage']['lea'], 'tom': TENUES['saison']['tom'], 'B': TENUES['plage']['B']})
