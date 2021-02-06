import random
import string
import re

s = []

letter_punctuation = string.ascii_letters + string.digits + '@$#&_~'

for i in range(16):
    randomLetter = random.choice(letter_punctuation)
    s.append(randomLetter)

randomString = "".join(s)
print("生成的随机密码：", randomString)

