# # 将求阶乘的功能封装成一个函数
# def function(n):
#     result = 1
#     for j in range(1, n + 1):
#         result *= j
#     return result
#
#
# print(function(2))


# python的一些的内置函数
print(abs(-1.2345))  # 绝对值
print(round(-1.2345, 1))  # 四舍五入保留1位小数
print(pow(1.2345, 5))  # 计算第一个数的5次方


def my_filter(my_str):
    return len(my_str) == 6


fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])  # 返回切片fruits的从1-3的元素，前闭后开

# filter函数：函数接受两个参数：一个函数和一个可迭代对象。它将可迭代对象中的每个元素传递给函数，并收集函数返回 `True` 的那些元素
# list函数：函数接受一个可迭代对象（在这里是 `filter` 函数的输出）并将其转换为一个列表。
fruits2 = list(filter(my_filter, fruits))
print(fruits)
print(fruits2)
