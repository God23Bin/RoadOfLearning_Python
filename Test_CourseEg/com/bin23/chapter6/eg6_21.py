def fun():
    x = 5
    global y # 函数内声明全局变量
    y = 10
    return a + x + y

a = 10
print(fun())
print(y)