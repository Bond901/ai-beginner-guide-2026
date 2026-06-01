# 維護指南（季度刷新 + 新增指南）

AI 工具更新快，本站價值在於「準確 + 夠新」。每季（建議每 3 個月）跑一次「季度刷新」流程；要新增一篇指南時，照「新增一篇指南」一節逐步走完。

## 季度刷新 checklist

逐篇（`guides/*.html`）檢查：

- [ ] 模型版本 / 名稱是否仍正確（例：旗艦模型代號、API 版本）
- [ ] 價格 / 額度 / 免費條款是否變動
- [ ] 功能 / 介面描述是否仍符合現況
- [ ] 外部連結是否失效（官方文件、論文）
- [ ] 截圖 / 範例是否過時

每篇處理後：

- [ ] 更新該篇 `<meta name="last-verified">` 為今天（即使內容沒改）
- [ ] 若有實質改動，另更新 `<meta name="last-updated">`，並在 `UPDATES.md` 補一筆給讀者看的白話說明
- [ ] 同步更新 `index.html` 對應卡片的「驗證日」
- [ ] 若**標題或日期有改**，重跑 `python3 scripts/inject_jsonld.py` 讓 JSON-LD 結構化資料同步
- [ ] 若該篇納入 NotebookLM 公開筆記本，重新整理來源

> 註：搜尋索引（`pagefind/`）與 `sitemap.xml` **已自動化** —— push 到 `main` 後，GitHub Actions（`.github/workflows/reindex.yml`）會自動重建並 commit 回 repo，**不用手動跑**。

## 新增一篇指南

新增一篇 guide 的完整步驟。**內容原則**（來源權威性、語氣、中立性）見 `CONTRIBUTING.md`；本節聚焦「要動哪些檔、順序為何」。

### 1. 建立頁面骨架

- 從現有 `guides/*.html` 複製一份當骨架——**沿用既有結構**，不要自創排版。固定段落順序：Hero → 目錄 → 總覽 → 各工具／章節 → 比較 → 決策 → 起步 → 來源／資料邊界 → footer。
- 共用樣式與腳本一律走 `assets/site.css`、`assets/site.js`，**不要把它們 inline 回單頁**。
- 顏色／間距用 `:root` 的 CSS 變數（design tokens），**不要寫死 hex**——深色模式靠 token 連動切換；新工具配色沿用既有 `--tN-color` / `--tN-bg` token 命名（細節見 `CONTRIBUTING.md`）。

### 2. head meta（必填，**含硬規定**）

每頁 `<head>` 須含下列兩個 `<meta>`（皆 `YYYY-MM-DD`）：

```html
<meta name="last-updated" content="2026-06-01">
<meta name="last-verified" content="2026-06-01">
```

- `last-updated`：內容最後一次實質改動日。
- `last-verified`：最後一次人工核對「仍然正確」的日期；新頁直接填今天。

> 🔴 **`last-verified` 是硬規定，不能漏。** `scripts/gen_sitemap.py` 以它作為 `sitemap.xml` 每筆的 `lastmod`，且**對缺漏採 fail-loud**：只要任一頁缺 `last-verified`，腳本會印出缺漏清單並以 **exit code 1** 中止，**不產生 sitemap**。push 到 `main` 後負責重建索引的 GitHub Actions 會在這一步直接**變紅**、sitemap 產生中止。送出前務必在本機先跑 `python3 scripts/gen_sitemap.py` 確認 exit 0（見第 6 步）。

### 3. 首頁卡片 + 同步寫死的篇數字串

在 `index.html` 對應分類的 `.guide-grid` 內，照既有卡片格式新增一張：

```html
<a href="guides/<新檔名>.html" class="guide-card cat-<分類>">
  <span class="card-arrow">→</span>
  <div class="card-num">入門</div>
  <h3>指南標題</h3>
  <p class="card-desc">一句話描述。</p>
  <div class="card-tags"><span class="tag">標籤</span></div>
  <div class="card-verified">✓ 驗證 2026-06-01</div>
</a>
```

- `cat-<分類>` 用該指南所屬分類（`cat-base` / `cat-tools` / `cat-adv` / `cat-flow`），對應首頁四大分類錨點。
- `card-verified` 的日期 = 該頁 `last-verified`。

**同步更新散落各處的寫死篇數**（目前是「11 篇」，加一篇要一起改成「12 篇」）：

- 該分類標題列的「N 篇 · …」計數（`.cat-meta`）。
- Hero 副標：「…N 篇完整指南帶你快速上手…」。
- Hero 的「N Guides」徽章。
- 索引區開場：「N 篇指南，依主題分成四類…」。
- `<head>` 的 `<meta name="description">` 與 `og:description`（兩處同一句，開頭「…N 篇繁體中文 AI 工具入門指南…」）。

> 改完 `og:description` 後務必重跑第 4 步的 `inject_jsonld.py`——首頁 `WebSite` JSON-LD 的描述由這個 meta 衍生，得一起更新。

### 4. JSON-LD（`CATS` 補一行 → 重跑腳本）

每頁 `<head>` 內含 JSON-LD（首頁 `WebSite`、`about.html` 麵包屑、各 guide `Article` + `BreadcrumbList`），由 `scripts/inject_jsonld.py` 從既有 meta **就地注入**（idempotent，重跑只更新自己注入的區塊）。新增 guide 時：

1. 在 `scripts/inject_jsonld.py` 的 `CATS` 字典補一行：`"<新檔名>.html": ("<分類顯示名>", "<首頁分類錨點>")`（錨點即第 3 步的 `cat-*`）。
2. 跑 `python3 scripts/inject_jsonld.py`。

> 漏補 `CATS` 不會壞站——該頁會被印成 `SKIP (add to CATS)` 跳過，只是少了該頁的 JSON-LD（補上 `CATS` 後重跑即可補回）。

### 5. UPDATES.md 補一筆白話

在 `UPDATES.md` 最上方、當天日期下，補一筆**給讀者看的白話**說明：

```markdown
## 2026-06-01

- 新增指南：**<指南標題>**。
```

### 6. 本機驗證

```bash
python3 scripts/gen_sitemap.py        # 應印出 URL 數、exit 0（缺 last-verified 會在此 fail-loud）
python3 scripts/inject_jsonld.py      # 新頁應顯示 Article+BreadcrumbList，而非 SKIP
python3 -m http.server 8000           # 開 http://localhost:8000/ 預覽：卡片、頁面、搜尋、深色模式
```

（搜尋／JSON-LD 需經 HTTP 服務才正確，勿用 `file://` 直接開檔。）

### 7. 上線

內容合併進 `main` 後即自動發佈。搜尋索引（`pagefind/`）與 `sitemap.xml` **已自動化**——push 到 `main` 後 GitHub Actions（`.github/workflows/reindex.yml`）會自動重建並 commit 回，**不用手動跑**（細節見下節）。

## 搜尋索引 / sitemap（已自動化）

正常情況**不用手動執行**：push 後 Actions 會自動重建 `pagefind/` + `sitemap.xml` 並 commit（commit 訊息帶 `[skip ci]`）。

僅在以下情況需手動（例如本機預覽、或 Actions 暫時故障）：

```bash
python3 scripts/gen_sitemap.py        # 更新 sitemap.xml
npx -y pagefind@1 --site .            # 重建 ./pagefind/（釘 major 版）
git add pagefind sitemap.xml && git commit -m "chore: reindex search [skip ci]"
```

## 過時警示

每篇若 `last-verified` 距今 > 180 天，頁面會自動顯示「可能已變動」提示條（純前端，無需手動）。
