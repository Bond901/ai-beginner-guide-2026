# Changelog

本專案所有重要變更皆記錄於此。

格式依循 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [Unreleased]

（尚無未發布變更）

## [1.13.0] - 2026-05-31

### Added

- 結構化資料 JSON-LD：13 頁 `<head>` 注入 schema.org 結構化資料——首頁 `WebSite`、`about.html` `BreadcrumbList`、11 篇 guide `Article` + `BreadcrumbList`（首頁 → 分類 → 篇名）。協助 Google／AI 搜尋引擎正確理解與顯示（麵包屑路徑、文章作者與日期）。新增 `scripts/inject_jsonld.py`（從既有 meta 衍生、idempotent；FAQ 已於 2026-05 被 Google 停用故未採用）。
- 入口 ②完成：11 篇 guide 頁尾新增「關於 · 編輯原則與方法論」連結（`no-print`、不入搜尋索引），`about.html` 自此全站每頁可達。

### Changed

- `MAINTENANCE.md`：新增 guide 時補 `CATS` + 重跑 `inject_jsonld.py` 的步驟；標題／日期變動後同步重跑。

## [1.12.0] - 2026-05-31

### Added

- 新增「關於 · 方法論」頁 `about.html`：說明本站編輯原則（以官方／原始論文為權威骨幹、衝突標分歧、不臆測、每篇標驗證日）、維護與透明（連 CHANGELOG／CONTRIBUTING／Discussions）、維護者簡介。沿用全站設計系統（深色 hero + 暖紙身 + ⌘K 搜尋 + 深色模式 + 完整 SEO meta），建立內容可信度（E-E-A-T）地基。
- 入口：首頁「關於本站」區塊新增「編輯原則與方法論」連結；首頁頁尾新增「關於 · 方法論」連結。

### Changed

- `scripts/gen_sitemap.py` 納入 `about.html`；`sitemap.xml` 由 12 增為 13 個 URL。

## [1.11.1] - 2026-05-30

### Added

- SEO：`index.html` 加入 Google Search Console 網站驗證 meta（`google-site-verification`），用於驗證 URL-prefix property 並提交 sitemap，以取得實際搜尋字詞與索引狀態。

## [1.11.0] - 2026-05-30

### Added

- CI 自動化：新增 `.github/workflows/reindex.yml`——push 到 `main` 後自動重建 Pagefind 搜尋索引與 `sitemap.xml` 並 commit 回 repo（commit 帶 `[skip ci]`），消除手動維護步驟。採 A1 commit-back（保持 branch-based Pages，workflow 失敗時網站仍照常部署）。
- 新增 `.nojekyll`：確保 `pagefind/` 等靜態資產不被 GitHub Pages 的 Jekyll 處理（靜態站標準做法）。

### Changed

- `pagefind` 在 CI 釘 major 版 `pagefind@1`，避免未來 2.0 破壞性改版無聲破壞索引流程。
- 更新 `MAINTENANCE.md` / `CONTRIBUTING.md`：手動 reindex/sitemap 步驟改註明「已自動化」，僅保留為 fallback。

## [1.10.0] - 2026-05-30

### Added

- 社群入口：新增 `CONTRIBUTING.md`（貢獻指南——回報過時／錯誤、內容準確與來源原則、新增指南的格式與維護步驟、範圍與授權）；並於 GitHub 啟用 **Discussions** 討論區，供讀者問答、許願與回報過時內容（近零維護）。

## [1.9.2] - 2026-05-30

### Changed

- 首頁 `description` / `og:description` 由 87 字補長至 150 字（涵蓋各篇主題與「免費、附原始來源、標註驗證日」），落入社群分享／SEO 建議的最佳長度（110–160 字）。

## [1.9.1] - 2026-05-30

### Added

- 新增 Open Graph 社群分享圖 `assets/og.png`（1200×630 品牌橫幅），與生成用的 `assets/og-banner.html`。`og:image` 自此有縮圖，分享卡完整呈現。

## [1.9.0] - 2026-05-30

### Added

- **SEO 基礎**：12 頁 `<head>` 加入 `meta description`、`canonical`、Open Graph（og:type/site_name/locale/title/description/url/image）與 Twitter Card（`summary_large_image`）；新增 `robots.txt` 與 `sitemap.xml`（12 URL，`lastmod` 取自各頁最後驗證日），以及 `scripts/gen_sitemap.py`（加課程後重跑即自動更新 sitemap）。社群分享縮圖 `assets/og.png` 另行產出。

