# 带else的循环语句
n = int(input('请输入一个正整数：'))
i = n
while i > 0:
    if i % 23 == 0:
        print("小于等于", n, "且能被23整除的最大整数是：", i)
        break
    i = i - 1
else:
    print("未找到")