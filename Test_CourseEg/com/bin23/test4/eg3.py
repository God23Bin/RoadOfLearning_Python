

# 单位 万元
amount_list1 = [2.3, 4.5, 24, 17, 1, 7.8, 39, 21, 0.5, 1.2, 4, 1, 0.3]

sum_p = 0
sum_g = 0
sum_s = 0
sum_o = 0

for i in amount_list1:
    if i >= 10:
        sum_p += 1
    elif 5 <= i < 10:
        sum_g += 1
    elif 3 <= i < 5:
        sum_s += 1
    else:
        sum_o += 1

degree_dict = {'platinum(铂金)' : sum_p, 'gold(金卡)' : sum_g, 'silver(银卡)' : sum_s, 'ordinary(普通)' : sum_o }

print(degree_dict)