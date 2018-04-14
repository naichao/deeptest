# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':
    '''字符连接和切割'''
    tuple = ('1','2','3','4','a','b','cde')

    # 用 - 将tuple中元素连接成一个新的字符串
    str_new = '-'.join(tuple)
    print(str_new)

    # 将str_new以 - 进行切割
    str_set = str_new.split('-')
    print(str_set)

    # 将tuple中的元素合并成一个新的字符串
    str_new2 = ''.join(tuple)
    print(str_new2)

    '''字符串查找和替换'''
    str_source = 'it is my book , please show it , wa ka ka , yo yo yo !'

    # 从左往右查找yo
    print(u'从左往右查找yo')
    print(str_source.find('yo'))
    print(str_source.index('yo'))

    # 从右往左找yo
    print(u'从右往左找yo')
    print(str_source.rfind('yo'))
    print(str_source.rindex('yo'))

    # 替换所有的yo
    print(u'替换所有的yo')
    print(str_source.replace('yo','ha'))

    # 替换2次yo
    print(u'替换2次yo')
    print(str_source.replace('yo','ha',2))

    '''去字符串前后空格'''
    str_delete_space = ' 我的前 后 和 中 间 都有空格 '
    print(str_delete_space)

    # 去除前面的空格
    print(str_delete_space.lstrip())

    # 去除后面的空格
    print(str_delete_space.rstrip())

    # 去除前后的空格
    print(str_delete_space.strip())

    '''判断字符串类型'''
    str_1 = '1234567'
    str_2 = 'abcdABCD'
    str_3 = '123abcABC'
    str_4 = 'abcd'
    str_5 = 'ABCD'
    str_6 = '    '
    str_7 = '  abc'

    # isalnum
    print(str_3.isalnum())
    # isalpha
    print(str_2.isalpha())
    # isdigit
    print(str_1.isdigit())
    # islower
    print(str_4.islower())
    print(str_2.islower())
    # isupper
    print(str_4.isupper())
    print(str_2.isupper())
    # isspace
    print(str_6.isspace())
    print(str_7.isspace())
