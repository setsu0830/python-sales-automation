sales1 = [
    {"name": "りんご", "price": 150, "quantity": 3},
    {"name": "みかん", "price": 100, "quantity": 5},
    {"name": "りんご", "price": 150, "quantity": 2},
    {"name": "ばなな", "price": 200, "quantity": 4},
]

sales2 = [
    {"name": "ぶどう", "price": 500, "quantity": 2},
    {"name": "りんご", "price": 150, "quantity": 4},
    {"name": "ぶどう", "price": 500, "quantity": 1},
]

#売上集計関数
def calculate_sales(sales):
    total = {}
    #集計処理
    for item in sales:
        name = item["name"]
        amount = item["price"] * item["quantity"]

        if name not in total:
            total[name] = 0

        total[name] += amount

    return total

#集計出力関数
def print_sales(title,result):
    #文字列出力
    print(f"【{title}】")
    for name, amount in result.items():
        print(f"{name}: {amount}円")
    print()

result1 = calculate_sales(sales1)
result2 = calculate_sales(sales2)

#集計出力
data_str1 = "出力データ1"
data_str2 = "出力データ2"

print_sales(data_str1,result1)
print_sales(data_str2,result2)

#end
