# 19. 定义父类Shape，该类包含计算面积的方法area
# 通过继承实现父类的方法，分别计算不同图形（圆、三角形、矩形）的面积。（25分）

class Shape:

    def area(self):
        pass

class Circle(Shape):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, c, k):
        self.c = c
        self.k = k

    def area(self):
        return self.c * self.k

class Triangle(Shape):
    def __init__(self, d, h):
        self.d = d
        self.h = h

    def area(self):
        return 1/2 * self.d * self.h

if __name__ == '__main__':
    r = eval(input("请输入圆的半径："))
    c = Circle(r)
    print("圆的面积：", c.area());

    v = eval(input("请输入矩形的长宽："))
    c = v[0]
    k = v[1]
    rect = Rectangle(c, k)
    print("矩形的面积", rect.area())

    t = eval(input("请输入三角形的底和高："))
    d = t[0]
    h = t[1]
    tri = Triangle(d, h)
    print("三角形面积", tri.area())