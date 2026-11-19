# The quote request

The studio has three online quote forms. None needs an account or payment, and all go to the same people at the studio. The formal quote comes by email after the studio has looked at the request.

- **One item, https://teleportpress.com/order-v2, 新版詢價表單（測試版）**: the new form, a beta that is still changing, in zh-TW only. The user marks what each face gets, on a drawing board if they like, and sees a live price range once size, quantity and one technique are filled in.
- **One item, https://teleportpress.com/order, 原本的詢價表單**: the original form. Its English view translates only parts of the page. It shows a preliminary estimate after sending, not while filling in.
- **Several different items, https://teleportpress.com/order-items, 一次詢價多個品項**: one request for a whole job, such as a wedding suite (see "Several items" below).

For one item, offer both forms and say plainly that the new one is a beta. Suggest the new form when the user isn't sure which techniques to use, has no design file yet, or wants to see a price range as they go. Suggest the original form when they would rather use the settled one or can't read Chinese (fill it in for them with the quote spec below, or send the spec to info@teleportpress.com). Both ask for the same facts under different labels: 希望哪一天收到 / 希望交期 (date), 設計檔雲端連結 / 檔案連結 (file link), 整體備註 / 備註 (notes).

Your job: collect everything the form asks, so the user can fill it in one pass (or paste it into an email to info@teleportpress.com). Collect it with the one-round interview in SKILL.md step 2 (product and specs, finished size, quantity, lead time, who designs); the quote spec below uses the same five headings. Let the user press 送出 (submit) themselves: it sends emails under their name.

## The new form (/order-v2), section by section

Field names as of 2026-11-19.

**① 從哪裡開始 Where to start**
- 我想做… product: 名片 name card, 喜帖 invitation, 卡片 card, 信封 envelope, 紅包袋 red packet, 吊牌 hang tag. Picking one fills in its usual size and cutting, both of which can be changed. Anything else: pick the closest and explain in 整體備註.
- Start from: A an example the studio has made, B 上傳我的設計稿 a picture of the design (JPG, PNG or a phone photo, up to 10 MB, one per face; for quoting only, never printed), or 從空白開始 blank.

**② 每一面要做什麼 What each face gets**
- 成品尺寸 finished size, W × H in cm (e.g. 9 × 5.4).
- Per face (正面 front, 背面 back; 對裱 adds a sheet, up to three sheets), tick the techniques:
  - 凸版印刷: how many colours (1–3 on the form; more goes in 整體備註), each colour's name (a Pantone U code if known) and its 版面尺寸 (W × H cm of the area that colour covers, not the whole card).
  - 燙金: the foil colours (one plate each), each with its 版面尺寸.
  - 打凸 emboss: its 版面尺寸.
  - 打凹 deboss (pressed into the paper by a matched pair of plates, no ink): its 版面尺寸. It is priced exactly like 打凸, so it is in the form's live range and a blank size widens the range the same way.
  - 壓凹 (pressed into the paper by a single plate, no ink): its 版面尺寸. Tick 上透明墨 under it for clear ink, which raises the contrast slightly so the line doesn't break up under different light; it adds an ink fee.
  - 紙邊上色: whole piece, no size.
- An area covering half the face or more triggers a question about large solids, large foil, large emboss or large deboss. Answer it honestly (see `techniques.md`).
- The drawing board's 框範圍 frames and 拼貼 collage pieces offer the same techniques.
- Drawn frames on the form's drawing board fill in 版面尺寸 for you. If you built plates with `scripts/make_plates.py`, its `plates.json` lists each plate's 版面尺寸.

