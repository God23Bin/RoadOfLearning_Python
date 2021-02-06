strs = ['Mike', 'Hi', 'Null', 'Apple', 'Shit', 'Null', 'Banana']

for n in strs:
    if n == 'Null':
        continue

    for m in n:
        if m == 'i':
            continue
        print(m, end=' ')

    print()

print('结束')