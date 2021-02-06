#ftower 原始塔
#ttower 目标塔
#atower 过渡塔
def han(n, ftower, ttower, atower):
    if n == 1:
        print(n, "from", ftower, "to", ttower)
    else:
        han(n - 1, ftower, atower, ttower)
        print(n, "from", ftower, "to", ttower)
        han(n - 1, atower, ttower, ftower)

a = int(input("请输入n："))
han(a, "A", "B", "C")