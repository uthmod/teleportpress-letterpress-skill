# The print file (印刷檔／完稿)

What the studio makes plates from, and how to build or check one. Values are from the studio's own guides and production tools as of 2026-11-03; the studio ruled on bleed (3 mm) and the smallest text sizes on 2026-11-03. Re-read https://teleportpress.com/guides/preparing-files if a user questions a number.

## Contents

1. What to deliver
2. Artboard, bleed, safe area
3. One plate per ink and process
4. Minimum sizes per process
5. Press and die limits
6. Colour, halftones, overlaps
7. Building plates with the scripts
8. When you can't make the file

## 1. What to deliver

- **Format.** The studio prefers an Illustrator `.ai` original; SVG, a vector PDF or EPS work too. The scripts here write SVG + PDF; to hand over an `.ai`, open the SVG in Illustrator and Save As `.ai`. Raster art (a Photoshop file) only at 600–1200 dpi: text and fine lines need 1200 dpi, images at least 600 dpi. A screenshot, low-resolution JPG or flattened file cannot be used for plates.
- **One design per artboard, at finished size.** Don't step-and-repeat cards onto a sheet: the studio lays out the press sheet itself.
- **One file (or one clearly named layer) per plate.** Name each file `<design>-<face>-<process>-<colour>`, for example `chen-card-front-letterpress-PANTONE-2766-U.pdf`, `chen-card-front-foil-matte-gold.pdf`, `chen-card-back-emboss.pdf`, `chen-card-dieline.pdf`.
- **A colour preview** of each face, marked as a preview, so the studio sees how the plates combine.
- **The spec** (quote request) listing every plate with its ink, foil or process (`quote-request.md`).
- Delivery: upload the files to Google Drive or Dropbox, share as "anyone with the link can view", and paste the link in the order form's 「設計檔雲端連結」 field (「檔案連結」 on the original form). The picture you can attach in the new form's first step is for quoting only and never used for printing.

## 2. Artboard, bleed, safe area

- **Artboard = finished size + bleed on every side**, units in mm. Finished size (成品尺寸) is the trimmed piece: Taiwan's name card is 9 × 5.4 cm.
- **Bleed (出血): 3 mm each side.** Anything meant to run off the edge must extend to the bleed line.
- **Safe area (安全距離): keep text and important artwork at least 3 mm inside the trim, 5 mm is safer.** The cut can wander 0.5–1 mm, and art close to the edge then looks crooked. Borders near a die-cut edge also need 3–5 mm (die-cut tolerance is about 1 mm).
- **No gripper margin (咬口), no crop marks needed, no sheet layout.** The studio adds its gripper and trim room itself. An artboard larger than finished size + bleed gets the piece printed at the wrong size.
- Folded or glued pieces (信封, 紅包袋): the new form takes the finished (folded) size and a template or 我有自己的展開圖; the original form's 客製信封 asks for the 展開尺寸 (the flat sheet, flap included) and a complete die drawing (展開圖) with the fold lines marked, with the finished size in 備註. Either way, send your own die drawing as the die-line plate.

## 3. One plate per ink and process

The studio prices and prints one plate per colour per pass ("一色一版"). Build the file the same way:

| Plate | What goes on it | Notes |
|---|---|---|
| 凸版印刷 ink | everything printed in one Pantone ink on one face | one plate per ink colour; name the ink as a Pantone **U** (uncoated) code |
| 空壓／打凹 blind deboss | shapes pressed in without ink (or with 透明墨 clear ink) | counts as a plate; made on the letterpress |
| 燙金 foil | everything stamped in one foil colour on one face | one plate per foil colour |
| 打凸 emboss | the raised shape | male + female die; the back shows a dent at the same spot |
| 刀模線 die line | the cut outline as a thin line | only for special shapes; not printed |
| 紙邊上色 edge paint | no file | a colour note in the spec |

