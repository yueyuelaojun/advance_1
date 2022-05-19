class Batman:
    def __init__(self,hp):
        self.hp=hp
    @staticmethod
    def f():
        print('static method!')

    @staticmethod
    def calc_avg(x):
        return sum(x)/len(x)

    @classmethod
    def fff(cls):
        cls(100).f()

Batman.f();
x=[1,2,3,4,5,6,7,8,9,10]
y=Batman.calc_avg(x)
print(y)