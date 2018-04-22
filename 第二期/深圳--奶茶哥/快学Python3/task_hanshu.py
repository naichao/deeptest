# coding:utf8

__author__ = u'奶茶哥'

# 乘法表
def multi():
    data = []
    for i in range(1,10):
        line = []
        for j in range(i,10):
            line.append('%d * %d = %2d   ' % (i, j, i*j))
        data.append(line)
    return data

# 元组传递
# 求和
def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum

# 字符串传递
def str_join(str1,str2,str3):
    return str1 + str2 + str3

if __name__ == '__main__':
    for d in multi():
        print(d)

    tuple_1 = [1,3,5,7,9]
    sum = sum_tuple(tuple_1)
    print(u'和为：%d' % sum)

    str1 = '山重'
    str2 = '水复'
    str3 = '疑无路'
    print(str_join(str1,str2,str3))
















