# 递归方法，猴子吃桃
def f(n):
    if n == 7:
        s = 1
    else:
        s = (f(n + 1) + 1) * 2
    return s

print("桃子数共：", f(1))