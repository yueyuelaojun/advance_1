from Test_1 import Product  # parent class/base class
# child class/derived class
class Drink(Product):  # override
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

d = Drink('珍珠奶茶', 80, 600)
print(d.volume)
print(isinstance(d,Drink))
print(isinstance(d,Product))
print(type(Drink))
