# scores = input("请输入学生成绩：")
# s = scores.split(",")
# print(len(s))
# sum = 0
# for i in s:
#     sum = sum + int(i)
# print("所以平均成绩为： ",end="")
# print(sum/len(s))

scores = eval(input("请输入学生成绩："))
print(len(scores))
print("平均成绩为：", end="")
print(sum(scores)/len(scores))
