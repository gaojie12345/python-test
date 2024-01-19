# # 用while循环，让用户不断的猜数字，直到猜对
# import random
#
# temp = random.randint(1, 100)
# count = 0
# while True:
#     count += 1
#     f = int(input("请输入数字："))
#     if f > temp:
#         print("偏大了")
#     elif f < temp:
#         print("偏小了")
#     else:
#         print("恭喜你猜对了")
#         break
# # print("一共猜了 %d 次" % count)
# print(f"一共猜了{count}次")
# if count > 7:
#     print("你智商太低了！")

# # 打印int和float
# count = 2
# print(f"一共猜了{count}次")
#
# temp = 0.2
# print(f"一共猜了{temp}次{count}")

# 输出99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        temp = i * j
        # print(f"{i}*{j}={temp}", end= "  ")
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
