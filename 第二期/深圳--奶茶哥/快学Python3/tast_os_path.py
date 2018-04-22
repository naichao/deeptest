# coding:utf8
import os

__author__ = u'奶茶哥'

if __name__ == '__main__':

    # os模块

    # 返回完整的目录路径
    print('当前工作目录：',os.getcwd())

    # 返回目录路径.
    print('当前工作目录：',os.curdir)

    # 创建目录，目录必须不存在，存在则报错
    # os.mkdir('test_mk1')

    # 重命名目录
    # os.rename('test_mk1','test_mk2')

    # 删除指定目录，目录必须存在，无子目录，无子文件
    # os.removedirs('test_mk2')

    # 改变工作目录路径
    os.chdir('d:')
    print('当前工作目录：',os.getcwd())

    print('-' * 30)
    # path模块

    # 先初始化当前文件全路径变量
    path = __file__
    print('当前文件全路径是：%s' % path)

    # 判断是否为目录，是则返回True，否则返回False
    print('目录判断：%s' % os.path.isdir(path))

    # 判断是否为文件，是则返回True，否则返回False
    print('文件判断为：%s' % os.path.isfile(path))


    # 判断目录或文件是否存在
    print('目录或文件存在：%s' % os.path.exists(path))

    # 获取文件大小，若目标为目录则返回0
    print('文件大小：%s' % os.path.getsize(path))

    # 获取文件的绝对路径
    print('文件的绝对路径：%s' % os.path.abspath(path))

    # 将目标规范化，规范化的表达方式，跨平台标识
    print('规范化路径：%s' % os.path.normpath(path))

    # 将文件名和目录分割，若传入的是目录，则将最后的目录名作为文件名分割
    print('目录和文件名分割：', end='')
    print(os.path.split(path))

    # 分离文件名和扩展名
    print('文件名和扩展名分离：', end='')
    print(os.path.splitext(path))

    # 获取文件名
    print('文件名为：%s' % os.path.basename(path))

    # 获取文件所在的目录
    print('文件目录为：%s' % os.path.dirname(path))
























