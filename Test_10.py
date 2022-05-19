# try:
#     with open('f.txt', 'r')as f:
#         for line in f:
#             x = int(line.strip())
# except FileNotFoundError as err:
#     print(err)
# except ValueError:
#     print('could not convert to int')
# else:
#     print('no exception caught')
# finally:
#     print('in fianlly')

# try:
#     s = input('Please entera number:')
#     s = int(s)
# except ValueError:
#     print('ValueError,请输入数字！')
# except NameError:
#     print('NameError')
i=0
err_count=0
while True:
    try:
        s = input('please enter a number:')
        n = int(s)
        print(f'good,you entered:{n}')
    except ValueError:
        err_count+=1
        if err_count>=3:
            print('您已经输入3次了，不让你玩了！')
            break
        print('您怎么没有输入数字？')
    except KeyboardInterrupt: # Ctrl-C错误
        print('游戏结束！')
        break
    finally:
        i+=1
        print(f'这是你第{i}次玩！')
