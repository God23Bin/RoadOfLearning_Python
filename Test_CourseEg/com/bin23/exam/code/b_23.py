# 23. 有5、6、7、8四个数字，能组成多少个互不相同且无重复数字的三位数？输出所有结果，每行输出10个。

count = 0
ctrl = 0
for x in range(5, 9):
    for y in range(5, 9):
        for z in range(5, 9):
            if (x != y) and (x !=z ) and (y != z):
                print("%d%d%d" % (x, y, z), end='  ')
                count += 1
                ctrl += 1
                if ctrl == 10: # 控制每10个出来就换行
                    print('')
                    ctrl = 0
    # print('')
print()
print('最终结果为：%s个' % count)