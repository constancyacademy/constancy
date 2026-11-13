// cache hors ligne : le jeu reste dispo sans réseau ; la page est toujours prise sur le réseau d'abord (mises à jour immédiates)
const V = 'constancy-202611131523';
self.addEventListener('install', e => { self.skipWaiting(); e.waitUntil(caches.open(V).then(c => c.addAll(['./', './index.html', './manifest.webmanifest']))); });
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const page = e.request.mode === 'navigate' || /\/(index\.html)?$/.test(new URL(e.request.url).pathname);
  if (page) { e.respondWith(fetch(e.request).then(r => { const cp = r.clone(); caches.open(V).then(c => c.put(e.request, cp)); return r; }).catch(() => caches.match(e.request).then(h => h || caches.match('./index.html')))); return; }
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(r => { if (r.ok && (r.type === 'basic' || r.type === 'cors')) { const cp = r.clone(); caches.open(V).then(c => c.put(e.request, cp)); } return r; })));
});
