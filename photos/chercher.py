# Cherche des photos LIBRES (Wikimedia Commons) pour des fiches de lieux publics d'Assistant Rabe.
# Règle (Cédric, 06/11/2026) : lieux publics = photos libres et créditées ; commerces = leurs photos, avec accord.
# Une photo n'est retenue que si le nom du lieu figure dans son titre, sa description ou ses catégories
# (une photo voisine d'un autre lieu induirait en erreur). Licences acceptées : CC0, domaine public, CC BY, CC BY-SA.
# usage : python3 chercher.py demandes/x.json sorties/x/
import json, sys, os, re, time, unicodedata, urllib.request, urllib.parse
dem, out = sys.argv[1], sys.argv[2]; os.makedirs(out + '/apercus', exist_ok=True)
API = 'https://commons.wikimedia.org/w/api.php'
UA = {'User-Agent': 'AssistantRabe-photos/1.0 (https://assistant-rabe.com)'}
def get(params):
    for essai in range(3):
        try:
            u = API + '?' + urllib.parse.urlencode(params)
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
        except Exception as e:
            time.sleep(2 + 3 * essai)
    return {}
def norm(t): return re.sub(r'[^a-z0-9 ]', ' ', unicodedata.normalize('NFD', str(t)).encode('ascii', 'ignore').decode().lower())
VIDE = {'de','du','des','la','le','les','l','d','anse','plage','saint','st','barthelemy','barth','barths','sbh','et','a','au','aux','beach','pointe','morne','grand','grande','petit','petite'}
def mots(nom): return [m for m in norm(nom).split() if len(m) > 2 and m not in VIDE]
def nettoie(h): return re.sub(r'<[^>]+>', '', h or '').strip()
RAYON = {'Plages': 600, 'Géographie': 800, 'Sites & patrimoine': 250, 'Environnement': 600}
res = {}
for f in json.load(open(dem)):
    lat, lon = f['gps']
    q = get({'action': 'query', 'format': 'json', 'generator': 'geosearch', 'ggscoord': f'{lat}|{lon}',
             'ggsradius': RAYON.get(f['c'], 500), 'ggsnamespace': 6, 'ggslimit': 40,
             'prop': 'imageinfo|categories', 'iiprop': 'url|extmetadata|size|mime', 'iiurlwidth': 900, 'cllimit': 50})
    pages = (q.get('query') or {}).get('pages') or {}
    cles = mots(f['n']); retenus = []
    for p in pages.values():
        ii = (p.get('imageinfo') or [{}])[0]; md = ii.get('extmetadata') or {}
        if ii.get('mime') not in ('image/jpeg', 'image/png') or ii.get('width', 0) < 800: continue
        lic = (md.get('LicenseShortName') or {}).get('value', '')
        if not re.search(r'CC0|Public domain|CC BY(-SA)? ?\d|CC-BY|PD', lic, re.I): continue
        cats = ' '.join(c['title'] for c in p.get('categories') or [])
        texte = norm(p['title'] + ' ' + nettoie((md.get('ImageDescription') or {}).get('value')) + ' ' + cats)
        if not cles or not all(m in texte.split() for m in cles): continue
        if re.search(r'\b(map|carte|logo|plan|blason|coat of arms|flag|drapeau|diagram)\b', texte): continue
        auteur = nettoie((md.get('Artist') or {}).get('value'))[:80] or 'auteur inconnu'
        retenus.append({'url': ii.get('thumburl'), 'page': ii.get('descriptionurl'), 'titre': p['title'],
                        'auteur': auteur, 'licence': lic, 'licence_url': (md.get('LicenseUrl') or {}).get('value', ''),
                        'largeur': ii.get('width'), 'dist': p.get('index', 0)})
    retenus = retenus[:3]
    for k, r in enumerate(retenus):
        try:
            dat = urllib.request.urlopen(urllib.request.Request(r['url'], headers=UA), timeout=30).read()
            open(f"{out}/apercus/{f['i']}__{k}.jpg", 'wb').write(dat)
        except Exception as e:
            r['apercu_erreur'] = str(e)[:80]
    if retenus: res[f['i']] = {'n': f['n'], 'c': f['c'], 'photos': retenus}
    print(f"{f['n'][:40]:40} {len(pages):3} images proches · {len(retenus)} retenue(s)")
    time.sleep(0.3)
json.dump(res, open(out + '/photos.json', 'w'), ensure_ascii=False, indent=1)
print('fiches avec photo :', len(res))
