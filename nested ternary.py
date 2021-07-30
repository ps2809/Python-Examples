a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
min_value= a if a<b and a<c else b if b<c else c
print(min_value)