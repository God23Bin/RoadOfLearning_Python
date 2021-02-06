list1 = list(eval(input('输入正整数：')))
sum1 = 0
sum2 = 0
for val in list1:
    if val == -1:
        break
    if val % 2 == 0:
        sum1 += val
    else:
        sum2 += val

print("奇数和", sum2, "偶数和", sum1)
