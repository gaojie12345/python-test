# # 判断输入是不是闰年
# f = int(input("请输入年份："))
# if (f % 100 != 0) and (f % 4 == 0) or (f % 400 == 0):
#     print("闰年")
# else:
#     print("非闰年")


# 输入成绩，输出等级
f = float(input("请输入成绩:"))
if f >= 90:
    print("A")
elif 80 <= f < 90:
    print("B")
elif 70 <= f < 80:
    print("C")
elif 60 <= f < 70:
    print("D")
else:
    print("不及格")