**③ 紙張、數量、裁切與成型 Paper, quantity, cutting and forming**
- 紙張 paper: search by name and pick a 磅數 weight, or 「請幫我推薦」 (recommend one), or 「我會自備紙材」 (I'll supply my own).
- 數量 quantity: 100 / 200 / 300 / 500 / 1000 or any number.
- 外形 shape: 直角 square corners, 圓角 rounded corners, 特殊外形（需刀模） special shape (needs a die). 摺 fold: 不摺 or 對摺（加壓線） folded in half with a crease. 黏 glue: 不黏 or 信封・紅包袋（摺黏成型）, then a template: 直式紅包袋 9×18, 橫式紅包袋 19×9, 西式尖角信封 16×11.5, 西式尖角信封 18.5×13.3, 中式直式信封 13.3×18.5, 自訂尺寸 custom, 我有自己的展開圖 my own flat die drawing. 打孔 holes: a number (holes are cut by a die; the stock 紅包袋 dies take none, so holes need 自訂尺寸).
- 款式 variants: several designs? write each one's difference and quantity, e.g. 「A 款 王小明 200 張、B 款 李小華 100 張，紙和做法都一樣」.
- 整體備註 overall note: anything else, e.g. "logo in bright gold, text in dark blue", thermography, a press check, file status.

**④ 聯絡方式與交件細節 Contact and delivery**
- Email (required), 姓名 name, 電話 phone, 公司／品牌 company (optional).
- 希望哪一天收到 the date you need it. The page notes the usual 20–25 working days from confirmed files; an earlier date is fine to enter: the studio replies whether it can be done.
- 發票 invoice: 個人（二聯） personal or 公司（三聯） company with 統一編號 tax ID and 發票抬頭 title.
- 取件 pickup: 寄送 ship (address) or 到店自取 collect at the studio.
- 設計檔雲端連結 a Google Drive or Dropbox link to the print files (shared so anyone with the link can view).

## The original form (/order), step by step

About five minutes, in four to six steps depending on the product. Field names as of 2026-11-15.

**① 產品類型 Product**
- Product: 名片 name card, 客製信封 envelope, 喜帖 invitation, 卡片 card, 吊牌 hang tag, or 客製需求 for anything else (describe it in 備註).
- 尺寸 (cm) finished size: a preset (名片 9×5.4, 9×5, 方形 5.5×5.5) or 自訂 custom W × H. 客製信封 asks instead for the 展開尺寸 (the flat sheet before folding, flap included) and a complete die drawing with the fold lines marked, sent with the files in step ⑥.
- 每款數量 quantity per design: 100 / 200 / 300 / 500 / 1000 or any number. 比較其他數量 (optional, up to two) asks for a price at other quantities too.
- 款數 (name cards only): how many different designs. If their quantities differ, write the split in 各款數量分配, e.g. 「款A 100、款B 60」. For other products, describe several designs in 備註.

**② 印刷與加工 Printing and finishing** (tap each technique into 已選)
- 凸版印刷, with 印刷版數 (1版, 2版, or 3版以上 and the actual number): one plate per ink colour per face (`techniques.md`, plate counting).
- 燙金, with 燙金版數: one plate per foil colour; the colours come in step ③.
- 打凸 / 打凹: one choice for both. Mark the areas in the file (their own layer or a note) and say in 備註 which it is (凸 raised, 凹 pressed in); a deboss in 透明墨 clear ink goes in 備註 too.
- 烤松香（烤凸） thermography: needs at least one 凸版印刷 plate.
- 刷邊（紙邊上色） edge paint: all four edges; the colour can be left for the quote. Not with 刀模軋型 or 打凸 / 打凹.
- 對裱 duplex: the number of sheets and each sheet's paper come in step ④. With 打凸 / 打凹 as well, the form asks 凸 or 凹, front or back, and 對裱前 or 對裱後 (pressing before lamination hides the dent on the back).
- 刀模軋型 die cutting: special shapes, rounded corners, holes.
- 哪幾面有加工？: 正面 front, 背面 back, or both.

**③ 選燙箔色 Foil colours** (only with 燙金): pick from the in-stock list (`live-sources.md`).

**④ 紙張選擇 Paper**: pick a paper and its 紙厚度 weight from the list, or type a name under 「找不到紙張，告訴我們」 (the studio prices the closest paper; add a photo of the sample to the file link). A paper is needed to go on: when the user wants the studio to recommend one, pick the nearest and write 「請工作室推薦紙張」 in 備註. Paper the user supplies also goes in 備註. With 對裱: 對裱層數 (how many sheets) and the paper for each.

**⑤ 墨色選擇 Ink colours** (only with 凸版印刷): pick colours or type a Pantone U code or a description. List every colour in the design (background, lines, text): each is its own plate. 跳過 skips the step.

**⑥ 聯絡與送出 Contact and send**
- 姓名, Email, 電話 (all required).
- Optional: 預算範圍 budget; 希望交期 the date they need it (the page notes the usual 20–25 working days from full payment and files, and that an earlier date may carry a rush fee: the studio replies whether it can be done); 檔案連結 a Google Drive or Dropbox link to the print files, shared so anyone with the link can view; 備註 for everything the steps don't ask (版面尺寸 of each plate, shapes, folds, holes, variants): paste the quote spec there.
- 確認詢價內容 opens a summary to check before sending.

## Several items: /order-items

A job with several different items, such as a wedding suite (主卡 main card, 信封 envelope, 回函卡 reply card), goes through https://teleportpress.com/order-items (一次詢價多個品項, linked from the top of /order as 「品項很多？一次上傳規格表」): one request for all of them instead of one form per item. One item in several designs (名片 款數, or 款式 on the new form) stays on a one-item form. The page is zh-TW only, needs no account, and shows no estimate after sending. Fields as of 2026-11-15:

**① 上傳規格檔** (optional): PDF, .ai saved PDF-compatible, or photos; up to 10 files, 30 MB each, the first 30 pages read. SVG is refused: upload the PDF `make_plates.py` writes. A bigger file goes on a cloud drive, its link in 檔案雲端連結. An AI reads the pages to find each item's 數量 and 尺寸 (the page says the files don't train models).

