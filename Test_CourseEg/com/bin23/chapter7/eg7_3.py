import struct
f = open('eg7_1.dat', 'rb')
s = f.read()
t = struct.unpack('I3sf?', s)
print(t)
for x in t:
    print(x)
f.close()