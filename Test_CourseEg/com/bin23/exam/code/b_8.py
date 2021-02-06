# 8. 若将某素数的各位数字顺序颠倒后得到的数仍是素数，则此数为可逆素数。设计函数求出100以内的可逆素数

def calc_sushu_in_100():
    sushu100 = []
    for i in range(2, 100):  # 循环2-100，看哪个是素数

        for j in range(2, i):  # 从2开始判断，一直到输入的那个数为止
            if i % j == 0:  # 能整除，即余数为0，说明不是素数
                # print(" %d 不是素数" % n)
                break  # 这个break意思就是当该数不是质数时，就跳出整个循环，该数就不是我们要的数字了
        else:  # else与for对齐，for... else
            # print(" %d" % i, end="\t")
            sushu100.append(i)
    return sushu100


def calc_reverse_sushu(sushu_list):
    reverse_list = []
    for i in range(len(sushu_list)):
        reverse_i = int((str(sushu_list[i]))[::-1])
        if reverse_i != sushu_list[i]:
            reverse_list.append(reverse_i)
    return reverse_list


def calc_sushu_for(sushu_list):
    for i in range(0, len(sushu_list)):

        for j in range(2, sushu_list[i]):
            a = sushu_list[i]
            if sushu_list[i] % j == 0:
                break
        else:
            print(sushu_list[i], end="\t")


if __name__ == '__main__':
    sushu_list = calc_sushu_in_100()
    print("素数：", sushu_list)
    reverse_list = calc_reverse_sushu(sushu_list)
    print("上面素数颠倒：", reverse_list)
    print("逆素数如下：")
    calc_sushu_for(reverse_list)