- **Front and back are separate plates**, even in the same ink.
- **Plate artwork is solid 100% black (K 100) filled shapes.** The ink or foil is named in the file name and spec, not by colouring the artwork. Grey art is printed as if it were 100%.
- **Text turned into outlines** (Illustrator: Type → Create Outlines). **Strokes outlined to fills** so line weights can't change. **No transparency, blend modes, shadows, glows, textures, gradients or embedded photos.**
- **Shared plates (共版)**: several designs (e.g. one card per employee) can share a plate when the shared part is identical, in the same place and the same colour. Line shared details up on purpose.
- A 對裱 duplex card has 2–3 sheets: give each printed side of each sheet its own plates and say which sheet it is (正面 face sheet, 背面 back sheet).

## 4. Minimum sizes per process

1 pt = 0.353 mm. "Gap" is the white space between two strokes, including the counters inside a character.

| Process | Thinnest line | Narrowest gap | Smallest text | Source |
|---|---|---|---|---|
| 凸版印刷 letterpress | 0.25 pt; isolated dots 1 pt | 0.3 pt | 7 pt Chinese, 6 pt Latin | 檔案準備, 設計規範 guides; text sizes ruled by the studio 2026-11-03 |
| Reverse / knockout (white text inside an ink area) | strokes 0.4–0.5 pt | 0.3 pt | larger than normal text | 檔案準備 |
| 燙金 foil (gold, silver, colours, white) | 0.3 pt | 0.6 pt | 8 pt, white foil 9 pt; add a little letter-spacing | 檔案準備; text sizes ruled by the studio 2026-11-03 |
| 霧銀箔 matte silver MS-01 | 0.3 pt | 0.54 pt | 8 pt | 檔案準備 |
| 打凸／打凹 emboss / deboss | 0.5 pt | 0.8 pt | no body text: logos, marks, borders, patterns; the smallest lettering the studio has embossed is about 21 pt, debossed about 30 pt | quote form 打凸 card, 檔案準備, studio layout rules |
| 烤松香 thermography | — | — | 11 pt CJK, 9 pt Latin | quote form 烤松香 card |

- Very small Chinese text: print it 1:1 on a home printer first. If it blurs there, it blurs on the press; change the font or weight.
- Thin 明體 (serif) horizontals often fall under 0.25 pt at small sizes; a 黑體 (sans) or a heavier weight helps.
- QR codes: at least 1.2 × 1.2 cm, vector, error correction level L. The studio advises against pressing QR codes deeply: keep them low-density with a shallow impression, or print them by another method.
- Tight letter-spacing on small text presses into one blur: open it up.

## 5. Press and die limits

- **Letterpress, emboss, deboss:** the press takes a sheet up to 35 × 27.2 cm including the studio's margins, so keep the finished size within about **32.5 × 25 cm** (A4 fits).
- **Foil only:** the foil machine takes about A3, so about **39.5 × 27.6 cm** finished.
- **Die-cut shapes:** up to 36.7 × 24.3 cm; with letterpress on the same piece, the press limit above wins.
- Bigger than that, or a format you're unsure of: ask the studio.
- Standard round-corner dies exist (R 2, 2.5, 4, 5, 8 mm); any other shape needs a new die.

## 6. Colour, halftones, overlaps

- **Spot inks, not CMYK.** Name every ink as a Pantone Solid **Uncoated (U)** code; a C (coated) code shifts colour on the studio's uncoated papers. No swatch book? Give a CMYK value and ask the studio to suggest the Pantone. Fluorescent screen colours can't be printed as they look.
- **Inks are transparent.** Where two inks overlap they mix (pink over yellow turns orange-red). Knock the lower colour out where you don't want a mix; overlap on purpose where you do.
- **Registration:** separate plates can shift about 0.2 mm against each other. Don't design two colours that must meet edge to edge or line up exactly; leave visible space (the studio's layout tool keeps elements on different plates 1.5 mm apart) or overlap them deliberately.
- **Gradients, photos, watercolour** can't print as continuous tone. Options for a part of the design: convert it to a halftone or use solid shapes. A piece that is full colour throughout needs 數位印刷 or 合版印刷 (`full-colour.md`).
- **Halftones (網點) on letterpress**: about 70 lpi; single ink at 45°, a second ink at 75°; keep tones between 7% and 85%; ink spreads 20–30% on press, so set about 30–35% for a printed 50%; tints that must read apart should differ by 30% or more; elliptical dots give smoother steps. The ink is matched at 100%.

