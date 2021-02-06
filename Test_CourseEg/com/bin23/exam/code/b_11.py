# 11. 孪生素数问题，如果有一个数它只能整除1和自己，那么这个数据就是素数（质数）
# 而孪生素数即是相差2的一对素数。例如3和5 ，5和7, 11和13，…，10016957和10016959等等都是孪生素数。
# 编写程序分批输出10-100里的孪生素数。（25分）

# 获取100以内的素数，存储到列表中
a = []
for i in range(10, 100):
    for j in range(2, i - 1):
        if i % j == 0:
            break
    else:
        a.append(i)

# 从素数列表中，通过if判断，打印出孪生素数
for x in range(2, len(a)):
    if a[x] - a[x - 1] == 2:
        x = a[x - 1]
        y = a[x]
        print(x, y)
