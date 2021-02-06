import xlrd

workbook = xlrd.open_workbook('stock.xls')
# 获取工作簿中的工作表数量
nsheets = workbook.nsheets

for i in range(nsheets):
    # 获取第i个sheet
    sheet = workbook.sheet_by_index(i)
    # 输出当前工作表的名字
    print("第%d个工作表的名称为：%s" %(i + 1, sheet.name))
    # 获取并打印工作表的行数与列数
    nrows = sheet.nrows
    ncols = sheet.ncols
    print("该工作表中的行数为：%d，列数为：%d" %(nrows, ncols))
    print("该工作表中的数据如下：")
    # 遍历所有行
    for m in range(nrows):
        # 读取第m行数据，返回一个列表
        rowValues = sheet.row_values(m)
        # 遍历列表中的元素
        for v in rowValues:
            print(v, end='\t')
        print()