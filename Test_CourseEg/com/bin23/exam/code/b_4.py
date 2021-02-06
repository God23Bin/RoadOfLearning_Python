# 4. 编写函数，判断一个数是否为素数，调用该函数判断从键盘中输入的数是否为素数
# 素数也称质数，是指只能被1和它本身整除的数。（25分）
import math

def calc_sushu(n):
    for i in range(2, int(math.sqrt(n))+1):   # 从2开始判断，一直到输入的那个数为止
        if n % i == 0:      # 能整除，即余数为0，说明不是素数
            print(" %d 不是素数" % n)
            break   # 这个break意思就是当该数不是质数时，就跳出整个循环，该数就不是我们要的数字了
    else:           # else与for对齐，for... else
        print(" %d 是一个素数" % n)

if __name__ == '__main__':
    # n = int(input("请输入一个整数："))
    calc_sushu(100000037)
