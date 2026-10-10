"""Generates flat landmark illustrations (SVG, 160x100) for each country -> assets/countries/<code>.svg
Run:  python tools/make_country_art.py          (re-generates all SVGs)
To use a real photo instead, drop <code>.jpg / .png / .webp into assets/countries/ (it wins over the SVG)."""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "countries")


def R(x, y, w, h, f, rx=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"/>'
def P(pts, f): return f'<polygon points="{pts}" fill="{f}"/>'
def C(x, y, r, f): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}"/>'
def E(x, y, rx, ry, f): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{f}"/>'
def PA(d, f, extra=""): return f'<path d="{d}" fill="{f}" {extra}/>'
def L(x1, y1, x2, y2, c, w=1): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'


def hex2rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def mix(a, b, t):
    A, B = hex2rgb(a), hex2rgb(b)
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * t) for i in range(3))


# ------------------------------------------------------------------ landmarks (ground line y=80)
def eiffel(sk, g):
    c, l = "#4a3b5f", "#8b73b3"
    return (PA("M80 10 L84 38 L93 58 L104 80 L91 80 Q80 56 69 80 L56 80 L67 58 L76 38 Z", c)
            + R(72, 37, 16, 3, l) + R(64, 57, 32, 3, l) + L(80, 10, 80, 3, c, 1.2)
            + L(73, 40, 87, 57, l, .8) + L(87, 40, 73, 57, l, .8))


def bigben(sk, g):
    c, d = "#9a7b4f", "#5e4a2e"
    return (R(34, 62, 62, 18, "#b59468") + R(64, 24, 18, 56, c) + P("62,24 73,4 84,24", d) + R(61, 22, 24, 3, d)
            + C(73, 36, 6, "#fff7dc") + L(73, 36, 73, 32, d) + L(73, 36, 76, 38, d)
            + R(70, 48, 6, 10, d, 1) + R(70, 62, 6, 10, d, 1)
            + R(98, 56, 36, 24, "#b59468") + P("98,56 106,46 114,56", d) + P("118,56 126,48 134,56", d))


def liberty(sk, g):
    c, d = "#5fb59b", "#3f8f78"
    spikes = "".join(L(80, 31, 80 + 10 * math.cos(math.radians(a)), 31 - 10 * math.sin(math.radians(a)), c, 1.6)
                     for a in (30, 60, 90, 120, 150))
    return (E(80, 81, 52, 6, "#7a8f6a") + R(60, 70, 40, 11, "#9aa3ad") + R(66, 56, 28, 15, "#b9c1ca")
            + P("70,56 90,56 86,36 74,36", c) + C(80, 31, 5, c) + spikes + L(86, 38, 95, 18, c, 3.4)
            + R(93, 11, 4, 7, "#f5c542") + P("92,11 98,11 95,3", "#ff9f1c") + R(68, 40, 6, 9, d))


def cntower(sk, g):
    leaf = P("128,18 130,24 135,22 133,28 137,30 131,31 131,36 128,34 125,36 125,31 119,30 123,28 121,22 126,24", "#e0393e")
    return (leaf + P("79,4 81,4 84,80 76,80", "#aeb8c4") + E(80, 44, 10, 4.6, "#8a96a6") + E(80, 41, 6.5, 3, "#d5dde6")
            + R(78, 48, 4, 7, "#8a96a6") + R(30, 64, 12, 16, "#6b7a8c") + R(44, 56, 10, 24, "#7d8b9c")
            + R(106, 60, 12, 20, "#6b7a8c") + R(120, 68, 14, 12, "#7d8b9c"))


def opera(sk, g):
    w, w2 = "#fbfbf6", "#e3e0d2"
    return (R(28, 76, 104, 5, "#d9cbaa") + PA("M34 78 Q42 34 74 42 L74 78 Z", w) + PA("M56 78 Q62 24 98 34 L98 78 Z", w2)
            + PA("M82 78 Q90 38 122 52 L122 78 Z", w) + PA("M100 78 Q106 54 130 60 L130 78 Z", w2))


def brandenburg(sk, g):
    c, d = "#d8c9a3", "#a8956a"
    cols = "".join(R(42 + 14 * i, 42, 7, 38, c) for i in range(6))
    return (R(34, 80, 92, 3, d) + R(36, 36, 88, 6, d) + R(70, 28, 20, 8, c) + P("72,28 80,18 88,28", c)
            + C(76, 22, 2.2, d) + C(84, 22, 2.2, d) + cols + R(38, 42, 4, 38, d) + R(118, 42, 4, 38, d))


