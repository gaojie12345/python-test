# 01-24


# # 向Excel中写入数据，生成新的文件
# from openpyxl import Workbook
#
# wb = Workbook()
# ws = wb.active
#
# # 设置单元格`A1`的值为42
# ws['A1'] = 42
# # 向工作表（Worksheet）`ws`中追加一行数据
# # 如果之前工作表是空的，这些数字会被放入第一行（A1, B1, C1）。
# # 如果工作表已经有数据，它们会被放入现有数据下面的第一个空行中。
# ws.append([1, 2, 3])
# ws['A2'] = 333
#
# wb.save('D:\\dddd.xlsx')
