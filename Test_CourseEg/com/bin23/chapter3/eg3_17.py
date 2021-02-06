# 学生成绩统计

grade = float(input('请输入一个同学的成绩：'))
iSum = 0
iAvg = 0
iMax = -100
iMin = 150
iCount = 0

while grade >= 0:
    iSum += grade
    iCount = iCount + 1
    if grade > iMax:
        iMax = grade
    if grade < iMin:
        iMin = grade
    grade = float(input('请输入下一个同学的成绩：'))

print('计算机平均分：', iSum / iCount)
print('计算机最高分：', iMax)
print('计算机最低分：', iMin)

