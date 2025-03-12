import pandas as pd
import requests
import time

def get_village(address, api_key):
    """使用 Google Maps API 取得地址的里名"""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url).json()
    
    if response.get("status") == "OK":
        for comp in response["results"][0]["address_components"]:
            if "administrative_area_level_3" in comp["types"]:  # 台灣的「里」
                return comp["long_name"]
    
    return None  # 找不到則回傳 None

def add_village_info(input_path, output_path, api_key):
    """讀取房價資料，新增里名資訊，並儲存結果"""
    df = pd.read_csv(input_path)

    # 確保「土地位置建物門牌」欄位存在
    if "土地位置建物門牌" not in df.columns:
        raise ValueError("找不到『土地位置建物門牌』欄位，請確認 CSV 檔案內容！")

    # 批量查詢，每次間隔 0.5 秒以防止 API 限制
    df["里名"] = df["土地位置建物門牌"].apply(lambda x: get_village(x, api_key) if pd.notnull(x) else None)
    time.sleep(0.5)

    df.to_csv(output_path, index=False)
    print(f"已成功取得所有地址的『里』資訊！結果已儲存至 {output_path}")

# 範例使用方式
if __name__ == "__main__":
    input_path = "data/dataset.csv"
    output_path = "data/updated_housing_data.csv"
    api_key = "你的_API_Key"  # <== 請更換為你的 API Key
    add_village_info(input_path, output_path, api_key)