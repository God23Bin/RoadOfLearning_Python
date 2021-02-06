# 7. 已知1^2=1、2^2=1+3、3^2=1+3+5……。编程实现，输入一个数x，求x^2是由哪些奇数相加得到。（x<50）（25分)
# 整体思路：基本就是1，3，5，7，9，如果输入3，那么就直接打印前面3个数相加，先把这些存起来，存到列表中
def get_lst():
    lst = []
    for i in range(1, 100):
        if i % 2 == 1:
            lst.append(i)
    # print(lst) # 1,3,5,7,9,11,13,.....
    return lst

def calc(x):
    # lst = [1, 3, 5, 7, 9]
    lst1 = get_lst()
    lst2 = []
    new_lst = lst1[:x] # 比如输入3，那么就截取前3位，如何截取？=》列表进行切片lst[:3]
    for i in range(len(new_lst)): # 下面进行 + 号的添加，除了第一个数外，其他的都在前面添加上 + 号，放到新的列表
        if i == 0:
            a = str(new_lst[i])
            lst2.append(a)
        else:
            a = " + " + str(new_lst[i])
            lst2.append(a)
    all = "".join(lst2) # 把新列表拼接成一个字符串，就完整显示1 + 3 + 5这种
    print('{}² = {}'.format(x, all))

if __name__ == '__main__':
    x = int(input("请输入一个数："))
    print("由下列奇数组成，完整如下：")
    calc(x)

