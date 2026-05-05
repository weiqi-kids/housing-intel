# Housing Intel - 房地產供應鏈情報追蹤

## 專案狀態：🔵 初始建立 (2026-04-14)

專案剛完成初始建立，尚未進入自動化階段。

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **股價抓取** | 追蹤公司股票，Yahoo Finance | 🔲 待建立 |
| **新聞爬蟲** | 涵蓋 27 家公司 + 4 檔 ETF | 🔲 待建立 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | ✅ 從模板複製 |
| **報告生成** | 每日報告、7 日報告 | ✅ 從模板複製 |
| **前端** | D3.js Dashboard、供應鏈圖、事件時間軸 | ✅ 從模板複製 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 🔲 待設定 |

---

## 追蹤範圍

### 公司 (27 家 + 4 檔 ETF)

**上游 - 建材/鋼鐵/機械** (9 家)
- 台灣水泥(1101.TW)、亞洲水泥(1102.TW)、台灣玻璃(1802.TW)
- 東和鋼鐵(2006.TW)、日本製鐵(5401.T)
- CRH(NYSE)、Vulcan Materials(VMC NYSE)
- Caterpillar(CAT NYSE)、Saint-Gobain(SGO.PA)

**中游 - 營建/住宅建商** (18 家)
- 台灣：國建(2501.TW)、華固(2548.TW)、長虹(5534.TW)、興富發(2542.TW)、潤泰新(9945.TW)、冠德(2520.TW)、遠雄(5522.TW)、皇翔(2545.TW)、三圓(4416.TW)
- 美國：D.R. Horton(DHI)、Lennar(LEN)、PulteGroup(PHM)、Toll Brothers(TOL)、KB Home(KBH)、NVR(NVR)
- 日本：大和房屋(1925.T)、積水房屋(1928.T)、住友林業(1911.T)

**下游 - ETF**
- VNQ、XLRE、XHB、ITB

### 主題 (configs/topics.yml)

- 新屋開工 (housing_starts)
- 房貸利率 (mortgage_rates)
- 土地價格 (land_price)
- 營建成本 (construction_cost)
- REIT 殖利率 (reit_yield)
- 財報 (earnings)
- 展望 (guidance)

---

## 標準流程

```
fetch_news.py
    │
    ├─→ data/raw/{date}/news.jsonl    (原始抓取資料)
    │
    └─→ enrich_event.py
            │
            └─→ data/events/{date}.jsonl  (標準格式，唯一資料源)
                    │
            ┌───────┴───────────────┐
            │                       │
      sync_to_frontend.py     generate_metrics.py
            │                       │
            │                 data/metrics/{date}.json
            │                       │
            │                 generate_7d_report.py
            │                       │
            │                 reports/7d/{date}.json
            │                       │
      site/data/events.json   site/data/reports/7d/{date}.json
```

### 執行順序

1. `fetch_news.py` - 抓取所有公司新聞，輸出到 `data/raw/`
2. `enrich_event.py` - 標註事件，輸出到 `data/events/`（**唯一資料源**）
3. `generate_metrics.py` - 計算每日指標
4. `generate_7d_report.py` - 生成 7 日報告
5. `sync_to_frontend.py` - 同步事件到前端
6. `update_baselines.py` - 更新歷史基準線（最後執行）

**重要**：
- `data/events/*.jsonl` 是唯一的事件資料源
- 前端的 `site/data/events.json` 由 `sync_to_frontend.py` 生成
- 不要直接寫入 `site/data/events.json`

---

## 資料夾結構

