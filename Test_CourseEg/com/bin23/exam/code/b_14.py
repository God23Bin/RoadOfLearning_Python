# 14. 给定一段字符串“Here is my phone No. 020-87654321，yours is 0755-12345678，his is 0745-123456.”
# 使用正则表达式提取字符串中的电话号码

import re

s = "Here is my phone No. 020-87654321，yours is 0755-12345678，his is 0745-123456."

print(re.findall(r'[0-9]*-[0-9]*', s))