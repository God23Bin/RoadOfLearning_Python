strs = ['Mike', 'Tom', 'Null', 'Apple', 'Betty']

for i in strs:
    if i == 'Null':
        break
    print(i)

print('End')

print()

for i in strs:
    if i == 'Null':
        continue
    print(i)

print('End')