class Rectangle:
    def __init__(self,w,h):
        self.__width = w
        self.__height = h
    def getArea(self):
        return self.__width * self.__height
    def getPerimeter(self):
        return (self.__width + self.__height) * 2
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setWidth(self, w):
        if w > 0:
            self.__width = w
        else:
            print("宽度width有误")
    def setHeight(self, h):
        if h > 0:
            self.__height = h
        else:
            print("高度height有误")

t1 = Rectangle(15,6)
print("矩形t1的宽：", t1.getWidth(), ",高：",t1.getHeight())
print("矩形t1的面积：", t1.getArea())
print("矩形t1的周长：", t1.getPerimeter())

t1.setWidth(8)
print("矩形t1新的宽：", t1.getWidth())