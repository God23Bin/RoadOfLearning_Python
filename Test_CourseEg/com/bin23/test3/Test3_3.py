# 输出200以内的素数以及这些素数之和
import math

# def old_calc():
#     num = 0
#     for i in range(2, 200):
#         k = True
#         for j in range(2, i):
#             if i % j == 0:
#                 k = False
#                 break
#         if k:
#             print(i)
#             num = num + i
#     print("素数的和", num)

def new_calc():
    num = 0
    for i in range(2, 200):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            num += i

    print("新方法：素数的和：{}".format(num))

if __name__ == '__main__':
    # old_calc()
    new_calc()