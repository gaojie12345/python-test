# 01-25

# 连接mysql
# import pymysql
#
# no = int(input('部门编号:'))
# # name = input('部门名称:')
# # location = input('部门所在地:')
#
# # 1. 创建连接（Connection）
# conn = pymysql.connect(host='xxxx', port=3306,
#                        user='xxxxx', password='xxxxxx',
#                        database='hrs', charset='utf8mb4')
#
# try:
#     with conn.cursor() as cursor:
#         # affected_rows = cursor.execute('insert into `tb_dept` values(%s, %s, %s)', (no, name, location))
#         affected_rows = cursor.execute('delete from `tb_dept` where `dno` = %s', (no,))
#         if affected_rows == 1:
#             # print('新增部门成功!!!')
#             print('删除部门成功!!!')
#     conn.commit()
# except pymysql.MySQLError as e:
#     conn.rollback()
#     print(type(e), e)
# finally:
#     conn.close()


import openpyxl
import pymysql


# 直连mysql，查询数据并导出
def main():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))

    conn = pymysql.connect(host='xxxxx', port=3306,
                           user='xxxxx', password='xxxxx',
                           database='hrs', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute('select `eno`, `ename`, `job`, `sal`, coalesce(`comm`, 0), `dname` '
                           'from `tb_emp` natural join `tb_dept`')
            row = cursor.fetchone()
            while row:
                sheet.append(row)
                row = cursor.fetchone()
        wb.save('D:\\aaaaaa.xlsx')
    except pymysql.MySQLError as e:
        print(e)
    finally:
        wb.close()


if __name__ == '__main__':
    main()
