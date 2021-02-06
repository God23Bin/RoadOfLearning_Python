class Person:
    def __new__(cls, name, age):
        print("执行Person__new__方法")
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print("执行Person的__init__方法，初始化方法，构造方法")
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Teacher(Person):
    def __new__(cls, name, age):
        print("Teacher的__new__方法中，执行Person的__new__方法之前")
        return super(Teacher, cls).__new__(cls, name, age)

    def __init__(self, name, age):
        print("Teacher的__init__方法中，执行Person的__init__方法之前")
        super().__init__(name, age)
        print("Teacher的__init__方法中，执行Person的__init__方法之后")

if __name__ == '__main__':
    p = Teacher('Lily', 22)
    print('姓名：',p.getName())
    print('年龄：',p.getAge())