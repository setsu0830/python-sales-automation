import csv
import sys

#関数のインポート
from sales import calculate_sales, print_sales
from pathlib import Path

base_dir = Path(__file__).resolve().parent
readfilepath = base_dir / "data"
writefilepath = base_dir / "result.csv"
csv_files = list(readfilepath.glob("*.csv"))
#テストコード
print(readfilepath)

#ファイルチェック
if not csv_files:
    print("CSVファイルが見つかりませんでした。")
    sys.exit()

#集計結果のリスト
sales = []

#CSVファイルの読み込み
for file in csv_files:
    print(file.name)
    with open(file,"r",encoding="utf-8",newline="") as files:
        reader = csv.DictReader(files)

        for row in reader:
            #辞書を作成してsalesに追加
            item = {
                "name":row["name"],
                "price":int(row["price"]),
                "quantity":int(row["quantity"])
            }
            sales.append(item)

result = calculate_sales(sales)

#CSVファイルへの書き込み
with open(writefilepath, "w", encoding="utf-8", newline="") as files:
    writer = csv.writer(files)
    #ヘッダーを書き込む
    writer.writerow(["name","total"])
    #データを書き込む
    for name, amount in result.items():
        #商品名と売上金額を書き込む
        writer.writerow([name,amount])

#集計結果を出力
print_sales("CSV売上データ",result)

    
