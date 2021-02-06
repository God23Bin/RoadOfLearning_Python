# 1. 在购买某物品时，若标明的价钱x在下面范围内，所付钱y按对应折扣支付，其数学表达式如下,编程实现
# x < 1000时， y=x
# 1000 <= x < 2000 时， y = 0.9x
# 2000 <= x < 3000 时， y = 0.8x
# x >= 3000 时， y = 0.7x

def calc_pay(x):
    if x < 1000:
        pay = x
    elif 1000 <= x < 2000:
        pay = 0.9 * x
    elif 2000 <= x < 3000:
        pay = 0.8 * x
    else:
        pay = 0.7 * x
    return pay


if __name__ == '__main__':
    p1 = calc_pay(500)
    p2 = calc_pay(1500)
    p3 = calc_pay(2500)
    p4 = calc_pay(3500)

    print('500块的付{}，1500块的付{}，2500块的付{}，3500块的付{}'.format(p1, p2, p3, p4))
