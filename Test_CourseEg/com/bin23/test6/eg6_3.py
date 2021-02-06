for num in range(100, 1000):
    c = num % 10
    b = num // 10 % 10
    a = num // 100
    if num == pow(a, 3) + pow(b, 3) + pow(c, 3):
        print(num)