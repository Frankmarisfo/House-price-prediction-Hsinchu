#轉換經緯度為與竹科距離

from geopy.distance import geodesic
import pandas as pd

# 竹科正確座標
hsip_latlng = (24.7816152, 121.0059461)

# 讀取 CSV（請確認路徑）
df = pd.read_csv("dataset_with_coordinates.csv")

# 確保欄位名稱正確，請根據你的 CSV 修改
longitude_col = "經度"  # CSV 中的經度欄位名稱
latitude_col = "緯度"  # CSV 中的緯度欄位名稱

# 確保數據類型正確（可能需要轉換為 float）
df[longitude_col] = df[longitude_col].astype(float)
df[latitude_col] = df[latitude_col].astype(float)

# 計算與竹科的距離
df["與竹科距離_km"] = df.apply(lambda row: geodesic((row[latitude_col], row[longitude_col]), hsip_latlng).km, axis=1)

# 檢查結果
print(df[[latitude_col, longitude_col, "與竹科距離_km"]].head())

# 儲存新 CSV 檔案
df.to_csv("dataset_with_distance.csv", index=False)