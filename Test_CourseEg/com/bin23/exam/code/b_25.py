# 25. 古典问题
# 有一对兔子，
# 从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子。
# 假如兔子都不死。
# 问每个月的兔子总数为多少？
# 提示：其实这道题就是斐波那契数列的由来。
# 理清思路是关键，理解成满两个月后，每月都能生兔子，就好办了。

def calc_count(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    else:
        return calc_count(x-1) + calc_count(x-2)


if __name__ == '__main__':
    for i in range(1, 20):
        print(calc_count(i))
