# 9. 请用字典编程：已知某班学生的姓名和成绩如下：（其中**项为自己本人的名字）
# 姓名        成绩      姓名        成绩
# 张三        45        司音         90
# 李四        78        赵敏         78
# 徐来        40        张旭宁       99
# 沙思思      96        柏龙         60
# **          65        思琪         87
# 输出这个班的学生姓名和成绩，并求出全班同学的人数和总分，平均分并显示。（25分）

ng = {'张三': 45, '李四': 78, '徐来': 40, '沙思思': 96, '彬哥': 65, \
      '司音': 90, '赵敏': 78, '张旭宁': 99, '柏龙': 60, '思琪': 87, }

sum1 = 0
# 遍历字典
for n in ng:
    print("姓名：", n + "\t", "成绩：", ng[n])

# 遍历values
for g in ng.values():
    sum1 += g

avg = sum1 / len(ng)

print("总人数", len(ng), "总分", sum1, "平均分", avg)
