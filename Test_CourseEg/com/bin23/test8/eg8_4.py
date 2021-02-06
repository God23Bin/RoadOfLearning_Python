import datetime

class Sa:

    def area(self):
        pass

class Circle(Sa):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

class Rectangle(Sa):
    def __init__(self, c, k):
        self.c = c
        self.k = k

    def area(self):
        return self.c * self.k

if __name__ == '__main__':
    r = eval(input("请输入圆的半径："))
    c = Circle(r)
    print("圆的面积：", c.area());

    v = eval(input("请输入矩形的长宽："))
    c = v[0]
    k = v[1]
    rect = Rectangle(c, k)
    print("矩形的面积", rect.area())