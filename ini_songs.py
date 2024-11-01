# -*- coding: utf-8 -*-
"""ini_songs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cx8H4-lcIOyANlE0sFvsd9JUxUKFIxK9
"""

import pandas as pd
import random

file_path = '/Book1.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(file_path, sheet_name=sheet_name)

items = df.iloc[:, 0].dropna().tolist()

points = {item: 0 for item in items}

rounds = len(items) * 2

for _ in range(rounds):
    item1, item2 = random.sample(items, 2)

    print(f"choose 1: {item1} or 2: {item2}")
    choice = input( "choose (1 or 2): ")

    if choice == "1":
        points[item1] += 1
    elif choice == "2":
        points[item2] += 1
    else:
        print("無効な入力です。もう一度選択してください。")

ranking = sorted(points.items(), key=lambda x: x[1], reverse=True)

print("\nランキング:")
for i, (item, score) in enumerate(ranking, start=1):
    print(f"{i}位: {item} - {score} 点")

output_df = pd.DataFrame(ranking, columns=['項目', 'ポイント'])
output_df.to_excel("ranking_output.xlsx", index=False)