## [1.8.1] - 2026-05-30

### Changed

- **重構（行為不變）**：將各頁**完全相同**的 chrome 樣式（內容新鮮度、⌘K 搜尋面板與結果 chip、主題切換鈕）抽出為共用 `assets/site.css`；各頁的 `:root` tokens、bespoke 樣式、per-file 深色覆蓋與 `search-fab` 位置仍保留 inline（深色覆蓋以選擇器 specificity 勝出，不受 base 移到外部檔影響）。配合 1.8.0 的 `assets/site.js`，搜尋／深色／新鮮度／面板樣式自此皆為單一來源。

## [1.8.0] - 2026-05-30

### Changed

- **重構（行為不變）**：將各頁**完全相同**的前端腳本（主題切換、內容新鮮度、⌘K 搜尋指令面板）抽出為單一共用檔 `assets/site.js`，並以自身 script URL 推導站台根目錄達成**頁面無關**（同一檔在首頁與 `/guides/` 皆正確運作）；移除 12 頁的重複 inline 腳本。日後維護這些功能只需改 1 個檔案而非 12 個。FOUC 早期主題判斷與 `copyPageURL` 仍保留 inline。

## [1.7.2] - 2026-05-30

### Changed

- 指南頁新鮮度標示改為**條件顯示**：永遠顯示「最後更新」，僅當「最後驗證」日期**晚於**「最後更新」時才追加顯示，避免兩者相同時的視覺重複（季度刷新後自然分岔才秀出價值）。內嵌備援日期與 `<meta>` 同步，消除載入時的短暫閃動。

## [1.7.1] - 2026-05-30

### Fixed

- 搜尋結果點擊後 404：Pagefind 索引回傳的網址已內含專案路徑前綴（`/ai-beginner-guide-2026/…`），原程式又重複套上站台基底造成雙重前綴。改為先偵測網址是否已含基底路徑以避免重複，並相容無前綴的索引格式（兩種皆正確解析）。

## [1.7.0] - 2026-05-30

### Added

- **深色模式**（中性純黑風格）：跟隨系統 `prefers-color-scheme` 自動切換，並於右上角提供手動「日／夜」切換鈕，選擇記憶於 `localStorage`。涵蓋全部 12 頁（hero、分類卡、搜尋面板、程式碼框、表格、callout 等），明暗兩模式文字對比皆達 WCAG AA。深色樣式以 `@media screen` 包裹，**列印一律維持亮色**；並以 head 內早期 inline script 避免切換閃爍（FOUC）。

## [1.6.5] - 2026-05-30

### Changed

- 搜尋入口改為右下角**懸浮圖示鈕**（與「回首頁／回頂部」整合成一致的控制群組），移除各頁內嵌的大型搜尋框；點圖示或 `⌘K`／`/` 皆可開啟指令面板。
- 搜尋結果加入**相關性雙門檻**（`score ≥ max(1.0, 0.2×最高分)`），過濾亂數／低相關查詢的雜訊（例：輸入「333」不再回傳整頁低分結果）。

## [1.6.4] - 2026-05-30

### Changed

- 站內搜尋改為自製 **⌘K 指令面板**（取代 Pagefind 內建 Default UI）：彈窗式、鍵盤導航（`⌘K`／`/` 開啟、`↑↓` 瀏覽、`Enter` 開啟、`Esc` 關閉），每筆結果以「圖示＋標題＋分類標籤」精簡呈現，套用站體暖色系與四大分類配色。
- 改用 Pagefind **JS Search API** 自行渲染結果，並以**絕對 URL** 解析 bundle 與結果連結，徹底解決 GitHub Pages 專案頁子路徑問題。

## [1.6.3] - 2026-05-30

### Fixed

- 搜尋介面誤用簡體中文（如「找到 N 个…相关结果」「正在搜索」）：改為完整繁體中文 UI 字串（搜尋中、清除、載入更多、無結果、鍵盤提示等）。
- 搜尋結果摘要擷取頁面程式碼、雜亂且間隔過大：改為精簡呈現「標題 ＋ 分類 · 難度」（例：基礎觀念 · 入門），關閉結果縮圖並收緊間距。

### Changed

- 各指南頁加入 `data-pagefind-meta`（`tag:分類 · 難度`）供搜尋結果顯示；重建搜尋索引。

## [1.6.2] - 2026-05-30

### Fixed

