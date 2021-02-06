
def single(money, year_money_rate, n_year):
    s_money = money * (1 + n_year * 100/100) * year_money_rate
    print("单利：", s_money)

def more_and_more(money, year_money_rate, n_year):
    m_money = money * (1 + n_year * 100 / 100) ** year_money_rate
    print("复利：", m_money)


if __name__ == '__main__':
    money = 1000
    year_money_rate = 10
    year = 3
    print("本金", money)
    print("年利率" + str(year_money_rate) + "%")
    print("存款年限", year)
    single(money, year_money_rate, year)
    more_and_more(money, year_money_rate, year)
