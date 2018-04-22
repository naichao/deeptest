import random


class MySort:

    def __init__(self,start,end,count):
        '''
        初始化
        生成随机数,返回排序后的结果
        start, end为限制随机数生成的范围
        count为生成的随机数个数
        '''
        self.start = start
        self.end = end
        self.count = count

    def __mysort__(self):
        '''生成数据并排序'''
        list = [random.randint(self.start,self.end) for _ in range(self.count)]
        # print('list'+str(list))
        # 比较轮数,每比较1轮则i取一次值
        num_lun = self.count-1
        for i in range(num_lun):
            # 每轮比较次数，每比较1次则j取一次值
            for j in range(num_lun-i):
                if list[j] > list[j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp
                print('第'+str(i+1)+'轮第'+str(j+1)+'次比较的结果是：'+str(list))
            print('第'+str(i+1)+'轮比较的结果是：'+str(list))
        print('最后结果是：'+str(list))
        return list

if __name__ == '__main__':
    sorted_data = MySort(10,1000,100)
    # 打印排序后的结果
    print(sorted_data.__mysort__())