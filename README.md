# 時分印刷凸版印刷技能：如何安裝

時分印刷 TeleportPress，台北的凸版印刷工作室。https://teleportpress.com

## 這是什麼

這是一個技能（skill）。技能不是可以直接打開的程式，而是寫給 AI 助理看的工作說明：裝進 Anthropic 的 AI 助理 Claude Code 之後，您用平常說話的方式請 Claude 幫忙，它就會照我們工作室的做法來做。

裝了這個技能，Claude 會：

- 先問清楚報價需要的五件事，缺什麼就一次問完：品項和規格（紙張、油墨、燙金、打凸／打凹、紙邊上色、印哪幾面）、成品尺寸、數量、希望哪一天收到（是不是急件），以及設計由誰做。您有自己的檔案，它就幫您檢查；只有 AI 圖或示意圖，它可以幫您做印刷檔（SVG，也可以在 Illustrator 打開後另存成 .ai）。
- 先告訴您手上的是「示意圖」還是「印刷檔」。照片、AI 生成圖、3D 模擬圖只能看效果，不能直接拿來製版；印刷檔要照實際尺寸、用向量畫，每一個油墨顏色、燙金、打凸都要分開成一個版。
- 幫您做出或檢查印刷檔：成品尺寸、出血、安全距離、文字轉外框、最細線條、印刷機能印的最大尺寸，都照我們的規格。做不到的地方，會清楚列出要改什麼。
- 做示意圖時，只畫我們印得出來的效果：燙金是平滑有光澤的金屬膜，不是凸起的亮粉；打凸不上墨，和印墨的地方分開。
- 照詢價表單（https://teleportpress.com/order）要的內容，整理好品項、尺寸、數量、紙張、每一面的做法，讓您一次填完。
- 價格、紙張、交期這些會變動的資訊，它會先讀我們網站上最新的頁面再回答；網站上找不到的，會請您直接來信 info@teleportpress.com，不會自己編。
- 照片、漸層這類作品要用數位印刷或合版印刷，凸版印刷印不出來。這類訂單一般交給專門的印刷廠比較合適，它會直接告訴您，也可以幫您上網查您附近的印刷廠，列出網址、檔案規格、報價頁和交期。如果您希望由我們仔細檢查檔案、指出要調整的地方，或作品還要燙金、打凸、打凹、模切，我們也可以承接，費用另計。

它不會替您送出詢價，也不會自己報價：價格以我們回覆的報價為準。

## 您需要

- Claude Code：Anthropic 的 AI 助理，可以在您的電腦上讀寫檔案、執行程式（下載和安裝：https://claude.com/claude-code）。
- 想讓 Claude 直接做出印刷檔的話，電腦上要有 Python 3.9 以上。第一次使用時，Claude 會自己安裝需要的套件（fonttools、pymupdf；檢查細線另外需要 opencv-python、numpy、scipy）。
- 只想問問題、整理詢價內容，不需要 Python。

## 安裝

兩種方式，裝哪一種都一樣：

**方式一：下載壓縮檔**

