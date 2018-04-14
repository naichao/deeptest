# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':
    '''内置函数'''
    tuple_demo = (1,2,3,4,5,6,7,8)

    # 计算tuple_demo中元素个数
    print(len(tuple_demo))

    # 返回tuple_demo的最大值元素
    print(max(tuple_demo))

    # 返回tuple_demo的最小值元素
    print(min(tuple_demo))

    # 将列表转换成元组
    list_demo = [1,3,5,7,9]
    print(tuple(list_demo))

    # 将元组转换成列表
    print(list(tuple_demo))

    '''切片'''
    tuple_tools = ('selenium','appium','jemter','loadrunner','soapui')
    # 获取appium
    print(tuple_tools[1])

    # 获取loadrunner
    print(tuple_tools[-2])

    # 获取第2个元素后面的所有元素
    print(tuple_tools[1:])

    # 获取第2个元素到第4个元素
    print(tuple_tools[1:4])

    '''合并'''
    tuple1 = (1,3,5)
    tuple2 = ('a','b','c')
    tuple3 = tuple1 + tuple2
    print(tuple1)
    print(tuple2)
    print(tuple3)

    '''删除'''
    del tuple3
    # print(tuple3)

    '''运算'''
    # 复制元组
    tuple4 = tuple1 * 2
    print(tuple4)

    # 判断元素是否在元组中，是则返回Ture，反之返回False
    result1 = 5 in tuple1
    result2 = 7 in tuple1
    print(result1)
    print(result2)

    # 遍历元组
    for i in tuple1:
        print(i)