def colosseum(sk, g):
    out = P("20,80 26,34 134,34 140,80", "#d6b88c")
    for y in (38, 52, 66):
        for x in range(28, 132, 9):
            out += PA(f"M{x} {y + 10} v-5 a3.2 3.2 0 0 1 6.4 0 v5 z", "#9b7a4e")
    out += P("106,34 140,34 140,66 122,54", sk(50))
    return out


def sagrada(sk, g):
    c, d = "#cfae74", "#8a6a3c"
    out = R(28, 64, 104, 16, c)
    for x, t in zip((32, 46, 60, 74, 88, 102, 116), (46, 34, 22, 8, 22, 34, 46)):
        out += P(f"{x},80 {x + 10},80 {x + 9},{t + 14} {x + 5},{t} {x + 1},{t + 14}", c) + C(x + 5, t - 2, 2, "#e8b84a") + L(x + 5, t + 8, x + 5, 74, d, .8)
    return out


def windmill(sk, g):
    cols = ["#e84a5f", "#f9c74f", "#f28ab2", "#e84a5f", "#f9c74f", "#f28ab2", "#e84a5f", "#f9c74f"]
    out = "".join(R(i * 20, 80, 20, 20, col) for i, col in enumerate(cols))
    out += P("66,80 94,80 88,44 72,44", "#f2ede3") + P("69,44 91,44 80,31", "#a0522d") + R(76, 68, 8, 12, "#6b4f3a", 2)
    out += "".join(f'<g transform="rotate({a} 80 40)"><rect x="79" y="8" width="2.4" height="32" fill="#6b4f3a"/>'
                   f'<rect x="81.4" y="10" width="8" height="15" fill="#fffdf5" opacity=".95"/></g>' for a in (20, 110, 200, 290))
    return out + C(80, 40, 2.6, "#6b4f3a")


def matterhorn(sk, g):
    return (P("0,80 30,48 62,80", "#9fb3c8") + P("34,80 80,10 128,80", "#6c7f96") + P("80,10 128,80 100,80 84,38", "#4d5d72")
            + P("80,10 68,34 75,30 80,38 86,30 92,34", "#ffffff") + R(124, 18, 14, 14, "#d52b1e") + R(129, 20, 4, 10, "#fff") + R(126, 23, 10, 4, "#fff"))


def nyhavn(sk, g):
    cols = ["#e8575a", "#f4c95d", "#5aa9e6", "#f2a65a", "#7bc67e", "#e8575a", "#f2e394"]
    out = ""
    for i, col in enumerate(cols):
        x, h = 8 + i * 21, 30 + (i % 3) * 8
        out += R(x, 80 - h, 18, h, col) + P(f"{x - 1},{80 - h} {x + 9},{80 - h - 10} {x + 19},{80 - h}", "#8a5a44")
        for wx in (x + 3, x + 11):
            for wy in (80 - h + 6, 80 - h + 18):
                out += R(wx, wy, 4, 5, "#fff8e1")
    return out + L(20, 96, 20, 82, "#5a4630", 1.4) + P("20,84 32,92 8,92", "#fff")


def stockholm(sk, g):
    c = "#b5523b"
    return (R(30, 56, 62, 24, c) + R(94, 62, 36, 18, "#c4634c") + R(70, 26, 15, 54, c) + R(68, 24, 19, 3, "#8a3d2b")
            + P("70,24 77.5,10 85,24", "#4f9a82") + C(77.5, 8, 2, "#f5c542") + R(36, 62, 5, 8, "#f4e3b0") + R(48, 62, 5, 8, "#f4e3b0") + R(60, 62, 5, 8, "#f4e3b0"))


def fjord(sk, g):
    return (P("0,80 16,26 54,62 74,80", "#46627d") + P("160,80 142,18 100,62 82,80", "#5c7d99") + P("16,26 8,44 15,40 20,46 24,38 28,42", "#fff")
            + P("142,18 134,38 141,33 146,40 150,32 152,40", "#fff") + R(86, 70, 12, 9, "#c0392b") + P("85,70 92,62 99,70", "#6b3a2a")
            + P("40,86 64,86 58,92 46,92", "#7a4b2a") + L(52, 86, 52, 76, "#7a4b2a", 1.2) + P("52,76 62,84 52,84", "#f5f1e6"))


