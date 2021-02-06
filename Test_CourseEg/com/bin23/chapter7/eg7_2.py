import pickle
s = '好好学习'
li = [1, 2, '天天向上', 9.9]
d = {1:10, 2:20}
x = 8
y = 8.8
f = open('eg7_2.dat', 'wb')
pickle.dump(s, f)
pickle.dump(li, f)
pickle.dump(d, f)
pickle.dump(x, f)
pickle.dump(y, f)
f.close()
