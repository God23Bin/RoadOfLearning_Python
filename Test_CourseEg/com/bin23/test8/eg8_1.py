import math

class MyCube:
    __able = 0
    __volum = 0
    def __init__(self, a):
        self.__able = a
    def calcVolum(self):
        return round(self.__able ** 3, 2)
    def calcArea(self):
        self.__volum = 6 * self.__able ** 2
        return round(self.__volum, 2)

if __name__ == '__main__':
    try:
        num = float(input("请输入边长："))
        mc = MyCube(num)
        print("立方体的面积为", mc.calcArea())
        print("立方体的体积为", mc.calcVolum())
    except Exception:
        s = "输入的不是数字，请重新输入"
        print(s)
