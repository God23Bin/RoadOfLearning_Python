# 2. 编写程序，生成包含1000个0到100之间的随机整数，并统计每个元素的出现次数。

import random


def gen_int():
    lst = []
    # 循环1000次，随机生成，存到列表中
    for i in range(1000):
        a = random.randint(0, 100)
        lst.append(a)
    print(lst)
    count_dict = {}
    # 循环100次，以此统计每个元素的出现个数，存到字典中
    for j in range(100):
        c = lst.count(j)
        count_dict.update({j: '出现次数为' + str(c)})
    print(count_dict)
if __name__ == '__main__':
    gen_int()
