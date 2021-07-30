import re
string=input('enter your code:')
j=re. fullmatch('ps[a-k][0369][a-zA-Z0-9#]*',string)
if j!=None:
    print('valid string')
else:
    print('invalid string')
    
    
    
n=input ('enter your numbers:')
i=re. fullmatch('[6789][0-9]{9}',n)
b=re. fullmatch('[0][6789][0-9]{9}',n)
c=re. fullmatch('[91][6789][0-9]{9}',n)
d=re. fullmatch('[+91][6789][0-9]{9}',n)
if len(n)==10:
    if i!=None:
        print(f'{n} is valid number')
    else:
        print('Number must start with 6,7,8,9')
elif len(n)==11:
    if b!=None:
        print(f'{n} is valid number')
    else:
        print('Number must start with 6,7,8,9')
elif len(n)==12:
    if c!=None:
        print(f'{n} is valid number')
    else:
        print('Number must start with 6,7,8,9')
elif len(n)==13:
    if d!=None:
        print(f'{n} is valid number')
    else:
        print('Number must start with 6,7,8,9')

else:
    print('invalid number please enter 10 digit')