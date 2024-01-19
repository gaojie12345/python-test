# 求 1-100 加和
# range函数：左闭右开
# f = 0
# for x in range(1, 101):
#     f = f + x
# print(f)

# # 求 1-100 之间偶数的加和
# # range函数，第三个参数表示每隔几个取数,也就是步长
# f = 0
# for x in range(2, 101, 2):
#     f += x
# print(f)

# 求输入n的n!
n = int(input("请输入n："))
a = 1
for x in range(1, n + 1):
    a *= x
print(a)
