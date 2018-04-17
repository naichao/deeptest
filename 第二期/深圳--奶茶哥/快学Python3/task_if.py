# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':

    '''if语句'''
    var1 = int(input('请输入一个整数：'))

    # if var1 > 0 and var1 < 10:
    #     print('你输入了 一个大于0小于10的整数')
    # elif var1 > 10:
    #     print('你输入了一个大于10的整数')
    # else:
    #     print('你输入了一个负数')

    '''嵌套条件控制'''
    if var1 > 0:
        if var1 < 5:
            print('你输入了一个大于0小于5的整数')
        elif var1 >= 5 and var1 <=10:
            print('你输入了一个大于等于5,小于等于10的整数')
        else:
            print('你输入了一个大于10的整数')
    elif var1 < 0:
        print('你输入了一个负数')
    else:
        print('你输入了0')

