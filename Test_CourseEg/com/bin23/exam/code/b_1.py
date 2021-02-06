# 1. 编写程序，用逗号分隔，同时输入6个学生的成绩计算平均分并输出。（25分）

def calc_average(num_tuple):
    return sum(num_tuple) / len(num_tuple)

if __name__ == '__main__':
    num_tuple = eval(input("请输入学生成绩:"))
    print("总人数为", len(num_tuple))
    average = calc_average(num_tuple)
    print("平均分为", average)