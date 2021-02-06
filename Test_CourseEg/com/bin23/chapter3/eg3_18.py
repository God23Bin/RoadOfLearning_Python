# 天气状况
highTemp = [13, 13, 18, 18, 19, 15, 16]
lowTemp = [5, 7, 10, 13, 11, 8, 9]

maxValTemp = max(highTemp)
minValTemp = min(lowTemp)
maxTDay = highTemp.index(maxValTemp)
minTDay = lowTemp.index(minValTemp)

print("这周第" + str(maxTDay + 1) + "天最热，最高" + str(maxValTemp) + "C°")
print("这周第" + str(minTDay + 1) + "天最冷，最低" + str(minValTemp) + "C°")

avgDTemp = []

for i in range(len(highTemp)):
    avgDTemp.append((highTemp[i] + lowTemp[i])/2)

print("这周每天的日平均气温：", avgDTemp)

k = 0

for i in avgDTemp:
    if k < 5:
        if i >= 10:
            k += 1
        else:
            k = 0

avg = sum(avgDTemp)/len(avgDTemp)
print("周平均气温：", avg)

if k >= 5:
    print("上海这周已经入春")
else:
    print("上海这周还没入春")