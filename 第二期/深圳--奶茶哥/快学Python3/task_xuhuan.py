# coding:utf8

__author__ = u'奶茶哥'

if __name__ == '__main__':

    '''for循环'''
    # 遍历元组
    tuple1 = (1,2,3,4)
    for i in tuple1:
        print(i)

    # 遍历列表
    list1 = [5,6,7,8]
    for j in list1:
        print(j)

    # 遍历字典
    dict1 = {'name':'小花','age':99}
    for key,value in dict1.items():
        print('%s:%s' %(key,value))

    # range函数
    for d in range(2,10,3):
        print(d)

    '''嵌套'''
    for i in range(1,10):
        for j in range(i,10):
            print('%d * %d = %2d  ' %(i,j,j*i), end=' ')
        print('')

    '''while'''
    # 计算0-100的所有偶数和
    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2
    print('偶数和=%d' %sum)

    # 九九乘法表
    n = 1
    while n <= 9:
        for m in range(n,10):
            print('%d * %d = %2d   ' %(n,m,n*m), end='')
        print('')
        n = n + 1

    # break和continue
    for v in range(10):
        print(v)
        if v == 2:
            print('22222222')
            continue
        if v == 5:
            print('55555555555')
            break
        print('#####################')