- 站內搜尋仍無法載入（`Module name 'pagefind/pagefind.js' does not resolve to a valid URL`）：v1.6.1 改用的相對 `bundlePath` 在動態 `import()` 中被視為無效的 bare module specifier。本版改為在執行時從已載入的 `pagefind-ui.js` 之 `src` 推導**絕對** bundle 路徑（`new PagefindUI` 之前計算），於 GitHub Pages 子路徑、`localhost` 與自訂網域皆適用。

## [1.6.1] - 2026-05-30

### Fixed

- 站內搜尋在 GitHub Pages 專案頁（子路徑）無法載入（`Could not load search bundle: /pagefind/`）：由 Pagefind 元件式 UI 改為 Default UI 並指定相對 `bundlePath`，修正絕對路徑（root `/pagefind/`）解析錯誤；搜尋框尺寸一併校正。
- 各指南「最後更新／最後驗證」誤顯示為發布當日：改採 git 歷史的真實最後變更日（2026-05-29），首頁卡片同步。

## [1.6.0] - 2026-05-30

### Added

- **站內搜尋**：整合 Pagefind（純靜態、無後端、支援中文分詞）。首頁內嵌搜尋框、各指南頁可開搜尋彈窗；搜尋索引（`pagefind/`）隨站一同部署。
- **隱私友善訪客統計**：加入 GoatCounter（無 cookie、不收集個資、無需同意條），用於了解哪些指南較常被閱讀，作為後續更新優先序的依據。
- **內容新鮮度機制**：每篇指南顯示「最後更新／最後驗證」日期（由 `<meta>` 單一來源驅動）；當最後驗證距今超過 180 天，自動顯示「內容可能已變動」提示條。首頁各卡片標示驗證日期。
- `MAINTENANCE.md`：季度刷新檢查清單（模型版本／價格／功能／連結失效等），維持內容準確與時效。

### Changed

- 統一所有頁面 `<html lang>` 為 `zh-Hant`，改善中文搜尋分詞與語意正確性。

## [1.5.0] - 2026-05-30

### Added

- 首頁 hero 下方新增 **NotebookLM 公開筆記本** banner：一鍵開啟以本站內容建立的公開 NotebookLM 筆記本，可互動問答、找重點、生成 Audio Overview（語音導覽）。
- 首頁新增「依程度／目的」路徑導引（path strip）：完全新手／想用某個平台／想做 agent·自動化 三條入口，點擊直接跳至對應分類。
- `README.md` 新增「用 NotebookLM 互動學習」段落與公開筆記本連結。

### Changed

- 首頁指南區改為**四大主題分類**呈現（基礎觀念／平台工具／進階·Agent 擴充／流程·應用），每類獨立標題與配色，解決課程增加後版面凌亂的問題。
- 移除每張卡片的全站連續序號（原 Guide 01–11），改以「類別＋難度（入門／工具／進階）」標示，日後新增課程不必重新編號。
- 以精簡的「怎麼開始（依程度／目的）」取代原本冗長的九項「推薦閱讀順序」（`index.html` 與 `README.md` 同步）。

## [1.4.0] - 2026-05-29

### Added

- 新增 **Guide 11：RAG 檢索增強生成 完整指南**（`guides/rag-guide-2026.html`）。以原始論文與官方文件為權威骨幹彙整，涵蓋 Chunking → Embedding → Retrieval → Generation → Evaluation 五階段管線、Naive→Advanced→Modular 架構演進、CRAG / Self-RAG / GraphRAG / Agentic 進階架構、常見失敗模式與對策、安全風險與治理（OWASP / NIST）、RAG vs. Long Context 決策，以及附原始論文與官方來源、詞彙表與資料邊界。衝突數據一律以原始論文／第一手來源為準並標註分歧。

### Changed

- `index.html`：新增第 11 張 guide 卡片（teal `c11` 配色）、hero 改為「11 Guides」、推薦閱讀順序加入 RAG。
- `README.md`：指南列表新增 RAG 一列、推薦閱讀順序加入並重新編號（1–9）、總述改為「11 篇」。
- 統一各指南頁與紀錄文件的來源描述用語，僅保留「以官方／原始論文為權威骨幹」的權威性陳述。

## [1.3.1] - 2026-05-29

### Fixed

- 修正 Guide 03（AI 個人化設定）在首頁卡片與 `README.md` 的平台標示：「Gemini」更正為 **Antigravity**（該課程內容為 Antigravity 的 `GEMINI.md` 設定檔，非 Gemini App）。

### Added

- Guide 01（LLM 核心概念）Token 段補充 tokenizer 演進說明（ConvexTok，arXiv:2605.22821），並標明為漸進式改良、非革命性。

