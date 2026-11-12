# Sons des reels Assistant Rabe

Bibliothèque de morceaux libres de droits utilisés par l'agent « Rabe — publication des reels validés »
pour donner un son aux vidéos TikTok et Facebook (TikTok refuse d'ajouter une musique tout seul
quand on publie une vidéo par Metricool).

## Règles
- Uniquement des morceaux libres de droits, utilisables commercialement, sans attribution obligatoire
  (ex. Pixabay Music, bibliothèque audio YouTube « sans attribution »). Jamais un morceau commercial.
- Ambiance voulue par Cédric : house avec des bases afro-caribéennes (zouk, kompa, bouyon, soca),
  esprit DJ set de beach club. Pas d'ambiance molle (vagues, steel pan), pas de son synthétique « jouet ».
- Un fichier .mp3 par morceau, nom simple : `ambiance-titre.mp3` (ambiances : plage, soiree, info, sport, humour, chill).
- `catalogue.json` décrit chaque morceau : {"fichier", "titre", "artiste", "ambiance", "source", "licence"}.

## Utilisation par l'agent
Il choisit le morceau dont l'ambiance colle au reel (sans reprendre le même deux reels de suite),
l'intègre à la vidéo avec ffmpeg (coupé à la durée, fondu de sortie 0,8 s), pousse `reels/<id>-son.mp4`
et publie cette version sur TikTok et Facebook.
