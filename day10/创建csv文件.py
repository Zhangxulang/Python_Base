# 作者: 大数据 浪哥
# 2025年07月17日21时45分49秒
# 1054074422@qq.com


import csv

data = [
    ["日期", "门店", "品类", "销售额"],
    ["2025-07-01", "A店", "饮料", 1000],
    ["2025-07-01", "A店", "零食", 1500],
    ["2025-07-01", "B店", "饮料", 800],
    ["2025-07-02", "A店", "饮料", 1200],
    ["2025-07-02", "B店", "零食", 1800]
]

with open("sales.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV 文件创建成功！")