# 3. 编写程序，用户输入一个列表和2个整数作为下标，然后使用切片获取并输出列表中介于2个下标之间的元素组成的子列表。
# 例如用户输入[1, 2, 3, 4, 5, 6]和2,5，程序输出[3, 4, 5, 6]。

s = list(eval(input("请输入列表：")))
print(s)
a = eval(input("请输入下标，将会进行切片"))
new_s = s[a[0]:a[1] + 1]
print(new_s)
