# Changelog

本專案所有重要變更皆記錄於此。

格式依循 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [Unreleased]

（尚無未發布變更）

## [1.1.0] - 2026-05-29

### Added

- 新增 **Guide 09：Claude Opus 4.8 技術指南**（`guides/claude-opus-4-8-guide.html`）。彙整三份獨立草稿（by Claude / by GPT / by Gemini），以官方第一手為權威骨幹，涵蓋五大功能（Effort Control、Dynamic Workflows、Fast Mode、Mid-conversation System Messages、Adaptive Thinking）、4.6→4.7→4.8 benchmark 軌跡、選型決策樹，以及 4.7→4.8 API 遷移 checklist。衝突數據一律採官方口徑並標註分歧。
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

[Unreleased]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/Bond901/ai-beginner-guide-2026/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Bond901/ai-beginner-guide-2026/releases/tag/v1.0.0
