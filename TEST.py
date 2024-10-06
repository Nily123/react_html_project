import pandas as pd
from collections import OrderedDict
import datetime

# 假設你已經有一個現有的 CSV 檔案叫做 "user_results.csv"
csv_file = "D:/test.csv"

# 假設你已經有一個包含新結果的有序字典
new_result = OrderedDict({
    "ID": None,  # 這裡的 ID 會在後面生成
    "DateTime": None,  # 這裡的 DateTime 會在後面生成
    "Gender": "Male",
    "Age": "30~40",
    "BlackSpot": False,
    "wrinkled": True,
    "Brand": "B",
    "Product_name": "BX-III"
})

# 讀取現有的 CSV 檔案到 DataFrame
df = pd.read_csv(csv_file)

# 生成唯一的 ID，你可以根據需要調整 ID 的生成方式
# 這裡使用 DataFrame 的行數作為 ID，你可以根據你的需求進行更複雜的 ID 生成
new_result["ID"] = len(df) + 1

# 獲取當前日期時間
now = datetime.datetime.now()
new_result["DateTime"] = now.strftime("%Y-%m-%d %H:%M:%S")

# 將新結果添加到 DataFrame
df = df.append(new_result, ignore_index=True)

# 將更新後的 DataFrame 保存回 CSV 檔案
df.to_csv(csv_file, index=False)