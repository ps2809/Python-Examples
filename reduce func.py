from functools import * #reduce is not python's inbuilt func we have to import explicitly
l1=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l1)
print('result:',result)
j=reduce(lambda x,y:x+y, range(1,101))
print('j:',j)
    