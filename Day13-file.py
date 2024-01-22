# 01-22
import os.path
import time

# # 文件相关的操作
# # 如果open指定的文件打不开，会异常，所以需要捕获异常
# def function():
#     f = open('D:\\test.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()
#
#
# if __name__ == '__main__':
#     function()


# # 处理open文件过程中出现的异常
# def main():
#     f = None
#     try:
#         f = open('ttt')
#         print(f.read())
#     except FileNotFoundError:
#         print("无法打开文件")
#     finally:
#         if f:
#             f.close()
#
#
# if __name__ == '__main__':
#     main()


# # 如果不想在finally中显式的调用close方法
# # 可以使用with关键字指定文件的上下文环境，并在离开上下文环境时自动释放文件资源（相当于自动调用close）
# def main():
#     f = None
#     try:
#         with open('x') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print("无法打开文件")
#     except LookupError:
#         print("指定了未知的编码!")
#     except UnicodeDecodeError:
#         print("读取文件时解码错误!!")
#
#
# if __name__ == '__main__':
#     main()


# # 使用for-in循环逐行读取文件
# def main():
#     with open('D:\\test.txt') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()
#
#
# if __name__ == '__main__':
#     main()


# # 用readlines方法将文件按行读取到一个列表容器中
# def main():
#     with open('D:\\test.txt', encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
#
#
# if __name__ == '__main__':
#     main()


# 将文本信息写入file中
import os


def write_numbers_to_file(file_path, start, end):
    # 确保指定的目录存在，如果不存在，尝试创建它
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            print(f"Error: 创建目录失败 {directory}. {e}")
            return

    # 尝试写入文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for i in range(start, end + 1):
                f.write(str(i) + '\n')
    except IOError as e:
        print(f"Error: 写入文件失败 {file_path}. {e}")


def main():
    # 指定文件路径和要写入的数字范围
    file_path = 'D:\\b\\a.txt'
    start = 1
    end = 10
    # 写入数字
    write_numbers_to_file(file_path, start, end)


if __name__ == '__main__':
    main()
