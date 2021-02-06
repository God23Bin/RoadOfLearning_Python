# 2. 买地铁车票的规定如下：乘1-4站，3元/位；乘5-9站，4元/位；乘9站以上，5元/位.输入人数、站数，输出应付款。（25分）

people_count = 0
station_count = 0
pay = 0

def calc_payment(people_count, station_count):
    if 1 <= station_count <= 4:
        pay = 3 * people_count
    elif 5 <= station_count <= 9:
        pay = 4 * people_count
    else:
        pay = 5 * people_count
    return pay

if __name__ == '__main__':
    p_s = eval(input("请输入人数、站数："))
    payment = calc_payment(p_s[0], p_s[1])
    print("需要支付", payment, "元")

