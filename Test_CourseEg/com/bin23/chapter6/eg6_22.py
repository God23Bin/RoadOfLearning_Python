def fun(x, y):
    x += 10
    y.append(10)
    return x, y

a = 1
b = [1]
print("调用函数前，a=", a)
print("调用函数前，b=", b)
fun(a,b)
print("调用函数后，a=", a)
print("调用函数后，b=", b)
