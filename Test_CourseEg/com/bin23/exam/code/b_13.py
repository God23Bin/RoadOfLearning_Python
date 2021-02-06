# 13. 编写函数计算任意位数的黑洞数。（25分）
# （黑洞数是指，这个数字每位上的数字组成的最大数减去每位数字组成的最小数仍然得到这个数自身。
# 例如，3位黑洞数是495，因为954-459=495,4位数字是6174，因为7641-1467=6174。）

def black_hole_Number(number, pre_number_list=None):
    number = str(number)

    # 重排求差
    number_list = sorted([i for i in number])

    min_number = int(''.join(number_list))
    max_number = int(''.join(number_list[::-1]))
    new_number = str(max_number - min_number)

    # 数字的位数补全 如4位数 12 -->  0012
    diff = abs(len(new_number) - len(number))
    if diff != 0:
        new_number += diff * '0'

    print('number:{} -->  {} - {} = {}'.format(number, max_number, min_number, new_number))

    if not pre_number_list:
        pre_number_list = []

    if new_number in pre_number_list:  # 如果新计算出的数，在之前的数字中出现过，那么说明它是黑洞数
        print(number)
        return number
    elif new_number == '0':
        print('输入的数字各位数相同，无法求黑洞数.')
        return
    else:
        pre_number_list.append(number)
        black_hole_Number(new_number, pre_number_list)  # 递归计算

if __name__ == '__main__':
    black_hole_Number(456)