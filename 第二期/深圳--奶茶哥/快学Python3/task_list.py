# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':

    '''内置函数'''
    list_demo = [1,2,3,4,5,6,7,8,9,0]

    # 计算列表元素个数
    print(len(list_demo))

    # 返回列表最大值的元素
    print(max(list_demo))

    # 返回列表最小值的元素
    print(min(list_demo))

    # 将元组转换成列表
    tuple_demo = (1,2,3,4,5,6,7,8,9,0)
    print(list(tuple_demo))

    '''list方法'''
    list1 = [1,1,2,2,2,3,3,3,4,5,6]
    list2 = [7,8,9,0,10,11]

    # append,追加一个元素
    list1.append(100)
    print(list1)

    # count,统计1出现的次数
    count = list1.count(1)
    print(count)

    # extend,将list2追加到list1中
    list1.extend(list2)
    print(list1)

    # index，返回第一个4的索引
    index = list1.index(4)
    print(index)

    # insert,在列表的第一个位置插入200
    list1.insert(0,200)
    print(list1)

    # pop,删除最后一个元素
    list1.pop()
    print(list1)

    # reverse,把列表反向一下
    list1.reverse()
    print(list1)

    # sort，对列表进行排序
    list1.sort()
    print(list1)

    # copy,复制列表
    list3 = list1.copy()
    print('list1:' + str(list1))
    print('list3:' + str(list3))

    # clear，清空列表
    list1.clear()
    print(list1)
    print(list3)

    '''切片'''
    list_tools = ['selenium','appium','jemter','loadrunner','soapui']

    # 读取appium
    print(list_tools[1])

    # 读取倒数第2个元素
    print(list_tools[-2])

    # 切片，截取第2个元素开始后的所有元素
    print(list_tools[1:])

    # 切片，截取第2-4个元素
    print(list_tools[1:4])

    # 把soapui改成postman
    list_tools[4] = 'postman'
    print(list_tools[4])





