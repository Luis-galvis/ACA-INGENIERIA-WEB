# VidaSana 🌿

Página web de **recomendaciones saludables** desarrollada para la Actividad de Construcción Aplicada (ACA) de la asignatura **Ingeniería Web** — CUN Digital.

## Descripción

VidaSana es una plataforma que sugiere contenidos de alimentación, actividad física, descanso y bienestar. Incluye:

- Registro e inicio de sesión de usuarios.
- Perfil de salud (edad, estatura, peso, IMC, objetivo y preferencias).
- Búsqueda y filtrado de recomendaciones por categoría.
- Personalización de recomendaciones.
- Favoritos y seguimiento de hábitos.

## Estructura del proyecto

```
ACA_ingenieria_web/
├── index.html          → Prototipo navegable (desplegado en Vercel)
├── informe/            → Informe final (PDF y DOCX)
├── wireframes/         → Diseños de baja fidelidad
├── mockups/            → Diseños de alta fidelidad
└── supabase/
    └── schema.sql      → Esquema de la base de datos (PostgreSQL)
```

## Tecnologías

- HTML, CSS y JavaScript.
- Supabase (autenticación y base de datos PostgreSQL).
- Vercel (despliegue).

## Cómo verlo

- **En línea:** abre la URL de Vercel del proyecto.
- **En local:** abre `index.html` en el navegador.

## Base de datos

El archivo `supabase/schema.sql` contiene el esquema completo (tablas `recommendations`, `profiles`, `favorites` y `habits`) con sus políticas de seguridad (Row Level Security).
