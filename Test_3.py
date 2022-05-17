from abc import ABCMeta,abstractmethod

class Product(metaclass=ABCMeta):#不要用原本的type生成class
    @abstractmethod
    def hi(self):
        pass
#抽象类是需要被继承的，所有的抽象类都需要被override
class Drink(Product):
    def hi(self):
        print('hi')

d=Drink()