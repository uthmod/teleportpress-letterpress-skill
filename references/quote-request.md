# The quote request

The studio's order form is https://teleportpress.com/order (詢價). It takes about five minutes, needs no account and no payment, and shows a live price range once size, quantity and one technique are filled in. The formal quote comes by email after the studio has looked at the request. Field names below are from the zh-TW form as of 2026-11-03; the English page may still show an older layout asking for the same facts.

Your job: collect everything the form asks, in its order, so the user can fill it in one pass (or paste it into an email to info@teleportpress.com). Collect it with the one-round interview in SKILL.md step 2 (product and specs, finished size, quantity, lead time, who designs); the quote spec below uses the same five headings. Let the user press 送出 (submit) themselves: it sends emails under their name.

## The form, section by section

**① 從哪裡開始 Where to start**
- 我想做… product: 名片 name card, 喜帖 invitation, 卡片 card, 信封 envelope, 紅包袋 red packet, 吊牌 hang tag. Only used to suggest examples; it doesn't change the price. Anything else: pick the closest and explain in 整體備註.
- Start from: A an example the studio has made, B 上傳設計稿 a picture of your design (JPG, PNG or a phone photo, up to 10 MB, one per face; for quoting only, never printed), or blank.

**② 每一面要做什麼 What each face gets**
- 成品尺寸 finished size, W × H in cm (e.g. 9 × 5.4).
- Per face (正面 front, 背面 back; 對裱 adds a sheet, up to three sheets), tick the techniques:
  - 凸版印刷: how many colours (1–3 on the form; more goes in 整體備註), each colour's name (a Pantone U code if known) and its 版面尺寸 (W × H cm of the area that colour covers, not the whole card).
  - 燙金: the foil colours (one plate each), each with its 版面尺寸.
  - 打凸 emboss: its 版面尺寸.
  - 打凹 deboss (pressed into the paper, no ink; the box right under 打凸): its 版面尺寸. The price engine has no 打凹 price yet, so the form's live range leaves it out and says the studio quotes it after seeing the design. A deboss in 透明墨 clear ink: tick 打凹 and say "clear ink" in 整體備註.
  - 紙邊上色: whole piece, no size.
- An area covering half the face or more triggers a question about large solids, large foil or large emboss. Answer it honestly (see `techniques.md`).
- The drawing board's 框範圍 frames and 拼貼 collage pieces offer the same techniques, 打凹 included.
- Drawn frames on the form's drawing board fill in 版面尺寸 for you. If you built plates with `scripts/make_plates.py`, its `plates.json` lists each plate's 版面尺寸.
- 版面尺寸 is the box around everything on that plate, and foil and emboss plates are priced by their size. A thin foil border near the card edge makes the foil plate as big as the card: tell the user, so they can choose a smaller border or ink for it.

**③ 紙張、數量、裁切與成型 Paper, quantity, cutting and forming**
- 紙張 paper: search by name, or 「請幫我推薦」 (recommend one), or 「我會自備紙材」 (I'll supply my own).
- 數量 quantity: 100 / 200 / 300 / 500 / 1000 or any number.
- 外形 shape: 直角 square corners, 圓角 rounded corners, 特殊外形（需刀模） special shape (needs a die). 摺 fold: 不摺 or 對摺（加壓線） folded in half with a crease. 黏 glue: 不黏 or 信封・紅包袋（摺黏成型）, then a template: 直式紅包袋 9×18, 橫式紅包袋 19×9, 西式尖角信封 16×11.5, 西式尖角信封 18.5×13.3, 中式直式信封 13.3×18.5, 自訂尺寸 custom, 我有自己的展開圖 my own flat die drawing. 打孔 holes: a number (holes are cut by a die).
- 款式 variants: several designs? write each one's difference and quantity, e.g. 「A 款 王小明 200 張、B 款 李小華 100 張，紙和做法都一樣」.
- 整體備註 overall note: anything else, e.g. "logo in bright gold, text in dark blue", thermography, a press check, file status.

**④ 聯絡方式與交件細節 Contact and delivery**
- Email (required), 姓名 name, 電話 phone, 公司／品牌 company (optional).
- 希望哪一天收到 the date you need it. The page notes the usual 20–25 working days from confirmed files; an earlier date is fine to enter: the studio replies whether it can be done.
- 發票 invoice: 個人（二聯） personal or 公司（三聯） company with 統一編號 tax ID and 發票抬頭 title.
- 取件 pickup: 寄送 ship (address) or 到店自取 collect at the studio.
- 設計檔雲端連結 a Google Drive or Dropbox link to the print files (shared so anyone with the link can view).

## Quote spec template

The same five headings as the interview (SKILL.md step 2). Fill it in the user's language; keep the studio's zh-TW terms in brackets. Every line gets a value, a default you named, "請工作室推薦 studio to recommend", or "不需要 none".

```
TeleportPress 時分印刷 詢價內容 Quote request

1. 品項與規格 Product and specs
   品項 Product: 名片 name card   款式 Variants: 1 (or: A 款 … 張, B 款 … 張)
   紙張 Paper: [name + weight, or 請幫我推薦]   對裱 Duplex: none / 2 sheets: 正面 … + 背面 …
   正面 Front:
     凸版印刷: 2 colours: PANTONE 2766 U (版面 5 × 4 cm), PANTONE 7621 U (版面 1.5 × 3.5 cm)
     燙金: none | 打凸: none | 打凹: none
   背面 Back: none
   紙邊上色 Edge paint: none   外形 Shape: 直角 square corners
2. 成品尺寸 Finished size: 9 × 5.4 cm
3. 數量 Quantity: 300
4. 交期 Lead time: 希望收到 [date, or "no fixed date"]; rush: [no / yes, needed by …]
   (studio standard 20–25 working days from confirmed files and payment; the studio replies whether a date works)
5. 設計與檔案 Design and files
   設計 Designer: [the user / their designer / made by the assistant from an AI image or mockup]
   印刷檔 Print file: ready, 2 plate files (SVG/PDF, or .ai) at [link] | needs file prep 需要製作印刷檔: [what is missing]
備註 Notes: [anything else; risks the user accepted, e.g. large solid area]
```

## Prices

- The form's range is an automatic estimate; the studio's emailed quote is the price. Prices are production only: layout and design are separate, paid services. Quotes are before tax.
- Fixed-price everyday products (no waiting for a quote) are in the shop: https://teleportpress.com/shop.
- Only when the user asks for a price: read https://teleportpress.com/facts.html now and quote its indicative range for the item it names, word for word, with the link and "indicative only". Don't add ranges together, scale them, or carry a name-card figure over to another product: for anything the page doesn't list, send the user to the form's live range.
- What raises a price: more plates (colours, faces, foil colours, designs), larger foil or emboss areas, extra processes, special shapes, and small quantities (plate costs spread over fewer pieces).

## After sending

1. Preliminary quote by email (初步報價), to check against the budget. Over budget? Say so before booking a visit; the studio proposes cheaper papers or techniques.
2. Formal quotation (正式報價單): accept it on the quotation page (「同意報價並確認下單」) and pay in full; production is scheduled after payment.
3. Upload the print files when asked; the studio checks them and sends a proof to approve before making plates.
4. Production, optional press check (看印) by arrangement, inspection, then shipping or pickup.

Studio visits are by appointment, after a quote: the booking link comes with the quote email. Questions after ordering go in the 「管理訂單」 page's chat. Read https://teleportpress.com/guides/printing-process and the facts page if the user asks about steps; the studio changes them from time to time.
