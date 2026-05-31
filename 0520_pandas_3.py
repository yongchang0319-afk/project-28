import pandas as pd

# 1. 讀取資料與檢視
# 備註：請將下載的資料檔案與此腳本放於同一資料夾，或使用絕對路徑
file_path = "SuperMarket Analysis.csv"
df = pd.read_csv(file_path)

print("===== 1. 檢視資料筆數與前幾筆內容 =====")
print(f"總資料筆數: {len(df)} 筆")
print("\n前 5 筆資料內容:")
print(df.head())
print("-" * 50)

# 2. 篩選出 Branch 為 A 開頭 且 Customer type 為 Member 的交易資料
# 使用 .str.startswith('A') 確保篩選 A 開頭的 Branch
filtered_df = df[(df['Branch'].str.startswith('A', na=False)) & (df['Customer type'] == 'Member')]
print("\n===== 2. 篩選特定交易資料 (Branch A開頭 & Member) =====")
print(f"符合條件的交易筆數: {len(filtered_df)} 筆")
print(filtered_df.head())
print("-" * 50)

# 3. 以 Product line 為單位，計算各產品線的總銷售額 (Sales) 與平均評分 (Rating)
# 使用 agg 進行不同欄位的不同聚合計算，並四捨五入至小數後 2 位
product_summary = df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2).reset_index()

print("\n===== 3. 各產品線銷售額與平均評分彙總 =====")
print(product_summary)
print("-" * 50)

# 4. 依 City 與 Gender 分組，計算平均銷售額與交易筆數
city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Invoice ID', 'count') # 或者使用任意非空欄位計算筆數
).round(2).reset_index()

print("\n===== 4. 依 City 與 Gender 分組分析 =====")
print(city_gender_summary)
print("-" * 50)

# 5. 找出總銷售額最高的產品線
# 使用 idxmax() 找到 Total_Sales 最大值所在的索引
top_product = product_summary.loc[product_summary['Total_Sales'].idxmax()]
print("\n===== 5. 總銷售額最高的產品線 =====")
print(f"最高銷售額產品線: {top_product['Product line']}")
print(f"總銷售金額: {top_product['Total_Sales']}")
print("-" * 50)

# 6. 將各產品線的銷售與評分彙總結果輸出為 0520_pandas_3OK.CSV 檔案
output_file = "0520_pandas_3OK.CSV"
# encoding='utf-8-sig' 可確保若產品線有名稱包含特殊字元或中文時，在 Excel 開啟不會亂碼
product_summary.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n===== 6. 匯出成功 =====\n已將彙總結果輸出至檔案: {output_file}")