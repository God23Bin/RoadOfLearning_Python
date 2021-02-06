import random
numbers = []
for i in range(15):
    n = random.randint(1, 9)
    numbers.append(n)
print("产生的15个数：", numbers)
afterNumbers = list(set(numbers)) # 搞成set集合来去重
print("去重后：", afterNumbers)
