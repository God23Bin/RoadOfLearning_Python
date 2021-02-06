import math
price = int(input('请输入标准价格：'))
quantity = int(input('请输入订货量：'))

if quantity < 0:
    coff = -1
elif quantity < 300:
    coff = 0.0
elif quantity < 500:
    coff = 0.03
elif quantity < 1000:
    coff = 0.05
elif quantity < 2000:
    coff = 0.08
else:
    coff = 0.1

if quantity >=0 and price >= 0:
    pays = quantity * price * (1 - coff)
    print("支付金额：",pays)
else:
    print("输入的订货量与标准价格不能小于0！")




