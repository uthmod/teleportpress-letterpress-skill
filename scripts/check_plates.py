#!/usr/bin/env python3
"""Check letterpress plate files the way TeleportPress 時分印刷's file rules ask (one plate per file).

    python check_plates.py plate1.svg plate2.pdf --finished 90x54 [--bleed 3]
    python check_plates.py --selftest

Each file must be ONE plate: one ink colour, one foil colour, the emboss shape, or the die line.
Errors (exit 1): wrong artboard size, live text (not outlined), raster images, gradients /
patterns / filters / masks, transparency or blend modes, more than one colour on the plate.
Warnings: strokes left as strokes, a colour other than 100% black, more than one page.
SVG needs only Python; PDF needs PyMuPDF (pip install pymupdf).
"""
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

MM_PER = {"mm": 1.0, "cm": 10.0, "in": 25.4, "pt": 25.4 / 72, "pc": 25.4 / 6, "px": 25.4 / 96, "": 25.4 / 96}
SHAPES = {"path", "rect", "circle", "ellipse", "polygon", "polyline", "line"}
BANNED = {"text": "live text: convert all text to outlines", "tspan": "live text: convert all text to outlines",
          "textPath": "live text: convert all text to outlines", "image": "raster image on a plate",
          "linearGradient": "gradient (letterpress prints solid ink; make it a halftone or drop it)",
          "radialGradient": "gradient (letterpress prints solid ink; make it a halftone or drop it)",
          "pattern": "pattern fill", "filter": "filter effect (shadow / blur / texture)", "mask": "mask",
          "foreignObject": "embedded HTML"}


def length_mm(v):
    m = re.fullmatch(r"\s*([-+]?[\d.]+(?:e[-+]?\d+)?)\s*([a-z]*)\s*", v or "", re.I)
    if not m or m.group(2).lower() not in MM_PER:
        return None
    return float(m.group(1)) * MM_PER[m.group(2).lower()]


