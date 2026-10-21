# Generates listing.md and checks Apple's character limits.
name = "Diu sí al valencià"
subs = ["Aprende valenciano jugando", "Valenciano de A1 a C2", "Lecciones de valenciano", "Habla valenciano cada día"]
promo = "Aprende valenciano con lecciones cortas, audio con voz valenciana y un murciélago que celebra tu racha. De A1 a C2, gratis y sin cuenta. ¡Bon dia!"
desc = """Diu sí al valencià es una app gratuita para aprender valenciano desde el castellano, con lecciones cortas y un camino de aprendizaje paso a paso.

DE A1 A C2
• 80 lecciones organizadas por niveles del Marco Común Europeo, desde los saludos de A1 hasta textos y registros de C2.
• Cada lección tiene 3 niveles. Gana hojas al completarlos y desbloquea la siguiente.
• Ejercicios variados: tarjetas de vocabulario, elegir la respuesta, escribir la traducción, ordenar palabras y unir parejas.

PRONUNCIACIÓN VALENCIANA
• Escucha cada palabra y frase con una voz de acento valenciano.
• Botón 🐢 para escucharla más despacio.
• Puedes activar o desactivar el sonido cuando quieras.

TU RACHA, CON UN MURCIÉLAGO
• Practica cada día para mantener la racha 🔥.
• Gana protectores de racha y celebra cada hito.
• Te acompaña un murciélago con una hoja en la cabeza que se alegra, piensa o duerme según cómo vayas.

AYUDA CUANDO LA NECESITAS
• Botón «?» en cada ejercicio: pista antes de responder y, después, explicación con significado, gramática, pronunciación y errores típicos. Consultar la ayuda no cuesta vidas.
• «¿Cómo se dice…?»: un diccionario de frases con más de 600 expresiones útiles, buscador en castellano y respuestas a dudas frecuentes de gramática («perquè» o «per què», «ser» o «estar», «ix» o «eix»…).

REFERENCIA NORMATIVA
El contenido sigue el valenciano normativo. Desde las explicaciones puedes abrir la palabra en el Diccionari Normatiu Valencià (DNV) de l'Acadèmia Valenciana de la Llengua (www.avl.gva.es). Esta app no está afiliada a la AVL.

SIN CUENTA Y SIN CONEXIÓN
• No hace falta registrarse.
• Tu progreso se guarda solo en tu dispositivo.
• Funciona sin conexión una vez abierta: las lecciones y el diccionario de frases están en el dispositivo y el audio se guarda al escucharlo.
• Sin anuncios y sin compras dentro de la app.

Voz: Matxa-TTS (Projecte Aina, BSC).

Diu sí al valencià!"""
kw = "valenciano,valencià,catalán,aprender,idiomas,curso,vocabulario,gramática,AVL,frases,lengua,A1,C2"
subs_main, subs_opts = subs[0], subs[1:]
for t, lim, v in [("Name", 30, name)] + [("Subtitle", 30, s) for s in subs] + [("Promo", 170, promo), ("Description", 4000, desc), ("Keywords", 100, kw)]:
    assert len(v) <= lim, (t, len(v), lim)
assert ", " not in kw
counts = {"name": len(name), "subs": [len(s) for s in subs], "promo": len(promo), "desc": len(desc), "kw": len(kw)}
md = f"""# App Store listing — Diu sí al valencià
Apple ID 6825331980 · bundle `com.diusialvalencia.app` · idioma principal: Español (España)
Character counts were checked by `build_listing.py` (Unicode characters).

## Nombre ({counts['name']}/30)
```
{name}
```

## Subtítulo ({counts['subs'][0]}/30)
```
{subs_main}
```
Alternativas:
""" + "".join(f"- `{s}` ({len(s)}/30)\n" for s in subs_opts) + f"""
## Texto promocional ({counts['promo']}/170)
```
{promo}
```

## Descripción ({counts['desc']}/4000)
```
{desc}
```

## Palabras clave ({counts['kw']}/100)
```
{kw}
```

## URLs
- Soporte: https://richkngxxx.github.io/valencia/
- Marketing: https://richkngxxx.github.io/valencia/
- Política de privacidad: https://richkngxxx.github.io/valencia/privacy.html
- Email de soporte/contacto: soporte@diusialvalencia.com (⚠️ el dominio aún no está comprado: el buzón no funcionará hasta configurar dominio y reenvío)

## Categoría
- Principal: Educación (Education)
- Secundaria: Referencia (Reference)

## Precio
Gratis (Free), todos los territorios. Sin compras dentro de la app.

## Copyright
```
2026 Ricardo Lopez
```

## Clasificación por edades (todas las respuestas: Ninguna / No) → 4+
- Violencia de dibujos animados o fantasía: Ninguna
- Violencia realista: Ninguna
- Violencia realista prolongada o gráfica: Ninguna
- Contenido sexual o desnudez: Ninguno
- Contenido sexual gráfico y desnudez: Ninguno
- Lenguaje soez o humor crudo: Ninguno
- Temas de terror o miedo: Ninguno
- Temas médicos o de tratamiento: Ninguno
- Referencias a alcohol, tabaco o drogas: Ninguna
- Simulación de apuestas: Ninguna
- Temas maduros o sugerentes: Ninguno
- Concursos: Ninguno
- Navegador web sin restricciones: No
- Apuestas: No
- Generación de contenido / chat con IA, mensajería o contenido de usuarios: No
- Anuncios: No · Controles parentales: no aplica · Verificación de edad: no aplica

## Notas para la revisión (App Review Information)
```
No se necesita cuenta ni inicio de sesión: la app abre directamente en el camino de lecciones.
Todo el progreso (racha, XP, hojas) se guarda localmente en el dispositivo; la app no recoge datos ni usa analíticas.
El audio de pronunciación está pregenerado con la voz Matxa-TTS (Projecte Aina, Barcelona Supercomputing Center), cuya licencia permite el uso no comercial; la app es gratuita, sin anuncios ni compras.
Los enlaces «Ver en el DNV (AVL)» abren el diccionario público de l'Acadèmia Valenciana de la Llengua en Safari; la app no está afiliada a la AVL.
Para probar: toca la primera lección, usa el botón «?» durante un ejercicio y el botón 💬 «¿Cómo se dice…?» en la pantalla principal.
```
Contacto de revisión: nombre, teléfono y email → **rellenar en App Store Connect** (no incluidos aquí).

## Privacidad de la app (App Privacy)
**Data Not Collected / Datos no recopilados.**
Verificado en `index.html` y `sw.js` (v15): las únicas peticiones de red son archivos estáticos del propio paquete
(`lessons.js`, `phrases.json`, `phrases_meta.json`, `help.json`, `qa.json`, `audio/manifest.json`, `audio/*.mp3`, fuentes e imágenes).
No hay analíticas, SDKs de terceros, cookies, publicidad ni cuentas. El progreso se guarda en `localStorage` del dispositivo.
El único enlace externo es al DNV (`https://www.avl.gva.es/lexicval/?paraula=…`), que se abre solo cuando el usuario lo toca y no envía datos de la app.
"""
open("listing.md", "w").write(md)
print(counts)
