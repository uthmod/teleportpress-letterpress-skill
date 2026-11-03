#!/usr/bin/env python3
"""Flag strokes thinner, and gaps narrower, than a process allows (TeleportPress 時分印刷 skill).

    python check_thin.py plate.pdf --process letterpress
    python check_thin.py plate.svg --line 0.15 --gap 0.15      (custom limits in mm)
    python check_thin.py --selftest

Run it on ONE plate at a time (one ink or one foil per file): it treats everything dark as ink.
Per page it writes <file>-p<N>-preflight.png (red = ink too thin, blue = gap too narrow,
circled) and prints each spot in mm from the page's top-left corner. Exits 1 when anything
is flagged. Needs: pip install opencv-python pymupdf numpy scipy
Port of the studio's own preflight-thin.py; the --process limits are the studio's file rules.
"""
import argparse
import sys
from pathlib import Path

import cv2
import fitz  # PyMuPDF opens PDF and SVG alike
import numpy as np
from scipy import ndimage

RED, BLUE = (255, 0, 0), (0, 90, 255)
PT = 25.4 / 72  # mm per point

# Minimum stroke and gap per process, in points (TeleportPress guide 檔案準備, 2026-09;
# 打凸 line from the quote form's 打凸 card). reverse = white text knocked out of an ink area.
PROCESS_PT = {
    "letterpress": (0.25, 0.3),
    "reverse": (0.25, 0.5),
    "foil": (0.3, 0.6),
    "matte-silver": (0.3, 0.54),
    "emboss": (0.5, 0.8),
}


def disk(px):
    px = max(1, int(round(px))) | 1
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (px, px))


def too_narrow(mask, width_px):
    """Pixels of mask in parts narrower than width_px (morphological opening)."""
    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, disk(width_px))
    # ponytail: an opening also shaves the convex corners of wide shapes; that residue
    # stays within ~0.2×width of what survived, so ignore anything that close.
    return mask & ~cv2.dilate(opened, disk(width_px * 0.5))


def spots(flag, mask, dpi, min_len_px):
    """[(x_mm, y_mm, width_mm)] per flagged blob; width = 2 × deepest point in mask."""
    n, labels, stats, cent = cv2.connectedComponentsWithStats(flag, connectivity=8)
    # ponytail: blobs shorter than min_len_px are the pointed tips and crotches every serif
    # font has, not hairlines or gaps; a real short defect under that length is skipped too.
    keep = [i for i in range(1, n) if max(stats[i, 2], stats[i, 3]) >= min_len_px]
    if not keep:
        return [], labels, keep, stats
    depth = ndimage.maximum(cv2.distanceTransform(mask, cv2.DIST_L2, 5), labels, keep)
    mm = 25.4 / dpi
    return [(cent[i][0] * mm, cent[i][1] * mm, 2 * d * mm) for i, d in zip(keep, depth)], labels, keep, stats


