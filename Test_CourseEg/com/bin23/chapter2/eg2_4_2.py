import math
x = input('请输入复数的实部和虚部，用","隔开：')
a, b = map(float,x.split(','))
c = math.sqrt(a ** 2 + b ** 2)
print("输入的复数为：" + str(a) + " + " + str(b) + "j","模为" + str(c))