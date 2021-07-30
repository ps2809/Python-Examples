from random import *
a='abcdefghijklmnopqrstuvwxyzQRSTUVWXYZABCDEFGHIJKLMNOP'
for i in range(10):
    print('The Password is:',end='')
    print(choice(a),str(randint(0,9)),choice(a),str(randint(0,9)),choice(a),str(randint(0,9)),sep='')