def helsinki(sk, g):
    w = "#f4f1ea"
    return (R(30, 82, 100, 3, "#d5d0c5") + R(36, 76, 88, 4, "#e5e0d5") + R(44, 52, 72, 24, w) + P("44,52 80,44 116,52", "#e5e0d5")
            + PA("M62 46 A18 18 0 0 1 98 46 Z", "#4fa58d") + R(77, 22, 6, 6, "#4fa58d") + C(80, 20, 2.4, "#f5c542") + R(78, 26, 4, 8, w)
            + PA("M46 52 A6 6 0 0 1 58 52 Z", "#4fa58d") + PA("M102 52 A6 6 0 0 1 114 52 Z", "#4fa58d")
            + "".join(R(50 + 11 * i, 56, 4, 20, "#d0cabd") for i in range(6)))


def vienna(sk, g):
    c = "#d6cbb5"
    zig = "".join(P(f"{44 + 8 * i},66 {48 + 8 * i},52 {52 + 8 * i},66", "#d2a14f" if i % 2 else "#4f8f8a") for i in range(9))
    return (R(44, 62, 72, 18, c) + zig + P("80,2 84,26 89,62 71,62 76,26", c) + L(80, 2, 80, -2, c, 1)
            + R(106, 38, 9, 26, c) + P("105,38 110,22 116,38", "#8a8070") + R(77, 36, 3, 7, "#8a8070") + R(77, 48, 3, 7, "#8a8070"))


