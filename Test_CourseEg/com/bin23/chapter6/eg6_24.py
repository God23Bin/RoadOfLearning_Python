def fac(n):
    if n == 1:
        s = 1
    else:
        s = n * fac(n - 1)
    return s

a = eval(input("请输入n："))
print(str(a) + "!=", fac(a))