# # 掷骰子决定做什么事情
# from random import randint
#
# f = randint(1, 6)
# if f == 1:
#     result = "唱歌"
# elif f == 2:
#     result = "跳舞"
# elif f == 3:
#     result = "蹦迪"
# elif f == 4:
#     result = "喝啤酒"
# elif f == 5:
#     result = "洗澡"
# else:
#     result = "吃饭"
#
# print(result)


import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % area)
else:
    print('不能构成三角形')
