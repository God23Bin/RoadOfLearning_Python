import xlwt,xlrd,xlutils
import xlutils.copy

# 从stock.xls获取xlrd.Book工作簿
rb = xlrd.open_workbook('stock.xls')
# 利用xlutils.copy中的copy方法，从xlrd.Book对象中复制得到xlwt.Workbook对象
wb = xlutils.copy.copy(rb)
# 获取第0个sheet
sheet1 = wb.get_sheet(0)
sheet1.write(0, 0, 'number')
sheet1.write(0, 1, 'code')
sheet1.write(0, 2, 'name')
# 添加一个sheet
sheet2 = wb.add_sheet('增加的工作簿')
sheet2.write(0, 0, '0')
sheet2.write(1, 1, '1')
sheet2.write(2, 2, '2')

wb.save('stock_add.xls')
