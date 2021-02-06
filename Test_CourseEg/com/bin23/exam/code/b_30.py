# 30．编写程序，创建类MyMath，计算圆的周长、面积和球的表面积和体积，结果均保留两位小数。
# 若输入的是非数字，则输出：请输入数字！
# 提示：要引入math包
# 球的体积：V = 4πR³/3
# 球的面积：S = 4πR^2
import math


class MyMath:
    def __init__(self, r):
        self.r = r

    def calc_c(self):
        c = 2 * math.pi * self.r
        return c

    def calc_s(self):
        s = math.pi * pow(self.r, 2)
        return s

    def calc_ball_v(self):
        v = 4 / 3 * math.pi * pow(self.r, 3)
        return v

    def calc_ball_s(self):
        bs = 4 * math.pi * pow(self.r, 2)
        return bs


if __name__ == '__main__':
    try:
        r = float(input('请输入半径：'))
        circle = MyMath(r)
        # 通过round()来保留2位小数
        c = round(circle.calc_c(), 2)
        s = round(circle.calc_s(), 2)
        bv = round(circle.calc_ball_v(), 2)
        bs = round(circle.calc_ball_s(), 2)
        print('半径为{}的圆，其周长为：{}，面积为：{}，球的体积为：{}，球的表面积为：{}'.format(r, c, s, bv, bs))
    except Exception:
        print("请输入数字！")
