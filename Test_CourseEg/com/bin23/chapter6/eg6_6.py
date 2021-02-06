def futureValue(money, yearRate, year):
    monthRate = yearRate/12
    value = money * (1 + monthRate) ** (year * 12)
    return value

money = 1000
numerator = float(input("请输入年回报率（百分号之前的数）："))
yearRate = numerator/100

print("投资额：" + str(money), "\n年回报率：" + str(numerator) + "%")
print("年份", "投资的未来价值")
for year in range(1, 11):
    x = futureValue(money, yearRate, year)
    print("%2d" % year, "%10.2f" % x)