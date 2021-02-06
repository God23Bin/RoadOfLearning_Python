ng = {'张三' : 45, '李四' : 78, '徐来' : 40, '沙思思' : 96, '如一' : 65,\
      '司音' : 90, '赵敏' : 78, '张旭宁' : 99, '柏龙' : 60, '思琪' : 87, }

sum1 = 0
# 遍历字典
for n in ng:
    print("姓名：", n + "\t", "成绩：", ng[n])

# 遍历values
for g in ng.values():
    sum1 += g

avg = sum1/len(ng)


print("总人数", len(ng), "平均分", avg)