# 20. 给出公式： x=1时，f(x) = 1，x > 1时，f(x) = f(x-1) + x^2
# 编写程序，用递归方式求x=10的时候f(x)的解，并输出结果。（25分）
def calc(x):
    if x == 1:
        return 1
    else:
        return calc(x-1) + pow(x, 2)

if __name__ == '__main__':
    result = calc(10)
    print('f(10) = {}'.format(result))