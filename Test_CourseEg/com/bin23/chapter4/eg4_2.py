list1 = []
list2 = []
print("列表list1：")
for i in range(4):
    x = int(input("请输入" + str(i + 1) + "个整数："))
    list1 += [x]
print("列表list2：")
for i in range(3):
    x = int(input("请输入" + str(i + 1) + "个整数："))
    list2.append(x)

print("list1:", list1)
print("list2:", list2)
list1.extend(list2) # list2 合并到 list1
print("list2合并到list1后的lsit1：", list1)

list1 = list1 + [90, 100]
print("加上90，100后的list1：", list1)

list1.sort(reverse = True)
print("降序后的list1：", list1)