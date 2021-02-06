# 12. 编写程序，从你选中的试题里，获得所有中文字，并将这些中文字输出到XXXXX学号姓名题号.txt文档中去。（25分）

import re

s = "编写程序，从你选中的试题里，获得所有中文字，并将这些中文字输出到XXXXX学号姓名题号.txt文档中去。"

chinese_word = re.findall(r'[\u4E00-\u9FFF]', s)
print(chinese_word)

# 写入文件
with open('1808030450郑伟彬.txt', 'a+', encoding='utf-8') as f:
    f.write(str(chinese_word))