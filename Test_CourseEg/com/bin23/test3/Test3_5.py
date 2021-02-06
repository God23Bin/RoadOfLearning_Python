# 质因数分解：已知正整数n是两个不同的质数的乘积，试求出较大的那个质数。
# 输入只有一行，包含一个正整数 n。
# 输出只有一行，包含一个正整数 p，即较大的那个质数，假如除数和商不是质数的话，输出说明。

n = int(input("请输入正整数："))
s = str(n)
minPrimeNumber = 2
while minPrimeNumber < n:
    if minPrimeNumber % n == 0:
        n = n // minPrimeNumber
        s = s + str(minPrimeNumber) + "*"
    else:
        minPrimeNumber += 1

s = s + str(minPrimeNumber)
print(s)