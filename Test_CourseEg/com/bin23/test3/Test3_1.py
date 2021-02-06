# 从键盘接收整数的一百分制成绩（0~100），要求输出其对应的成绩等级A~E。
# 其中，90分（包含）以上为A，80~89（均包含）分为B，70~79（均包含）分为C，60~69（均包含）分为D，60分以下为E。

while True:
    grade = eval(input("请输入成绩"))
    if grade >= 90:
        print("A")
    elif 80 <= grade < 90:
        print("B")
    elif 70 <= grade < 80:
        print("C")
    elif 60 <= grade < 70:
        print("D")
    else:
        print("E")
