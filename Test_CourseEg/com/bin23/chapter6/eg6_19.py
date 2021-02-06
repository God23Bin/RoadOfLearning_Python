def snn1(args):
    print(args)
    s = 0
    for i in args:
        s += i
    return s

def snn2(args):
    print(args)
    s = 0
    for i in args.keys():
        s += args[i]
    return s

print("snn1:")
aa = [1,2,3]
print(snn1(aa))
print(snn1([4,5]))

bb = (6,2,3,1)
print(snn1(bb))
print()

print("snn2:")
cc = {'x':1, 'y':2, 'c':3}
print(snn2(cc))
print(snn2({'aa': 1, 'bb': 2, 'cc': 4, 'dd': 5, 'ee': 6}))