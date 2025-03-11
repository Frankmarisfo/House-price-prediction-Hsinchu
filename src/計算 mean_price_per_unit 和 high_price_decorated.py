#計算 mean_price_per_unit 和 high_price_decorated

import pandas as pd
import numpy as np
from sklearn.neighbors import BallTree

# 載入資料集
df = pd.read_csv("dataset_with_distance.csv")

# 確保經緯度是數值型態
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# 移除缺失值，避免 NaN 值影響運算
df = df.dropna(subset=["latitude", "longitude", "price_per_unit"]).reset_index(drop=True)

# 地球半徑 (公里)
R = 6371  

# 轉換為弧度
df["lat_rad"] = np.radians(df["latitude"])
df["lng_rad"] = np.radians(df["longitude"])

# 建立 BallTree 來加速搜尋
tree = BallTree(df[["lat_rad", "lng_rad"]].values, metric="haversine")

# 設定 1 公里內的鄰近房屋
indices = tree.query_radius(df[["lat_rad", "lng_rad"]].values, r=1/R)

# 計算區域內的平均單價
mean_prices = []
for idx_list in indices:
    valid_indices = [i for i in idx_list if i < len(df)]  # 過濾超出範圍的索引
    mean_price = df.loc[valid_indices, "price_per_unit"].mean() if valid_indices else np.nan
    mean_prices.append(mean_price)

df["mean_price_per_unit"] = mean_prices

# 判斷是否為「高價裝潢」
threshold = 1.15  # 設定高於區域內平均單價 15% 為「高價裝潢」
df["high_price_decorated"] = (df["price_per_unit"] > df["mean_price_per_unit"] * threshold).astype(int)

# 儲存處理後的資料
df.to_csv("processed_data.csv", index=False)

print("處理完成，已儲存為 processed_data.csv")
