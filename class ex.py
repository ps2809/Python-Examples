class example:
    schoolname='M.D.Shah' #this is class level or staic variable
    ''' This is an example of class''' #optional
    def __init__(self): #self is ref var for current object
       #constructor
        example.grade='High School' #definiing static var inside constructor
        self.name=input('enter name:')     #these are the instance variable
        self.city=input('enter city:')
        self.work=input('enter work:')
        print('Address of self:',id(self),'\n')
    '''this method is instance method'''
    def info(self):
        #del self.name     #to delete variable inside class
        self.stds='9th to 12th' #defining static var in instance method
        self.passion=input('Enter your Passion:')
        print('Hello I am:',self.name)
        print(f'{self.name} is from',self.city)
        print('I\'m:',self.work)
        print('My Passion is:',self.passion) 
        print('''\n"Static var inside instance method"\nStandards :''',self.stds)
            
    @classmethod #decorator is mandatory
    def getscl(cls):
        cls.streams=('Science','Commerce','Arts') #static var inside class method
        print('\n School Name:', cls.schoolname,example.grade)
         #static var can be called either by using cls or by class name inside the class method
        print('Availbale Courses:',example.streams)
        print('address of cls:',end='')
        print(id(cls))
    @staticmethod     #This method is independent of the any variable
    def getsum(a,b):
        example.subject='Computer & Sanskrit' #static var inside static method
        print('Optional Subjects in Science: ', example.subject)
        c=a+b #local variable
        print('Sum of entered numbers is:',c)
z=input('Do you want to help of the Class[yes/No]:').lower()
if z=='yes':
    help(example)
print('Address of class:',id(example),'\n')
print('\"This is an example of the Instance Method\"')       
s1=example() #calling class or creating object  
print('Info of S1 grp:',end='  ')
print(s1.name) #printing variables of the class
print('\t\t',s1.city)
print('\t\t',s1.work)
print('\nAddress of s1:',id(s1),'\n')
s1.info() #adding instance variable into method
s1.goal=input('Enter your Goal:') #adding instance variable outside of the class
print('My Goal is to Become:',s1.goal,'\n')
print('='*72,'\n\"This is an example of the Class Method\"','\n','='*72,sep='')
s1.getscl()
print('\n\"This is an example of the Static Method\":' , s1.getsum(10,20))
s2=example()
#del s1.name,s2.city     #to delete the Instance variable outside of the class
print('s1 dict:',s1.__dict__)
s1.name='Sonagara'     #changing variable data
x=input('Do you want to read dictionary of The Class[Yes/No]:')
if x=='yes':
    print('='*72,'\nThese are the Dictionaries of the all variables in the Class:\n','='*72,sep='')
    print('\nModified s1 dict:',s1.__dict__)
    print('\ns2 dict:',s2.__dict__)
    print('\nclass dict:',example.__dict__)

#class a:
#    def b(self): #creating constructor with same name
#        print('constructor1')
#    def b(self,x):
#        print('constructor2')
#        
#        
#        
#s=a()
#s.b()
#s.b(10)