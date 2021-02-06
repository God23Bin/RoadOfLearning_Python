# 4. 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果

import random

lst = []
lst1 = []
lst2 = []
for i in range(20):
    a = random.randint(0, 20)
    lst.append(a)

print("总的", lst)
lst1 = lst[:10]
lst1 = sorted(lst1)
print("前10个：", lst1)
lst2 = lst[10:20]
lst2 = sorted(lst2, reverse=True)
print("后10个：", lst2)
