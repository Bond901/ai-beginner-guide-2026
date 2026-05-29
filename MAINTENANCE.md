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
- [ ] 若有實質改動，另更新 `<meta name="last-updated">` + 寫 `CHANGELOG.md`
- [ ] 同步更新 `index.html` 對應卡片的「驗證日」
- [ ] 內容有改 → 重跑搜尋索引：`npx -y pagefind --site .` 後 commit `pagefind/`
- [ ] 若該篇納入 NotebookLM 公開筆記本，重新整理來源

## 搜尋索引（每次內容變動後）

```bash
npx -y pagefind --site .      # 重建 ./pagefind/
git add pagefind && git commit -m "chore: reindex search"
```

## 過時警示

每篇若 `last-verified` 距今 > 180 天，頁面會自動顯示「可能已變動」提示條（純前端，無需手動）。
