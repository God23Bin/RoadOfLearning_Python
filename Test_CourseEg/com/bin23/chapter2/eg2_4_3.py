import math
x = input('请输入复数的实部和虚部，用","隔开：')
a, b = map(float,x.split(','))
m = complex(a, b)
c = abs(m)
print("输入的复数为：" + str(m), "模为" + str(c))