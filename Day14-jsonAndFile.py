# 01-23
import json


# json模块主要有四个比较重要的函数，分别是：
#
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
def main():
    mydict = {
        'name': '高杰',
        'age': 16,
        "qq": 123344,
        'friends': ['王大锤', '白展堂'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('D:\\data.txt', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('数据保存完成！')


if __name__ == '__main__':
    main()
