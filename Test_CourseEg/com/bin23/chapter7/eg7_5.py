import xlwt

workbook = xlwt.Workbook(encoding='UTF-8')
sheet1 = workbook.add_sheet('工作表1', cell_overwrite_ok=True)
# 以元组形式保存需要写入的数据
d_tuple = (('序号','代码','名称'),\
           ('1', '600536','阿里巴巴集团'),\
           ('2', '215346','百度信息'),\
           ('3', '645686','腾讯软件'),\
           ('4', '483216','中国科技'),\
           )
# 将元组中的数据逐一写入单元格中
for i in range(len(d_tuple)):
    for j in range(len(d_tuple[0])):
        sheet1.write(i, j, d_tuple[i][j])

workbook.save('stock.xls')
