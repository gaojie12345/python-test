# # 用while循环实现1-100求和
# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
#
# print(sum)


# # 用while循环实现1-100求和
# sum = 0
# num = 2
# while num <= 100:
#     sum += num
#     num += 2
#
# print(sum)

# 输出费布那切数列前20个数
a = 0
b = 1
for _ in range(0, 20):

    temp = a
    a = b
    b = temp + b
    print(a, end=' ')

