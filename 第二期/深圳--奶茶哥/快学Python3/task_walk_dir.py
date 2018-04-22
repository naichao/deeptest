# coding:utf8
import os

__author__ = u'奶茶哥'


def walk_dir(target_dir):
    # 遍历目录
    # root:当前根目录，dirs:root下的子目录，files:root下的子文件
    walk_result = os.walk(target_dir)
    print(type(walk_result))
    for root,dirs,files in walk_result:
        print(type(root),type(dirs),type(files))
        print('-',root)
        # 遍历当前子目录
        for name in dirs:
            print('--',name)
        for name in files:
            print('---',name)

if __name__ == '__main__':

    target_dir = os.curdir
    walk_dir(target_dir)
