n = input("输入一个正整数n（n <= 1000）：")
while not n.isdigit() or int(n) > 1000 or int(n) <= 0:
    print("输入错误，请重新输入")
    n = input("输入一个正整数n（n <= 1000）：")
else:
    n = int(n)
    a = list(filter(lambda x:n % x == 0, range(2, int(n//2) + 1)))
    print("因子为：", a, "和为：", sum(a))