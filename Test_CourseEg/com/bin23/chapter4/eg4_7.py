client = {'A': 0.9, 'B': 0.92, 'C': 9.5, 'D': 1.00}
degree = input('请输入客户等级（A-D or a-d）：')
orderNum = input('请输入订货量：')

while degree != '' and orderNum != '' and degree.upper() in ['A', 'B', 'C', 'D'] and orderNum.isdigit():
    discount1 = client[degree.upper()]
    orderNum = int(orderNum)
    if orderNum < 500:
        discount2 = 0
    elif orderNum < 2000:
        discount2 = 0.05
    elif orderNum < 5000:
        discount2 = 0.1
    elif orderNum < 20000:
        discount2 = 0.15
    else:
        discount2 = 0.2
    total = 100 * orderNum * (discount1) * (1 - discount2)
    print('客户等级折扣为：', discount1)
    print('订货量折扣为：', discount2)
    print('订货金额为：', total)
    degree = input('请输入客户等级（A-D or a-d）：')
    orderNum = input('请输入订货量：')
else:
    print('请输入正确的信息')
