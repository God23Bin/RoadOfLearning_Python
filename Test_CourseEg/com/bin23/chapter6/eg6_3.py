def jc(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

i = int(input("输入整数，求其阶乘："))

while i > 0:
    k = jc(i)
    print(str(i) + "! =", k)
    i = int(input("输入整数，求其阶乘："))
