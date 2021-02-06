def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


n = int(input("请输入个数："))
L = fib(n)
for x in L:
    print(x)