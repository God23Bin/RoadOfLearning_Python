def fdiv(x, y):
    if x < y:
        x, y = y, x
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

a = fdiv(25, 45)
print("25和45的最大公约数：", a)
m = 36
n = 12
b = fdiv(m, n)
print(str(m) + "和" + str(n) + "的最大公约数：", b)