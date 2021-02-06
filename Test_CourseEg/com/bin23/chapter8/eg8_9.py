import datetime
class Person:
    number = 0
    def __init__(self, name):
        self.name = name
        Person.number += 1

    def getName(self):
        return self.name

    @staticmethod
    def getNumber():
        print("总人数为：", Person.number)

if __name__ == '__main__':
    p = Person("Lily")
    print('姓名：',p.getName())
    p.getNumber()
    Person.getNumber()

    print()

    p2 = Person("God23Bin")
    print('姓名：',p2.getName())
    p2.getNumber()
    Person.getNumber()
    p.getNumber()

