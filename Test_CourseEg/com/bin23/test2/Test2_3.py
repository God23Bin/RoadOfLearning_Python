print("希望在孩子满10周岁（120个月）时能够提取5万元用于教育")
print("计算在孩子出生时该投资多少钱来购买基金，使得孩子10周岁时能取回5万元用于教育")
print("月数120个月")
monthNum = 12
print("最终金额50,000元")
finalMoney = 500000
monthIncomeRate = eval(input("输入你的月收益率"))
investment = finalMoney/pow((1+monthIncomeRate),monthNum)
print("所需投资金额为",end="")
print(investment)
