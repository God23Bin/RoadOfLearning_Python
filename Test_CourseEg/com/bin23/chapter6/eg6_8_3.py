def circles(r):
    if r <= 0:
        print("请输入正数！")
        return
    area = 3.14 * r * r
    perimeter = 2 * 3.14 * r
    return area, perimeter

r = 3
print(circles(r))

r = -3
print(circles(r))