def atomium(sk, g):
    pts = [(80, 16), (56, 32), (104, 32), (80, 46), (56, 62), (104, 62), (80, 76)]
    lines = [(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (2, 5), (3, 4), (3, 5), (4, 6), (5, 6), (1, 2), (4, 5), (3, 6), (0, 3)]
    out = "".join(L(*pts[a], *pts[b], "#9aa6b5", 2.6) for a, b in lines)
    for x, y in pts:
        out += C(x, y, 7, "#c4ccd6") + C(x - 2, y - 2, 2.4, "#f5f7fa")
    return out + L(80, 76, 80, 80, "#9aa6b5", 3)


def moher(sk, g):
    return (P("0,28 74,28 88,80 0,80", "#7b6f5c") + P("0,28 74,28 76,35 0,36", "#4f9a4b")
            + "".join(L(8 + 14 * i, 38, 14 + 14 * i, 80, "#5d5444", 1) for i in range(5))
            + R(40, 12, 7, 17, "#8a8a80") + P("39,12 43.5,3 48,12", "#6d6d66") + R(42, 16, 3, 4, "#333"))


def fuji(sk, g):
    pag = ""
    for i in range(4):
        w = 24 - i * 4
        pag += R(36 - w / 2 + 12 - 12, 72 - i * 11, w, 7, "#c0392b") + P(f"{36 - w / 2 - 4},{72 - i * 11} {36},{72 - i * 11 - 7} {36 + w / 2 + 4},{72 - i * 11}", "#3f3f46")
    return (P("22,80 80,18 142,80", "#5b6fa8") + P("80,18 64,40 73,35 80,44 88,35 97,40", "#ffffff") + C(124, 26, 9, "#e63946")
            + R(10, 78, 40, 3, "#3f3f46") + pag + L(36, 40, 36, 33, "#3f3f46", 1.4))


def heaven(sk, g):
    return (R(44, 72, 72, 8, "#efe8d8") + R(52, 68, 56, 5, "#efe8d8") + R(70, 60, 20, 9, "#c0392b")
            + E(80, 56, 20, 4.5, "#2f6fb0") + R(72, 48, 16, 8, "#c0392b") + E(80, 46, 14, 4, "#2f6fb0")
            + R(75, 38, 10, 8, "#c0392b") + E(80, 36, 9, 3.4, "#2f6fb0") + P("80,22 84,34 76,34", "#2f6fb0") + C(80, 21, 2, "#f5c542"))


def seoul(sk, g):
    return (E(80, 82, 60, 12, "#4f7f5f") + R(79, 26, 2.4, 50, "#cfd6df") + E(80, 46, 9, 4, "#9fb0c4") + E(80, 43, 6, 2.6, "#e2e8f0")
            + R(76, 18, 8, 9, "#e2e8f0") + L(80, 18, 80, 8, "#cfd6df", 1.2) + R(72, 70, 16, 8, "#9fb0c4"))


def taipei(sk, g):
    out = ""
    for i in range(8):
        y = 72 - i * 7.2
        w = 11 + (i % 2) * 2 + (0 if i < 7 else -4)
        out += P(f"{80 - w / 2},{y} {80 + w / 2},{y} {80 + w / 2 + 2.5},{y - 7.2} {80 - w / 2 - 2.5},{y - 7.2}", "#3f8f7a" if i % 2 == 0 else "#5fb59b")
    return R(72, 72, 16, 8, "#2f6f5f") + out + P("78,12 82,12 80.6,4 79.4,4", "#2f6f5f")


def marina(sk, g):
    out = ""
    for x, dx in ((50, 4), (78, 0), (106, -4)):
        out += P(f"{x},80 {x + 14},80 {x + 14 + dx},26 {x + dx},26", "#e8eef5")
        out += L(x + 7, 80, x + 7 + dx, 26, "#b7c4d4", 1)
    return out + PA("M38 24 H122 L112 30 H48 Z", "#cfd8e3") + R(96, 22, 14, 2, "#4fa58d") + C(100, 19, 3, "#4fa58d")


def petronas(sk, g):
    out = ""
    for x in (56, 90):
        out += R(x, 40, 16, 40, "#c4ccd6") + P(f"{x},40 {x + 16},40 {x + 12},26 {x + 4},26", "#aab4c2") + P(f"{x + 4},26 {x + 12},26 {x + 8},12", "#c4ccd6") + L(x + 8, 12, x + 8, 3, "#aab4c2", 1.2)
        out += "".join(L(x, 44 + 7 * i, x + 16, 44 + 7 * i, "#8f9bab", .8) for i in range(5))
    return out + R(72, 54, 18, 3, "#8f9bab") + R(30, 66, 12, 14, "#8f9bab") + R(120, 62, 14, 18, "#8f9bab")


def hagia(sk, g):
    c, d = "#d8b58c", "#a67c52"
    mins = "".join(R(x, 30, 4, 50, "#e5d3b8") + P(f"{x - 1},30 {x + 2},18 {x + 5},30", "#7a8a96") for x in (34, 122))
    return (mins + R(46, 54, 68, 26, c) + PA("M52 54 A28 28 0 0 1 108 54 Z", d) + PA("M42 66 A12 12 0 0 1 66 66 Z", d)
            + PA("M94 66 A12 12 0 0 1 118 66 Z", d) + R(66, 62, 28, 18, "#c79d6b")
            + "".join(R(58 + 8 * i, 44, 3, 6, "#6b4f3a") for i in range(5)))


def budapest(sk, g):
    c = "#e8e0d0"
    out = R(26, 58, 108, 22, c)
    for x in range(30, 130, 8):
        out += P(f"{x},58 {x + 4},50 {x + 8},58", "#cfc7b6")
    return out + R(70, 38, 20, 20, c) + PA("M68 38 Q80 6 92 38 Z", "#5f8f9f") + L(80, 12, 80, 2, "#5f8f9f", 1.2) \
        + R(36, 44, 8, 14, c) + P("35,44 40,32 45,44", "#5f8f9f") + R(116, 44, 8, 14, c) + P("115,44 120,32 125,44", "#5f8f9f")


def warsaw(sk, g):
    c = "#b9a98e"
    return (R(54, 56, 52, 24, c) + R(66, 44, 28, 14, "#c7b89d") + R(72, 32, 16, 14, c) + R(76, 22, 8, 12, "#c7b89d")
            + P("76,22 80,8 84,22", "#8a7f6b") + L(80, 8, 80, 1, "#8a7f6b", 1) + R(44, 62, 10, 18, "#c7b89d") + P("43,62 49,52 55,62", "#8a7f6b")
            + R(106, 62, 10, 18, "#c7b89d") + P("105,62 111,52 117,62", "#8a7f6b"))


def prague(sk, g):
    c = "#a89f8f"
    arches = "".join(PA(f"M{28 + 22 * i} 80 Q{39 + 22 * i} 66 {50 + 22 * i} 80", sk(82)) for i in range(5))
    return (R(24, 72, 112, 8, c) + arches + R(48, 38, 12, 34, "#cfc6b4") + P("46,38 54,10 62,38", "#6e8f86") + R(66, 42, 12, 30, "#cfc6b4")
            + P("64,42 72,16 80,42", "#6e8f86") + R(84, 54, 40, 18, "#cfc6b4") + P("84,54 104,44 124,54", "#b25a4a"))


def skytower(sk, g):
    return (P("0,80 22,42 46,66 62,80", "#4f7a6a") + P("160,80 138,36 112,62 98,80", "#6a9a86") + P("79,10 81,10 83,80 77,80", "#9fb0c0")
            + E(80, 40, 10, 5, "#7e92a6") + E(80, 36, 6, 3, "#cfd8e3") + R(79, 18, 2, 14, "#7e92a6") + L(80, 10, 80, 2, "#7e92a6", 1))


def burj(sk, g):
    out = ""
    for w, y in ((16, 62), (13, 52), (10, 42), (8, 32), (6, 24), (4, 17)):
        out += R(80 - w / 2, y, w, 80 - y, "#b7c3d1")
    return (out + L(80, 17, 80, 4, "#9fb0c0", 1.4) + R(30, 66, 10, 14, "#9fb0c0") + R(44, 58, 9, 22, "#8da0b4")
            + R(110, 60, 10, 20, "#8da0b4") + R(124, 68, 12, 12, "#9fb0c0"))


def kingdom(sk, g):
    body = PA("M62 80 V26 Q80 12 98 26 V80 Z M72 36 Q80 74 88 36 Q80 26 72 36 Z", "#b9c4cf", 'fill-rule="evenodd"')
    return body + L(80, 14, 80, 4, "#9fb0c0", 1.4) + R(34, 64, 12, 16, "#9fb0c0") + R(114, 60, 12, 20, "#9fb0c0")


def skyline(sk, g):
    out = ""
    for x, w, h, col in ((16, 14, 32, "#9fb0c0"), (32, 12, 46, "#b7c3d1"), (46, 10, 26, "#8da0b4"), (58, 14, 58, "#c4ccd6"),
                         (74, 12, 36, "#9fb0c0"), (88, 16, 50, "#b7c3d1"), (106, 12, 30, "#8da0b4"), (120, 14, 40, "#9fb0c0")):
        out += R(x, 80 - h, w, h, col)
    return out + P("58,22 72,22 65,10", "#c4ccd6")


def basil(sk, g):
    out = R(46, 56, 68, 24, "#b5483a") + "".join(R(46, 62 + 8 * i, 68, 2, "#f2e8d8") for i in range(3))
    out += R(74, 26, 12, 32, "#e8dcc8") + P("73,26 80,6 87,26", "#c0392b")
    for x, y, col in ((54, 46, "#2f9e8f"), (66, 40, "#e0a526"), (94, 40, "#2f6fb0"), (106, 46, "#c0392b")):
        out += R(x - 4, y, 8, 12, "#e8dcc8") + E(x, y, 6, 6, col) + P(f"{x - 2},{y - 4} {x},{y - 12} {x + 2},{y - 4}", col) + C(x, y - 13, 1.2, "#f5c542")
    return out + C(80, 5, 1.6, "#f5c542")


def taj(sk, g):
    w, w2 = "#fbf6ee", "#e9dfce"
    mins = "".join(R(x, 40, 5, 40, w2) + R(x - 1, 38, 7, 3, w) + E(x + 2.5, 36, 3.2, 3.2, w) for x in (28, 127))
    return (mins + R(46, 62, 68, 18, w) + R(60, 44, 40, 20, w) + PA("M60 44 Q80 -6 100 44 Z", w) + L(80, 8, 80, 1, "#d8c27a", 1.2)
            + PA("M72 80 V62 a8 8 0 0 1 16 0 V80 Z", "#a9a08e") + PA("M46 62 Q52 50 58 62 Z", w) + PA("M102 62 Q108 50 114 62 Z", w))


def pyramids(sk, g):
    return (P("10,80 50,40 96,80", "#d9b36a") + P("50,40 96,80 70,80", "#b98f44") + P("56,80 108,22 156,80", "#e3c27e")
            + P("108,22 156,80 128,80 112,40", "#c19a52") + P("96,80 124,56 150,80", "#cfa965"))


def christ(sk, g):
    robe = "#f3f3ee"
    return (P("20,80 62,54 80,48 98,54 140,80", "#3f7a52") + P("40,80 80,40 120,80", "#4d8f63") + R(78, 12, 4, 30, robe) + R(62, 18, 36, 4.5, robe)
            + C(80, 10, 3.4, robe) + P("76,22 84,22 87,40 73,40", robe) + R(72, 40, 16, 6, "#b7bfc7"))


def chichen(sk, g):
    out = ""
    for i, w in enumerate((70, 60, 50, 40, 30, 20)):
        y = 80 - (i + 1) * 8
        out += R(80 - w / 2, y, w, 8, "#cdbf9f" if i % 2 == 0 else "#b8a985")
    return out + R(74, 78 - 6 * 8 - 10, 12, 10, "#cdbf9f") + R(77, 20, 6, 9, "#6b5d45") + R(76, 50, 8, 30, "#e0d4b6") + R(10, 70, 22, 10, "#3f7a52") + R(130, 66, 24, 14, "#3f7a52")


def parthenon(sk, g):
    c = "#f3ecde"
    cols = "".join(R(42 + 11.5 * i, 44, 5.5, 28, c) for i in range(8))
    return (P("26,80 36,66 124,66 134,80", "#a8987a") + R(34, 72, 92, 4, "#e6dcc6") + R(36, 68, 88, 4, c) + cols
            + R(38, 40, 84, 5, "#e6dcc6") + P("36,40 80,22 124,40", c) + P("48,38 80,26 112,38", "#d8cbb2"))


def belem(sk, g):
    c = "#e6dcc6"
    cren = "".join(R(52 + 9 * i, 38, 5, 5, c) for i in range(6))
    return (R(34, 82, 92, 4, "#7aa6c4") + R(48, 44, 56, 36, c) + cren + R(52, 28, 22, 16, "#d8cdb2") + R(56, 22, 14, 7, "#c9bda0")
            + PA("M44 44 a5 5 0 0 1 10 0 v6 h-10z", "#c9bda0") + PA("M98 44 a5 5 0 0 1 10 0 v6 h-10z", "#c9bda0")
            + R(60, 52, 6, 10, "#8a7f6b", 3) + R(76, 52, 6, 10, "#8a7f6b", 3) + R(90, 52, 6, 10, "#8a7f6b", 3) + C(63, 34, 4, "#c9bda0"))


def table(sk, g):
    return (P("0,80 22,56 40,50 120,50 146,60 160,80", "#7f9f8f") + P("26,50 44,40 118,40 136,50", "#8fb0a0") + R(26, 49, 110, 3, "#6f8f7f")
            + E(86, 38, 44, 6, "#ffffff") + E(58, 34, 26, 6, "#ffffff") + E(112, 36, 22, 5, "#ffffff") + R(50, 68, 4, 12, "#c0392b") + R(112, 66, 10, 14, "#d9b36a"))


def globe(sk, g):
    return (C(80, 50, 36, "#4a90e2") + PA("M58 36 q8 -10 18 -6 q4 8 -2 12 q-10 4 -14 12 q-8 -4 -2 -18z", "#58b368")
            + PA("M86 52 q12 -4 18 6 q-2 14 -12 18 q-8 -6 -6 -24z", "#58b368") + PA("M76 18 q10 -2 14 4 q-6 6 -14 2z", "#58b368")
            + '<ellipse cx="80" cy="50" rx="14" ry="36" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width=".8"/>'
            + '<ellipse cx="80" cy="50" rx="36" ry="12" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width=".8"/>'
            + '<circle cx="80" cy="50" r="36" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="1.2"/>')


# code: (sky_top, sky_bottom, ground, sun, fn)
SCENES = {
    "fr": ("#7fb2f0", "#fbd7e4", "#3d4a63", "#fff3b0", eiffel), "gb": ("#8fa8c8", "#e9e4dc", "#3b4a5a", None, bigben),
    "us": ("#6aa7ff", "#ffe1c4", "#35506b", "#fff1b8", liberty), "ca": ("#8ec5ff", "#fff0e0", "#2e5a4a", None, cntower),
    "au": ("#57b8ff", "#fff0c9", "#2a6f97", "#ffe27a", opera), "de": ("#8ab6e8", "#f9e3c8", "#3a5a40", "#fff0b0", brandenburg),
    "it": ("#ffb37a", "#ffe7c2", "#6b5b4b", "#fff2c2", colosseum), "es": ("#ff9e6b", "#ffdca8", "#5a4a3f", "#fff0b8", sagrada),
    "nl": ("#7fc4f5", "#e3f4ff", "#5a9e5a", None, windmill), "ch": ("#6aa5e8", "#eaf4ff", "#4a7c59", None, matterhorn),
    "dk": ("#8cc0ee", "#f1e6dc", "#2f5d7c", None, nyhavn), "se": ("#7ab0e6", "#fbe3cf", "#2f5d7c", "#fff0b0", stockholm),
    "no": ("#6a9ed8", "#d8ecf7", "#2f5d7c", None, fjord), "fi": ("#8fb4e0", "#f1ece4", "#4a6c7c", None, helsinki),
    "at": ("#86b3e8", "#f8e6d0", "#4a5a3f", "#fff2b6", vienna), "be": ("#9bbcf2", "#f2e3f0", "#4a5a6a", None, atomium),
    "ie": ("#8dc0e6", "#e9f3e6", "#2f7fa0", None, moher), "jp": ("#ffb5c0", "#fff0e8", "#3a5a6a", "#ffffff", fuji),
    "cn": ("#f4a259", "#fbe8c8", "#4a5a40", "#fff1b8", heaven), "kr": ("#7aa9f0", "#ffe3e3", "#3f5f4a", "#fff0b8", seoul),
    "tw": ("#6ab0f0", "#e5f3ff", "#3a5a4a", "#fff0b8", taipei), "sg": ("#4fa8e8", "#ffe0c8", "#2a6f8a", "#fff0b8", marina),
    "my": ("#5aa8ef", "#ffe4d0", "#3a6a4f", "#fff0b8", petronas), "tr": ("#6aa5e8", "#ffe3c4", "#6a5a4a", "#fff0b8", hagia),
    "hu": ("#8cb0e8", "#f8e3d4", "#4a5a50", "#fff0b8", budapest), "pl": ("#86a8e6", "#f6e0e0", "#4a5a50", None, warsaw),
    "cz": ("#7fa8e8", "#f9e2d0", "#4a5a50", "#fff0b8", prague), "nz": ("#68b0f0", "#e8f6ff", "#3a7a5a", "#fff0b8", skytower),
    "ae": ("#f2a65a", "#ffe9c4", "#c9a46a", "#fff1b8", burj), "sa": ("#f0b060", "#ffe8c0", "#c9a46a", "#fff1b8", kingdom),
    "qa": ("#e9a86a", "#ffe8cc", "#c9a46a", "#fff1b8", skyline), "ru": ("#8aa8e0", "#f4e4ee", "#4a5a6a", None, basil),
    "in": ("#ffb88c", "#ffe7d6", "#6a8a6a", "#fff1b8", taj), "eg": ("#f2a55a", "#ffe8b8", "#d8b878", "#fff1b8", pyramids),
    "br": ("#5ab0f0", "#d8f3e0", "#2f7a4f", "#fff0b8", christ), "mx": ("#5aa8ee", "#ffe4c0", "#2f6a4a", "#fff0b8", chichen),
    "gr": ("#3f8fe0", "#eaf6ff", "#c8b898", "#fff0b8", parthenon), "pt": ("#6aaae8", "#ffe6cc", "#3a6a8a", "#fff0b8", belem),
    "za": ("#5aa8ee", "#ffe8d0", "#3f6a4f", "#fff0b8", table), "globe": ("#d6e6ff", "#f4f8ff", "#d6e6ff", None, globe),
}


def build(code):
    top, bot, ground, sun, fn = SCENES[code]
    sk = lambda y: mix(top, bot, min(max(y / 100, 0), 1))
    clouds = (f'<ellipse cx="30" cy="22" rx="14" ry="4" fill="#fff" opacity=".55"/><ellipse cx="40" cy="19" rx="9" ry="3.4" fill="#fff" opacity=".55"/>'
              f'<ellipse cx="124" cy="14" rx="12" ry="3.4" fill="#fff" opacity=".45"/>') if code != "globe" else ""
    sun_el = f'<circle cx="128" cy="26" r="9" fill="{sun}" opacity=".85"/>' if sun else ""
    gnd = "" if code == "globe" else R(0, 80, 160, 20, ground)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/></linearGradient></defs>'
            f'<rect width="160" height="100" fill="url(#g)"/>{sun_el}{clouds}{gnd}{fn(sk, ground)}</svg>')


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for code in SCENES:
        with open(os.path.join(OUT, f"{code}.svg"), "w", encoding="utf-8") as f:
            f.write(build(code))
    print(f"wrote {len(SCENES)} SVGs to {os.path.normpath(OUT)}")