**② 品項表**: one row per item, up to 30. A row needs 品項名稱 (30 characters at most), 數量 and 完成尺寸 長 × 寬 (cm); the other columns are optional (使用紙張, 印製方法, 正面版數, 背面版數, 燙金（版數）, 紙邊上色, 打凸, 軋型, 對裱, 烤松香, 其它). The AI marks every 數量 or 尺寸 it can't find on the pages; the user fills those cells. 「一次貼上多個品項」 adds the rows at once from one line per item, `名稱，數量，尺寸`, e.g. `名片，300，9×5.4 cm` (anything after the size goes to 其它), or from a sheet copied out of Excel or Google Sheets (the page has a 規格表範本).

**③ 聯絡資料**: 姓名, 聯絡電話, Email (required); optional 希望收件日期 (the page notes about 20–25 working days of production), 印刷預算, 檔案雲端連結, 取貨方式 (來店自取 or 宅配), 從哪裡知道我們, 備註 (4,000 characters at most).

**④ 確認送出**: an item missing its 數量 or 尺寸 can still be sent, but the studio then quotes an estimated figure, and a corrected re-quote joins the back of the queue. Give every item both.

Prepare: the quote spec below once per item (one block each), one paste line per item for ②, and the print files as PDF for ①. The spec blocks go in 備註. After 送出 the page shows a 需求編號 (request number); the studio checks each item against the files and emails the quote.

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

- The new form's live range and the original form's preliminary estimate (shown after sending) are automatic; the studio's emailed quote is the price. Prices are production only: layout and design are separate, paid services. Quotes are before tax.
- Fixed-price everyday products (no waiting for a quote) are in the shop: https://teleportpress.com/shop.
- Only when the user asks for a price: read https://teleportpress.com/facts.html now and quote its indicative range for the item it names, word for word, with the link and "indicative only". Don't add ranges together, scale them, or carry a name-card figure over to another product: for anything the page doesn't list, send the user to the new form's live range (https://teleportpress.com/order-v2, a beta), and say the exact price comes in the studio's quote after they send the request.
- What raises a price: more plates (colours, faces, foil colours, designs), larger foil or emboss areas, extra processes, special shapes, and small quantities (plate costs spread over fewer pieces).
- 版面尺寸 is the box around everything on a plate, and foil and emboss plates are priced by their size. A thin foil border near the card edge makes the foil plate as big as the card: tell the user, so they can choose a smaller border or ink for it.

## After sending

1. Preliminary quote by email (初步報價), to check against the budget. Over budget? Say so before booking a visit; the studio proposes cheaper papers or techniques.
2. Formal quotation (正式報價單): accept it on the quotation page (「同意報價並確認下單」) and pay in full; production is scheduled after payment.
3. Upload the print files when asked; the studio checks them and sends a proof to approve before making plates.
4. Production, optional press check (看印) by arrangement, inspection, then shipping or pickup.

Studio visits are by appointment, after a quote: the booking link comes with the quote email. Questions after ordering go in the 「管理訂單」 page's chat. Read https://teleportpress.com/guides/printing-process and the facts page if the user asks about steps; the studio changes them from time to time.
