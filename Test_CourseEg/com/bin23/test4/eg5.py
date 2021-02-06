for x in range(0, 301):
    for y in range(0, 34):
        for z in range(0, 21):
            if x%3 == 0 and x//3 + y*3 + z*5 == 100 and x + y + z == 100:
                print('小鸡', x, '母鸡', y, '公鸡', z)