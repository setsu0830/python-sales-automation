import csv
from sales import calculate_sales, print_sales

sales = []
#CSVファイルの読み込み
with open("sales.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        #辞書を作成してsalesに追加
        item = {
            "name":row["name"],
            "price":int(row["price"]),
            "quantity":int(row["quantity"])
        }
        sales.append(item)

result = calculate_sales(sales)

print_sales("CSV売上データ",result)
#CSVファイルへの書き込み
with open("result.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    #ヘッダーを書き込む
    writer.writerow(["name","total"])
    #データを書き込む
    for name, amount in result.items():
        #商品名と売上金額を書き込む
        writer.writerow([name,amount])

    