```
housing-intel/
├── lib/                        # 規則引擎
│   ├── __init__.py
│   ├── matcher.py              # 關鍵字匹配
│   ├── sentiment.py            # 情緒分析
│   ├── scorer.py               # 重要性評分
│   └── anomaly.py              # 異常偵測
│
├── scripts/                    # 執行腳本
│   ├── fetch_news.py           # 整合抓取
│   ├── fetch_stocks.py         # 股價抓取
│   ├── enrich_event.py         # 事件標註
│   ├── generate_metrics.py     # 每日指標
│   ├── detect_anomalies.py     # 異常偵測
│   ├── generate_daily.py       # 每日報告
│   ├── generate_7d_report.py   # 7 日報告
│   ├── sync_to_frontend.py     # 同步事件到前端
│   └── update_baselines.py     # 更新基準線
│
├── configs/                    # 設定檔
│   ├── companies.yml           # 27 家公司 + 上下游關係
│   ├── topics.yml              # 主題 + 關鍵字
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   └── anomaly_rules.yml       # 異常偵測規則
│
├── fetchers/                   # 公司新聞爬蟲（待建立）
│
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件
│   ├── metrics/                # 每日指標
│   ├── baselines/              # 歷史基準線
│   ├── normalized/             # 股價資料
│   ├── financials/             # 財務數據
│   ├── holders/                # 持股資料
│   └── fund_flow/              # 資金流向
│
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
│
├── site/
│   ├── index.html              # D3.js Dashboard
│   └── data/                   # 前端資料
│
└── CLAUDE.md
```

---

## 快速啟動

```bash
cd repos/housing-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 6230 -d site

# 瀏覽器開啟
open http://localhost:6230
```

---

## 故障排除

### 常見問題

1. **GitHub Actions 失敗**
   - 檢查 `gh run view <run-id> --log-failed`
   - 常見原因：網站結構變更、API 限制

2. **爬蟲抓不到資料**
   - 檢查目標網站是否改版
   - 更新 `fetchers/` 對應的爬蟲

3. **前端資料未更新**
   - 確認 `sync_to_frontend.py` 有執行
   - 檢查 `site/data/events.json` 時間戳


---


## 前端同步規則

`site/index.html` 所有 repo 共用同一份程式碼，由 `weiqi-kids/intel-template` 統一管理。

**禁止直接修改本 repo 的 index.html。** 修改流程：
1. 在 `memory-intel` 開發和測試
2. 複製到 `intel-template/site/index.html` 並 push
3. `sync-downstream.yml` 會自動向本 repo 建 PR
4. Merge PR 完成同步

## 每日例行（進入此 repo 時自動提醒）

當你讀取此 CLAUDE.md 時，主動執行以下檢查並提醒用戶：

### 自動檢查清單

1. **同步最新** — `git pull origin main`
2. **今日 Actions 狀態** — `gh run list --limit 1`
3. **今日事件數** — `wc -l data/events/$(date +%Y-%m-%d).jsonl`
4. **關鍵字審計** — 讀取 `site/data/reports/daily/$(date +%Y-%m-%d).json` 的 `filter_audit` 欄位

### 提醒格式

```
📋 每日狀態
- Actions: ✅/❌
- 今日事件: N 筆
- 關鍵字審計: ✅ 通過 / ⚠️ gate2 擋住率 XX%，建議檢視
```

若 `filter_audit.alert` 為 true 或 `gate2_block_rate > 30%`，提醒用戶：「有關鍵字需要調整，要執行關鍵字審計嗎？」

### 關鍵字審計流程（用戶確認後執行）

1. 檢視 `filter_audit.gate2_samples` 中被擋住的文章標題
2. 判斷每篇是否與本追蹤產業相關
3. 相關的文章 → 找出缺少的關鍵字，建議新增到 `configs/topics.yml`
4. 呈現結果：

```
## 關鍵字審計結果

通過率：XX% | Gate 2 擋住率：XX%

### 被擋住但應通過的文章
| 標題 | 缺少的關鍵字 | 建議加入的主題 |
|------|-------------|--------------|

### 建議新增關鍵字
topics.yml → {topic_id} → keywords 新增：
- keyword1
- keyword2
```

5. 用戶確認後更新 `configs/topics.yml`，commit + push

