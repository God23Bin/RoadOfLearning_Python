# 15. 编写程序，分别统计本题目的数字、英文字符、中文字、中英文标点符号的个数，并输出到文件-统计.txt。（25分）
import re

s = "编写程序，分别统计本题目的数字、英文字符、中文字、中英文标点符号的个数，并输出到文件。"

# 以列表类型返回全部能匹配的子串
num = re.findall(r'[0-9]', s)
letter = re.findall(r'[a-zA-Z]', s)
chinese_word = re.findall(r'[\u4E00-\u9FFF]', s)
other = len(s) - len(num) - len(letter) - len(chinese_word)
print("数字个数：", len(num))
print("英文字符个数：", len(letter))
print("中文字个数：", len(chinese_word))
print("中英文标点符号个数：", other)

# 写入文件
with open('统计.txt', 'a+', encoding='utf-8') as f:
    f.write("数字个数：" + str(len(num)) + "\n")
    f.write("英文字符个数：" + str(len(letter)) + "\n")
    f.write("中文字个数：" + str(len(chinese_word)) + "\n")
    f.write("中英文标点符号个数：" + str(other) + "\n")