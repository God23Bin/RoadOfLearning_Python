import math
r = eval(input("请输入圆的半径："))

if r >= 0:
    d = 2 * math.pi * r
    s = math.pi * pow(r, 2)
    # print("圆的周长 = ", d, "圆的面积 = ", s)
    print("圆的周长 = %.2f,圆的面积 = %.2f" % (d, s))
