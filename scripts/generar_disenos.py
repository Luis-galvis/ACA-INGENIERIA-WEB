# -*- coding: utf-8 -*-
"""Genera wireframes y mockups de la página 'VidaSana' (recomendaciones saludables)."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIRE_DIR = os.path.join(BASE, "wireframes")
MOCK_DIR = os.path.join(BASE, "mockups")
os.makedirs(WIRE_DIR, exist_ok=True)
os.makedirs(MOCK_DIR, exist_ok=True)

FD = "C:/Windows/Fonts"


def F(size, bold=False, italic=False):
    name = "arialbd.ttf" if bold else ("ariali.ttf" if italic else "arial.ttf")
    return ImageFont.truetype(os.path.join(FD, name), size)


# ------------------------------------------------------------------ helpers
def lerp(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def gradient(draw, box, c1, c2):
    x0, y0, x1, y1 = box
    h = max(1, y1 - y0)
    for i in range(h):
        draw.line([(x0, y0 + i), (x1, y0 + i)], fill=lerp(c1, c2, i / (h - 1)))


def wrap(draw, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def twrap(draw, xy, text, font, fill, maxw, lh=None):
    x, y = xy
    lh = lh or int(font.size * 1.3)
    for line in wrap(draw, text, font, maxw):
        draw.text((x, y), line, font=font, fill=fill)
        y += lh
    return y


def shadow(draw, box, radius=18, alpha_color=(220, 224, 228)):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle([x0 + 3, y0 + 5, x1 + 3, y1 + 5], radius=radius,
                           fill=alpha_color)


def card(draw, box, fill=(255, 255, 255), radius=18, outline=None, width=1,
         do_shadow=True):
    x0, y0, x1, y1 = box
    if do_shadow:
        shadow(draw, box, radius)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                           outline=outline, width=width)


def center_text(draw, cx, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text((cx - w / 2, y), text, font=font, fill=fill)


# ------------------------------------------------------------------ icons
def icon_search(draw, cx, cy, s, color, width=4):
    r = int(s * 0.55)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=width)
    draw.line([cx + r * 0.8, cy + r * 0.8, cx + s, cy + s], fill=color, width=width)


def icon_heart(draw, cx, cy, s, color, filled=True, outline=False):
    # heart using two circles + triangle
    r = int(s * 0.34)
    x0, y0 = cx - r, cy - int(s * 0.22)
    draw.ellipse([x0, y0, x0 + 2 * r, y0 + 2 * r], fill=color, outline=color)
    draw.ellipse([x0 + 2 * r - 2, y0, x0 + 4 * r - 2, y0 + 2 * r], fill=color,
                 outline=color)
    draw.polygon([(cx - int(s * 0.62), cy - int(s * 0.05)),
                  (cx + int(s * 0.62), cy - int(s * 0.05)),
                  (cx, cy + int(s * 0.62))], fill=color)


def icon_star(draw, cx, cy, s, color):
    import math
    pts = []
    for i in range(10):
        r = s if i % 2 == 0 else s * 0.45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    draw.polygon(pts, fill=color)


def icon_check(draw, x, y, s, color, width=5):
    draw.line([(x, y + s * 0.5), (x + s * 0.35, y + s * 0.85)], fill=color, width=width)
    draw.line([(x + s * 0.35, y + s * 0.85), (x + s, y + s * 0.1)], fill=color, width=width)


def icon_leaf(draw, cx, cy, s, color):
    draw.ellipse([cx - s * 0.55, cy - s * 0.7, cx + s * 0.55, cy + s * 0.3],
                 fill=color)
    draw.line([cx, cy - s * 0.7, cx, cy + s * 0.3], fill=(255, 255, 255), width=2)


def icon_apple(draw, cx, cy, s, color):
    r = int(s * 0.6)
    draw.ellipse([cx - r, cy - s * 0.35, cx + r, cy + s * 0.55], fill=color)
    draw.rectangle([cx - 2, cy - s * 0.75, cx + 2, cy - s * 0.35], fill=color)
    draw.ellipse([cx, cy - s * 0.8, cx + s * 0.35, cy - s * 0.55], fill=color)


def icon_bolt(draw, cx, cy, s, color):
    draw.polygon([(cx + s * 0.15, cy - s * 0.7), (cx - s * 0.45, cy + s * 0.1),
                  (cx - s * 0.05, cy + s * 0.1), (cx - s * 0.15, cy + s * 0.7),
                  (cx + s * 0.45, cy - s * 0.1), (cx + s * 0.05, cy - s * 0.1)],
                 fill=color)


def icon_moon(draw, cx, cy, s, color, carve):
    draw.ellipse([cx - s * 0.6, cy - s * 0.6, cx + s * 0.6, cy + s * 0.6], fill=color)
    draw.ellipse([cx - s * 0.1, cy - s * 0.75, cx + s * 0.75, cy + s * 0.1],
                 fill=carve)


def icon_user(draw, cx, cy, s, color):
    draw.ellipse([cx - s * 0.35, cy - s * 0.7, cx + s * 0.35, cy - s * 0.05],
                 fill=color)
    draw.ellipse([cx - s * 0.6, cy + s * 0.1, cx + s * 0.6, cy + s * 0.75],
                 fill=color)


# ------------------------------------------------------------------ chrome
W, H = 1240, 1600
NAV_H = 88
FOOT_H = 150

NAV_LINKS = ["Inicio", "Categorías", "Mi salud", "Favoritos"]

MOCK = {
    "primary": (30, 122, 46),
    "primary_dark": (22, 82, 32),
    "primary_light": (99, 190, 106),
    "primary_soft": (232, 245, 233),
    "accent": (255, 143, 0),
    "accent_soft": (255, 243, 224),
    "bg": (246, 250, 244),
    "card": (255, 255, 255),
    "text": (30, 36, 40),
    "muted": (116, 128, 134),
    "border": (226, 232, 240),
    "white": (255, 255, 255),
}

CAT_COLORS = {
    "Alimentación": (46, 125, 50),
    "Actividad física": (245, 124, 0),
    "Descanso": (57, 110, 176),
    "Bienestar": (123, 84, 178),
}


def nav(draw, mode, active=None):
    if mode == "wire":
        draw.rectangle([0, 0, W, NAV_H], fill=(238, 238, 238))
        draw.rectangle([80, 26, 176, 62], fill=(200, 200, 200))
        center_text(draw, 128, 33, "LOGO", F(18, True), (100, 100, 100))
        cx = 420
        for i, link in enumerate(NAV_LINKS):
            col = (80, 80, 80) if link == active else (130, 130, 130)
            center_text(draw, cx, 34, link, F(17, link == active), col)
            cx += 170
        draw.rounded_rectangle([1010, 24, 1160, 64], radius=12, outline=(150, 150, 150), width=2)
        center_text(draw, 1085, 32, "Botón", F(15, True), (110, 110, 110))
    else:
        draw.rectangle([0, 0, W, NAV_H], fill=(255, 255, 255))
        draw.line([0, NAV_H, W, NAV_H], fill=MOCK["border"], width=1)
        # logo
        icon_leaf(draw, 110, 44, 22, MOCK["primary"])
        draw.text((142, 26), "VidaSana", font=F(26, True), fill=MOCK["primary"])
        cx = 470
        for i, link in enumerate(NAV_LINKS):
            col = MOCK["primary"] if link == active else MOCK["muted"]
            if link == active:
                draw.rounded_rectangle([cx - 22, 52, cx + 22, 72], radius=8,
                                       fill=MOCK["primary_soft"])
            center_text(draw, cx, 30, link, F(17, link == active), col)
            cx += 175
        draw.rounded_rectangle([1000, 22, 1160, 66], radius=14, fill=MOCK["primary"])
        center_text(draw, 1080, 30, "Iniciar sesión", F(15, True), (255, 255, 255))


def footer(draw, mode):
    y0 = H - FOOT_H
    if mode == "wire":
        draw.rectangle([0, y0, W, H], fill=(235, 235, 235))
        center_text(draw, W / 2, y0 + 45, "LOGO", F(18, True), (110, 110, 110))
        center_text(draw, W / 2, y0 + 80, "Texto de pie de página · Enlaces · Redes",
                    F(14), (130, 130, 130))
    else:
        draw.rectangle([0, y0, W, H], fill=MOCK["primary_dark"])
        draw.text((80, y0 + 40), "VidaSana", font=F(22, True), fill=(255, 255, 255))
        draw.text((80, y0 + 80), "Tu guía para una vida más saludable", font=F(13),
                  fill=(188, 220, 190))
        draw.text((680, y0 + 40), "Contacto: hola@vidasana.com", font=F(14),
                  fill=(220, 238, 222))
        draw.text((680, y0 + 70), "© 2026 VidaSana · Privacidad · Términos", font=F(13),
                  fill=(188, 220, 190))


def section_title(draw, mode, x, y, title, subtitle=None):
    if mode == "wire":
        draw.rectangle([x, y, x + 300, y + 18], fill=(205, 205, 205))
        draw.text((x, y + 6), title.upper(), font=F(15, True), fill=(90, 90, 90))
    else:
        draw.text((x, y), title, font=F(30, True), fill=MOCK["text"])
        if subtitle:
            draw.text((x, y + 44), subtitle, font=F(16), fill=MOCK["muted"])


def image_placeholder(draw, mode, box, label=None, color=None):
    x0, y0, x1, y1 = box
    if mode == "wire":
        draw.rectangle(box, fill=(225, 225, 225), outline=(170, 170, 170), width=2)
        draw.line([x0, y0, x1, y1], fill=(170, 170, 170), width=2)
        draw.line([x0, y1, x1, y0], fill=(170, 170, 170), width=2)
        if label:
            center_text(draw, (x0 + x1) / 2, (y0 + y1) / 2 - 10, label, F(16, True),
                        (140, 140, 140))
    else:
        gradient(draw, box, color, lerp(color, (255, 255, 255), 0.35))
        draw.rounded_rectangle(box, radius=14, outline=(255, 255, 255), width=3)


# ================================================================== WIREFRAMES
def wire_inicio():
    img = Image.new("RGB", (W, H), (250, 250, 250))
    d = ImageDraw.Draw(img)
    nav(d, "wire", active="Inicio")
    # hero
    d.rectangle([0, NAV_H, W, 330], fill=(240, 240, 240))
    d.rectangle([80, 140, 560, 176], fill=(205, 205, 205))
    d.rectangle([80, 196, 520, 212], fill=(225, 225, 225))
    d.rectangle([80, 216, 460, 232], fill=(225, 225, 225))
    d.rounded_rectangle([80, 250, 400, 292], radius=10, fill=(232, 232, 232),
                        outline=(170, 170, 170), width=2)
    center_text(d, 240, 259, "BUSCADOR", F(14, True), (120, 120, 120))
    image_placeholder(d, "wire", (760, 128, 1160, 300), "IMAGEN")
    # categorias
    section_title(d, "wire", 80, 360, "Categorías")
    cats = ["Alimentación", "Actividad física", "Descanso", "Bienestar"]
    x = 80
    for c in cats:
        d.rectangle([x, 400, x + 250, 560], fill=(245, 245, 245), outline=(175, 175, 175), width=2)
        d.rectangle([x + 95, 430, x + 155, 490], fill=(215, 215, 215), outline=(170, 170, 170), width=2)
        center_text(d, x + 125, 510, c, F(15, True), (95, 95, 95))
        center_text(d, x + 125, 532, "12 ítems", F(12), (140, 140, 140))
        x += 280
    # destacadas
    section_title(d, "wire", 80, 600, "Recomendaciones destacadas")
    for i in range(3):
        x = 80 + i * 380
        d.rectangle([x, 640, x + 340, 980], fill=(245, 245, 245), outline=(175, 175, 175), width=2)
        image_placeholder(d, "wire", (x + 16, 656, x + 324, 800), "IMAGEN")
        d.rectangle([x + 16, 816, x + 300, 832], fill=(210, 210, 210))
        d.rectangle([x + 16, 844, x + 240, 858], fill=(225, 225, 225))
        d.rectangle([x + 16, 870, x + 300, 884], fill=(225, 225, 225))
        d.rectangle([x + 16, 930, x + 110, 958], fill=(220, 220, 220))
    footer(d, "wire")
    return img


def wire_registro():
    img = Image.new("RGB", (W, H), (250, 250, 250))
    d = ImageDraw.Draw(img)
    nav(d, "wire")
    card(d, (300, 150, 940, 1460), fill=(250, 250, 250), radius=20, do_shadow=False)
    d.rectangle([300, 150, 940, 1460], outline=(175, 175, 175), width=2)
    center_text(d, W / 2, 190, "Título de la página", F(22, True), (90, 90, 90))
    center_text(d, W / 2, 226, "Subtítulo descriptivo", F(14), (140, 140, 140))
    # tabs
    d.rectangle([420, 262, 620, 306], fill=(200, 200, 200))
    d.rectangle([620, 262, 820, 306], fill=(235, 235, 235), outline=(175, 175, 175), width=2)
    center_text(d, 520, 272, "Iniciar sesión", F(15, True), (100, 100, 100))
    center_text(d, 720, 272, "Registrarse", F(15, True), (100, 100, 100))
    # fields
    fy = 340
    labels = ["Nombre completo", "Correo electrónico", "Contraseña",
              "Confirmar contraseña", "Edad", "Estatura / Peso", "Objetivo"]
    for lab in labels:
        d.text((370, fy), lab, font=F(14, True), fill=(110, 110, 110))
        d.rectangle([370, fy + 24, 870, fy + 66], fill=(238, 238, 238),
                    outline=(175, 175, 175), width=2)
        fy += 104
    d.rounded_rectangle([370, fy + 10, 870, fy + 62], radius=12, outline=(150, 150, 150), width=2)
    center_text(d, 620, fy + 22, "BOTÓN PRINCIPAL", F(15, True), (100, 100, 100))
    center_text(d, 620, fy + 96, "Enlace / texto legal", F(13), (140, 140, 140))
    footer(d, "wire")
    return img


def wire_perfil():
    img = Image.new("RGB", (W, H), (250, 250, 250))
    d = ImageDraw.Draw(img)
    nav(d, "wire", active="Mi salud")
    section_title(d, "wire", 80, 130, "Perfil de salud")
    # left user card
    d.rectangle([80, 180, 460, 560], fill=(245, 245, 245), outline=(175, 175, 175), width=2)
    d.ellipse([230, 220, 330, 320], fill=(210, 210, 210), outline=(170, 170, 170), width=2)
    center_text(d, 280, 340, "Usuario", F(17, True), (95, 95, 95))
    center_text(d, 280, 368, "correo@email.com", F(13), (140, 140, 140))
    d.rounded_rectangle([190, 400, 370, 444], radius=12, outline=(160, 160, 160), width=2)
    center_text(d, 280, 410, "Editar", F(14, True), (110, 110, 110))
    # metrics
    section_title(d, "wire", 500, 180, "Datos de salud")
    for i in range(4):
        x = 500 + (i % 2) * 330
        y = 230 + (i // 2) * 150
        d.rectangle([x, y, x + 290, y + 120], fill=(245, 245, 245),
                    outline=(175, 175, 175), width=2)
        center_text(d, x + 145, y + 34, "Métrica", F(13, True), (130, 130, 130))
        center_text(d, x + 145, y + 62, "Valor", F(20, True), (90, 90, 90))
    # preferences
    section_title(d, "wire", 80, 610, "Preferencias")
    d.rectangle([80, 660, 1160, 1000], fill=(245, 245, 245), outline=(175, 175, 175), width=2)
    for i in range(4):
        y = 700 + i * 70
        d.rectangle([110, y, 150, y + 40], fill=(215, 215, 215), outline=(160, 160, 160), width=2)
        d.rectangle([180, y + 6, 700, y + 30], fill=(225, 225, 225))
    d.rounded_rectangle([820, 1050, 1160, 1110], radius=12, outline=(150, 150, 150), width=2)
    center_text(d, 990, 1066, "GUARDAR", F(15, True), (100, 100, 100))
    footer(d, "wire")
    return img


def wire_busqueda():
    img = Image.new("RGB", (W, H), (250, 250, 250))
    d = ImageDraw.Draw(img)
    nav(d, "wire")
    d.rounded_rectangle([80, 130, 1160, 180], radius=10, fill=(238, 238, 238),
                        outline=(170, 170, 170), width=2)
    center_text(d, 620, 143, "BUSCADOR", F(16, True), (120, 120, 120))
    # filters
    for i in range(4):
        x = 80 + i * 285
        d.rectangle([x, 210, x + 255, 250], fill=(240, 240, 240),
                    outline=(175, 175, 175), width=2)
        center_text(d, x + 127, 218, "Filtro", F(14, True), (115, 115, 115))
    # chips
    d.rounded_rectangle([80, 280, 230, 320], radius=16, fill=(225, 225, 225))
    center_text(d, 155, 288, "Etiqueta ×", F(13), (100, 100, 100))
    # results
    for i in range(3):
        y = 360 + i * 220
        d.rectangle([80, y, 1160, y + 180], fill=(245, 245, 245),
                    outline=(175, 175, 175), width=2)
        image_placeholder(d, "wire", (104, y + 20, 264, y + 160), "IMAGEN")
        d.rectangle([300, y + 30, 700, y + 52], fill=(210, 210, 210))
        d.rectangle([300, y + 68, 560, y + 86], fill=(228, 228, 228))
        d.rectangle([300, y + 100, 640, y + 118], fill=(228, 228, 228))
        d.rectangle([300, y + 134, 420, y + 156], fill=(220, 220, 220))
        d.rounded_rectangle([1040, y + 60, 1110, y + 120], radius=12,
                            outline=(165, 165, 165), width=2)
    footer(d, "wire")
    return img


def wire_detalle():
    img = Image.new("RGB", (W, H), (250, 250, 250))
    d = ImageDraw.Draw(img)
    nav(d, "wire")
    d.text((80, 120), "Inicio / Categoría / Detalle", font=F(13), fill=(140, 140, 140))
    image_placeholder(d, "wire", (80, 150, 740, 520), "IMAGEN")
    d.rectangle([80, 540, 560, 580], fill=(205, 205, 205))
    d.rectangle([80, 596, 400, 614], fill=(225, 225, 225))
    d.rectangle([80, 640, 720, 660], fill=(228, 228, 228))
    d.rectangle([80, 668, 660, 688], fill=(228, 228, 228))
    d.rectangle([80, 696, 600, 716], fill=(228, 228, 228))
    d.rectangle([80, 750, 300, 772], fill=(215, 215, 215))
    # buttons
    d.rounded_rectangle([80, 800, 340, 856], radius=12, outline=(150, 150, 150), width=2)
    center_text(d, 210, 815, "BOTÓN", F(15, True), (100, 100, 100))
    d.rounded_rectangle([360, 800, 600, 856], radius=12, outline=(150, 150, 150), width=2)
    center_text(d, 480, 815, "BOTÓN", F(15, True), (100, 100, 100))
    # side
    d.rectangle([780, 150, 1160, 560], fill=(245, 245, 245), outline=(175, 175, 175), width=2)
    d.rectangle([800, 180, 850, 220], fill=(210, 210, 210))
    d.rectangle([800, 240, 1140, 300], fill=(228, 228, 228))
    d.rectangle([800, 320, 1000, 360], fill=(228, 228, 228))
    # related
    section_title(d, "wire", 80, 900, "Relacionados")
    for i in range(3):
        x = 80 + i * 380
        d.rectangle([x, 940, x + 340, 1240], fill=(245, 245, 245),
                    outline=(175, 175, 175), width=2)
        image_placeholder(d, "wire", (x + 16, 956, x + 324, 1080), "IMAGEN")
        d.rectangle([x + 16, 1100, x + 280, 1120], fill=(210, 210, 210))
    footer(d, "wire")
    return img


def wire_favoritos():
    img = Image.new("RGB", (W, H), (250, 250, 250))
    d = ImageDraw.Draw(img)
    nav(d, "wire", active="Favoritos")
    section_title(d, "wire", 80, 130, "Favoritos")
    for i in range(3):
        x = 80 + i * 380
        d.rectangle([x, 180, x + 340, 520], fill=(245, 245, 245),
                    outline=(175, 175, 175), width=2)
        image_placeholder(d, "wire", (x + 16, 196, x + 324, 340), "IMAGEN")
        d.rectangle([x + 16, 360, x + 280, 380], fill=(210, 210, 210))
        d.rectangle([x + 16, 400, x + 240, 418], fill=(228, 228, 228))
    section_title(d, "wire", 80, 570, "Seguimiento de hábitos")
    for i in range(4):
        y = 620 + i * 110
        d.rectangle([80, y, 1160, y + 84], fill=(245, 245, 245),
                    outline=(175, 175, 175), width=2)
        d.rectangle([104, y + 18, 500, y + 40], fill=(210, 210, 210))
        d.rectangle([104, y + 52, 760, y + 66], fill=(225, 225, 225))
        d.rectangle([1000, y + 24, 1080, y + 64], fill=(220, 220, 220))
    footer(d, "wire")
    return img


# ================================================================== MOCKUPS
def cat_badge(draw, cx, cy, s, name, color):
    draw.ellipse([cx - s, cy - s, cx + s, cy + s], fill=color)
    isz = int(s * 0.95)
    if name == "Alimentación":
        icon_apple(draw, cx, cy, isz, (255, 255, 255))
    elif name == "Actividad física":
        icon_bolt(draw, cx, cy, isz, (255, 255, 255))
    elif name == "Descanso":
        icon_moon(draw, cx, cy, isz, (255, 255, 255), carve=color)
    elif name == "Bienestar":
        icon_leaf(draw, cx, cy, isz, (255, 255, 255))


def tag_chip(draw, x, y, text, color):
    f = F(12, True)
    w = int(draw.textlength(text, font=f)) + 22
    draw.rounded_rectangle([x, y, x + w, y + 24], radius=12, fill=color)
    draw.text((x + 11, y + 4), text, font=f, fill=(255, 255, 255))


def rating(draw, x, y, stars=5, filled=5, size=13):
    for i in range(stars):
        col = MOCK["accent"] if i < filled else (214, 218, 222)
        icon_star(draw, x + i * (size + 6) + size / 2, y + size / 2, size * 0.55, col)


def mock_inicio():
    img = Image.new("RGB", (W, H), MOCK["bg"])
    d = ImageDraw.Draw(img)
    nav(d, "mock", active="Inicio")
    # hero
    hero = (0, NAV_H, W, 380)
    gradient(d, hero, (232, 245, 233), (246, 250, 244))
    d.text((80, 160), "Vive más sano, cada día", font=F(40, True), fill=MOCK["primary_dark"])
    twrap(d, (80, 220), "Recomendaciones personalizadas de alimentación, ejercicio, descanso "
                        "y bienestar para transformar tus hábitos.", F(18), MOCK["muted"], 560)
    # search bar
    card(d, (80, 292, 640, 352), radius=18)
    icon_search(d, 112, 322, 22, MOCK["muted"])
    d.text((140, 312), "¿Qué quieres mejorar hoy?", font=F(16), fill=MOCK["muted"])
    d.rounded_rectangle([520, 300, 620, 344], radius=12, fill=MOCK["primary"])
    center_text(d, 570, 308, "Buscar", F(15, True), (255, 255, 255))
    # hero image
    card(d, (720, 150, 1160, 360), radius=18)
    gradient(d, (720, 150, 1160, 360), MOCK["primary_light"], (197, 228, 199))
    icon_heart(d, 940, 210, 60, (255, 255, 255))
    icon_leaf(d, 940, 250, 34, (255, 255, 255))
    d.text((800, 300), "Bienestar integral", font=F(20, True), fill=(255, 255, 255))
    # categorias
    section_title(d, "mock", 80, 420, "Explora por categoría")
    cats = ["Alimentación", "Actividad física", "Descanso", "Bienestar"]
    x = 80
    for c in cats:
        card(d, (x, 480, x + 250, 680), radius=18)
        cat_badge(d, x + 125, 540, 40, c, CAT_COLORS[c])
        center_text(d, x + 125, 600, c, F(17, True), MOCK["text"])
        center_text(d, x + 125, 626, "12 recomendaciones", F(13), MOCK["muted"])
        x += 280
    # destacadas
    section_title(d, "mock", 80, 730, "Recomendaciones destacadas")
    recs = [
        ("Ensalada mediterránea rica en fibra", "Alimentación", "5 min", "4.9", (46, 125, 50)),
        ("Rutina HIIT de 20 minutos", "Actividad física", "20 min", "4.8", (245, 124, 0)),
        ("Meditación para dormir mejor", "Descanso", "10 min", "4.9", (57, 110, 176)),
    ]
    for i, (t, cat, dur, sc, col) in enumerate(recs):
        x = 80 + i * 380
        card(d, (x, 790, x + 340, 1110), radius=18)
        image_placeholder(d, "mock", (x + 16, 806, x + 324, 950), color=col)
        tag_chip(d, x + 16, 830, cat, col)
        d.text((x + 16, 970), t, font=F(17, True), fill=MOCK["text"])
        d.text((x + 16, 1000), f"{dur}  ·  ", font=F(13), fill=MOCK["muted"])
        rating(d, x + 16 + int(d.textlength(f"{dur}  ·  ", font=F(13))), 998)
        d.text((x + 16, 1040), "Consejos y beneficios para tu día a día.",
               font=F(13), fill=MOCK["muted"])
        d.text((x + 16, 1072), "Ver recomendación  →", font=F(14, True), fill=MOCK["primary"])
    footer(d, "mock")
    return img


def mock_registro():
    img = Image.new("RGB", (W, H), MOCK["bg"])
    d = ImageDraw.Draw(img)
    nav(d, "mock")
    card(d, (320, 140, 920, 1500), radius=24)
    center_text(d, W / 2, 190, "Crea tu cuenta", F(30, True), fill=MOCK["primary_dark"])
    center_text(d, W / 2, 240, "Comienza tu camino hacia una vida más saludable",
                F(15), fill=MOCK["muted"])
    # tabs
    d.rounded_rectangle([400, 280, 840, 336], radius=16, fill=(240, 244, 241))
    d.rounded_rectangle([400, 280, 620, 336], radius=16, fill=MOCK["primary"])
    center_text(d, 510, 292, "Registrarse", F(15, True), (255, 255, 255))
    center_text(d, 730, 292, "Iniciar sesión", F(15, True), MOCK["muted"])
    # fields
    fy = 366
    labels = ["Nombre completo", "Correo electrónico", "Contraseña",
              "Confirmar contraseña"]
    for lab in labels:
        d.text((370, fy), lab, font=F(13, True), fill=MOCK["text"])
        card(d, (370, fy + 24, 870, fy + 70), radius=12, fill=(248, 250, 249),
             outline=MOCK["border"], do_shadow=False)
        d.text((386, fy + 36), "••••••••••" if "ontraseña" in lab else "Escribe aquí…",
               font=F(14), fill=MOCK["muted"])
        fy += 96
    # perfil salud
    d.text((370, fy), "Datos de tu perfil de salud", font=F(15, True), fill=MOCK["primary_dark"])
    fy += 30
    row1 = ["Edad", "Estatura (cm)", "Peso (kg)"]
    x = 370
    for lab in row1:
        d.text((x, fy), lab, font=F(13, True), fill=MOCK["text"])
        card(d, (x, fy + 24, x + 150, fy + 70), radius=12, fill=(248, 250, 249),
             outline=MOCK["border"], do_shadow=False)
        d.text((x + 16, fy + 36), "—", font=F(14), fill=MOCK["muted"])
        x += 176
    d.text((x, fy), "Objetivo", font=F(13, True), fill=MOCK["text"])
    card(d, (x, fy + 24, x + 160, fy + 70), radius=12, fill=(248, 250, 249),
         outline=MOCK["border"], do_shadow=False)
    d.text((x + 16, fy + 36), "Perder peso ▾", font=F(14), fill=MOCK["muted"])
    fy += 110
    d.rounded_rectangle([370, fy, 870, fy + 60], radius=14, fill=MOCK["primary"])
    center_text(d, 620, fy + 17, "Crear cuenta", F(16, True), (255, 255, 255))
    fy += 82
    d.text((370, fy), "¿Ya tienes cuenta? ", font=F(13), fill=MOCK["muted"])
    d.text((370 + d.textlength("¿Ya tienes cuenta? ", font=F(13)), fy),
           "Inicia sesión", font=F(13, True), fill=MOCK["primary"])
    fy += 30
    twrap(d, (370, fy), "Al registrarte aceptas los términos y la política de privacidad. "
                        "Tus datos están protegidos con cifrado de extremo a extremo.",
          F(12), MOCK["muted"], 500)
    footer(d, "mock")
    return img


def mock_perfil():
    img = Image.new("RGB", (W, H), MOCK["bg"])
    d = ImageDraw.Draw(img)
    nav(d, "mock", active="Mi salud")
    section_title(d, "mock", 80, 140, "Mi perfil de salud")
    # left card
    card(d, (80, 210, 440, 560), radius=20)
    d.ellipse([230, 260, 330, 360], fill=MOCK["primary_soft"])
    icon_user(d, 280, 315, 40, MOCK["primary"])
    center_text(d, 260, 380, "Laura Gómez", F(20, True), MOCK["text"])
    center_text(d, 260, 412, "laura.gomez@email.com", F(14), MOCK["muted"])
    d.rounded_rectangle([170, 450, 350, 500], radius=14, outline=MOCK["primary"], width=2)
    center_text(d, 260, 462, "Editar perfil", F(15, True), MOCK["primary"])
    # metrics
    d.text((500, 210), "Datos de salud", font=F(20, True), fill=MOCK["text"])
    metrics = [("Edad", "28 años"), ("Estatura", "165 cm"), ("Peso", "62 kg"),
               ("IMC", "22.8 · Saludable")]
    for i, (k, v) in enumerate(metrics):
        x = 500 + (i % 2) * 330
        y = 250 + (i // 2) * 150
        card(d, (x, y, x + 290, y + 120), radius=18)
        d.text((x + 22, y + 22), k, font=F(13, True), fill=MOCK["muted"])
        d.text((x + 22, y + 52), v, font=F(24, True), fill=MOCK["primary_dark"])
    # objetivo
    card(d, (500, 560, 1160, 620), radius=18, fill=MOCK["accent_soft"], do_shadow=False)
    d.text((524, 578), "Objetivo actual: ", font=F(15, True), fill=MOCK["text"])
    d.text((524 + d.textlength("Objetivo actual: ", font=F(15, True)), 578),
           "Mejorar energía y condición física", font=F(15, True), fill=MOCK["accent"])
    # preferencias
    section_title(d, "mock", 80, 680, "Preferencias y restricciones")
    card(d, (80, 750, 1160, 1080), radius=20)
    prefs = [
        ("Dieta vegetariana", True),
        ("Sin gluten", True),
        ("Baja en azúcar", False),
        ("Alergia a frutos secos", True),
    ]
    for i, (p, on) in enumerate(prefs):
        y = 790 + i * 70
        d.text((110, y + 6), p, font=F(16), fill=MOCK["text"])
        tw = 360
        draw_switch(d, 1000, y, on)
    d.rounded_rectangle([820, 1120, 1160, 1180], radius=14, fill=MOCK["primary"])
    center_text(d, 990, 1136, "Guardar cambios", F(16, True), (255, 255, 255))
    footer(d, "mock")
    return img


def draw_switch(draw, x, y, on):
    w, h = 60, 32
    col = MOCK["primary"] if on else (203, 209, 216)
    draw.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=col)
    cx = x + w - 16 if on else x + 16
    draw.ellipse([cx - 12, y + 4, cx + 12, y + h - 4], fill=(255, 255, 255))


def mock_busqueda():
    img = Image.new("RGB", (W, H), MOCK["bg"])
    d = ImageDraw.Draw(img)
    nav(d, "mock")
    d.text((80, 130), "Búsqueda y filtrado", font=F(30, True), fill=MOCK["text"])
    # search
    card(d, (80, 185, 1160, 245), radius=18)
    icon_search(d, 112, 215, 22, MOCK["primary"])
    d.text((142, 203), "Ensalada", font=F(16), fill=MOCK["text"])
    d.rounded_rectangle([1050, 198, 1130, 232], radius=10, fill=MOCK["primary"])
    center_text(d, 1090, 204, "Buscar", F(14, True), (255, 255, 255))
    # filters
    filters = ["Categoría: Alimentación ▾", "Duración: Cualquiera ▾",
               "Dificultad: Fácil ▾", "Ordenar: Mejor valorados ▾"]
    x = 80
    for f_ in filters:
        w_ = int(d.textlength(f_, font=F(14))) + 30
        d.rounded_rectangle([x, 270, x + w_, 316], radius=14, fill=(255, 255, 255),
                            outline=MOCK["border"])
        d.text((x + 15, 286), f_, font=F(14), fill=MOCK["text"])
        x += w_ + 20
    # chips
    d.rounded_rectangle([80, 340, 210, 380], radius=16, fill=MOCK["primary_soft"])
    d.text((100, 350), "Alimentación  ✕", font=F(13, True), fill=MOCK["primary"])
    d.rounded_rectangle([226, 340, 320, 380], radius=16, fill=MOCK["primary_soft"])
    d.text((246, 350), "Fácil  ✕", font=F(13, True), fill=MOCK["primary"])
    d.text((80, 410), "6 resultados encontrados", font=F(14), fill=MOCK["muted"])
    # results
    results = [
        ("Ensalada mediterránea rica en fibra", "Fácil", "5 min", "4.9", (46, 125, 50)),
        ("Ensalada César saludable", "Fácil", "10 min", "4.7", (99, 160, 80)),
        ("Bowl de quinoa y vegetales", "Media", "15 min", "4.8", (245, 160, 40)),
    ]
    for i, (t, dif, dur, sc, col) in enumerate(results):
        y = 450 + i * 220
        card(d, (80, y, 1160, y + 180), radius=18)
        image_placeholder(d, "mock", (104, y + 20, 264, y + 160), color=col)
        tag_chip(d, 104, y + 26, "Alimentación", MOCK["primary"])
        d.text((300, y + 30), t, font=F(18, True), fill=MOCK["text"])
        d.text((300, y + 66), f"{dif} · {dur}", font=F(14), fill=MOCK["muted"])
        rating(d, 300, y + 96)
        d.text((375, y + 98), sc, font=F(14, True), fill=MOCK["text"])
        d.text((300, y + 132), "Rica en fibra, vitaminas y grasas saludables.",
               font=F(13), fill=MOCK["muted"])
        d.rounded_rectangle([1030, y + 60, 1100, y + 122], radius=14,
                            outline=MOCK["border"], width=2)
        icon_heart(d, 1065, y + 91, 24, MOCK["primary"])
    footer(d, "mock")
    return img


def mock_detalle():
    img = Image.new("RGB", (W, H), MOCK["bg"])
    d = ImageDraw.Draw(img)
    nav(d, "mock")
    d.text((80, 120), "Inicio  ›  Alimentación  ›  Ensalada mediterránea",
           font=F(13), fill=MOCK["muted"])
    # main image
    card(d, (80, 150, 740, 520), radius=18)
    image_placeholder(d, "mock", (80, 150, 740, 520), color=MOCK["primary_light"])
    tag_chip(d, 104, 176, "Alimentación", MOCK["primary"])
    icon_heart(d, 690, 180, 30, (255, 255, 255))
    d.text((120, 430), "Ensalada mediterránea", font=F(28, True), fill=(255, 255, 255))
    # title + meta
    d.text((80, 560), "Ensalada mediterránea rica en fibra", font=F(28, True),
           fill=MOCK["primary_dark"])
    rating(d, 80, 600)
    d.text((160, 602), "4.9  (128 valoraciones)", font=F(14), fill=MOCK["muted"])
    tag_chip(d, 80, 640, "Fácil · 5 min", MOCK["accent"])
    tag_chip(d, 210, 640, "Vegetariana", MOCK["primary"])
    twrap(d, (80, 690), "Una combinación fresca de vegetales de temporada, aceite de oliva "
                        "extra virgen, queso feta y hierbas aromáticas. Ideal para una comida "
                        "ligera, nutritiva y llena de sabor.",
          F(16), MOCK["text"], 640)
    d.text((80, 790), "Beneficios", font=F(18, True), fill=MOCK["text"])
    bens = ["Alta en fibra", "Fuente de vitaminas A y C", "Baja en calorías"]
    by = 826
    for b in bens:
        icon_check(d, 80, by, 16, MOCK["primary"])
        d.text((112, by - 4), b, font=F(15), fill=MOCK["text"])
        by += 36
    # buttons
    d.rounded_rectangle([80, 960, 360, 1020], radius=14, fill=MOCK["primary"])
    icon_heart(d, 150, 990, 20, (255, 255, 255))
    d.text((190, 978), "Guardar en favoritos", font=F(15, True), fill=(255, 255, 255))
    d.rounded_rectangle([380, 960, 660, 1020], radius=14, outline=MOCK["primary"], width=2)
    icon_check(d, 460, 990, 18, MOCK["primary"])
    d.text((492, 978), "Marcar como completado", font=F(15, True), fill=MOCK["primary"])
    # side info card
    card(d, (780, 150, 1160, 520), radius=18)
    d.text((812, 180), "Información nutricional", font=F(18, True), fill=MOCK["text"])
    rows = [("Calorías", "320 kcal"), ("Proteínas", "9 g"), ("Carbohidratos", "18 g"),
            ("Grasas", "22 g")]
    ry = 230
    for k, v in rows:
        d.text((812, ry), k, font=F(15), fill=MOCK["muted"])
        d.text((1070, ry), v, font=F(15, True), fill=MOCK["text"])
        d.line([812, ry + 28, 1128, ry + 28], fill=MOCK["border"], width=1)
        ry += 48
    d.text((812, 440), "Porción: 1 plato (250 g)", font=F(13), fill=MOCK["muted"])
    # relacionadas
    section_title(d, "mock", 80, 1080, "Recomendaciones relacionadas")
    rels = [("Bowl de quinoa", "Alimentación", (245, 160, 40)),
            ("Sopa de verduras", "Alimentación", (99, 160, 80)),
            ("Ensalada de garbanzos", "Alimentación", (46, 125, 50))]
    for i, (t, cat, col) in enumerate(rels):
        x = 80 + i * 380
        card(d, (x, 1140, x + 340, 1420), radius=18)
        image_placeholder(d, "mock", (x + 16, 1156, x + 324, 1280), color=col)
        d.text((x + 16, 1300), t, font=F(16, True), fill=MOCK["text"])
        d.text((x + 16, 1332), cat, font=F(13), fill=MOCK["muted"])
        d.text((x + 16, 1378), "Ver →", font=F(14, True), fill=MOCK["primary"])
    footer(d, "mock")
    return img


def mock_favoritos():
    img = Image.new("RGB", (W, H), MOCK["bg"])
    d = ImageDraw.Draw(img)
    nav(d, "mock", active="Favoritos")
    section_title(d, "mock", 80, 140, "Mis favoritos")
    favs = [("Ensalada mediterránea", "Alimentación", (46, 125, 50)),
            ("Rutina HIIT de 20 min", "Actividad física", (245, 124, 0)),
            ("Meditación para dormir", "Descanso", (57, 110, 176))]
    for i, (t, cat, col) in enumerate(favs):
        x = 80 + i * 380
        card(d, (x, 210, x + 340, 560), radius=18)
        image_placeholder(d, "mock", (x + 16, 226, x + 324, 370), color=col)
        tag_chip(d, x + 16, 250, cat, col)
        d.text((x + 16, 390), t, font=F(17, True), fill=MOCK["text"])
        d.text((x + 16, 424), "Guardado · 4.9 ★", font=F(13), fill=MOCK["muted"])
        d.rounded_rectangle([x + 16, 452, x + 220, 500], radius=12,
                            outline=MOCK["border"], width=2)
        d.text((x + 34, 464), "Ver detalle", font=F(14, True), fill=MOCK["primary"])
        icon_heart(d, x + 300, 500, 24, MOCK["primary"])
    # habitos
    section_title(d, "mock", 80, 620, "Seguimiento de hábitos")
    card(d, (80, 690, 1160, 1090), radius=20)
    d.rounded_rectangle([80, 690, 340, 740], radius=20, fill=MOCK["accent"])
    icon_bolt(d, 130, 715, 20, (255, 255, 255))
    d.text((160, 702), "Racha actual: 12 días", font=F(16, True), fill=(255, 255, 255))
    habits = [
        ("Beber 2 litros de agua", "6 de 8 vasos", 0.75),
        ("Caminar 8.000 pasos", "5.240 pasos", 0.65),
        ("Dormir 8 horas", "7.2 horas", 0.90),
        ("Meditar 10 minutos", "4 de 7 días", 0.57),
    ]
    for i, (h, sub, prog) in enumerate(habits):
        y = 780 + i * 95
        d.text((110, y), h, font=F(16, True), fill=MOCK["text"])
        d.text((110, y + 26), sub, font=F(13), fill=MOCK["muted"])
        # progress bar
        bx, bw, bh = 620, 380, 14
        d.rounded_rectangle([bx, y + 18, bx + bw, y + 18 + bh], radius=7,
                            fill=(234, 238, 242))
        d.rounded_rectangle([bx, y + 18, bx + int(bw * prog), y + 18 + bh], radius=7,
                            fill=MOCK["primary"])
        # check circle
        cx, cy = 1090, y + 22
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], outline=MOCK["primary"], width=3)
        if prog >= 0.9:
            d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=MOCK["primary"])
            icon_check(d, cx - 9, cy - 9, 18, (255, 255, 255), width=4)
        else:
            icon_check(d, cx - 9, cy - 9, 18, MOCK["primary"], width=4)
    footer(d, "mock")
    return img


WIRE_FNS = [wire_inicio, wire_registro, wire_perfil, wire_busqueda, wire_detalle, wire_favoritos]
MOCK_FNS = [mock_inicio, mock_registro, mock_perfil, mock_busqueda, mock_detalle, mock_favoritos]
NAMES = ["01_inicio", "02_registro_login", "03_perfil_salud", "04_busqueda_filtrado",
         "05_detalle_recomendacion", "06_favoritos_habitos"]

for fn, name in zip(WIRE_FNS, NAMES):
    fn().save(os.path.join(WIRE_DIR, name + ".png"))
    print("wire", name)

for fn, name in zip(MOCK_FNS, NAMES):
    fn().save(os.path.join(MOCK_DIR, name + ".png"))
    print("mock", name)

print("LISTO")
