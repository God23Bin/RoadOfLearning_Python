# 25. 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

def calc_profit_to_money(profit, award):
    if profit <= 10:
        money = award * (1 + 0.1)
    elif 10 < profit <= 20:
        money = award * (1 + 0.075)
    elif 20 < profit <= 40:
        money = award * (1 + 0.05)
    elif 40 < profit <= 60:
        money = award * (1 + 0.03)
    elif 60 < profit <= 100:
        money = award * (1 + 0.015)
    else:
        money = award * (1 + 0.01)
    return money

if __name__ == '__main__':
    profit = eval(input("输入当月利润(万):"))
    money = calc_profit_to_money(profit, 2) # 奖金默认2万
    print(money)