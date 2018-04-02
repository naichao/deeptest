import random


class MySort:

    def __init__(self,start,end,count):
        '''初始化'''
        self.start = start
        self.end = end
        self.count = count

    def __mysort__(self):
        '''生成数据并排序'''
        list = [random.randint(self.start,self.end) for _ in range(self.count)]
        print(list)
        print(len(list))



if __name__ == '__main__':
    sorted_data = MySort(10,1000,100)
    # 打印排序后的结果
    # print(sorted_data).
    sorted_data.__mysort__()