def analyse(page, dpi, line_mm, gap_mm, threshold):
    pix = page.get_pixmap(dpi=dpi, alpha=False)
    img = np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.w, pix.n)[:, :, :3]
    # ponytail: any channel darker than threshold counts as ink; pale inks need a higher --threshold.
    ink = (img.min(axis=2) < threshold).astype(np.uint8) * 255
    paper = 255 - ink
    px = dpi / 25.4
    thin = too_narrow(ink, line_mm * px)
    gap = too_narrow(paper, gap_mm * px)
    thin_spots, *thin_blobs = spots(thin, ink, dpi, 2 * line_mm * px)
    gap_spots, *gap_blobs = spots(gap, paper, dpi, 2 * gap_mm * px)

    out = (img * 0.35 + 255 * 0.65).astype(np.uint8)  # faded artwork underneath
    ring = max(8, int(px))  # 1 mm
    for (lab, keep, stats), colour in ((thin_blobs, RED), (gap_blobs, BLUE)):
        hit = np.isin(lab, keep).astype(np.uint8)
        out[cv2.dilate(hit, disk(px * 0.2)) > 0] = colour  # thicken so it shows zoomed out
        for i in keep:
            x, y, w, h = stats[i, :4]
            cv2.rectangle(out, (x - ring, y - ring), (x + w + ring, y + h + ring), colour, max(2, ring // 4))
    return out, thin_spots, gap_spots


def run(path, dpi, line_mm, gap_mm, threshold):
    flagged = 0
    with fitz.open(path) as doc:
        for n, page in enumerate(doc, 1):
            out, thin, gap = analyse(page, dpi, line_mm, gap_mm, threshold)
            png = Path(path).with_name(f"{Path(path).stem}-p{n}-preflight.png")
            cv2.imwrite(str(png), out[:, :, ::-1])
            print(f"page {n}: {len(thin)} thin, {len(gap)} narrow gaps -> {png}")
            for kind, items in (("thin line", thin), ("narrow gap", gap)):
                for x, y, w in items:
                    print(f"  {kind:10}  x {x:7.2f} mm  y {y:7.2f} mm  ~{w:.2f} mm wide")
            flagged += len(thin) + len(gap)
    return flagged


def selftest():
    pt = 72 / 25.4
    doc = fitz.open()
    page = doc.new_page(width=90 * pt, height=54 * pt)
    box = lambda x0, y0, x1, y1: page.draw_rect(fitz.Rect(x0 * pt, y0 * pt, x1 * pt, y1 * pt), fill=(0, 0, 0), width=0)
    line = lambda y, w: page.draw_line((5 * pt, y * pt), (40 * pt, y * pt), width=w * pt)
    box(5, 5, 30, 15)                      # thick block: corners must not flag
    line(25, 0.05)                         # too thin
    line(32, 0.5)                          # fine
    box(50, 5, 60, 15); box(60.08, 5, 70, 15)   # 0.08 mm gap: too narrow
    box(50, 25, 60, 35); box(61, 25, 71, 35)    # 1 mm gap: fine
    _, thin, gap = analyse(page, 1200, 0.15, 0.15, 128)
    near = lambda items, x, y: [s for s in items if abs(s[0] - x) < 15 and abs(s[1] - y) < 2]
    assert near(thin, 22, 25), thin
    assert not near(thin, 22, 32) and not near(thin, 17, 10), thin
    assert len(thin) == 1, thin
    assert [s for s in gap if abs(s[0] - 60) < 1 and 4 < s[1] < 16], gap
    assert not [s for s in gap if abs(s[0] - 60.5) < 1 and 24 < s[1] < 36], gap
    assert len(gap) == 1, gap
    # the letterpress limits: a 0.2 pt hairline flags, a 0.5 pt rule passes
    page2 = doc.new_page(width=90 * pt, height=54 * pt)
    page2.draw_line((5 * pt, 20 * pt), (40 * pt, 20 * pt), width=0.2 * 72 / 72)  # 0.2 pt
    page2.draw_line((5 * pt, 30 * pt), (40 * pt, 30 * pt), width=0.5)  # 0.5 pt
    lp_line, lp_gap = (v * PT for v in PROCESS_PT["letterpress"])
    _, thin2, _ = analyse(page2, 1200, lp_line, lp_gap, 128)
    assert len(thin2) == 1 and abs(thin2[0][1] - 20) < 1, thin2
    print("selftest ok", thin, gap)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="PDF or SVG")
    ap.add_argument("--process", choices=sorted(PROCESS_PT), help="use the studio's limits for this process")
    ap.add_argument("--line", type=float, default=0.15, help="minimum stroke width, mm (default 0.15)")
    ap.add_argument("--gap", type=float, default=0.15, help="minimum gap between ink, mm (default 0.15)")
    ap.add_argument("--dpi", type=int, default=1200, help="render resolution (default 1200; lower for big sheets)")
    ap.add_argument("--threshold", type=int, default=128, help="darkest channel below this = ink (default 128)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        sys.exit(0)
    if not a.file:
        ap.error("give a PDF or SVG")
    if a.process:
        line_pt, gap_pt = PROCESS_PT[a.process]
        a.line, a.gap = line_pt * PT, gap_pt * PT
        print(f"{a.process}: line >= {line_pt} pt ({a.line:.3f} mm), gap >= {gap_pt} pt ({a.gap:.3f} mm)")
    sys.exit(1 if run(a.file, a.dpi, a.line, a.gap, a.threshold) else 0)
