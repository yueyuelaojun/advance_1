# closure 闭包
# lifecycle
def f():
    x=1 # enclosed
    def qqq():
        print('qqq')
    class Batman:
        def __init__(self):
            print('I am batman!')
    def inner():
        print(x) # local
        qqq()
        b=Batman()
    return inner
y=f()
y()