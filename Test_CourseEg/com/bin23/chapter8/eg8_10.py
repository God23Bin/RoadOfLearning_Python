import datetime
class Person:
    __number = 0
    def __init__(self):
        Person.__number += 1

    @classmethod
    def getNumber(cls):
        return cls.__number

class Student(Person):
    def __init__(self, name):
        self.name = name
        super().__init__()


if __name__ == '__main__':
    s1 = Student('Lily')
    print(s1.getNumber())
    print(Person.getNumber())

    print()

    s2 = Student('God23Bin')
    print(s2.getNumber())
    print(Person.getNumber())
    print(s1.getNumber())

