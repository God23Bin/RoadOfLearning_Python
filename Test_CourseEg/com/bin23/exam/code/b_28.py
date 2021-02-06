# 28. 随机给出一个1~100之间的数字，然后让玩家猜这个数字。如果没有猜出正确答案，给出“大了”还是“小了”的提示；
# 如果猜出正确答案，打印出“恭喜，你猜了X次猜对了答案！”。
# 每个玩家有5次猜数字的机会，如果5次都没有猜对，给出“是否继续游戏”的提示。

import random

num = random.randint(0, 100)
count = 0

while count <= 5:
    if count == 5:
        x = int(input("是否继续游戏？输入1继续，其他停止游戏："))
        if x == 1:
            count = 0
        else:
            break
    n = int(input("猜猜看："))
    if n < num:
        print("小了")
        count += 1
    elif n > num:
        print("大了")
        count += 1
    else:
        print("恭喜，你猜了{}次猜对了答案！，答案是{}".format(count, num))
        break

