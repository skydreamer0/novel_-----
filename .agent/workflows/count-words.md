---
description: 計算指定目錄或檔案的中文字數
---

這個工作流會統計 Markdown 檔案中的字數，包括總字數（不含空白）以及純中文字數。

### 使用方法

1. **統計全書字數 (3000字檢查)**
// turbo
```bash
python3 .agent/scripts/word_count.py 正文 3000
```

2. **匯出 CSV 報表**
// turbo
```bash
python3 .agent/scripts/word_count.py 正文 3000 字數統計.csv
```

3. **統計特定目錄或檔案**
```bash
python3 .agent/scripts/word_count.py <路徑>
```

3. **統計大綱字數**
// turbo
```bash
python3 .agent/scripts/word_count.py 大綱
```

### 輸出說明
- **Total**: 總字數（排除空白字元，包含標點符號）。
- **Chinese**: 純中文字數（僅包含 Unicode 範圍內的漢字）。
- **Status**: 如果設定了門檻（如 3000），會標示是否達標。
