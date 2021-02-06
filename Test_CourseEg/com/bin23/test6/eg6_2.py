# 整数 a 除以整数 b(b≠0) 的商正好是整数而没有余数，我们就说 b 是 a 的因子
def factor_except_No1(num):
    for i in range(2, num):
        if num % i == 0:
            print(i)

def factor_complete(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
            # print(i)
    if s == num:
        print(num, "是完全因子")

def factor_com_in_num(num):
    for i in range(1, num):
        factor_complete(i)

if __name__ == '__main__':
    num = int(input("请输入一个数："))
    factor_except_No1(num)
    factor_complete(num)
    num1 = int(input("请输入一个数："))
    factor_com_in_num(num1)

