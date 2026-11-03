#!/usr/bin/env python3
"""Build letterpress plate files from a layout JSON (TeleportPress 時分印刷 skill).

    python make_plates.py layout.json [--out DIR]
    python make_plates.py --selftest

For every plate (one per ink colour, foil colour, emboss, die line) it writes
<name>-<face>-<plate>.svg, plus a .pdf of it when PyMuPDF is installed: 100% black
filled shapes on an artboard of finished size + bleed, text already turned into
outlines, no strokes, no transparency. It also writes <name>-<face>-preview.svg,
a to-scale colour layout marked "PREVIEW, NOT FOR PRINT" (the reference for any
mockup), and plates.json with each plate's area (版面尺寸, cm) for the order form.

Coordinates are mm from the top-left corner of the trimmed piece; bleed is negative.
Element types (all need "plate": "<plate id>"):
  text    text, font (a .ttf/.otf/.ttc path), size_pt, x_mm, y_mm (baseline),
          optional anchor start|middle|end, tracking (em, e.g. 0.05), weight (variable
          fonts), leading (line height in em, default 1.4; "\\n" starts a new line)
  rect    x_mm, y_mm, w_mm, h_mm, optional stroke_pt (an outline instead of a fill)
  circle  cx_mm, cy_mm, r_mm, optional stroke_pt
  line    x1_mm, y1_mm, x2_mm, y2_mm, width_pt (drawn as a filled bar)
  path    d (SVG path data), optional box [minx, miny, w, h] of that data plus
          x_mm, y_mm, w_mm to place and scale it (no box: d is already in mm)
Needs Python 3.9+; fonttools for text (pip install fonttools); pymupdf for PDF.
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path

PT_MM = 25.4 / 72  # one point in mm
PROCESSES = ("letterpress", "foil", "emboss", "deboss", "dieline")


def fmt(v):
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


# ── shapes → path data (mm) ────────────────────────────────────────────────

def rect_d(x, y, w, h):
    return f"M{fmt(x)} {fmt(y)}H{fmt(x + w)}V{fmt(y + h)}H{fmt(x)}Z"


def circle_d(cx, cy, r):
    return (f"M{fmt(cx - r)} {fmt(cy)}A{fmt(r)} {fmt(r)} 0 1 0 {fmt(cx + r)} {fmt(cy)}"
            f"A{fmt(r)} {fmt(r)} 0 1 0 {fmt(cx - r)} {fmt(cy)}Z")


def bar_d(x1, y1, x2, y2, width):
    """A line of `width` mm as a filled quadrilateral (plates carry no strokes)."""
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy) or 1.0
    ox, oy = -dy / n * width / 2, dx / n * width / 2
    pts = [(x1 + ox, y1 + oy), (x2 + ox, y2 + oy), (x2 - ox, y2 - oy), (x1 - ox, y1 - oy)]
    return "M" + "L".join(f"{fmt(a)} {fmt(b)}" for a, b in pts) + "Z"


_NUM = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
_TOK = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
_ARGS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}


def place_path(d, box, x, y, w):
    """Absolute-coordinate path data `d` (inside `box`) scaled to `w` mm wide at (x, y)."""
    bx, by, bw, _ = box
    s = w / bw
    out, cmd, toks, i = [], None, _TOK.findall(d), 0
    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]
            i += 1
            if cmd in "Zz":
                out.append("Z")
                continue
        if cmd is None or cmd.islower():
            raise ValueError("path: use absolute commands (M L H V C S Q T A Z, upper case) with a box")
        n = _ARGS[cmd]
        a = [float(t) for t in toks[i:i + n]]
        i += n
        if cmd == "H":
            v = [x + (a[0] - bx) * s]
        elif cmd == "V":
            v = [y + (a[0] - by) * s]
        elif cmd == "A":
            v = [a[0] * s, a[1] * s, a[2], a[3], a[4], x + (a[5] - bx) * s, y + (a[6] - by) * s]
        else:
            v = [x + (c - bx) * s if k % 2 == 0 else y + (c - by) * s for k, c in enumerate(a)]
        out.append(cmd + " ".join(fmt(c) for c in v))
        if cmd == "M":
            cmd = "L"
    return "".join(out)


def arc_points(x1, y1, rx, ry, phi, fa, fs, x2, y2, n=24):
    """Points along an SVG elliptical arc (endpoint form, SVG spec F.6.5)."""
    rx, ry = abs(rx), abs(ry)
    if rx == 0 or ry == 0:
        return [(x2, y2)]
    c, s_ = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    xp, yp = c * dx + s_ * dy, -s_ * dx + c * dy
    lam = xp * xp / (rx * rx) + yp * yp / (ry * ry)
    if lam > 1:
        rx, ry = rx * math.sqrt(lam), ry * math.sqrt(lam)
    num = rx * rx * ry * ry - rx * rx * yp * yp - ry * ry * xp * xp
    k = math.sqrt(max(num, 0) / (rx * rx * yp * yp + ry * ry * xp * xp)) * (-1 if fa == fs else 1)
    cxp, cyp = k * rx * yp / ry, -k * ry * xp / rx
    cx, cy = c * cxp - s_ * cyp + (x1 + x2) / 2, s_ * cxp + c * cyp + (y1 + y2) / 2
    ang = lambda ux, uy: math.atan2(uy, ux)
    t1 = ang((xp - cxp) / rx, (yp - cyp) / ry)
    dt = ang((-xp - cxp) / rx, (-yp - cyp) / ry) - t1
    if fs and dt < 0:
        dt += 2 * math.pi
    elif not fs and dt > 0:
        dt -= 2 * math.pi
    return [(cx + rx * math.cos(t1 + dt * i / n) * c - ry * math.sin(t1 + dt * i / n) * s_,
             cy + rx * math.cos(t1 + dt * i / n) * s_ + ry * math.sin(t1 + dt * i / n) * c) for i in range(n + 1)]


def path_bbox(d):
    """Bbox of absolute path data; curves count their control points, arcs are sampled."""
    xs, ys, cur, start = [], [], (0.0, 0.0), (0.0, 0.0)
    for cmd, args in re.findall(r"([MLHVCSQTAZ])([^MLHVCSQTAZ]*)", d):
        a = [float(n) for n in _NUM.findall(args)]
        if cmd == "Z":
            cur = start
            continue
        if cmd in "HV":
            for v in a:
                cur = (v, cur[1]) if cmd == "H" else (cur[0], v)
                xs.append(cur[0]); ys.append(cur[1])
            continue
        if cmd == "A":
            for k in range(0, len(a) - 6, 7):
                for x, y in arc_points(*cur, *a[k:k + 7]):
                    xs.append(x); ys.append(y)
                cur = (a[k + 5], a[k + 6])
            continue
        xs += a[0::2]; ys += a[1::2]
        if len(a) >= 2:
            cur = (a[-2], a[-1])
            if cmd == "M":
                start = (a[0], a[1])
    return (min(xs), min(ys), max(xs), max(ys)) if xs and ys else None


# ── text → outlines ────────────────────────────────────────────────────────

_FONTS = {}


def load_font(path, weight=None):
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        sys.exit("text needs fonttools: pip install fonttools")
    key = (path, weight)
    if key not in _FONTS:
        font = TTFont(path, fontNumber=0) if str(path).lower().endswith((".ttc", ".otc")) else TTFont(path)
        loc = None
        if "fvar" in font:
            tag = {a.axisTag for a in font["fvar"].axes}
            if "wght" in tag and weight:
                loc = {"wght": float(weight)}
        gs = font.getGlyphSet(location=loc) if loc else font.getGlyphSet()
        _FONTS[key] = (font, gs, font.getBestCmap(), font["head"].unitsPerEm)
    return _FONTS[key]


def text_d(el):
    font, gs, cmap, upem = load_font(el["font"], el.get("weight"))  # exits with a pip hint if fonttools is missing
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    s = el["size_pt"] * PT_MM / upem
    track = el.get("tracking", 0) * upem
    lead = el.get("leading", 1.4) * el["size_pt"] * PT_MM
    parts = []
    for n, line in enumerate(str(el["text"]).split("\n")):
        names = []
        for ch in line:
            g = cmap.get(ord(ch))
            if g is None:
                raise ValueError(f"font {Path(el['font']).name} has no glyph for {ch!r}; pick a font that covers it")
            names.append(g)
        width = sum(gs[g].width for g in names) + track * max(len(names) - 1, 0)
        anchor = el.get("anchor", "start")
        pen_x = {"start": 0, "middle": -width / 2, "end": -width}[anchor]
        base_y = el["y_mm"] + n * lead
        for g in names:
            pen = SVGPathPen(gs)
            gs[g].draw(TransformPen(pen, (s, 0, 0, -s, el["x_mm"] + pen_x * s, base_y)))
            cmds = pen.getCommands()
            if cmds:
                parts.append(cmds)
            pen_x += gs[g].width + track
    return " ".join(parts)


# ── layout → files ─────────────────────────────────────────────────────────

def element_d(el):
    t = el["type"]
    if t == "text":
        return text_d(el), "nonzero"
    if t == "rect":
        x, y, w, h = el["x_mm"], el["y_mm"], el["w_mm"], el["h_mm"]
        if el.get("stroke_pt"):
            k = el["stroke_pt"] * PT_MM
            return rect_d(x - k / 2, y - k / 2, w + k, h + k) + rect_d(x + k / 2, y + k / 2, w - k, h - k), "evenodd"
        return rect_d(x, y, w, h), "nonzero"
    if t == "circle":
        cx, cy, r = el["cx_mm"], el["cy_mm"], el["r_mm"]
        if el.get("stroke_pt"):
            k = el["stroke_pt"] * PT_MM
            return circle_d(cx, cy, r + k / 2) + circle_d(cx, cy, r - k / 2), "evenodd"
        return circle_d(cx, cy, r), "nonzero"
    if t == "line":
        return bar_d(el["x1_mm"], el["y1_mm"], el["x2_mm"], el["y2_mm"], el["width_pt"] * PT_MM), "nonzero"
    if t == "path":
        d = el["d"]
        if "box" in el:
            d = place_path(d, el["box"], el["x_mm"], el["y_mm"], el["w_mm"])
        return d, el.get("fill_rule", "nonzero")
    raise ValueError(f"unknown element type {t!r}")


def svg_doc(w, h, bleed, body, title):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{fmt(w)}mm" height="{fmt(h)}mm" '
            f'viewBox="{fmt(-bleed)} {fmt(-bleed)} {fmt(w)} {fmt(h)}">\n<title>{title}</title>\n{body}</svg>\n')


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def slug(s):
    s = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", str(s)).strip("-")
    return s or "plate"


def build(layout, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    fw, fh = layout["finished_mm"]
    bleed = layout.get("bleed_mm", 3)
    safe = layout.get("safe_mm", 5)
    W, H = fw + 2 * bleed, fh + 2 * bleed
    name = slug(layout.get("name", "design"))
    report = {"name": layout.get("name", "design"), "finished_mm": [fw, fh], "bleed_mm": bleed,
              "artboard_mm": [W, H], "faces": [], "warnings": []}
    try:
        import fitz  # PyMuPDF: SVG → PDF
    except ImportError:
        fitz = None
        report["warnings"].append("PyMuPDF not installed: SVG plates only (pip install pymupdf for PDF)")
    for face in layout["faces"]:
        fname = face["face"]
        plates = {p["id"]: p for p in face["plates"]}
        groups = {pid: [] for pid in plates}
        for el in face["elements"]:
            if el["plate"] not in plates:
                raise ValueError(f"{fname}: element uses unknown plate {el['plate']!r}")
            d, rule = element_d(el)
            groups[el["plate"]].append((d, rule, el))
        face_rep = {"face": fname, "plates": []}
        preview = [f'<rect x="{fmt(-bleed)}" y="{fmt(-bleed)}" width="{fmt(W)}" height="{fmt(H)}" fill="#ffffff"/>',
                   f'<rect x="0" y="0" width="{fmt(fw)}" height="{fmt(fh)}" fill="{esc(layout.get("paper_preview", "#f3eee4"))}"/>']
        for pid, plate in plates.items():
            proc = plate.get("process", "letterpress")
            if proc not in PROCESSES:
                raise ValueError(f"{fname}/{pid}: process must be one of {PROCESSES}")
            items = groups[pid]
            if not items:
                report["warnings"].append(f"{fname}/{pid}: plate has no elements")
                continue
            body = "".join(f'<path d="{d}" fill="#000000" fill-rule="{r}"/>\n' for d, r, _ in items)
            base = f"{name}-{fname}-{slug(pid)}-{proc}-{slug(plate.get('colour', ''))}".rstrip("-")
            svg = svg_doc(W, H, bleed, body, esc(f"{fname} / {proc} / {plate.get('colour', '')} — 100% K plate"))
            (out / f"{base}.svg").write_text(svg, encoding="utf-8")
            files = [f"{base}.svg"]
            if fitz:
                doc = fitz.open(stream=svg.encode("utf-8"), filetype="svg")
                (out / f"{base}.pdf").write_bytes(doc.convert_to_pdf())
                doc.close()
                files.append(f"{base}.pdf")
            boxes = [b for b in (path_bbox(d) for d, _, _ in items) if b]
            x0 = max(min(b[0] for b in boxes), 0); y0 = max(min(b[1] for b in boxes), 0)
            x1 = min(max(b[2] for b in boxes), fw); y1 = min(max(b[3] for b in boxes), fh)
            area = [math.ceil(max(x1 - x0, 0) / 5) * 0.5, math.ceil(max(y1 - y0, 0) / 5) * 0.5]
            for d, _, el in items:
                b = path_bbox(d)
                if el["type"] == "text" and b and (b[0] < safe or b[1] < safe or b[2] > fw - safe or b[3] > fh - safe):
                    report["warnings"].append(f"{fname}/{pid}: text {str(el['text'])[:12]!r} is inside the {safe} mm safe margin")
                if b and (b[0] < 0 < b[2] or b[1] < 0 < b[3] or b[0] < fw < b[2] or b[1] < fh < b[3]) \
                        and (b[0] > -bleed + 0.01 and b[0] < 0 or b[1] > -bleed + 0.01 and b[1] < 0
                             or b[2] < fw + bleed - 0.01 and b[2] > fw or b[3] < fh + bleed - 0.01 and b[3] > fh):
                    report["warnings"].append(f"{fname}/{pid}: a {el['type']} crosses the trim but stops short of the {bleed} mm bleed")
            face_rep["plates"].append({"id": pid, "process": proc, "colour": plate.get("colour", ""),
                                       "plate_area_cm": area, "files": files})
            colour = plate.get("preview") or {"foil": "#c9a55c", "emboss": "#d9d2c4", "deboss": "#d9d2c4",
                                             "dieline": "#e6007e"}.get(proc, "#222222")
            blend = ' style="mix-blend-mode:multiply"' if proc == "letterpress" else ""
            preview.append(f'<g fill="{esc(colour)}"{blend}>' + "".join(
                f'<path d="{d}" fill-rule="{r}"/>' for d, r, _ in items) + "</g>")
        k = 0.15
        preview += [
            f'<rect x="0" y="0" width="{fmt(fw)}" height="{fmt(fh)}" fill="none" stroke="#888" stroke-width="{k}"/>',
            f'<rect x="{fmt(safe)}" y="{fmt(safe)}" width="{fmt(fw - 2 * safe)}" height="{fmt(fh - 2 * safe)}" '
            f'fill="none" stroke="#3a7bd5" stroke-width="{k}" stroke-dasharray="1 1"/>',
            f'<text x="{fmt(-bleed + 0.5)}" y="{fmt(fh + bleed - 0.6)}" font-size="1.8" fill="#c00" '
            f'font-family="sans-serif">PREVIEW 示意 · NOT FOR PRINT · {fmt(fw)}×{fmt(fh)} mm</text>']
        pv = f"{name}-{fname}-preview.svg"
        (out / pv).write_text(svg_doc(W, H, bleed, "\n".join(preview) + "\n", "preview, not for print"), encoding="utf-8")
        face_rep["preview"] = pv
        report["faces"].append(face_rep)
    (out / "plates.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def find_font():
    for p in ("C:/Windows/Fonts/NotoSansTC-VF.ttf", "C:/Windows/Fonts/msjh.ttc", "C:/Windows/Fonts/arial.ttf",
              "/System/Library/Fonts/PingFang.ttc", "/System/Library/Fonts/Helvetica.ttc",
              "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(p).exists():
            return p
    return None


def selftest():
    import tempfile
    font = find_font()
    layout = {"name": "selftest", "finished_mm": [90, 54], "bleed_mm": 3,
              "faces": [{"face": "front",
                         "plates": [{"id": "ink1", "process": "letterpress", "colour": "PANTONE 2766 U"},
                                    {"id": "foil1", "process": "foil", "colour": "matte gold"}],
                         "elements": [{"plate": "ink1", "type": "rect", "x_mm": 10, "y_mm": 10, "w_mm": 20, "h_mm": 5},
                                      {"plate": "ink1", "type": "line", "x1_mm": 10, "y1_mm": 40, "x2_mm": 60,
                                       "y2_mm": 40, "width_pt": 0.5},
                                      {"plate": "foil1", "type": "circle", "cx_mm": 75, "cy_mm": 27, "r_mm": 6},
                                      {"plate": "foil1", "type": "path", "d": "M0 0L10 0L5 10Z", "box": [0, 0, 10, 10],
                                       "x_mm": 60, "y_mm": 10, "w_mm": 5}]}]}
    if font:
        layout["faces"][0]["elements"].append({"plate": "ink1", "type": "text", "text": "Ab 12", "font": font,
                                               "size_pt": 10, "x_mm": 10, "y_mm": 30})
    with tempfile.TemporaryDirectory() as tmp:
        rep = build(layout, tmp)
        plates = rep["faces"][0]["plates"]
        assert [p["id"] for p in plates] == ["ink1", "foil1"], plates
        svg = (Path(tmp) / plates[0]["files"][0]).read_text(encoding="utf-8")
        assert 'width="96mm" height="60mm"' in svg and 'viewBox="-3 -3 96 60"' in svg, svg[:300]
        assert "<text" not in svg and "stroke" not in svg and set(re.findall(r'fill="(#[0-9a-f]+)"', svg)) == {"#000000"}
        assert plates[0]["plate_area_cm"] == [5.0, 3.5], plates[0]  # x 10–60, y 10–40.09 → 5.0 × 3.5 cm
        assert plates[1]["plate_area_cm"] == [2.5, 2.5], plates[1]  # x 60–81, y 10–33
        assert "PREVIEW" in (Path(tmp) / rep["faces"][0]["preview"]).read_text(encoding="utf-8")
        if font:
            assert svg.count("<path") == 3 and len(re.findall(r"[MLQCZ]", svg)) > 20, "text did not outline"
        if not rep["warnings"]:
            import fitz
            pdf = fitz.open(str(Path(tmp) / plates[0]["files"][1]))
            page = pdf[0]
            assert abs(page.rect.width - 96 / PT_MM) < 0.5 and abs(page.rect.height - 60 / PT_MM) < 0.5, page.rect
            assert not page.get_text().strip() and not page.get_images(), "PDF plate has text or images"
            assert page.get_drawings(), "PDF plate lost its vector shapes"
            pdf.close()
    print(f"selftest ok (font: {font or 'none found, text skipped'})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("layout", nargs="?", help="layout JSON")
    ap.add_argument("--out", help="output folder (default: plates/ next to the layout)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.layout:
        ap.error("give a layout JSON")
    src = Path(a.layout)
    layout = json.loads(src.read_text(encoding="utf-8"))
    for face in layout.get("faces", []):  # font paths may be relative to the layout file
        for el in face.get("elements", []):
            if el.get("font") and not Path(el["font"]).is_absolute() and (src.parent / el["font"]).exists():
                el["font"] = str(src.parent / el["font"])
    rep = build(layout, a.out or src.with_name("plates"))
    for f in rep["faces"]:
        for p in f["plates"]:
            print(f"{f['face']:6} {p['process']:11} {p['colour'] or '-':24} 版面 {p['plate_area_cm'][0]}×{p['plate_area_cm'][1]} cm  {', '.join(p['files'])}")
        print(f"{f['face']:6} preview     {f['preview']}")
    for w in rep["warnings"]:
        print("WARNING:", w)


if __name__ == "__main__":
    main()
