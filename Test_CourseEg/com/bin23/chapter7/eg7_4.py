import pickle
f = open('eg7_2.dat', 'rb')
try:
    while True:
        x = pickle.load(f)
        print(x)
except EOFError:
    print("读取完毕")
f.close()