## [1.3.0] - 2026-05-29

### Added

- 新增 **Guide 10：Claude Code Skills 技術指南**（`guides/claude-code-skills-guide.html`）。以官方文件為權威骨幹，涵蓋三層漸進式載入、SKILL.md 結構與 frontmatter、存放位置與叫用控制、字串替換／動態上下文／subagent、Skill vs CLAUDE.md vs Prompt 比較、內建 bundled skills 與各平台差異、最佳實務、安全性、決策樹與起步範例。

### Changed

- `index.html`：新增第 10 張 guide 卡片（slate `c10` 配色）、hero 改為「10 Guides」、推薦閱讀順序加入 Claude Code Skills。
- `README.md`：指南列表新增 Claude Code Skills 一列、推薦閱讀順序加入並重新編號（1–8）、總述改為「10 篇」。

## [1.2.0] - 2026-05-29

### Added

- 每篇指南頂部新增「匯出 / 分享列」：一鍵**匯出 PDF**（透過瀏覽器列印 → 另存 PDF）、**開啟 NotebookLM**、**複製本頁網址**，方便讀者存檔、加入自己的 NotebookLM 筆記本或分享連結。
- 列印樣式表（`@media print`）：匯出 PDF 時自動隱藏互動元件與懸浮按鈕，並避免表格跨頁切斷列、程式碼區塊溢出。

### Changed

- 提升次要文字色彩對比至 WCAG AA（調深 `--muted`），改善可讀性與無障礙。
- Claude Opus 4.8 技術指南更新為彙整完整版，並與其餘指南統一加入上述「匯出 / 分享列」。

## [1.1.0] - 2026-05-29

### Added

- 新增 **Guide 09：Claude Opus 4.8 技術指南**（`guides/claude-opus-4-8-guide.html`）。以官方第一手為權威骨幹彙整，涵蓋五大功能（Effort Control、Dynamic Workflows、Fast Mode、Mid-conversation System Messages、Adaptive Thinking）、4.6→4.7→4.8 benchmark 軌跡、選型決策樹，以及 4.7→4.8 API 遷移 checklist。衝突數據一律採官方口徑並標註分歧。
- 全部 9 篇 guide 右下角新增「回到首頁」懸浮按鈕（連至 `index.html`），位於既有「回到頂部」按鈕上方；採 SVG house icon 確保跨字型一致顯示。
- 為 `guides/claude-opus-4-8-guide.html` 補上「回到頂部」懸浮按鈕與對應 script，使 9 篇行為一致。
- 新增 `.gitignore` 規則忽略 `.DS_Store`、`Thumbs.db`。

### Changed

- `index.html`：新增第 9 張 guide 卡片（紅色 `c9` 配色變數）、hero 改為「9 Guides」、推薦閱讀順序加入 Opus 4.8、hero 與「關於本站」更新日期改為 `2026-05-29`。
- `README.md`：指南列表新增 Opus 4.8 一列、推薦閱讀順序重新編號（1–7）、總述由「8 篇」改為「9 篇」。

## [1.0.0] - 2026-05-27

### Added

- 首次發布：8 篇繁體中文 AI 入門指南、首頁總覽（`index.html`）與 `README.md`。
- 指南清單：LLM 核心概念、Prompt Engineering 演進、AI 個人化設定精煉、Claude Desktop 入門、OpenAI 三工具入門、Google Gemini 生態系、AI Agent 擴充機制、AI 時代軟體開發流程。
- 每篇 guide 右下角「回到頂部」懸浮按鈕。
- MIT License。

[Unreleased]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.13.0...HEAD
[1.13.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.12.0...v1.13.0
[1.12.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.11.1...v1.12.0
[1.11.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.11.0...v1.11.1
[1.11.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.10.0...v1.11.0
[1.10.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.9.2...v1.10.0
[1.9.2]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.9.1...v1.9.2
[1.9.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.9.0...v1.9.1
[1.9.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.8.1...v1.9.0
[1.8.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.8.0...v1.8.1
[1.8.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.7.2...v1.8.0
[1.7.2]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.7.1...v1.7.2
[1.7.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.6.5...v1.7.0
[1.6.5]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.6.4...v1.6.5
[1.6.4]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.6.3...v1.6.4
[1.6.3]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.6.2...v1.6.3
[1.6.2]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.6.1...v1.6.2
[1.6.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.6.0...v1.6.1
[1.6.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Bond901/ai-beginner-guide-2026/releases/tag/v1.0.0
