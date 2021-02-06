f = open('D:\SoftWare\Python\PycharmProjects\Learn\Test_CourseEg\com\\bin23\chapter7\\test.txt', 'w+')
f.write('567\n')
f.write("ABC")

a_list = ['\n123', '\nabc']
f.writelines(a_list)
f.close()