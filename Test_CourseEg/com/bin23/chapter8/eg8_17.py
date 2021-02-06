from eg8_16 import Rational

def suan(r1, r2):
    print("r1:", r1, "r2:", r2)
    print(r1, "+", r2, "=", r1 + r2)
    print(r1, "-", r2, "=", r1 - r2)
    print(r1, "*", r2, "=", r1 * r2)
    print(r1, "/", r2, "=", r1 / r2)

def compare(r1, r2):
    print(r1, ">", r2, "=", r1 > r2)
    print(r1, ">=", r2, "=", r1 >= r2)
    print(r1, "==", r2, "=", r1 == r2)
    print(r1, "<", r2, "=", r1 < r2)
    print(r1, "<=", r2, "=", r1 <= r2)
    print(r1, "!=", r2, "=", r1 != r2)

if __name__ == "__main__":
    r1 = Rational(-2, 8)
    r2 = Rational(-2, 16)
    suan(r1, r2)
    compare(r1, r2)
    # print()
    #
    # r1 = Rational(1, 8)
    # r2 = Rational(0, 16)
    # suan(r1, r2)
    # compare(r1, r2)

