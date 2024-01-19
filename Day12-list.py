# 01-19


# # 列表的相关操作
# # 找出列表中最大或最小的元素
# def main():
#     fruits = ["grape", "apple", "strawberry", "waxberry"]
#     # 直接使用内置的max和min函数找出列表中最大和最小元素
#     # print(max(fruits))
#     # print(min(fruits))
#     max_vale = min_value = fruits[0]
#     for index in range(1, len(fruits)):
#         if fruits[index] > max_vale:
#             max_vale = fruits[index]
#         elif fruits[index] < min_value:
#             min_value = fruits[index]
#
#     print(f"Max-Value:{max_vale}")
#     print(f"Min-Value:{min_value}")
#
#
# if __name__ == '__main__':
#     main()


# # 列表的CURD
# def main():
#     fruits = ["grape", "apple", "strawberry", "waxberry"]
#     print(fruits)
#     # 通过下标访问元素
#     print(fruits[0])
#     print(fruits[1])
#     print(fruits[-1])
#     print(fruits[-2])
#
#     # 修改元素
#     fruits[1] = "@pple"
#     print(fruits)
#
#     # 添加元素
#     fruits.append('pitaya')
#     fruits.insert(0, "banana")
#     print(fruits)
#
#     # 删除元素
#     fruits.pop()
#     fruits.pop(0)
#     fruits.remove('@pple')
#     print(fruits)
#
#
# if __name__ == "__main__":
#     main()


# 列表拼接、翻转
# def main():
#     my_list = ['g1', 'g2', 'g3', 'g4']
#     my_list += ['j1', 'j2']
#     for index in range(len(my_list)):
#         print(my_list[index], end=' ')
#
#     print()
#     my_list1 = my_list[1:4]
#     print(my_list1)
#
#     my_list2 = my_list[:]
#     print(my_list2)
#
#     my_list3 = my_list[-3:-1]
#     print(my_list3)
#
#     # 翻转列表
#     my_list4 = my_list[::-1]
#     print(my_list4)
#
#
# if __name__ == '__main__':
#     main()



