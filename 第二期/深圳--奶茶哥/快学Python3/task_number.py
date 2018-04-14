# coding:utf8
import math
import random

import cmath

__author__ = u'奶茶哥'

if __name__ == '__main__':
    x = -100
    y = 1.9
    a = 1.68
    b = 10

    # 将a转换成整数
    print(int(a))

    # 将b转换成浮点型
    print(float(b))

    # 将a转换成复数，实数部分为a,虚数部分为0
    print(complex(a))

    # 将a,b转换成复数，实数部分为a，虚数部分为b
    print(complex(a,b))

    print(u'常用数学函数')
    # 返回绝对值
    print(abs(x))

    # 返回最大值
    print(max(x,y))

    # 返回最小值
    print(min(x,y))

    # 计算y^2
    print(pow(y,2))

    # 返回平方根
    print(math.sqrt(y))

    print(u'常用随机数')
    list = [1,2,3,4,5,6,7,8,9]

    # 从列表中随机选中一个值
    print(random.choice(list))

    # 生成一个随机数，它们在0-1之间
    print(random.random())

    print(u'常用的三角函数')
    x = 60

    # 返回x的反余弦弧度值
    print(cmath.acos(x))

    # 返回x的余弦弧度值
    print(cmath.cos(x))

    # 返回x的正弦弧度值
    print(cmath.sin(x))

    print(u'常用的数学常量')
    # 返回π值
    print(cmath.pi)