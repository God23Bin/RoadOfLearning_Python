# 某幼儿园里，有m个小朋友围成一圈，他们的编号为1、2、…m他们身上都有若干个糖果，现在他们做一个分糖果游戏。
# 从1号小朋友开始，将自己的糖果均分三份（如果有多余的糖果，则立即吃掉），自己留一份，其余两份分给他相邻的
# 两个小朋友。接着2号、3号、…m号小朋友同样这么做。问n轮后，每个小朋友手上分别有多少糖果？

m = int(input("请输入参加的小朋友个数："))
print("输入", m, "个整数，代表每个小朋友手中的糖果数量，用','分开。", end='')
candy = list(eval(input("请输入：")))
n = 1
lun = int(input("输入需要分的轮数："))

while n <= lun:
    for i in range(len(candy)):
        share = candy[i] // 3
        if i == 0:
            candy[m - 1] = candy[m - 1] + share
            candy[1] = candy[1] + share
            # candy[0] = candy[0] - 2 * share
        elif i == m-1:
            candy[0] = candy[0] + share
            candy[m - 2] = candy[m - 2] + share
            # candy[m-1] = candy[m-1] - 2 * share
        else:
            candy[i + 1] = candy[i + 1] + share
            candy[i - 1] = candy[i - 1] + share
            # candy[i] = candy[i] - 2 * share
        candy[i] = share
    print("第", n, "轮分完后，小朋友手中的糖果为：", candy)
    n = n + 1


