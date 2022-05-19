# @property实现getter setter封装功能
# encapsulation封装 OOP
class Batman:
    def __init__(self, hp):
        self.hp = hp
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp=hp
        if hp>100:
            self._hp=100
        elif hp<0:
            self._hp=0
        else:
            self._hp=hp
b1=Batman(100)
b1.hp=150
print(b1.hp)