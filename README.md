# 房價預測系統

本專案提供一個基於 Python 的房價預測系統，允許使用者輸入房屋資訊，並透過統計數據與機器學習方法預測房屋總價。

## 1. 安裝與環境設置

### 1.1 先決條件
本專案使用 `pandas` 和 `numpy` 來處理數據，請確保您的環境已安裝 Python 3 及相關套件。

### 1.2 安裝必要套件
使用以下命令安裝必要的 Python 套件：
```bash
pip install pandas numpy
```

## 2. 使用方式

### 2.1 執行方式
1. 執行 `python main.py`，系統會提示您依序輸入房屋資訊。
2. 根據輸入數據，系統將計算單價，並預測房屋的總價。
3. 預測結果會顯示在終端機。

## 3. 數據輸入與處理流程

### 3.1 使用者輸入
使用者需要手動輸入房屋相關資訊，包括但不限於：
- 土地與建物面積
- 交易時間
- 車位資訊
- 建物類型與用途
- 是否有管理組織、電梯、特殊交易
- 經緯度與距離竹科的距離

### 3.2 數據驗證與預處理
在數據輸入過程中，系統會對數據進行驗證與轉換：
- 確保數值型數據的有效性
- 使用 One-Hot Encoding 來處理分類變數，如建物型態與都市土地使用分區
- 使用 Target Encoding 為區名與里名創建數值特徵
- 根據歷史數據計算 `district_village_interaction` 互動特徵

## 4. 預測流程

### 4.1 讀取參考價格表
- 使用 `price_lookup_table.csv` 來獲取歷史均價，若無匹配則使用全局均價。

### 4.2 計算單價與總價
- 使用歷史均價計算 `log_unit_price`
- 根據 `average_unit_price` 預測房屋總價

### 4.3 輸出結果
- 預測的平均單價 (元/平方公尺)
- 預測總價 (元)

## 5. 參考資料

- `price_lookup_table.csv`：存放歷史平均單價數據
- `test.csv`：訓練數據集，提供 Target Encoding 參考值

## 6. 直接在 Google Colab 執行  
點擊下方連結，在 Google Colab 中運行 Notebook：  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TP7jo9xLGEq1XrKEAo4Jw9ADn2L0-yN7?usp=sharing)

## 7. 版權與許可

本專案僅供學術研究與個人使用，未經授權請勿用於商業用途。
