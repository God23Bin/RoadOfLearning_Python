import re

x = ["13915556234", "13025621456", "15325645124", "15202362459"]

for i in range(len(x)):
    if re.findall(r'13[456789]\d', x[i]) or re.findall(r'15[01289]\d', x[i]):
        print(x[i], "是移动号码")

