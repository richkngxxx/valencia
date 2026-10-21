// Limpieza: la app se movió a /app/. Este SW reemplaza al antiguo de la raíz (v16), borra sus cachés y se desregistra.
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil((async()=>{
  for(const k of await caches.keys()){const m=/^valencia-v(\d+)$/.exec(k);if(m&&+m[1]<17)await caches.delete(k)}
  await self.registration.unregister();
  for(const c of await self.clients.matchAll({type:'window'}))c.navigate(c.url);
})()));
