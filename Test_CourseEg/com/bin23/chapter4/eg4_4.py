print("输入任意字符串组成list1，输入y或yes结束，大小写无关")
yy = 'n'
i = 1
list1 = []

while yy.upper() not in ['Y', 'YES']:
    x = input("请输入第" + str(i) + "个元素：")
    list1.append(x)
    i += 1
    yy = input("结束输入？（y或yes结束：）")

tuple1 = tuple(list1)
print(list1)
print(tuple1)