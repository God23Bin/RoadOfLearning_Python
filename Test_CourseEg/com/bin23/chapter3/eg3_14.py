
num = int(input('请输入一个自然数：'))
while num!= -1:
    count = num//2
    while count > 0:
        if num % count == 0:
            break
        count = count -1
    print(count, '是', num, '的最大公因数')
    num = int(input('请再输入一个自然数：'))

print('程序结束')