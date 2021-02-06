print("温度转换")
print("1.华氏温度转为摄氏温度")
print("2.摄氏温度转为华氏温度")
x = int(input("请选择上方数字选项进行温度转换"))

if x == 1:
    f = eval(input("请输入华氏温度："))
    c = (f-32)*5/9
    print("转为的摄氏温度为：")
    print(c)
elif x == 2:
    c = eval(input("请输入摄氏温度："))
    f = c*9/5+32
    print("转为的华氏温度为：")
    print(f)

