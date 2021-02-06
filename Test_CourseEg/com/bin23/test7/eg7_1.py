# 打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + "x" + str(j) + "=" + str(i * j) + "\t", end="")
    print()

# 写入文件
with open('lab7_1.txt', 'a+') as f:
    for i in range(1, 10):
        for j in range(1, i + 1):
            f.write(str(i) + "x" + str(j) + "=" + str(i * j) + "\t")
        f.write("\n")