## 7. Building plates with the scripts

Python 3.9+. `pip install fonttools pymupdf` for `make_plates.py` and PDF checks; `pip install opencv-python pymupdf numpy scipy` for `check_thin.py`. Each script has `--selftest`.

1. **Write a layout JSON** (copy `assets/layout-example.json`): finished size, bleed 3, one entry per face with its plates (`process`: letterpress, foil, emboss, deboss or dieline; `colour`; a `preview` colour) and elements (`text`, `rect`, `circle`, `line`, `path`), each assigned to a plate. Coordinates are mm from the top-left corner of the trimmed piece; bleed is negative. Text needs a font file on this machine that covers every character; Noto Sans TC / Noto Serif TC (思源黑體／宋體, SIL Open Font License) are safe choices, or the user's own licensed font. Run `python scripts/make_plates.py --help` for every field.
2. **Build**: `python scripts/make_plates.py layout.json --out plates/`. You get one SVG + PDF per plate (100% black, text outlined), `<name>-<face>-preview.svg`, and `plates.json` with each plate's 版面尺寸 (plate area, cm, rounded up to 0.5 cm) for the quote spec and the new form's per-plate 版面尺寸 boxes. Read its warnings: text inside the safe margin, art that crosses the trim without reaching the bleed.
3. **Check structure**: `python scripts/check_plates.py plates/*.pdf --finished 90x54`. Every plate must say `ok`. The same check works on files the user made (SVG or PDF): it reports wrong artboard size, live text, images, gradients, transparency and more than one colour per plate.
4. **Check thin lines and gaps**: `python scripts/check_thin.py <plate.pdf> --process letterpress` (also `reverse`, `foil`, `matte-silver`, `emboss`). Run it per plate. It writes a PNG with red circles (ink too thin) and blue circles (gap too narrow); coordinates are mm from the artboard corner, bleed included. Flags inside the sharp inner corners of letters like M, N, V, W, and in tight counters of bold Chinese characters, are normal at small sizes: look at the PNG and fix the real ones (a counter that closes up, a hairline that would break) by enlarging the text, changing weight or font, or opening the spacing.
5. **Look at the preview** before you hand anything over.

Without Python, build the same thing by hand in SVG: an `<svg width="96mm" height="60mm" viewBox="-3 -3 96 60">` per plate (for a 90 × 54 card), filled black `<path>`s only. You can't outline text without a font tool, so mark such files "text not outlined yet" in the spec.

## 8. When you can't make the file

Say exactly what's missing, file by file. A typical list for an AI preview:

- Needs a vector drawing of the artwork at finished size; the image is a picture of a card, not the card's artwork.
- The watercolour background / gradient / photo can't print by letterpress as shown: choose a solid shape, a halftone or a coloured paper. If the whole piece only works in full colour, see `full-colour.md`.
- Each colour must be its own plate: say which parts are ink 1, ink 2, foil.
- Text must be retyped (the image's text can't be used) and outlined.
- The glittery raised gold in the image is not something foil looks like: foil is a flat, glossy metal film.

Then offer the two ways forward: the user (or their designer) fixes the file with this list, or the request goes in marked "file prep needed 需要製作印刷檔" and the studio prepares the file as a paid service (read https://teleportpress.com/guides/pricing-ordering for the current file-handling terms before you mention a fee). The studio also gives a free quick look at layout and letter-spacing on a design sent with the quote request.
