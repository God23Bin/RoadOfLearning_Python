def snn3(x,y,z):
    return x + y + z

aa = [1,2,3]
print(snn3(*aa))

bb = (6,2,3)
print(snn3(*bb))

cc = [8,9]
print(snn3(7, *cc))