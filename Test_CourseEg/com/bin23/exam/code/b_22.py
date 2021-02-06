# 22. 编写程序，输入字符串，计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：
# Hello world!
# 然后，输出应该是：
# 大写实例 1
# 小写实例 9
import re

def calc_count(s):
    up = re.findall(r'[A-Z]', s)
    low = re.findall(r'[a-z]', s)
    print('大写字母数量为{}，小写字母数量为{}'.format(len(up), len(low)))

if __name__ == '__main__':
    s = "Hello world!"
    calc_count(s)