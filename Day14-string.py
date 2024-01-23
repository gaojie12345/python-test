# 01-23


import re


# 验证输入用户名和QQ号是否有效并给出对应的提示信息
# 要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为

# def main():
#     username = input("请输入用户名")
#     qq = input("请输入QQ号")
#     bool1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
#     if not bool1:
#         print("请输入有效的用户名")
#     bool2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not bool2:
#         print("请输入有效的QQ")
#     if bool1 and bool2:
#         print("信息输入正确")
#
#
# if __name__ == '__main__':
#     main()


# # 替换字符串中的不良内容
# def main():
#     msg = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
#     purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', msg, flags=re.IGNORECASE)
#     print(purified)
#
#
# if __name__ == '__main__':
#     main()


# 拆分长字符串
def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(sentence_list)
    # while '' in sentence_list:
    #     sentence_list.remove('')
    # print(sentence_list)


if __name__ == '__main__':
    main()
