list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list2 = []
print("原始：",list1)

list2 = list1[::2]
list2.sort()
list1[::2] = list2
print("偶数下标上升：", list1)