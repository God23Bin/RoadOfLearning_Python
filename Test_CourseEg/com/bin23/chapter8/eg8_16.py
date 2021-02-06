# 求两个正整数的最大公约数
def fdiv(x, y):
    if x < y:
        x, y = y, x
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

class Rational:
    # x代表分子，y代表分母
    def __init__(self, x, y):
        if x != 0:
            # 求最大公约数
            z = fdiv(abs(x), y)
            (self.x, self.y) = (x/z, y/z)
        else:
            (self.x, self.y) = (x, y)

    # + 加
    def __add__(self, other):
        m = self.x * other.y + other.x * self.y
        n = self.y * other.y
        return Rational(m, n)
    # - 减
    def __sub__(self, other):
        m = self.x * other.y - other.x * self.y
        n = self.y * other.y
        return Rational(m, n)
    # * 乘
    def __mul__(self, other):
        m = self.x * other.x
        n = self.y * other.y
        return Rational(m, n)
    # / 真除
    def __truediv__(self, other):
        if other.x == 0:
            return "第 2 个有理数为 0，不能用/"
        elif other.x < 0:
            t2 = -1
        else:
            t2 = 1
        if self.x < 0:
            t1 = -1
        else:
            t1 = 1
        m = abs(self.x) * other.y
        n = self.y * abs(other.x)
        return Rational(t1 * t2 * m, n)
    # 小于
    def __lt__(self, other):
        aa = self.__sub__(other)
        if aa.x >= 0:
            return False
        else:
            return True

    # <= 小于等于
    def __le__(self, other):
        aa = self.__sub__(other)
        if aa.x > 0:
            return False
        else:
            return True

    # = 等于
    def __eq__(self, other):
        aa = self.__sub__(other)
        if aa.x == 0:
            return True
        else:
            return False

    # != 不等于
    def __ne__(self, other):
        aa = self.__sub__(other)
        if aa.x == 0:
            return False
        else:
            return True

    # > 大于
    def __gt__(self, other):
        aa = self.__sub__(other)
        if aa.x > 0:
            return True
        else:
            return False

    # >= 大于等于
    def __ge__(self, other):
        aa = self.__sub__(other)
        if aa.x >= 0:
            return True
        else:
            return False

    def __str__(self):
        if self.y == 1 or self.x == 0:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)