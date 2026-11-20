# The quote request

The studio has two online quote forms. Neither needs an account or payment, and both go to the same people at the studio. The formal quote comes by email after the studio has looked at the request.

- **One item, https://teleportpress.com/order, 詢價表單**: the order form. It shows a preliminary estimate after sending, not while filling in. Its English view translates only parts of the page: for a user who can't read Chinese, fill it in for them with the quote spec below, or send the spec to info@teleportpress.com.
- **Several different items, https://teleportpress.com/order-items, 一次詢價多個品項**: one request for a whole job, such as a wedding suite (see "Several items" below).

Your job: collect everything the form asks, so the user can fill it in one pass (or paste it into an email to info@teleportpress.com). Collect it with the one-round interview in SKILL.md step 2 (product and specs, finished size, quantity, lead time, who designs); the quote spec below uses the same five headings. Let the user press 送出 (submit) themselves: it sends emails under their name.

## The form (/order), step by step

Four steps, about five minutes. Field names as of 2026-11-20, when step ② became face by face.

**① 產品類型 Product**
- Product: 名片 name card, 客製信封 envelope, 喜帖 invitation, 卡片 card, 吊牌 hang tag, or 客製需求 for anything else (describe it in 備註).
- 尺寸 (cm) finished size: a preset (名片 9×5.4, 9×5, 方形 5.5×5.5) or 自訂 custom W × H. 客製信封 asks instead for the 展開尺寸 (the flat sheet before folding, flap included) and a complete die drawing with the fold lines marked, sent with the files in step ④.
- 每款數量 quantity per design: 100 / 200 / 300 / 500 / 1000 or any number. 比較其他數量 (optional, up to two) asks for a price at other quantities too.
- 款數 (name cards only): how many different designs. If their quantities differ, write the split in 各款數量分配, e.g. 「款A 100、款B 60」. For other products, describe several designs in 備註.

**② 印刷與加工 Printing and finishing**, in three tabs: ① 正面 front, ② 背面 back, ③ 整張加工 whole sheet.
- On each face, 加一個加工 (then 再加一個加工) adds a row, and its 選加工 menu picks the technique: 凸版印刷, 燙金／燙銀／燙箔, 打凸, 打凹, 壓凹, or 烤松香（烤凸） once the face has 凸版印刷. Each technique once per face; 這是什麼加工？ shows what each one does.
  - 凸版印刷: 選墨色 picks the ink colours on that row. List every colour in the design (background, lines, text): each is its own plate. 印刷版數 = 共用版 (plates every design shares) + 每款各自的版 (plates each design has its own of); the form adds them up, e.g. 「共用 1 版＋每款 1 版 × 3 款 ＝ 4 版」. One plate per ink colour per face (`techniques.md`, plate counting).
  - 燙金: 選燙箔色 picks the foils from the in-stock list (`live-sources.md`); 燙金版數 the same way, one plate per foil colour.
  - 打凸 raised / 打凹 pressed in: a matched pair of dies, no ink; an optional 版面尺寸 W × H cm. The back carries the same shape in reverse, and the form says so.
  - 壓凹: one zinc plate pressed in, no ink; optional 版面尺寸, and 上透明墨 for clear ink (a little more contrast, and the line stays visible in any light).
- 背面 starts with 背面印在哪一張紙上？ on products that can be duplexed: 同一張紙的背面 (the back of the same sheet), 另一張紙（對裱） two sheets, or 三張紙（夾心對裱） three sheets with an unprinted middle. Then its rows, or 背面不加工 for a blank back. The front needs at least one technique; the back needs one or 背面不加工.
- ③ 整張加工 (optional): 刀模軋型 die cutting (special shapes, rounded corners, holes) and 刷邊（紙邊上色） edge paint (all four edges; the colour can be left for the quote). Not both, and no 刷邊 with 打凸 / 打凹. With 對裱 and 打凸 / 打凹, it asks 對裱前 or 對裱後 (pressing before lamination hides the mark on the back). A summary, 印刷與加工的組合, closes the step; with only 打凸 / 打凹 / 壓凹 (no ink, no foil) or with 烤松香, it says the studio prices that combination by hand and the rest is sent as usual.

**③ 紙張選擇 Paper**: pick a paper and its 紙厚度 weight from the list, or type a name under 「找不到紙張，告訴我們」 (the studio prices the closest paper; add a photo of the sample to the file link). A paper is needed to go on: when the user wants the studio to recommend one, pick the nearest and write 「請工作室推薦紙張」 in 備註. Paper the user supplies also goes in 備註. With 對裱 from step ②: 每一張紙用哪一種紙？ sets the paper for each sheet.

**④ 聯絡與送出 Contact and send**
- 姓名, Email, 電話 (all required).
- Optional: 預算範圍 budget; 希望交期 the date they need it (the page notes the usual 20–25 working days from full payment and files, and that an earlier date may carry a rush fee: the studio replies whether it can be done); 檔案連結 a Google Drive or Dropbox link to the print files, shared so anyone with the link can view; 備註 for everything the steps don't ask (版面尺寸 of each plate, shapes, folds, holes, variants): paste the quote spec there.
- 確認詢價內容 opens a summary to check before sending.

## Several items: /order-items

A job with several different items, such as a wedding suite (主卡 main card, 信封 envelope, 回函卡 reply card), goes through https://teleportpress.com/order-items (一次詢價多個品項, linked from the top of /order as 「品項很多？一次上傳規格表」): one request for all of them instead of one form per item. One item in several designs (名片 款數) stays on /order. (After sending, /order also offers 再詢價一個品項, a fresh form with the contact details kept; still send a whole suite here.) The page is zh-TW only, needs no account, and shows no estimate after sending. Fields as of 2026-11-15:

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

- The form's preliminary estimate, shown after sending, is automatic; the studio's emailed quote is the price. Prices are production only: layout and design are separate, paid services. Quotes are before tax.
- Fixed-price everyday products (no waiting for a quote) are in the shop: https://teleportpress.com/shop.
- Only when the user asks for a price: read https://teleportpress.com/facts.html now and quote its indicative range for the item it names, word for word, with the link and "indicative only". Don't add ranges together, scale them, or carry a name-card figure over to another product: for anything the page doesn't list, say the exact price comes in the studio's quote after they send the request (https://teleportpress.com/order).
- What raises a price: more plates (colours, faces, foil colours, designs), larger foil or emboss areas, extra processes, special shapes, and small quantities (plate costs spread over fewer pieces).
- 版面尺寸 is the box around everything on a plate, and foil and emboss plates are priced by their size. A thin foil border near the card edge makes the foil plate as big as the card: tell the user, so they can choose a smaller border or ink for it.

## After sending

1. Preliminary quote by email (初步報價), to check against the budget. Over budget? Say so before booking a visit; the studio proposes cheaper papers or techniques.
2. Formal quotation (正式報價單): accept it on the quotation page (「同意報價並確認下單」) and pay in full; production is scheduled after payment.
3. Upload the print files when asked; the studio checks them and sends a proof to approve before making plates.
4. Production, optional press check (看印) by arrangement, inspection, then shipping or pickup.

Studio visits are by appointment, after a quote: the booking link comes with the quote email. Questions after ordering go in the 「管理訂單」 page's chat. Read https://teleportpress.com/guides/printing-process and the facts page if the user asks about steps; the studio changes them from time to time.
