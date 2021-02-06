# 6. 编写程序，生成一个为30个不重复的大小写字母组成的列表。（25分）

import string
import random

def random_letters(n):
    # 定义一个空列表保存随机字母
    letters_list = []
    while len(letters_list) < n :
        a_str = string.ascii_letters
        # 字母：string.ascii_letters
        # 大写：string.ascii_uppercase
        # 小写：string.ascii_lowercase
        random_letter = random.choice(a_str)
        if (random_letter not in letters_list) :
            letters_list.append(random_letter)
        else:
            pass
    return letters_list

if __name__ == '__main__':
    n_int = int(input("请输入需要的随机不重复大小写字母个数："))
    print(random_letters(n_int))

