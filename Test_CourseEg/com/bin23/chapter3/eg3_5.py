import math
cType = int(input('请输入客户类型（小于5为新客户）：'))
price = float(input('请输入标准价格：'))
quantity = int(input('请输入订货量：'))

if cType > 0 and price > 0 and quantity >0:
    if cType < 5:
        if quantity < 800:
            coff = 0
        else:
            coff = 0.02
    else:
        if quantity < 500:
            coff = 0.03
        elif quantity < 1000:
            coff = 0.05
        elif quantity < 2000:
            coff = 0.08
        else:
            coff = 0.1
    pays = quantity * price * (1 - coff)
    print("应付款：",pays)
else:
    print("输入错误！")




