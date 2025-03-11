#新增鄰里資訊

import pandas as pd
import requests
import time

# Google Maps API 金鑰
API_KEY = "你的API金鑰"

# 讀取房價資料
df = pd.read_csv("dataset.csv")

# 定義函數：查詢 Google Maps API，獲取「里」
def get_village(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url).json()
    
    if response["status"] == "OK":
        for comp in response["results"][0]["address_components"]:
            if "administrative_area_level_3" in comp["types"]:  # 台灣的「里」
                return comp["long_name"]
    
    return None  # 找不到則回傳 None

# 批量查詢，每次間隔 0.5 秒以防止 API 限制
df["里名"] = df["土地位置建物門牌"].apply(lambda x: get_village(x) if pd.notnull(x) else None)
time.sleep(0.5)  # 讓 API 有時間處理

# 存回 CSV
df.to_csv("updated_housing_data.csv", index=False)

print("已成功取得所有地址的『里』資訊！")
