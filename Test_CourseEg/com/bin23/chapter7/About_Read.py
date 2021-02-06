f = open('D:\SoftWare\Python\PycharmProjects\Learn\Test_CourseEg\com\\bin23\chapter7\\testR.txt')
# print(f.read(3))
# print(f.read(2))
# print(f.read())

# print(f.readline())
# print(f.readline(3))
# print(f.readline())

# print(f.readlines())

# 读取文件代替readlines方法一
# line = f.readline()
# while line:
#     print(line, end="")
#     line = f.readline()
# f.close()

# 读取文件代替readlines方法二
# for line in iter(f):
#     print(line,end="")
# f.close()

# 读取文件代替readlines方法三
for line in f:
    print(line, end='')
f.close()