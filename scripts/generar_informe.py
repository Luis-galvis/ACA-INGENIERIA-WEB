# -*- coding: utf-8 -*-
"""Genera el informe DOCX de la ACA de Ingeniería Web."""
import os
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIRE = os.path.join(BASE, "wireframes")
MOCK = os.path.join(BASE, "mockups")
OUT = os.path.join(BASE, "informe", "ACA_Ingenieria_Web_VidaSana.docx")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

GREEN = RGBColor(0x16, 0x52, 0x20)
GREEN2 = RGBColor(0x2E, 0x7D, 0x32)
GRAY = RGBColor(0x44, 0x44, 0x44)

doc = Document()

# --- formato global ---
sec = doc.sections[0]
sec.top_margin = Cm(2.54)
sec.bottom_margin = Cm(2.54)
sec.left_margin = Cm(2.54)
sec.right_margin = Cm(2.54)

normal = doc.styles["Normal"]
normal.font.name = "Arial"
normal.font.size = Pt(12)
normal.font.color.rgb = GRAY
pf = normal.paragraph_format
pf.line_spacing = 1.5
pf.space_after = Pt(6)

for name, size in [("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 12)]:
    st = doc.styles[name]
    st.font.name = "Arial"
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = GREEN
    st.paragraph_format.space_before = Pt(12)
    st.paragraph_format.space_after = Pt(6)


def title_style():
    st = doc.styles["Title"]
    st.font.name = "Arial"
    st.font.size = Pt(24)
    st.font.bold = True
    st.font.color.rgb = GREEN


def body(text, bold=False, align=None, color=None, size=12, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    r.bold = bold
    if color:
        r.font.color.rgb = color
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(12)
    return p


def heading(text, level=1):
    p = doc.add_heading(level=level)
    r = p.add_run(text)
    r.font.name = "Arial"
    r.bold = True
    r.font.color.rgb = GREEN
    return p


def figure(path, caption, width=6.0):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run()
    run.add_picture(path, width=Inches(width))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(14)
    r = cap.add_run(caption)
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.bold = True
    r.italic = True
    r.font.color.rgb = GREEN2


def page_break():
    doc.add_page_break()


# ================================================================== PORTADA
title_style()
for _ in range(2):
    body("", space_after=0)
body("CORPORACIÓN UNIFICADA NACIONAL DE EDUCACIÓN SUPERIOR – CUN",
     bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=16, color=GREEN, space_after=4)
body("CUN Digital", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=2)
body("Programa académico: Ingeniería de Sistemas", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=2)
body("Asignatura: Ingeniería Web", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=18)

body("ACTIVIDAD DE CONSTRUCCIÓN APLICADA (ACA)",
     bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=18, color=GREEN, space_after=10)

body("Diseño de Wireframe, Mockup y Prototipo para una Página de Recomendaciones Saludables",
     bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=16, space_after=4)
body("“VidaSana”", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, color=GREEN2, space_after=30)

body("Estudiantes:", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=2)
body("Luis Fernando Galvis Moreno — Ficha 54487", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=2)
body("Julieth Anyelina Herrera Olivar — Ficha 55572", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=10)
body("Docente: Sergio Mora", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=4)
body("Fecha de entrega: 08 de noviembre de 2026", align=WD_ALIGN_PARAGRAPH.CENTER, size=13, space_after=4)
page_break()

# ================================================================== 1. INTRO
heading("1. Introducción", 1)
body("El presente informe documenta el proceso completo de diseño de la interfaz de "
     "“VidaSana”, una página web de recomendaciones saludables desarrollada en el marco de la "
     "Actividad de Construcción Aplicada (ACA) de la asignatura Ingeniería Web. La temática "
     "abordada consiste en una plataforma que sugiere a sus usuarios contenidos relacionados con "
     "la alimentación, la actividad física, el descanso y el bienestar, con el propósito de "
     "fomentar hábitos de vida más saludables.")
body("El alcance del proyecto comprende los tres niveles progresivos de concreción de una idea de "
     "diseño: un wireframe de baja fidelidad que define la estructura y la jerarquía de la "
     "información; un mockup de alta fidelidad que incorpora la identidad visual (paleta de "
     "colores, tipografía, iconografía y composición); y un prototipo navegable e interactivo que "
     "simula la experiencia de uso de la página. Adicionalmente, se realiza el análisis argumentado "
     "de los cinco requerimientos funcionales y los cinco requerimientos no funcionales definidos "
     "en la guía de la actividad.")
body("Para la elaboración de los diseños se emplearon herramientas de prototipado y diseño de "
     "interfaces como Figma y Balsamiq como referencia metodológica, y se construyó un prototipo "
     "funcional en HTML, CSS y JavaScript, conectado a una base de datos PostgreSQL en Supabase y "
     "publicado en línea mediante Vercel, lo que permite recorrer los flujos principales del usuario "
     "con datos persistentes y reales. El propósito del informe es evidenciar, de manera ordenada y "
     "argumentada, cómo cada requerimiento fue interpretado y resuelto en los diseños elaborados.")

# ================================================================== 2. OBJETIVOS
heading("2. Objetivos", 1)
heading("2.1 Objetivo general", 2)
body("Desarrollar las habilidades prácticas para la gestión integral de un proyecto de desarrollo "
     "web, mediante la elaboración del wireframe, el mockup y el prototipo de una página de "
     "recomendaciones saludables, aplicando metodologías ágiles y tradicionales para el diseño de "
     "interfaces de usuario centradas en la experiencia del usuario.")
heading("2.2 Objetivos específicos", 2)
bullet("Analizar de manera argumentada los requerimientos funcionales y no funcionales establecidos "
       "para la página de recomendaciones saludables.")
bullet("Diseñar el wireframe de la página, definiendo la estructura, la distribución de los "
       "elementos y la jerarquía de la información.")
bullet("Elaborar el mockup incorporando la totalidad de los elementos de diseño visual que reflejan "
       "la apariencia final de la página.")
bullet("Construir un prototipo funcional y navegable que refleje con precisión la interacción del "
       "usuario con la página.")

# ================================================================== 3. RF
heading("3. Análisis de requerimientos funcionales", 1)
body("A continuación se analiza, requerimiento por requerimiento, la manera en que cada uno fue "
     "interpretado y la forma en que se resolvió en los diseños elaborados (wireframe, mockup y "
     "prototipo).")

heading("RF1. Gestión de usuarios y perfil de salud", 2)
body("Este requerimiento fue interpretado como la necesidad de que la página permita a cada usuario "
     "crear una cuenta, iniciar sesión y configurar un perfil con información de salud relevante "
     "para personalizar su experiencia. Se resolvió mediante una pantalla de registro e inicio de "
     "sesión (Figura 8) que solicita datos básicos de identificación y, de forma complementaria, "
     "datos del perfil de salud como la edad, la estatura, el peso y el objetivo personal (perder "
     "peso, ganar músculo o mejorar energía). Adicionalmente, se diseñó la pantalla “Mi perfil de "
     "salud” (Figura 9), donde el usuario visualiza sus métricas (edad, estatura, peso e IMC "
     "calculado automáticamente) y configura sus preferencias y restricciones alimentarias. Esta "
     "información es la base sobre la cual se personalizan las recomendaciones.")

heading("RF2. Gestión de contenidos saludables", 2)
body("Se interpretó como la capacidad de organizar, clasificar y presentar de manera estructurada "
     "los contenidos de la página (recetas, rutinas de ejercicio, consejos de descanso y de "
     "bienestar). En los diseños se resolvió organizando el contenido en cuatro categorías "
     "principales —Alimentación, Actividad física, Descanso y Bienestar— presentes tanto en la "
     "página de inicio (Figura 7) como en la búsqueda. Cada recomendación se presenta mediante una "
     "tarjeta que muestra el título, la categoría, la dificultad, la duración y la valoración, y "
     "cuenta con una vista de detalle (Figura 11) que incluye la descripción, los beneficios y la "
     "información nutricional. Esta estructura de componentes reutilizables facilita la gestión y "
     "escalabilidad del contenido.")

heading("RF3. Búsqueda y filtrado", 2)
body("Este requerimiento fue interpretado como la posibilidad de que el usuario encuentre "
     "rápidamente una recomendación específica. Se resolvió mediante un buscador global ubicado en "
     "la sección principal de la página de inicio y, de manera más completa, en una pantalla "
     "dedicada de búsqueda (Figura 10) que integra una barra de búsqueda, filtros por categoría, "
     "duración y dificultad, y un ordenamiento por valoración. Los filtros seleccionados se "
     "visualizan como etiquetas activas que el usuario puede retirar, y los resultados se muestran "
     "en una lista con tarjetas que incluyen la opción de guardar la recomendación directamente.")

heading("RF4. Personalización de recomendaciones", 2)
body("Se interpretó como la capacidad del sistema de adaptar las recomendaciones al perfil, las "
     "preferencias y el objetivo de salud de cada usuario. Se resolvió vinculando el perfil de salud "
     "con la sección de “Recomendaciones destacadas” de la página de inicio (Figura 7): a partir de "
     "los datos registrados (objetivo, restricciones y preferencias), la página prioriza y destaca "
     "los contenidos más afines al usuario. De esta manera, dos usuarios con perfiles distintos "
     "reciben una experiencia y un orden de recomendaciones diferentes, cumpliendo con el enfoque "
     "de personalización solicitado.")

heading("RF5. Favoritos y seguimiento de hábitos", 2)
body("Este requerimiento se interpretó en dos partes. Por un lado, la posibilidad de guardar "
     "recomendaciones para consultarlas después, resuelta mediante el botón de corazón presente en "
     "las tarjetas y en la vista de detalle, y mediante la pantalla “Mis favoritos” (Figura 12) que "
     "reúne todas las recomendaciones guardadas. Por otro lado, el seguimiento de hábitos, resuelto "
     "en la misma pantalla mediante un módulo que muestra el progreso de hábitos diarios (consumo "
     "de agua, pasos, horas de sueño y meditación) con barras de progreso, casillas de cumplimiento "
     "y una racha de días consecutivos, lo que motiva al usuario a mantener la constancia.")

# ================================================================== 4. RNF
heading("4. Análisis de requerimientos no funcionales", 1)
body("Los requerimientos no funcionales fueron considerados de forma transversal en el diseño y "
     "desarrollo del proyecto, tal como se explica a continuación.")

heading("RNF1. Rendimiento", 2)
body("Se consideró garantizando una experiencia rápida y fluida. En el diseño se priorizó una "
     "interfaz ligera con componentes simples y reutilizables, imágenes optimizadas y carga "
     "progresiva del contenido, de modo que las transiciones entre pantallas y los resultados de "
     "búsqueda se muestren sin demoras perceptibles para el usuario.")

heading("RNF2. Escalabilidad", 2)
body("Se abordó mediante un sistema de diseño basado en componentes y tarjetas reutilizables, y en "
     "variables de estilo (colores y tipografía definidos una sola vez). Esto permite agregar nuevas "
     "categorías, recomendaciones o pantallas sin necesidad de rediseñar la interfaz, garantizando "
     "que la página pueda crecer en contenido y funcionalidades de manera sostenible.")

heading("RNF3. Seguridad y privacidad", 2)
body("Dado que se gestionan datos sensibles de salud, se reflejó mediante un flujo de autenticación "
     "seguro (registro e inicio de sesión con contraseña cifrada), avisos explícitos de privacidad y "
     "consentimiento al momento del registro, y mensajes que informan al usuario que sus datos están "
     "protegidos. Asimismo, las preferencias y restricciones de salud solo son visibles para el "
     "propio usuario dentro de su perfil.")

heading("RNF4. Experiencia de usuario", 2)
body("Se garantizó mediante una navegación clara y consistente, jerarquía visual definida, "
     "microinteracciones con retroalimentación (estados activos, botones de guardar y de "
     "cumplimiento) y textos legibles con contraste adecuado entre el fondo y la tipografía. Cada "
     "pantalla fue diseñada con un objetivo claro y una acción principal identificable, siguiendo un "
     "enfoque centrado en el usuario.")

heading("RNF5. Compatibilidad con dispositivos", 2)
body("Se consideró mediante un diseño adaptable (responsive) que reorganiza los elementos según el "
     "tamaño de la pantalla: las rejillas de categorías y recomendaciones pasan de cuatro o tres "
     "columnas en escritorio a dos o una columna en tabletas y móviles, y los controles se adaptan a "
     "objetivos táctiles cómodos. El prototipo implementado en HTML y CSS incluye estas reglas de "
     "adaptación responsiva.")

# ================================================================== 5. WIREFRAME
page_break()
heading("5. Wireframe", 1)
body("El wireframe representa la estructura de baja fidelidad de la página, definiendo la "
     "distribución de bloques, la jerarquía de la información y la ubicación de menús, buscador, "
     "listados y formularios, sin aplicar color, tipografía definitiva ni imágenes reales. A "
     "continuación se presentan las pantallas diseñadas con su respectiva explicación.")
figure(os.path.join(WIRE, "01_inicio.png"),
       "Figura 1. Wireframe de la pantalla de inicio.")
body("La pantalla de inicio organiza la información en un encabezado con el logotipo y el menú, una "
     "sección principal (hero) con el buscador, un bloque de categorías y un listado de "
     "recomendaciones destacadas, culminando con el pie de página.")
figure(os.path.join(WIRE, "02_registro_login.png"),
       "Figura 2. Wireframe de la pantalla de registro e inicio de sesión.")
body("Presenta un formulario central con pestañas para alternar entre iniciar sesión y registrarse, "
     "campos para los datos del usuario y un botón de acción principal, reflejando el flujo de "
     "autenticación.")
figure(os.path.join(WIRE, "03_perfil_salud.png"),
       "Figura 3. Wireframe de la pantalla de perfil de salud.")
body("La estructura separa la información del usuario (a la izquierda) de los datos de salud y las "
     "preferencias (a la derecha), estableciendo una jerarquía clara entre identidad, métricas y "
     "configuración.")
figure(os.path.join(WIRE, "04_busqueda_filtrado.png"),
       "Figura 4. Wireframe de la pantalla de búsqueda y filtrado.")
body("Ubica el buscador en la parte superior, seguido de los filtros, las etiquetas activas y la "
     "lista de resultados en tarjetas, garantizando que todos los requerimientos funcionales tengan "
     "un espacio dentro de la estructura.")
figure(os.path.join(WIRE, "05_detalle_recomendacion.png"),
       "Figura 5. Wireframe de la pantalla de detalle de una recomendación.")
body("Presenta la imagen principal, el título, la descripción, los botones de acción y una columna "
     "lateral de información complementaria, además de un bloque de recomendaciones relacionadas.")
figure(os.path.join(WIRE, "06_favoritos_habitos.png"),
       "Figura 6. Wireframe de la pantalla de favoritos y seguimiento de hábitos.")
body("Combina la rejilla de recomendaciones guardadas con el módulo de seguimiento de hábitos, "
     "organizando visualmente ambos propósitos dentro de una misma pantalla.")

# ================================================================== 6. MOCKUP
page_break()
heading("6. Mockup", 1)
body("El mockup constituye la representación visual de alta fidelidad construida a partir del "
     "wireframe. Para su elaboración se definió una paleta de colores inspirada en la salud y la "
     "naturaleza: verde principal (#2E7D32), verde oscuro (#165220), naranja de acento (#FF8F00) y "
     "fondos claros neutros que aportan frescura y legibilidad. La tipografía utilizada es Arial, "
     "elegida por su alta legibilidad en pantalla y su disponibilidad universal. La iconografía "
     "emplea pictogramas simples y reconocibles (manzana, rayo, luna y hoja) para representar cada "
     "categoría, y la composición mantiene la consistencia entre pantallas mediante tarjetas, "
     "esquinas redondeadas y sombras suaves.")
figure(os.path.join(MOCK, "01_inicio.png"),
       "Figura 7. Mockup de la pantalla de inicio.")
figure(os.path.join(MOCK, "02_registro_login.png"),
       "Figura 8. Mockup de la pantalla de registro e inicio de sesión.")
figure(os.path.join(MOCK, "03_perfil_salud.png"),
       "Figura 9. Mockup de la pantalla de perfil de salud.")
figure(os.path.join(MOCK, "04_busqueda_filtrado.png"),
       "Figura 10. Mockup de la pantalla de búsqueda y filtrado.")
figure(os.path.join(MOCK, "05_detalle_recomendacion.png"),
       "Figura 11. Mockup de la pantalla de detalle de una recomendación.")
figure(os.path.join(MOCK, "06_favoritos_habitos.png"),
       "Figura 12. Mockup de la pantalla de favoritos y seguimiento de hábitos.")
body("En conjunto, el mockup refleja la apariencia final de la página, incorporando la totalidad de "
     "los elementos de diseño visual (colores, tipografía, iconografía, espaciados y estilo de los "
     "componentes) y verificando el contraste, la legibilidad y la adaptación de la interfaz a "
     "distintos tamaños de pantalla.")

# ================================================================== 7. PROTOTIPO
page_break()
heading("7. Prototipo", 1)
body("El prototipo es la versión navegable e interactiva del diseño, construida como una aplicación "
     "web en HTML, CSS y JavaScript que reproduce con fidelidad la interfaz definida en el mockup. "
     "A diferencia de un mockup estático, el prototipo permite recorrer los flujos principales del "
     "usuario e interactuar con los elementos de la interfaz.")
body("El prototipo se conecta a una base de datos PostgreSQL en Supabase, lo que hace que el "
     "registro y el inicio de sesión sean reales (autenticación por correo y contraseña) y que el "
     "perfil de salud, los favoritos y el seguimiento de hábitos se guarden de forma persistente "
     "para cada usuario. El prototipo navegable se publicó en línea y se puede consultar en el "
     "siguiente enlace:")
body("[ENLACE DEL PROTOTIPO EN VERCEL]", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER,
     size=12, color=GREEN2, space_after=10)
body("Al abrir el prototipo se pueden recorrer los siguientes flujos implementados:")
bullet("Registro e inicio de sesión: el usuario puede alternar entre los formularios de registro e "
       "inicio de sesión y completar los datos de su perfil de salud.")
bullet("Búsqueda y filtrado: el buscador permite escribir un término y filtrar los resultados por "
       "categoría mediante los botones de filtro, mostrando la lista de recomendaciones que "
       "coinciden con los criterios seleccionados.")
bullet("Consulta del detalle: al seleccionar una recomendación se abre su vista de detalle con la "
       "descripción, los beneficios, la información nutricional y las recomendaciones relacionadas.")
bullet("Guardar en favoritos: desde las tarjetas o desde el detalle, el usuario puede marcar o "
       "desmarcar una recomendación como favorita, y esta aparece en la pantalla “Mis favoritos”.")
bullet("Seguimiento de hábitos: el usuario visualiza el progreso de sus hábitos mediante barras y "
       "puede marcar el cumplimiento diario de cada uno.")
body("El prototipo implementa los estados interactivos (elementos activos, botones de guardar y de "
     "cumplimiento), la navegación entre pantallas y la persistencia de datos en la base de datos, "
     "simulando la experiencia de uso real de la página. Las capturas de las pantallas del prototipo "
     "corresponden a los diseños presentados en las Figuras 7 a 12 de la sección de mockup.")

# ================================================================== 8. CONCLUSIONES
heading("8. Conclusiones", 1)
bullet("El recorrido completo por los tres niveles de diseño (wireframe, mockup y prototipo) "
       "permitió comprender que el diseño de interfaces es un proceso progresivo: primero se define "
       "la estructura, luego la identidad visual y, finalmente, la interacción. Este orden evita "
       "retrabajos y garantiza que la experiencia del usuario sea el eje del proyecto.")
bullet("El análisis argumentado de los requerimientos demostró que cada decisión de diseño debe "
       "estar justificada: la ubicación de un buscador, la organización por categorías o la "
       "inclusión de un módulo de hábitos no son decisiones estéticas, sino respuestas concretas a "
       "los requerimientos funcionales y no funcionales de la página.")
bullet("La principal dificultad encontrada fue mantener la consistencia visual entre todas las "
       "pantallas a medida que crecía la cantidad de elementos. Se superó mediante la definición "
       "previa de un sistema de diseño (paleta, tipografía, componentes reutilizables), lo que "
       "facilitó la construcción del mockup y del prototipo.")

# ================================================================== 9. REFERENCIAS
heading("9. Referencias", 1)
refs = [
    "Adobe Inc. (2023). Adobe XD: diseño y prototipado de experiencias de usuario [Software, "
    "discontinuado]. Adobe. https://www.adobe.com/products/xd.html",
    "AlexCG Design. (2020). Curso Figma desde CERO | Curso de Introducción a Figma. YouTube. "
    "https://www.youtube.com/watch?v=SqO_-olNvnU",
    "Balsamiq Studios. (2024). Balsamiq: fast, focused wireframing [Herramienta en línea]. "
    "https://balsamiq.com/",
    "Dribbble. (2024). Dribbble: the leading destination to find and showcase creative work "
    "[Comunidad en línea]. https://dribbble.com/",
    "EDteam. (2017). Minicurso de Balsamiq Mockups (1) – Los wireframes y la interfaz. YouTube. "
    "https://www.youtube.com/watch?v=4WqfxF1QjTM",
    "Figma. (2024). Figma: the collaborative interface design tool [Software en línea]. "
    "https://www.figma.com/",
    "InVision. (2024). InVision: digital product design platform [Plataforma digital, servicio "
    "cerrado en diciembre de 2024]. https://www.invisionapp.com/",
    "Mozilla Developer Network. (2024). MDN Web Docs [Documentación técnica en línea]. "
    "https://developer.mozilla.org/en-US/",
    "W3Schools. (2024). W3Schools: online web tutorials [Plataforma educativa en línea]. "
    "https://www.w3schools.com/",
]
for r_ in refs:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-1.0)
    run = p.add_run(r_)
    run.font.name = "Arial"
    run.font.size = Pt(11)

doc.save(OUT)
print("Informe guardado en", OUT)
