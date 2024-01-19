# 将华氏温度转换为摄氏温度
# F = 1.8C + 32
# f = float(input("请输入华氏温度："))
# c = (f - 32) / 1.8
#
# # print("%.f华氏度 = %.1f摄氏度" % (f, c))
# print("{:.1f}华氏度 = {:.1f}摄氏度".format(f, c))
import math

# 输入圆的半径，输出圆的周长和面积
a = float(input("请输入圆的半径："))
f = math.pi * 2 * a
c = math.pi * a * a
print("圆的周长为{:.2f}, 面积为{:.2f}".format(f, c))
