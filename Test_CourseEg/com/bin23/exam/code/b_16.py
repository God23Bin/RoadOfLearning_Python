# 16. 定义一个学生类。（25分）
    # 有下面的类属性：
    # 1 姓名
    # 2 年龄
    # 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
    # 类方法：
    # 1 获取学生的姓名：get_name() 返回类型:str
    # 2 获取学生的年龄：get_age() 返回类型:int
    # 3 返回3门科目中最高的分数。get_course() 返回类型:int
    # 写好类以后，可以定义2个同学测试下:
    # zm = Student('zhangming',20,[69,88,98])
    # 返回结果：
    # zhangming
    # 20
    # 98

class Student:
    stu_name = ""
    stu_age = 0
    stu_grade = []

    def __init__(self, name, age, grade):
        # self.stu_name = name
        # self.stu_age = age
        # self.stu_grade = grade
        Student.stu_name = name
        Student.stu_age = age
        Student.stu_grade = grade


    @classmethod
    def get_name(cls):
        return cls.stu_name

    @classmethod
    def get_age(cls):
        return cls.stu_age

    @classmethod
    def get_course(cls):
        return max(cls.stu_grade)

if __name__ == '__main__':
    zs = Student("ZhangSan", 20, [50,65,95])
    zs.get_name()
    zs.get_age()
    zs.get_course()
    print('姓名：{}，年龄：{}，成绩最高分：{}'.format(zs.get_name(), zs.get_age(), zs.get_course()))
