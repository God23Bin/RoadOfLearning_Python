# 5. 编写程序输出九九乘法表

def get_multi_table_for_for():
    for i in range(1, 10):
        print()
        for j in range(1, i + 1):
            print(str(j) + "x" + str(i) + "=" + str(i * j), end="\t")


def get_multi_table_for_for_2():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()


def get_by_while_while():
    i = 1
    while i <= 9:
        j = 1
        while (j <= i):  # j的大小是由i来控制的
            print('%dx%d=%-3d' % (i, j, i * j), end='\t')
            j += 1
        print('')
        i += 1


if __name__ == '__main__':
    get_multi_table_for_for()
    get_multi_table_for_for_2()
    get_by_while_while()
