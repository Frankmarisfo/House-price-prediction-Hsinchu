import googlemaps
import pandas as pd
import time
from config import API_KEY  # 從 config.py 匯入 API Key

# 初始化 Google Maps 客戶端
gmaps = googlemaps.Client(key=API_KEY)

def convert_address_to_coordinates(input_file, output_file):
    """ 讀取 CSV 並將門牌地址轉換為經緯度 """
    df = pd.read_csv(input_file)

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
    df.to_csv(output_file, index=False)
    print(f"轉換完成，已儲存為 {output_file}")

# 範例使用方式
if __name__ == "__main__":
    input_path = "data/raw_data.csv"  # 修改成你的 CSV 檔案路徑
    output_path = "data/dataset_with_coordinates.csv"
    convert_address_to_coordinates(input_path, output_path)
