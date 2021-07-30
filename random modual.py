from random import *
y=input('Enter name of the function:').strip().lower()
print('your entered function:',y)
x=int(input('enter value of x to get your desired result:'))
if y=='random':
    help(random)
    print('\n examples of random function:')
    print()
    for i in range(1,x+1):
        print(' example',str(i),'of Random() to generate random float value b/w 0 and 1 (0,1)\n\t\t=',round(random(),6),'\n')
elif y=='uniform':
    help(uniform)
    print(' examples of uniform function:')
    print()
    for j in range(1,x+1):
        print('\n example',str(j),'of uniform() to generate random float value b/w (0,100) \n\t\t=',round(uniform(0,100),6),'\n')
elif y=='random int':
    help(randint)
    print('\n example of randint function')
    print()
    for k in range(1,x+1):
        print(' example',str(k),'of randint() to generate random int value b/w (0,100)\t=',randint(0,100),'\n')
elif y=='random range':
    help(randrange)
    b=int(input('enter the value of step:'))
    print('\n example of randint function in range of 1 to 100:')
    print()
    for k in range(1,x+1):
        print(' example',str(k),'of randrange() to generate random int value=',randrange(0,100,b),'\n')