1. 下載 https://teleportpress.com/downloads/teleportpress-letterpress.zip
2. 把壓縮檔解壓縮到 Claude Code 的 skills 資料夾：
   - Mac／Linux：`~/.claude/skills/`
   - Windows：`C:\Users\<您的使用者名稱>\.claude\skills\`
   解壓縮後，skills 資料夾裡會有一個 `teleportpress-letterpress` 資料夾，裡面有 `SKILL.md`。
3. 重新開啟 Claude Code。

**方式二：從 GitHub 取得**

公開的儲存庫在 https://github.com/uthmod/teleportpress-letterpress-skill 。用 git 下載到 skills 資料夾，以後用 `git pull` 就能更新：

```
git clone https://github.com/uthmod/teleportpress-letterpress-skill ~/.claude/skills/teleportpress-letterpress
```

然後重新開啟 Claude Code。

其他支援 Agent Skills 格式的 AI 助理，也可以把 `teleportpress-letterpress` 資料夾放到它讀取技能的資料夾。

## 怎麼用

直接用平常說話的方式告訴 Claude，例如：

- 「這是我用 AI 做的喜帖示意圖，想請時分印刷印 120 張，要準備什麼？」
- 「幫我設計一張雙色凸版名片，做成可以詢價的印刷檔。」
- 「幫我檢查 card-front.pdf 能不能直接拿去做凸版。」
- 「黑色的紙可以印白色的字嗎？」
- 「時分印刷現在交期大概多久？有哪些燙金箔色？」

## 隱私

技能只會讀取我們網站的公開頁面和公開的網站內容資料。除非您自己在詢價表單按下送出，或寄信給我們，否則不會有任何資料傳到時分印刷。

## 授權

時分印刷凸版印刷技能以 CC BY-NC 4.0 授權：https://creativecommons.org/licenses/by-nc/4.0/deed.zh-hant 。可以自由使用和修改，但不能用在商業用途，並請註明出處：時分印刷 TeleportPress（https://teleportpress.com）。全文在 `LICENSE`。

---

# TeleportPress letterpress skill: how to install

TeleportPress 時分印刷 is a letterpress studio in Taipei. https://teleportpress.com

## What this is

A skill: written instructions for an AI assistant, not a program you open. Once it is in Anthropic's AI assistant Claude Code, you ask Claude in plain words and it works the way our studio does:

- It first asks, in one round and only for what's missing, the five things a quote needs: product and specs (paper, inks, foil, emboss/deboss, edge paint, which faces), finished size, quantity, the date you need it (and whether it's a rush), and who is designing. If you have your own files it checks them; if you only have an AI image or a mockup it can make the print file (SVG, or open it in Illustrator and save as .ai).
- It tells you early whether you have a preview (a photo, AI image or render, which can't be used to make plates) or a print file (to scale, vector, one plate per ink colour and per process).
- It makes or checks print files to our rules (finished size, bleed, safe margin, outlined text, minimum line widths, press size limits) and lists exactly what to fix when it can't.
- Its mockups show only effects we can print: foil as a flat glossy film, emboss without ink and apart from the printed areas.
- It prepares a quote request that matches our quote form (https://teleportpress.com/order), so you can fill it in one pass.
- For prices, papers and lead time it reads our live pages first, and says "please ask the studio" (info@teleportpress.com) when they don't cover the question.
- Full-colour work (photos, gradients) needs digital (數位印刷) or gang-run (合版印刷) printing, not letterpress. Those jobs usually suit a specialist printer: it says so plainly and can look some up near you with their links, file specs, quote pages and lead times. We still take them on, at an extra charge, if you want us to check your files carefully and point out what to improve, or if the piece also needs foil, embossing, debossing or die cutting.

It doesn't submit the form for you and doesn't quote prices itself.

## You need

- Claude Code (https://claude.com/claude-code).
- Python 3.9+ if Claude should build print files; it installs the packages it needs (fonttools, pymupdf; opencv-python, numpy and scipy for the thin-line check).

## Install

Either way gives you the same skill.

- **Zip:** download https://teleportpress.com/downloads/teleportpress-letterpress.zip and unzip it into Claude Code's skills folder: `~/.claude/skills/` on Mac/Linux, `C:\Users\<your user name>\.claude\skills\` on Windows. You should see `teleportpress-letterpress/SKILL.md`. Restart Claude Code.
- **GitHub:** the public repo is https://github.com/uthmod/teleportpress-letterpress-skill. Clone it into your skills folder (`git clone https://github.com/uthmod/teleportpress-letterpress-skill ~/.claude/skills/teleportpress-letterpress`), restart Claude Code, and `git pull` to update.

Other assistants that read the Agent Skills format can load the same folder from their own skills folder.

## Try

- "Here's my AI wedding invitation mockup. I want 120 printed by TeleportPress. What do I need?"
- "Design a two-colour letterpress business card and make it ready to quote."
- "Can card-front.pdf go straight to letterpress?"
- "Can you print white text on black paper?"
- "What's TeleportPress's lead time right now, and which foil colours can I pick?"

## Privacy

The skill only reads our public web pages and public site content. Nothing reaches us unless you submit the order form or email us.

## Licence

CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/): free to use and adapt, not for commercial use, with credit to TeleportPress 時分印刷 (https://teleportpress.com). Full text in `LICENSE`.
