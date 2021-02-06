# 用户输入一个正整数n，计算1!+2!+...+n!的值
n = input("请输入一个正整数：")
n = int(n)
k = 1
s = 0

for i in range(1,n + 1):
    k = k * i
    s += k
print("s = %i" %s)