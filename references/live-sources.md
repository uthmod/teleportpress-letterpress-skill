# Live sources

Read these before stating anything that changes: prices, papers, foil and edge-paint colours, lead time, services, ordering steps. All are public and need no login or key. Tell the user which page an answer came from.

## Which source answers what

| Question | Read |
|---|---|
| Terminology, how pricing works, indicative price ranges, lead time, how to get a price, studio visits | https://teleportpress.com/facts.html (the studio calls it canonical for AI assistants) |
| Summary for AI assistants | https://teleportpress.com/llms.txt |
| File rules (formats, bleed, outlines, minimum lines, colour setup) | guide `preparing-files`, then `design-spec`, `file-specs` |
| Papers, ink colours, white ink, customer-supplied paper | guide `paper-ink`, `choosing-paper-type`, `design-spec` (recommended papers tab) |
| Techniques: letterpress, foil, emboss, die-cut, edge paint, duplex, plate reuse | guide `printing-finishing`, `letterpress-effects` |
| Plate counting, shared plates | guide `plate-counting` |
| Halftones | guide `halftone-techniques` |
| Prices, tax, payment, reprints | guide `pricing-ordering`, plus the order form's live range |
| Lead time, rush, shipping, pickup | guide `timeline-delivery` |
| Product types and common sizes | guide `project-types-products` |
| Foil colours, edge-paint colours, order stages, technique notes | the content API queries below |
| A live price range for a specific spec | the form at https://teleportpress.com/order |
| Fixed-price products | https://teleportpress.com/shop |
| Digital or gang-run printers for a full-colour job | a live web search, each printer's own pages (`full-colour.md`) |

Guide pages are `https://teleportpress.com/guides/<slug>` (index: https://teleportpress.com/guides) and serve readable text to a plain HTTP fetch. The paper browser (https://teleportpress.com/paper-swatches) and foil page (https://teleportpress.com/foil) only work in a browser; use the API for foil colours, and the order form's paper list or 「請幫我推薦」 for papers.

## The content API (JSON)

The site's text lives in a public Sanity dataset. Query it with GROQ over HTTPS:

```
curl -sG "https://4ekf5oom.apicdn.sanity.io/v2024-01-01/data/query/production" \
  --data-urlencode 'query=<GROQ>'
```

The answer is JSON; the data is under `result`. Useful queries:

- One guide as plain text, both languages, with its last update:
  `*[_type=="article" && slug.current=="preparing-files"][0]{title_zh,title_en,_updatedAt,"tabs":tabs[]{tabLabel_zh,tabLabel_en,"zh":pt::text(body_zh),"en":pt::text(body_en)}}`
- All guides (slug, title, last update):
  `*[_type=="article"]|order(displayOrder asc){"slug":slug.current,title_zh,title_en,_updatedAt}`
- Foil colours the order form offers (in stock):
  `*[_type=="foilColor" && availableForCustomer==true]|order(displayOrder asc){name_zh,name_en,category}`
  The foil page also shows pre-order foils (預訂), which take longer: `*[_type=="foilColor" && availableForCustomer==false]{name_zh,name_en}`
- Edge-paint colours:
  `*[_type=="edgePaintColor" && availableForCustomer==true]|order(displayOrder asc){name_zh,name_en}`
- Technique notes (limits, what each suits, what moves its price):
  `*[_type=="quoteFinish"]|order(sortOrder asc){label,description_zh,description_en,"notes":strikePlate{whenZh,whenEn,avoidZh,avoidEn,likesZh,likesEn,addOnZh,addOnEn}}`
- Print methods offered: `*[_type=="quotePrintMethod"]|order(sortOrder asc){label,description_zh,description_en}`
- Glossary: `*[_type=="glossaryTerm"]{term_zh,term_en,"text":pt::text(description_zh)}`
- What each order stage means: `*[_type=="orderStageGuide"][0].stages[]{stageKey,meaning_zh,meaning_en,action_zh,action_en}`

Ask only for the fields you need, as above.

## When sources disagree

- Prefer the newer `_updatedAt`. The facts page and the 費用與訂購 / 時程與交件 guides (updated 2026-10-02) are current on lead time and payment: 20–25 working days and full payment before production. The older 承印流程 guide (`printing-process`, 2026-07) still mentions a ten-working-day timeline and a half deposit; don't repeat those.
- For file rules, use the stricter value (see `print-file.md`) and say the studio confirms details when it checks the file.
- Live page versus this skill: the live page wins.

## Snapshot (2026-11-03), for when you can't read the live pages

Say it is a snapshot and give the date.

- Lead time: 20–25 working days for every custom order, counted from the working day after the studio has confirmed the files and received full payment; weekends, public holidays and shipping are not included.
- Contact: info@teleportpress.com; quotes through https://teleportpress.com/order.
- Prices: none in this snapshot. Send the user to the order form or the facts page.

## Ask the studio

When no source answers it (a paper not listed, a size past the press limits, an unusual process, a deadline, a discount), say plainly that you don't know, and suggest the user write to info@teleportpress.com or add the question to 整體備註 on the order form. Don't fill the gap with general letterpress knowledge or another printer's practice: this studio's terms and prices differ. (Looking up other printers for a full-colour job is different: there you report each printer's own pages, read live, as theirs; see `full-colour.md`.)
