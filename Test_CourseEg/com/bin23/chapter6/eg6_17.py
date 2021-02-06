def all_5(** args):
    print(args)
    s = 0
    for i in args.keys():
        s += args[i]
    return s


print(all_5(x=1, y=2, c=3))
print(all_5(aa=1, bb=2, cc=4, dd=5, ee=6))
