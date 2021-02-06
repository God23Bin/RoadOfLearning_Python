class Person:
    def __init__(self,n,y,w,h):
        self.name = n
        self.year = y
        self.__weight = w
        self.__height = h
    def old(self,y):
        return y - self.year

p1 = Person("Lily", 1998, 49, 1.5)
print("姓名为",p1.name,"，体重为",p1._Person__weight,"千克")
p1._Person__weight = 48 # 访问私有成员变量
print("现在的体重为", p1._Person__weight,"千克")

myyear = 2020
myage = p1.old(myyear)
if myage > 0:
    print("到" + str(myyear) + "年" + str(myage) + "岁")
elif myage < 0:
    print(str(myyear) + "年还没出生呢，出生于" + str(p1.year) + "年")
else:
    print(str(myyear) + "年刚出生")
