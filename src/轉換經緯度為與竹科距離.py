from geopy.distance import geodesic
import pandas as pd

# 竹科座標
HSIP_LATLNG = (24.7816152, 121.0059461)

def calculate_distance_to_hsip(input_path, output_path, latitude_col="latitude", longitude_col="longitude"):
    """計算每筆資料與竹科的距離"""
    df = pd.read_csv(input_path)

    # 確保欄位存在
    if latitude_col not in df.columns or longitude_col not in df.columns:
        raise ValueError(f"找不到指定的經緯度欄位：{latitude_col}, {longitude_col}")

    # 確保數據類型正確
    df[longitude_col] = df[longitude_col].astype(float)
    df[latitude_col] = df[latitude_col].astype(float)

    # 計算與竹科的距離
    df["與竹科距離_km"] = df.apply(lambda row: geodesic((row[latitude_col], row[longitude_col]), HSIP_LATLNG).km, axis=1)

    # 儲存新 CSV 檔案
    df.to_csv(output_path, index=False)
    print(f"距離計算完成！結果已儲存至 {output_path}")

# 範例使用方式
if __name__ == "__main__":
    input_path = "data/dataset_with_coordinates.csv"
    output_path = "data/dataset_with_distance.csv"
    calculate_distance_to_hsip(input_path, output_path)