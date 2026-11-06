# Coordination des sessions Claude — posts « utilisation de l'app » (6 novembre 2026)

Cédric (9 h 55 SBH) : « Vous êtes deux à faire ça, Metricool et toi, en même temps. Travaillez ensemble. »
Sessions : A = session_01DognAuFQ1jfAaoVpMw8U4Y (montage) · B = session_01DognAvj9e1J1YzRZpwEs1s (Metricool / publication).
Avant de toucher à ce dossier : `git pull`, lire ce fichier, écrire ici ce qu'on prend.

## Partage proposé (A)
- **A — enregistrement et montage** : `enregistrer.cjs`, demandes, contrôle des réponses, montage des reels/stories
  (vraies vidéos de Cédric + Mr. Bob/Capitaine Rab + vraie capture de l'app dans l'iPhone), rangement dans
  « Posts du jour Rabe » (statut « validé », règle du 3/11).
- **B — publication** : programmation Metricool (Instagram, Facebook, TikTok), son, heures, relevé des stats.
- Le workflow `.github/workflows/enregistrer-app.yml` : A le modifie ; B signale ici ce qu'il veut changer.

## Fait
- 0ca74a9 (A) enregistreur + workflow ; e1765f5 (B) chemins relatifs ; 903a49f (A) HD 1179 px, ralenti ×4, avis d'essai fermé ;
  e0a78d9 (B) heure de l'appareil notée.
- Sorties HD `sorties/2026-11-06-utilisation-hd/` : 5 questions, toutes « En ligne → En ligne ».

## Contrôle des réponses (A, 9 h 50)
- **ti-bus** : bonne réponse (trajet, lun-sam 6 h-20 h, toutes les 15 min, arrêts, QR de l'appli Collectivité) → reel v2 « Demande à Rab » en montage par A.
  Arrêt « Gare maritime » : confirmé par Cédric (06/11, 9 h 57) — la réponse de l'app est juste, la note du 30/10 était périmée.
- **ce-soir** (9 h 42) : commence par « Il est 9h42 le matin… » → à refaire le soir (≈ 18 h SBH), pas publiable tel quel.
- **pharmacie** : « Je n'ai pas d'adresse de pharmacie de garde » → pas publiable ; manque de données dans l'app.
- **plage-calme** : « je n'ai pas sa fiche » (Grand Cul-de-Sac) → pas publiable ; fiche à ajouter.
- **resto-dimanche** : pas d'horaires → pas publiable.

## En cours
- A : FAIT — v1475 en ligne (assistant-rabe f30ea19 + 6576bc3, workflow Mise en ligne vert) : 3 trous comblés + photos des lieux. Vérifié en vrai par l'enregistreur (sorties/2026-11-06-apres-v1475, 2026-11-06-photos-en-ligne) : pharmacies, plages calmes, restos ouverts dimanche midi, photos de Colombier chargées.
- Posts possibles maintenant (vraies réponses) : « Resto ouvert dimanche midi à Gustavia ? » (très bonne réponse), « La plage de Colombier, c'est comment ? » (avec photos).
- A (10 h 20) : PHOTOS dans les réponses (demande de Cédric, 10 h 13). Règle choisie par Cédric : lieux publics = photos libres créditées (Wikimedia Commons, workflow `photos-libres.yml`, dossier `photos/`) ; commerces = leurs propres photos AVEC leur accord, demandé par lot dans les mails aux commerçants. Ne pas aspirer de photos de commerces sur Internet.
- A : FAIT (10 h 10) — reel « Demande à Rab — Ti Bus » (10,7 s, vérifié image par image) rangé dans « Posts du jour Rabe », doc `2026-11-07_reel-ti-bus-il-va-ou`, statut « validé », samedi 7/11 15 h SBH (remplace la v1 sans l'app). → à B pour Metricool.
- A ensuite : refaire « On fait quoi ce soir ? » vers 18 h SBH (demande poussée vers 17 h 45) pour la story du soir.
- A : FAIT (11 h 50) — série « Capitaine Rab » (Rab vedette, 3 sketchs dessin animé validés par Cédric), rangés dans « Posts du jour Rabe », statut « validé » → à B pour Metricool :
  - `2026-11-07_reel-rab-montee-de-saline` — samedi 7/11, 19 h SBH (le Ti Bus reste à 15 h) ;
  - `2026-11-08_reel-rab-dimanche-13h` — dimanche 8/11, 11 h SBH (avant le déjeuner) ;
  - `2026-11-09_reel-rab-local-mauvaise-foi` — lundi 9/11, 18 h SBH.
  ⚠ Les trois vidéos affichent « Commente ATR » : la réponse automatique aux commentaires (Meta Business Suite, mots-clés ATR / atr / Atr) doit être active avant publication. Sur TikTok, pas d'automatisme : légende « lien en bio ». Si l'automatisme n'est pas actif à l'heure de publier, prévenir Cédric plutôt que publier.
- A : FAIT (16 h 40) — série Capitaine Rab CORRIGÉE (relecture image par image demandée par Cédric à 16 h 28) et VALIDÉE POUR PUBLICATION EN VRAI par Cédric (« Tu pourras le poster en vrai »). Les 3 docs de « Posts du jour Rabe » pointent vers les nouvelles vidéos (champ video_url, version 2) — B : utiliser ces versions-là, pas celles de 11 h 50. Heures inchangées (sam. 19 h, dim. 11 h, lun. 18 h SBH). La condition ATR (réponse automatique Meta Business Suite) reste valable.
- B : à compléter.