def style_of(el):
    props = {k: v for k, v in el.attrib.items()}
    for part in (el.get("style") or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            props[k.strip()] = v.strip()
    return props


def norm_colour(c):
    c = (c or "").strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return {"black": "#000000", "rgb(0,0,0)": "#000000"}.get(c.replace(" ", ""), c)


def check_svg(path, size):
    errors, warnings = [], []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return [f"not a readable SVG: {e}"], []
    tag = lambda el: el.tag.split("}")[-1]
    w, h = length_mm(root.get("width")), length_mm(root.get("height"))
    if w is None or h is None:
        vb = (root.get("viewBox") or "").split()
        warnings.append("width/height missing or without units: set them in mm (e.g. width=\"96mm\")")
        if len(vb) == 4:
            w, h = float(vb[2]) * MM_PER["px"], float(vb[3]) * MM_PER["px"]
    if size and w is not None and (abs(w - size[0]) > 0.2 or abs(h - size[1]) > 0.2):
        errors.append(f"artboard is {w:.1f}×{h:.1f} mm, expected {size[0]:g}×{size[1]:g} mm (finished size + bleed)")
    fills, strokes = set(), 0
    # Inherited paint: walk with the parent's fill so <g fill="..."> counts.
    def walk(el, fill, stroke):
        nonlocal strokes
        t, st = tag(el), style_of(el)
        if t in BANNED:
            errors.append(BANNED[t])
        if t == "use" and not (el.get("href") or el.get("{http://www.w3.org/1999/xlink}href") or "").startswith("#"):
            errors.append("<use> pointing at an outside file")
        for k in ("opacity", "fill-opacity", "stroke-opacity"):
            try:
                if float(st.get(k, "1")) < 1:
                    errors.append(f"transparency ({k} {st[k]}): plates print solid ink only")
            except ValueError:
                pass
        if st.get("mix-blend-mode", "normal") != "normal":
            errors.append(f"blend mode {st['mix-blend-mode']}")
        if st.get("filter") or st.get("mask"):
            errors.append("filter or mask on a shape")
        fill = st.get("fill", fill)
        stroke = st.get("stroke", stroke)
        if t in SHAPES:
            if fill and fill != "none":
                if "url(" in fill:
                    errors.append("gradient or pattern fill")
                else:
                    fills.add(norm_colour(fill))
            if stroke and stroke != "none":
                strokes += 1
                fills.add(norm_colour(stroke))
        for ch in el:
            if tag(ch) not in {"defs", "title", "desc", "metadata", "clipPath", "style"}:
                walk(ch, fill, stroke)
    walk(root, "#000000", None)
    for el in root.iter():  # gradients, patterns and filters usually sit in <defs>
        if tag(el) in {"linearGradient", "radialGradient", "pattern", "filter", "mask"}:
            errors.append(BANNED[tag(el)])
    fills.discard("")
    if len(fills) > 1:
        errors.append(f"{len(fills)} colours on one plate ({', '.join(sorted(fills))}): split them into one file per ink/process")
    elif fills and fills != {"#000000"}:
        warnings.append(f"plate is drawn in {fills.pop()}; plate artwork should be 100% black (name the ink in the file name instead)")
    if strokes:
        warnings.append(f"{strokes} shape(s) use strokes: outline strokes to fills so line widths can't change")
    if not any(tag(el) in SHAPES for el in root.iter()):
        errors.append("no artwork on this plate")
    return errors, warnings


def check_pdf(path, size):
    try:
        import fitz
    except ImportError:
        return [], ["PyMuPDF not installed, PDF not checked (pip install pymupdf)"]
    errors, warnings = [], []
    with fitz.open(path) as doc:
        if doc.page_count > 1:
            warnings.append(f"{doc.page_count} pages: one plate per file is easiest to check")
        for n, page in enumerate(doc, 1):
            box = page.trimbox if page.trimbox != page.mediabox else page.mediabox
            w, h = box.width * MM_PER["pt"], box.height * MM_PER["pt"]
            if size and (abs(w - size[0]) > 0.2 or abs(h - size[1]) > 0.2):
                errors.append(f"page {n} is {w:.1f}×{h:.1f} mm, expected {size[0]:g}×{size[1]:g} mm (finished size + bleed)")
            if page.get_text().strip():
                errors.append(f"page {n}: live text, convert all text to outlines")
            if page.get_images():
                errors.append(f"page {n}: raster image on a plate")
            colours, strokes = set(), 0
            for d in page.get_drawings():
                for key in ("fill", "color"):
                    c = d.get(key)
                    if c is not None:
                        colours.add(tuple(round(v, 3) for v in c))
                if d.get("color") is not None and d.get("type") in ("s", "fs"):
                    strokes += 1
                for key in ("fill_opacity", "stroke_opacity"):
                    if (d.get(key) or 1) < 0.999:
                        errors.append(f"page {n}: transparency: plates print solid ink only")
                        break
            if not page.get_drawings() and not page.get_images():
                errors.append(f"page {n}: no artwork")
            if len(colours) > 1:
                errors.append(f"page {n}: {len(colours)} colours on one plate: split them into one file per ink/process")
            elif colours and colours.pop() not in ((0.0, 0.0, 0.0), (0.0,), (0.0, 0.0, 0.0, 1.0)):
                warnings.append(f"page {n}: artwork is not 100% black; name the ink in the file name instead")
            if strokes:
                warnings.append(f"page {n}: {strokes} stroked path(s): outline strokes to fills")
    return errors, warnings


def parse_size(s):
    m = re.fullmatch(r"\s*([\d.]+)\s*[x×*]\s*([\d.]+)\s*", s or "")
    if not m:
        raise argparse.ArgumentTypeError("size like 90x54 (mm)")
    return float(m.group(1)), float(m.group(2))


def check(path, finished=None, bleed=3.0):
    size = (finished[0] + 2 * bleed, finished[1] + 2 * bleed) if finished else None
    if Path(path).suffix.lower() == ".pdf":
        return check_pdf(path, size)
    if Path(path).suffix.lower() == ".svg":
        return check_svg(path, size)
    return [f"{Path(path).suffix or 'this'} file can't be checked here: plates go in as vector PDF, SVG or .ai"], []


def selftest():
    import tempfile
    good = ('<svg xmlns="http://www.w3.org/2000/svg" width="96mm" height="60mm" viewBox="-3 -3 96 60">'
            '<path d="M10 10H30V15H10Z" fill="#000000"/></svg>')
    bad = ('<svg xmlns="http://www.w3.org/2000/svg" width="90mm" height="54mm"><defs><linearGradient id="g"/></defs>'
           '<text x="5" y="5" font-family="Arial">Hi</text><rect width="5" height="5" fill="#ff0000" opacity="0.5"/>'
           '<circle r="3" fill="none" stroke="#0000ff"/></svg>')
    with tempfile.TemporaryDirectory() as tmp:
        g, b = Path(tmp, "good.svg"), Path(tmp, "bad.svg")
        g.write_text(good, encoding="utf-8")
        b.write_text(bad, encoding="utf-8")
        e, w = check(g, (90, 54), 3)
        assert not e and not w, (e, w)
        e, w = check(b, (90, 54), 3)
        text = " | ".join(e)
        for want in ("artboard is 90.0×54.0", "live text", "gradient", "transparency", "2 colours"):
            assert want in text, (want, e)
        assert any("strokes" in x for x in w), w
        try:
            import fitz
        except ImportError:
            print("selftest ok (SVG only; PyMuPDF missing)")
            return
        pdf = Path(tmp, "good.pdf")
        doc = fitz.open(stream=good.encode(), filetype="svg")
        pdf.write_bytes(doc.convert_to_pdf())
        doc.close()
        e, w = check(pdf, (90, 54), 3)
        assert not e and not w, (e, w)
        e, _ = check(pdf, (85, 55), 3)
        assert e and "expected 91×61" in e[0], e
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--finished", type=parse_size, help="finished (trim) size in mm, e.g. 90x54")
    ap.add_argument("--bleed", type=float, default=3.0, help="bleed per side, mm (default 3)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.files:
        ap.error("give one or more plate files")
    failed = False
    for f in a.files:
        errors, warnings = check(f, a.finished, a.bleed)
        failed |= bool(errors)
        print(f"{'FAIL' if errors else 'ok  '}  {f}")
        for e in dict.fromkeys(errors):
            print(f"      error:   {e}")
        for w in dict.fromkeys(warnings):
            print(f"      warning: {w}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
