# 关于输入
# x = input("请输入x值：")
# print(x)
# print(type(x))
# print("input()函数不管输入什么内容，返回的都是字符串")

print("--------------int()函数--------可将数字或不带小数点的字符串转成整数-------")
        # int([x]) -> integer
        # int(x, base=10) -> integer  base，指定该字符串x是什么进制，默认十进制，其有效范围0和2~36，功能：转成十进制
print(int(23.54))
print(int(-3.52))
print(int('4'))
print(int('-4'))
# print(int('4.56')) 不能使用带小数的字符串来转换成int类型的整数

print(int('1001001', 2))    # 2 -> 10
print(int('2ef', 16))       # 16 -> 10
print(int('27', 8))         # 8 -> 10

print("--------------float()函数--------可将数字或不带小数点的字符串转成浮点数-------")
print(float(5))
print(float(5.67))
print(float('5'))
print(float('5.67'))

print("--------------eval()函数--------可解析计算，返回计算结果-------")
a = 3
print(eval('a + 1'))
print(eval('3 + 5'))
print(eval('[1,2,3]'))
print(eval('(1,2,3)'))
print(eval('{1:23, 2:32}'))
print(eval("__import__('os').getcwd()"))