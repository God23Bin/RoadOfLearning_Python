import math
a = input('请输入复数的实部：')
b = input('请输入复数的虚部：')
c = math.sqrt(float(a) ** 2 + float(b) ** 2)
print("输入的复数为：" + a + " + " + b + "j","模为" + str(c))