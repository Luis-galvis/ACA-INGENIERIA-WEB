# VidaSana — Guía de configuración (Supabase + Vercel)

Este proyecto tiene 3 partes:
1. **Informe PDF** (lo que entregas a la asignatura).
2. **Prototipo web** (`prototipo/index.html`) — ya está conectado a Supabase.
3. **Base de datos** (Supabase) — hay que crear las tablas una sola vez.

---

## ⚠️ IMPORTANTE — Cambia tu clave secreta (seguridad)

En un mensaje anterior pegaste el **JWT secret / service_role key** de Supabase.
Esa clave es **secreta** y ya quedó expuesta. Haz esto antes de seguir:

1. Entra a https://supabase.com/dashboard → tu proyecto **bdzumkaoamvirybjkhog**.
2. Ve a **Project Settings → API**.
3. En **"JWT Settings"** haz clic en **"Regenerate"** (regenerar el JWT secret).
   - Si aparece, también regenera la **service_role key**.
4. ⚠️ **No vuelvas a pegar** el JWT secret ni la service_role key en chats ni en el código.
   - La clave que sí se usa en el navegador es la **anon/publishable key**
     (`sb_publishable_...`), esa sí es pública y es normal que esté en el HTML.

---

## Paso 1 — Crear las tablas en Supabase (una sola vez)

1. Entra a https://supabase.com/dashboard → abre tu proyecto.
2. En el menú izquierdo haz clic en **SQL Editor**.
3. Haz clic en **New query**.
4. Abre el archivo `supabase/schema.sql` de esta carpeta, **copia TODO el contenido** y pégalo.
5. Haz clic en **Run** (o `Ctrl+Enter`).
6. Verás el mensaje **"Success. No rows returned"**. ✅

Eso crea 4 tablas: `recommendations`, `profiles`, `favorites` y `habits`,
con sus políticas de seguridad (RLS) y los datos de ejemplo.

---

## Paso 2 — Activar el registro sin confirmar correo

Para que el registro entre **de inmediato** (ideal para la demo):

1. Menú izquierdo → **Authentication → Providers → Email**.
2. Desactiva (apaga) el interruptor **"Confirm email"**.
3. Guarda.

> Si lo dejas activado, al registrarse el usuario recibe un correo de verificación
> y debe hacer clic antes de entrar. Para la clase es más fácil desactivarlo.

---

## Paso 3 — Probar en local (opcional)

Puedes abrir `prototipo/index.html` con doble clic y ya carga la BD real.
Pero para evitar bloqueos del navegador, lo ideal es un servidor local:

```bash
cd prototipo
npx serve
```

O simplemente desplegarlo en Vercel (siguiente paso) y probar en línea.

---

## Paso 4 — Publicar en Vercel

### Opción A — Con GitHub (recomendada)

1. Sube la carpeta `prototipo` a un repositorio de GitHub (solo el `index.html`).
2. Entra a https://vercel.com → **Add New → Project**.
3. Importa tu repositorio → Vercel lo detecta como sitio estático.
4. Haz clic en **Deploy**. Te da una URL tipo `https://vidasana.vercel.app`.

### Opción B — Con la CLI de Vercel

1. Instala la CLI: `npm i -g vercel`
2. En la carpeta `prototipo` ejecuta:
   ```bash
   vercel login
   vercel
   ```
   Responde **Enter** a las preguntas (usa los valores por defecto).
3. Te dará una URL de producción. Para subirlo a producción definitiva:
   ```bash
   vercel --prod
   ```

---

## Paso 5 — Poner el enlace en el informe

Cuando Vercel te dé la URL, abre el informe en Word
(`informe/ACA_Ingenieria_Web_VidaSana.docx`), busca el texto
**`[ENLACE DEL PROTOTIPO EN VERCEL]`** y reemplázalo por tu URL real
(por ejemplo `https://vidasana.vercel.app`).

Luego exporta a PDF de nuevo (Archivo → Guardar como → PDF) o dime la URL
y te lo regenero yo.

---

## Qué hace cada archivo

| Archivo | Función |
|---|---|
| `prototipo/index.html` | Prototipo completo (registro real, favoritos, hábitos, perfil) conectado a Supabase |
| `supabase/schema.sql`  | SQL para crear las tablas, los datos y la seguridad en Supabase |
| `informe/*.docx` / `.pdf` | El informe que se entrega |
| `wireframes/` y `mockups/` | Las imágenes de los diseños (van dentro del informe) |

---

## Credenciales del proyecto (para que no las pierdas)

- **URL:** https://bdzumkaoamvirybjkhog.supabase.co
- **anon / publishable key (pública, va en el HTML):**
  `sb_publishable_O6VcBrX2MsMFtsj0yQysAw_JBHHBM8g`
- **service_role / JWT secret:** ⚠️ **regenerada, no la compartas.**
