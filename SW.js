const CACHE = 'sixthstump-v1';
const OFFLINE_ASSETS = [
  '/',
  '/index.html',
];

// Install — cache shell
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(OFFLINE_ASSETS))
  );
  self.skipWaiting();
});

// Activate — clean old caches
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch — cache first for shell, network first for API/fonts
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);

  // Always network for API calls
  if (url.pathname.startsWith('/api/')) return;

  // Cache first for same-origin
  if (url.origin === location.origin) {
    e.respondWith(
      caches.match(e.request).then(cached => {
        if (cached) return cached;
        return fetch(e.request).then(res => {
          const clone = res.clone();
          caches.open(CACHE).then(cache => cache.put(e.request, clone));
          return res;
        }).catch(() => caches.match('/index.html'));
      })
    );
    return;
  }

  // Network first for external (fonts, logos)
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});

// Push notification handler
self.addEventListener('push', e => {
  const data = e.data ? e.data.json() : {};
  e.waitUntil(
    self.registration.showNotification(data.title || 'SixthStump', {
      body: data.body || 'IPL match update!',
      icon: 'https://documents.iplt20.com/ipl/assets/images/ipl-logo-new-old.png',
      badge: 'https://documents.iplt20.com/ipl/assets/images/ipl-logo-new-old.png',
      data: { url: data.url || '/' }
    })
  );
});

// Click notification — open app
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(
    clients.matchAll({ type: 'window' }).then(clientList => {
      if (clientList.length) return clientList[0].focus();
      return clients.openWindow(e.notification.data.url || '/');
    })
  );
});
