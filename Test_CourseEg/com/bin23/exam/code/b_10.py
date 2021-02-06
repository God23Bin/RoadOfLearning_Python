# 10. 下面的程序是否能够正常执行，若不能，请解释原因，并修改使程序能正常执行。（25分）
# from random import randint
# result=set()
# while True:
#         result.add(randint(1,10))
#     if len(result)==20:
#         break
# print(result)

from random import randint

result = set()
while True:
    result.add(randint(1, 10))
    if len(result) == 10:
        break
    print(result)

