# Bin23 有1000元，看中一双勒布朗17，正好活动打8.5折，输入其价格，输出折扣后的价格已经剩下的钱
total = 1000
price = float(input('请输入勒布朗17的价格：')) * 0.85
left = total - price
print("折扣后的勒布朗17的价格：", price)
print("剩下的钱：", left)