# Changelog

本專案所有重要變更皆記錄於此。

格式依循 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [Unreleased]

（尚無未發布變更）

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

[Unreleased]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Bond901/ai-beginner-guide-2026/releases/tag/v1.0.0
