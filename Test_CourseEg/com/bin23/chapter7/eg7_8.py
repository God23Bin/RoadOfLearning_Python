import openpyxl

workbook = openpyxl.Workbook()
# 找到默认的工作簿
sheet1 = workbook.active
sheet1.title = "new sheet"

d_tuple = (('序号','号码','姓'),\
           ('1','23','Jeams'),\
           ('2','3','Davis'),\
           ('3','0','Kuzma'),\
           ('4','9','Rando'),\
           )
# 获取数据行数
iRows = len(d_tuple)
# 获取数据的列数
iCols = len(d_tuple[0])
# 将数据写入单元格
for row in range(iRows):
    # 列号从"A"开始
    colName = 'A'
    for col in range(iCols):
        # 将信息写入单元格，如sheet1['A!'] = d_tuple[0][0]
        sheet1['%s%d' %(colName, row + 1)] = d_tuple[row][col]
        # 列号变为下一个ASCII码的字母
        colName = chr(ord(colName) + 1)

workbook.save('stock.xlsx')
