// Service Worker pour PWA - Gestion des Dépenses
const CACHE_NAME = 'depenses-cache-v1';

// Liste des fichiers à mettre en cache (hors ligne)
const urlsToCache = [
  '/',
  '/static/manifest.json',
  // Ajoutez ici vos CSS/JS si vous en avez
  // Exemple : '/static/css/style.css'
];

// Installation du Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Cache ouvert');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activation du Service Worker (supprime les anciens caches)
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Interception des requêtes : stratégie cache-first
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Si la ressource est en cache, on la renvoie
        if (response) {
          return response;
        }
        // Sinon, on la récupère sur le réseau
        return fetch(event.request)
          .then(response => {
            // On met en cache la nouvelle ressource pour les prochaines fois
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            const responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });
            return response;
          });
      })
  );
});