print('以","为分隔')
nn = input('请输入股票代码和股票名称：')
number, name = map(str, nn.split(','))
hl = input('请输入当天的最高价和最低价：')
highest, lower = map(float, hl.split(','))
diff = highest - lower
print("股票代码 + 股票名称： %s + %s" %(number, name))
print("最高价：%.2f,最低价：%.2f,差值：%.2f" %(highest,lower,diff))