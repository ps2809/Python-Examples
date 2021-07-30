l1=[1,2,3,4,5,6,7,8,9,10]
l2=list(map(lambda n:n*n,l1))
print('l2:',l2)
l3=list((map(lambda n,m:n*m,l1,l2)))#map function can take more than one sequence argument
print('l3:',l3)
#if the length of the sequence is not equal then function will perform till same length
l3.pop()
print('popped l3:',l3)
l4=list(map(lambda n,m,o:n+m+o,l1,l2,l3))
print('l4:',l4)