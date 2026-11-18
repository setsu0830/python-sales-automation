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

#end
