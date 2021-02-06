def all_2(* args):
    print(args)
    s = 0
    for i in args:
        s += i
    return s

print(all_2(1,2,3))
print(all_2(1,2,3,4,5,6))
