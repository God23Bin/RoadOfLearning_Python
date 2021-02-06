import string
import random

s = []

for i in range(15):
    randomLetter = random.choice(string.ascii_letters)
    if randomLetter in s:
        i = i - 1
        continue
    else:
        s.append(randomLetter)

randomNoRepeatString = "".join(s)
print("生成的不重复随机字母：", randomNoRepeatString)

noRepeatList = list(randomNoRepeatString)
newList = []

for j in range(len(noRepeatList)):
    if j % 2 != 0:
        continue
    else:
        newStr = noRepeatList[j]
        newList.append(newStr)

print('下标为偶数的字符组成的新数组{}'.format(''.join(newList)))

