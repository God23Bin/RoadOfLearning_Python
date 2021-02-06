# 求正整数阶乘的函数
def jc(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

# 求阶乘和的函数
def sjc(n):
    ss = 0
    for i in range(1, n + 1):
        ss += jc(i)
    return ss

# 主程序

i = int(input("输入整数，求其阶乘的和："))

while i > 0:
    k = sjc(i)
    print("其阶乘和为", k)
    i = int(input("输入整数，求其阶乘的和："))
