import re
f1=open('in(re).txt', 'r')
f2=open('op(re).txt','w')
for line in f1:
    list=re. findall('[6789][0-9]{9}',line)
    for number in list:
        f2.write(number+'\n')
    