# # 函数传入可变参数
# def function(*val):
#     sum = 0
#     for num in val:
#         sum += num
#     return sum
#
#
# print(function(1, 3))
# print(function(1, 3, 5, 7))
# print(function())


# # 关键字参数
# # `**kw`是一种特殊的参数，它允许函数接收任意数量的关键字参数
# # `**`是一个解包操作符，它将传递给函数的所有关键字参数收集到一个名为`kw`的字典中
# def f3(**kw):
#     if 'name' in kw:
#         print('欢迎你%s!' % kw['name'])
#     elif 'tel' in kw:
#         print('你的联系电话是: %s!' % kw['tel'])
#     else:
#         print('没找到你的个人信息!')
#
#
# param = {'name': '骆昊', 'age': 38}
# f3(**param)
# # f3(name='骆昊', age=38, tel='13866778899')
# # f3(user='骆昊', age=38, tel='13866778899')
# # f3(user='骆昊', age=38, mobile='13866778899')


# # 变量作用域
# def foo1():
#     a = 5
#
#
# foo1()
#
# b = 10
#
# def foo2():
#     print(b)
#
# foo2()
#
# def foo3():
#     b = 100  # 局部变量
#     print(b)
#
# foo3()
# print(b)
#
# def foo4():
#     global b
#     b = 200  # 全局变量
#     print(b)
#
# foo4()
# print(b)





# 输入学生的成绩计算平均分

def main():
    number = int(input("请输入学生个数:"))
    names = [None] * number
    scores = [None] * number
    for index in range(number):
        names[index] = (input(f"请输入第{index + 1}个学生的姓名:"))
        scores[index] = float(input(f"请输入第{index + 1}个学生的成绩:"))

    sum = 0
    for index in range(number):
        print(f"{names[index]} : {scores[index]}分")
        sum += scores[index]
    print(f"总分为{sum}")
    print(f"平均分为{sum / number}")


# 确定一个Python脚本是被直接运行还是作为模块导入到另一个脚本中
if __name__ == '__main__':
    main()
