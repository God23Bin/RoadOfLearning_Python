import datetime
class Person:
    pre_name = ""
    def __init__(self, name, year, weight, height):
        print("执行Person的__init__方法，初始化方法，构造方法")
        self.name = name
        self.year = year
        # 定义私有属性
        self.__weight = weight
        self.__height = height

    def old(self, year):
        return year - self.year

    # 定义私有方法
    def __getBMI(self):
        bmi = self.__weight/self.__height ** 2
        return bmi

    def getGrade(self):
        dd = datetime.datetime.now()
        now_age = self.old(dd.year)
        if now_age >= 18:
            bmi = self.__getBMI()
            print("身体质量指数BMI为：",'%.2f'%bmi, end='')
            if bmi < 18.5:
                print("过轻")
            elif bmi < 25.0:
                print("正常")
            elif bmi < 28.0:
                print("过重")
            elif bmi < 32.0:
                print("肥胖")
            else:
                print("非常肥胖")
        else:
            print("不到18岁不计算BMI")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

if __name__ == '__main__':
    p = Person("Lily", 1998, 48, 1.55)
    print('姓名：',p.getName())
    print('年龄：',p.old(2020))
    print('体重：', p._Person__weight, 'kg')
    print('身高：', p._Person__height, 'm')
    p.getGrade()

    print()

    p2 = Person("God23Bin", 1999, 64.5, 1.75)
    print('姓名：',p2.getName())
    print('年龄：',p2.old(2020))
    print('体重：', p2._Person__weight, 'kg')
    print('身高：', p2._Person__height, 'm')
    p2.getGrade()

