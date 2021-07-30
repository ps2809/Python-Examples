print('this is an example of an overloding')
class books:
    def __init__(self):
        self. pages=int(input('enter number of pages:'))
    def __add__(self,other):
        return self.pages+other.pages     

print('this is add magic method')
b1=books()
b2=books()
print('total pages of both books are:',b1+b2)
print()
class books:
    def __init__(self,pages):
        self. pages=pages
    def __add__(self,other):
        return books(self.pages+other.pages) 
    def __mul__(self,other):
        return books(self.pages*other.pages)     
    def __str__(self):
        return f'the total no of pages are:{self.pages}'
print('this is add magic method')
b1=books(100)
b2=books(200)
b3=books(200)
b4=books(200)
print(b1+b2+b3+b4)
print(b1+b2*b3+b4)
print()
class student:
    def __init__(self):
        self.name=str(input('enter name:'))
        self. marks=int(input('enter marks:'))
    def __gt__(self, other):
        return self. marks>other. marks
    def __le__(self, other):
        return self. marks<=other. marks
print('this is greater than magic method')
s1=student()
s2=student()
print(f'{s1.name} has more marks then {s2.name} is:',s1>s2)
print(f'{s1.name} has more marks then {s2.name} is:',s1<s2)
print(f'{s1.name} has more marks then {s2.name} is:',s1<=s2)
print(f'{s1.name} has more marks then {s2.name} is:',s1>=s2)
print()

class employee:
    def __init__(self):
        self. name=str(input('enter name:'))
        self. sal=float(input('enter your per day salary:'))
    def __mul__(self, other):
        return self. sal*other.days
        
class total_days:
    def __init__(self):
        self. days=float(input('enter working days of the month:'))
    def __mul__(self, other):
        return self. days*other.sal
e=employee()
t=total_days()
print(f'{e.name} your total salary of this month is:',e*t,'\n',t*e)
       