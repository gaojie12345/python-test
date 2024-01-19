# # 定义一个Student类练手
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%s 正在学习%s.' % (self.name, course_name))
#
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》' % self.name)
#         else:
#             print('%s正在看爱情电影' % self.name)
#
#
# def main():
#     # 创建学生对象并指定姓名和年龄
#     stu1 = Student('高杰', 20)
#     # 给对象发study消息
#     stu1.study('Python程序设计')
#     # # 给对象发watch_av消息
#     # stu1.watch_movie()
#     # stu2 = Student('王大锤', 15)
#     # stu2.study('思想品德')
#     # stu2.watch_movie()
#
#
# if __name__ == '__main__':
#     main()

# # 定义一个People练手
# class People:
#
#     def __init__(self, name, age, __weight):
#         self.name = name
#         self.age = age
#         self.__weight = __weight
#
#     def method(self):
#         print('%s说我%s岁了' % (self.name, self.age))
#
#
# def test():
#     p = People('高杰', 20, 74)
#     p.method()
#
#
# if __name__ == '__main__':
#     test()


# 根据Python的名称改写规则（name mangling）
# 当你在类的定义中使用双下划线`__`前缀时
# Python解释器会自动将该方法名改写成`_ClassName__MethodName`的形式。
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    # print(test._Test__foo)


if __name__ == "__main__":
    main()
