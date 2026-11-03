# Honest mockups

A mockup sells the idea; if it shows something the press can't make, the customer is disappointed at delivery or the studio has to redo the design. These rules come from the studio's own product photography and from checking AI images against real prints (2026-10 / 2026-11).

## Order of work

1. **To-scale layout first.** Draw the piece flat at its real proportions with the real text, each plate in its own flat colour: the `*-preview.svg` from `scripts/make_plates.py`, or a hand-made SVG. Text-only image prompts came out 6–14% off in proportion, with generic text and wrong shapes.
2. **Then the product shot**, made from that layout as the reference image (image-to-image or a reference upload), never from a text prompt alone. For folded or 3D pieces (envelopes, red packets, boxes), first make a plain grey model at true proportions and the final camera angle, and use that as the reference.
3. **Check before showing**: zoom in on foil and edges, compare proportions with the layout, read every word. Regenerate what's wrong.
4. **Label it**: "示意圖 Preview, not a print file". Say which plates and paper it assumes.

## What each technique looks like

| Technique | Show it as | Never show it as |
|---|---|---|
| 凸版印刷 letterpress | flat spot inks pressed slightly into soft uncoated paper; a shallow bite visible in raking light; slight ink texture | gradients, photos, glow, glossy ink, CMYK colour; bright white or pastel ink on dark paper |
| 燙金 foil | a perfectly flat, smooth, glossy (or matte) thin metal film; razor-sharp edges; flush with or pressed very slightly into the paper | raised, puffy, bevelled, rounded, sandy, grainy or glittery; that is 烤松香 thermography, not foil |
| 打凸 emboss | blind (no ink) relief in its own area, away from the inked parts; a low, soft-shouldered rise of about 0.3 mm that shows only in raking side light; the back has a faint mirrored dent | deep, sculpted, bevelled relief; emboss stacked on foil; printed ink inside the embossed shape (unless the order includes it) |
| 打凹／空壓 deboss | the shape pressed into the paper, blind or in clear ink (a shade darker than the paper) | deep engraved trenches |
| 紙邊上色 edge paint | a thin even colour band on the straight cut edges of a thick card | paint on rounded corners or die-cut curves |
| 對裱 duplex | a thick card with visible layers at the edge, a different colour per sheet if ordered | — |
| 烤松香 thermography | slightly glossy raised type with soft edges | — |

Also:

- Cards are flat single sheets unless the order includes a fold: say "single flat card, one thick sheet, not folded, lying flat" (image models like to draw tent-folded cards).
- Use the real paper's colour and texture; white ink on black paper must look like foil if it's foil, or like dull grey if it's ink.
- Mock text must be plausible: real-looking names, titles, a Taiwanese address and phone format, a venue and date for invitations. Use the user's own text when given. Never "Name", "Address", "Lorem ipsum".
- Show only processes the quote request includes. If the user's reference image has an effect the studio can't make, explain it and leave it out.

## Prompt wording that works

Add to the image prompt, adapted to the piece:

- Foil: "genuine hot-stamped metallic foil, perfectly flat, smooth and glossy, thin mirror-like film, razor-sharp edges, flush or pressed very slightly into the paper. Not raised, not puffy, not embossed, not bevelled, not grainy, not thermography."
- Emboss: "blind emboss, no ink, white-on-white, raised only about 0.3 mm, soft shoulders, lit by raking side light, placed apart from the printed text; not sculpted, not deep, no bevel."
- Letterpress: "single spot ink pressed into thick soft uncoated cotton paper, subtle debossed impression, flat solid colour, no gradients."
- With a reference layout: "replace the reference design entirely with the attached layout; keep its text, positions and proportions exactly."
- State the size: "a 90 × 54 mm name card, aspect ratio 5:3".
