# 随机预设一个0~100之间的整数，让用户猜一猜并输入所猜的数。
# 如果大于预设的数，显示“太大”；小于预设的数，显示“太小”。
# 如此循环，直至猜中该数，显示“恭喜，你猜中了！”。
import random

num = random.randint(0, 100)
shu = -1

while num != shu:
    shu = int(input("输入你猜想的 0-100 内的整数"))
    if num > shu:
        print("太小")
    elif num < shu:
        print("太大")
print("恭喜，你猜中了!")

print("生成的", num, "你猜的", shu)

