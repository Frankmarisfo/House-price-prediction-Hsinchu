#轉換門牌為經緯度

import googlemaps
import pandas as pd
import time

# 你的 Google Maps API Key（請換成你的 API Key）
API_KEY = "你的_API_Key"

# 初始化 Google Maps 客戶端
gmaps = googlemaps.Client(key=API_KEY)

# 讀取 CSV 檔案
file_path = "原始資料.csv"  # 修改成你的 CSV 檔案路徑
df = pd.read_csv(file_path)

# 創建兩個新欄位存放經緯度
df["latitude"] = None
df["longitude"] = None

# 批量轉換地址為經緯度
for index, row in df.iterrows():
    address = row["土地位置建物門牌"] + ", 台灣"  # 確保包含「台灣」
    
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]["geometry"]["location"]
            df.at[index, "latitude"] = location["lat"]
            df.at[index, "longitude"] = location["lng"]
        
        # 避免 API 限制，每次請求間隔 0.5 秒
        time.sleep(0.5)
    
    except Exception as e:
        print(f"無法解析 {address}: {e}")

# 儲存結果為新 CSV 檔案
output_path = "/mnt/data/dataset_with_coordinates.csv"
df.to_csv(output_path, index=False)
print(f"轉換完成，已儲存為 {output_path}")