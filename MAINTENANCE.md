# 維護指南（季度刷新）

AI 工具更新快，本站價值在於「準確 + 夠新」。每季（建議每 3 個月）跑一次以下流程。

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

## 搜尋索引 / sitemap（已自動化）

正常情況**不用手動執行**：push 後 Actions 會自動重建 `pagefind/` + `sitemap.xml` 並 commit（commit 訊息帶 `[skip ci]`）。

僅在以下情況需手動（例如本機預覽、或 Actions 暫時故障）：

```bash
python3 scripts/gen_sitemap.py        # 更新 sitemap.xml
npx -y pagefind@1 --site .            # 重建 ./pagefind/（釘 major 版）
git add pagefind sitemap.xml && git commit -m "chore: reindex search [skip ci]"
```

## 結構化資料 JSON-LD（新增 guide 時）

每頁 `<head>` 內含 JSON-LD（首頁 `WebSite`、`about.html` 麵包屑、各 guide `Article`+`BreadcrumbList`），由 `scripts/inject_jsonld.py` 從既有 meta 產生。

**新增一篇 guide 時：**

1. 在 `scripts/inject_jsonld.py` 的 `CATS` 字典補上 `檔名 → (分類名, 首頁分類錨點)`。
2. 跑 `python3 scripts/inject_jsonld.py`（idempotent，會注入新檔、不重複既有）。

> 漏補 `CATS` 不會壞——該檔會被跳過（印 `SKIP`），只是少了 JSON-LD。

## 過時警示

每篇若 `last-verified` 距今 > 180 天，頁面會自動顯示「可能已變動」提示條（純前端，無需手動）。
