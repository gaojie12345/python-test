# 打印三角形
# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range(i + 1):
        print("*", end='')
    print()

print()

# 打印三角形
#     *
#    **
#   ***
#  ****
# *****
for i in range(5):
    for j in range(5):
        if j < 5 - 1 - i:
            print(" ", end="")
        else:
            print("*", end="")
    print()

print()

# 打印三角形
#     *
#    ***
#   *****
#  *******
# *********
for i in range(5):
    for j in range(5 - 1 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end='')
    print()
