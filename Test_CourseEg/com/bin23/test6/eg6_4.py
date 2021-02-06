# 0 1 1 2 3 5 8 13 21 ...

fibonacci = []

def fibonacci(k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)


def fibonacci_it(k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    i = 3
    x = 0
    y = 1
    while i <= k:
        z = x + y
        x = y
        y = z
        i += 1
    return z

if __name__ == '__main__':
    for i in range(1, 30):
        print(fibonacci_it(i), end=" ")