class Pizza:
    def __init__(self, d):
        self.diameter = d
        print("调用__init__方法")
    def __del__(self):
        print("调用__del__方法")

if __name__ == '__main__':
    pz1 = Pizza(8)
    pz2 = Pizza(10)
    pz3 = pz2

    print("准备删除pz1")
    del pz1
    print("准备删除pz2")
    del pz2
    print("准备删除pz3")
    del pz3


