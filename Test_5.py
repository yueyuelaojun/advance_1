import time
def print_func(func):
    def inner():
        print('running...', func.__name__)
        func()
    return inner
def time_func(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print('elapsed:',end-start,'seconds')
    return inner

@print_func
@time_func
def test():
    for i in range(10000000):
        i+=1
    print('Hi')
@time_func
def test2():
    for i in range(10000000):
        i+=1
    print('你好!')
test()



