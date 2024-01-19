# 01-18


# # 字典的相关操作
# # 字典相当于java中的map
# def main():
#     scores = {"高杰": 26, "张三": "111"}
#     print(scores["高杰"])
#     print(scores["张三"])
#
#     print("***************************")
#     for elem in scores:
#         print(f"{elem} ---> {scores[elem]}")
#
#     scores["高杰"] = 1
#     scores["张三"] = 333
#     scores.update(李四=18, 王五=20)
#
#     print(scores)
#
#     print("***************************")
#
#     if "武则天" in scores:
#         print("武则天对应的value--->" + scores["武则天"])
#     print(scores.get("武则天"))
#     print(scores.get("武则天", 60))
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop("武则天", 100))
#     scores.clear()
#     print(scores)
#
#
# if __name__ == "__main__":
#     main()


def function():
    stu = {"name": "张三", "age": 14, "gender": True}
    print(stu)
    print(stu.keys())
    print("-----------------------")
    #items()该方法返回一个视图对象，包含字典中所有的键值对（key-value pairs）。
    # 这个视图对象可以用于迭代字典中的每一项，每项都表现为一个包含两个元素的元组（tuple），其中第一个元素是键，第二个元素是对应的值。
    print(stu.items())
    print("-----------------------")

    for i in stu.items():
        print(i)
        print(i[0], i[1])

    if "age" in stu:
        stu["age"] = 18
    print(stu)
    stu.setdefault("score", 60)
    print(stu)
    stu.setdefault("score", 80)
    print(stu)
    stu["score"] = 100
    print(stu)


if __name__ == "__main__":
    function()
