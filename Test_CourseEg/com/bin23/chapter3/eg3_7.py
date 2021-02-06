fSale = float(input("请输入订单的销售额："))
sumSales = 0

while fSale > 0:
    sumSales += fSale
    fSale = float(input("请输入下一个订单的销售额："))

print("商品的销售总额为：", sumSales)