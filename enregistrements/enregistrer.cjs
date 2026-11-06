// Enregistre l'app Assistant Rabe EN VRAI (assistant-rabe.com) sur un iPhone émulé :
// entrée (essai gratuit), question tapée comme une vraie personne, vraie réponse du serveur.
// Usage : node enregistrer.cjs <demande.json> <dossier_sortie> [url]
// demande.json : [{ "id": "ti-bus", "question": "…", "theme": "light"|"dark" }, …]
const { chromium, devices } = require('playwright');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const [, , demFile, outDir, url = 'https://assistant-rabe.com/'] = process.argv;
const demandes = JSON.parse(fs.readFileSync(demFile, 'utf8'));
const pause = (ms) => new Promise((r) => setTimeout(r, ms));

async function une(b, d) {
  const dir = path.join(outDir, d.id); fs.mkdirSync(path.join(dir, 'frames'), { recursive: true });
  const ctx = await b.newContext({ ...devices['iPhone 14 Pro'], viewport: { width: 393, height: 852 }, locale: 'fr-FR', timezoneId: 'America/St_Barthelemy', colorScheme: d.theme || 'light' });
  const p = await ctx.newPage();
  await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  await pause(1500);
  await p.getByRole('button', { name: 'Français' }).first().click().catch(() => {});
  await pause(400);
  await p.click('#qr-enter').catch(() => {});
  await pause(2500);
  const passer = await p.$('#logement-q-passe'); if (passer && await passer.isVisible()) { await passer.click(); await pause(600); }
  // avis d'essai : « J'ai compris » ; raccourcis repliés pour garder l'en-tête « En ligne » à l'écran
  const compris = p.getByRole('button', { name: /compris/i }).first(); if (await compris.isVisible().catch(() => false)) { await compris.click(); await pause(600); }
  const bascule = await p.$('#quick-bascule'); if (bascule && await bascule.isVisible()) { await bascule.click(); await pause(700); }
  await p.evaluate(() => window.scrollTo(0, 0)); await pause(300);
  // l'en-tête doit dire « En ligne » (jamais « Mode local »)
  let statut = '';
  for (let i = 0; i < 20; i++) { statut = (await p.textContent('#chat-status').catch(() => '')) || ''; if (/en ligne/i.test(statut)) break; await pause(500); }
  const zone = () => p.evaluate(() => { const w = document.querySelector('#chat-welcome'); const c = w ? w.parentElement : document.body; return c.innerText; });
  const avant = await zone();
  // capture pleine définition (1179 px) image par image ; animations CSS ralenties ×LENT, saisie ralentie ×LENT,
  // le montage réaccélère ×LENT (infos.json : "ralenti") — rendu fluide malgré la capture lente
  const LENT = 4;
  const cdp = await ctx.newCDPSession(p); const frames = []; let filme = true;
  await cdp.send('Animation.enable'); await cdp.send('Animation.setPlaybackRate', { playbackRate: 1 / LENT });
  const boucle = (async () => { while (filme) { const t = Date.now() / 1000; try { const r = await cdp.send('Page.captureScreenshot', { format: 'jpeg', quality: 90, clip: { x: 0, y: 0, width: 393, height: 852, scale: 3 } }); frames.push({ t, data: r.data }); } catch (e) { await pause(50); } } })();
  await pause(800 * LENT);
  await p.click('#chat-field');
  await p.type('#chat-field', d.question, { delay: 55 * LENT });
  await pause(500 * LENT);
  await p.click('#chat-send');
  const t0 = Date.now(); let last = '', stable = 0;
  while (Date.now() - t0 < 40000) {
    await pause(500);
    const z = await zone();
    if (z !== avant && z.length > avant.length + d.question.length + 20 && z === last) { stable += 500; if (stable >= 3000) break; } else stable = 0;
    last = z;
  }
  await pause(2500 * LENT);
  filme = false; await boucle;
  await p.screenshot({ path: path.join(dir, 'final.png') });
  const horlogeAppareil = await p.evaluate(() => { let e = null; try { e = window.RabeDirect && window.RabeDirect.etat(); } catch (x) {} return { fuseau: Intl.DateTimeFormat().resolvedOptions().timeZone, date: new Date().toString(), ile: e && { horloge: e.horloge, jour: e.jour }, vous: e && e.vous && { horloge: e.vous.horloge, jour: e.vous.jour } }; }).catch(() => null);
  const statutFin = (await p.textContent('#chat-status').catch(() => '')) || '';
  fs.writeFileSync(path.join(dir, 'reponse.txt'), (await zone()).slice(avant.length - 0));
  fs.writeFileSync(path.join(dir, 'infos.json'), JSON.stringify({ ...d, statut_avant: statut.trim(), statut_apres: statutFin.trim(), horloge_appareil: horlogeAppareil, images: frames.length, ralenti: LENT, quand: new Date().toISOString() }, null, 2));
  // assemblage : chaque image dure jusqu'à la suivante, sortie 30 i/s
  let list = '';
  frames.forEach((f, i) => { const fn = path.join(dir, 'frames', String(i).padStart(5, '0') + '.jpg'); fs.writeFileSync(fn, Buffer.from(f.data, 'base64'));
    const dur = (i < frames.length - 1 ? Math.max(0.001, frames[i + 1].t - f.t) : 0.5 * LENT); list += `file '${path.resolve(fn)}'\nduration ${dur.toFixed(4)}\n`; });
  if (frames.length) { list += `file '${path.resolve(path.join(dir, 'frames', String(frames.length - 1).padStart(5, '0') + '.jpg'))}'\n`;
    fs.writeFileSync(path.join(dir, 'liste.txt'), list);
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', path.join(dir, 'liste.txt'), '-vf', 'fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', path.join(dir, 'ecran.mp4')]); }
  fs.rmSync(path.join(dir, 'frames'), { recursive: true, force: true }); try { fs.rmSync(path.join(dir, 'liste.txt')); } catch (e) {}
  console.log(d.id, '·', statut.trim(), '→', statutFin.trim(), '·', frames.length, 'images');
  await ctx.close();
}
(async () => { fs.mkdirSync(outDir, { recursive: true }); const b = await chromium.launch();
  for (const d of demandes) { try { await une(b, d); } catch (e) { console.log('ÉCHEC', d.id, e.message); } }
  await b.close(); })();
