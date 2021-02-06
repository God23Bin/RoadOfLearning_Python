import random

f = open('test7_10.txt','w', encoding='utf-8')
while True:
    i = random.randint(1, 122)
    x = chr(i)
    if x.isupper() or x.islower() \
        or x.isdigit() or x in ['\n', '\r', '*', '&', '^', '$']:
        f.write(x)
    if f.tell() > 10000:
        break
f.close()