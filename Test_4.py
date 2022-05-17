import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(self):
        pass#这里写什么都不会执行

class Dog(Animal):
    def make_sound(self):
        print('bark')
class Cat(Animal):
    def make_sound(self):
        print('miao')

class Person(Animal):
    def make_sound(self):
        print('hi')
d=Dog()
d.make_sound()
c=Cat()
c.make_sound()
p=Person()
p.make_sound()