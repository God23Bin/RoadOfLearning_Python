# 带else的循环语句
sales = [5000, 3000, 8000, 10600, 6000, 5000]

for i in sales:
    if i >= 6000:
        print("第一个大于等于6000的销售额是：", i)
        break
else:
    print("未找到")