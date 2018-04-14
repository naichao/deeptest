# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':
    '''内置函数'''
    dict = {'name':'小花','age':99,'color':'yellow'}

    # len,计算字典长度
    print(len(dict))

    # str，打印字典
    print(str(dict))

    # 判断字典类型
    print(type(dict))

    '''字典方法'''
    dict2 = {'name':'花姑娘','age':99,'color':'yellow'}
    dict3 = {'age':99,'color':'yellow'}
    tuple2 = (1,2,3,4)

    # 复制字典
    dict_cp = dict2.copy()
    print(dict_cp)

    # fromkeys创建字典
    dict_new = dict.fromkeys(tuple2,'value')
    print(dict_new)

    # get，获取指定key的value
    value1 = dict2.get('name','我是默认值')
    value2 = dict2.get('yellow','我是默认值')
    print(value1)
    print(value2)
    print('dict2:'+str(dict2))

    # in 判断key是否存在
    key = 'name'
    result1 = key in dict2
    result2 = key in dict3
    print(result1)
    print(result2)

    # items,以元组的形式返回字典所有key和value
    items = dict2.items()
    print(items)

    # keys,以列表的形式返回字典所有的key
    keys = dict2.keys()
    print(keys)

    # setdefault,如果key存在，则返回对于的value值，
    # 否则将该key值和默认值插入到字典中，并返回默认值
    set_result1 = dict2.setdefault('name','默认值')
    set_result2 = dict2.setdefault('我是key','默认值')
    print(set_result1)
    print(set_result2)
    print('dict2:'+str(dict2))

    # update,更新字典
    dict2.update(dict_new)
    print(dict2)

    # value,返回字典中所有的value
    print(dict2.values())

    '''遍历、修改、删除'''
    dict4 = {'name':'花姑娘','age':99,'color':'yellow'}
    # 遍历字典
    for (key,value) in dict4.items():
        print('%s:%s' %(key,dict4[key]))

    for (key,value) in dict4.items():
        print('%s:%s' %(key,value))

    # 修改
    dict4['name'] = '默认值'
    print(dict4)

    # 删除指定元素
    del dict4['name']
    print(dict4)

    # 清空字典
    dict4.clear()
    print(dict4)





