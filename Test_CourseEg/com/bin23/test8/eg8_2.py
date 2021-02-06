import math
class Shape:

    def __init__(self, n):
        self.__name = n
        self.__s = 0
        self.__r = 0
        self.__w = 0
        self.__h = 0

    def calcS(self, *args):
        if len(args) == 1:
            self.__s = 2 * math.pi * args[0]
            return self.__s
        elif len(args) == 2:
            self.__s = args[0] * args[1]
            return self.__s

    def setR(self, r):
        self.__r = r

    def getR(self):
        return self.__r

    def setW(self, w):
        self.__w = w

    def getW(self):
        return self.__w

    def setH(self, h):
        self.__h = h

    def getH(self):
        return self.__h



if __name__ == '__main__':
    circle = Shape("圆形")
    rectangle = Shape("矩形")

    r = float(input("请输入圆形的半径"))
    v = eval(input("请输入矩形的长宽"))
    c = v[0]
    k = v[1]


    print("圆形面积%.2f" % circle.calcS(r))
    print("矩形面积%.2f" % rectangle.calcS(c, k))


