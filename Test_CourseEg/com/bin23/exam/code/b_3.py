# 3. 已有XXXXX学号姓名（拼音）字符串，如：1708010101ZhangSan
# 编写程序，截取学号姓名拼音字符串的前两位和后两位子字符串，分别用q2和h2两个变量存储。
# 然后，要求输出q2和h2，并单独输出q2和h2的id（）值。（25分）

if __name__ == '__main__':
    s = "1708010101ZhangSan"

    q2 = s[0: 2]
    print("q2:", q2)
    h2 = s[len(s)-2:len(s)]
    print("h2:", h2)

    print("id(q2):", id(q2))
    print("id(h2):", id(h2))

