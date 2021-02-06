num = int(input("请输入一个整数："))
count = num//2

while count > 0:
    if num % count == 0:
        break
    count = count -1

print(count, '是', num, '的最大因子')