
# 实现一个四则运算的类，要求实现任意两个数的加减乘除运算
class Calc:

    def __init__(self,a,b):
        '''初始化'''
        self.a = a
        self.b = b

    def add(self):
        '''加法'''
        return self.a+self.b

    def sub(self):
        '''减法'''
        return self.a - self.b

    def mul(self):
        '''乘法'''
        return self.a * self.b

    def div(self):
        '''除法'''
        if self.b == 0:
            print('0不能作为分母')
        else:
            return self.a / self.b

if __name__ == '__main__':
    calc = Calc(2,0)
    print(calc.add())
    print(calc.sub())
    print(calc.mul())
    print(calc.div())