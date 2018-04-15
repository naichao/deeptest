# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':

    set1 = set('appium,selenium')
    print(set1)

    set_source = set([1,1,2,3,4,5])
    set_demo = set([1,1,2,3,4,5])
    print('原始数据是：'+str(set_demo))

    # add方法添加单个元素
    set_demo.add(9)
    set_demo.add(8)
    print(set_demo)

    # remove删除元素
    set_demo.remove(9)
    print(set_demo)

    # update增加多个元素值
    set_demo.update(['a','b','c'])
    print(set_demo)

    # clear清空列表
    # set_source.clear()
    # print(set_source)

    # uion返回并集
    print(set_demo)
    print(set_source)
    print(set_demo.union(set_source))

    # intersection返回交集
    print(set_demo.intersection(set_source))

    # difference返回1中有，2中没有的元素
    print(set_demo.difference(set_source))