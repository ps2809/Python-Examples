class a:
    def __init__(self):
        self. x=10
    def m1(self):
        print("public variable and method")
    def m2(self):
        print(self.x)
        self. m1()
        
t=a()
t. m2()
t.x
t.m2()
print()
class A:
    def __init__(self):
        self. __x=20
    def __m1(self):
        print("private variable and method")
    def m2(self):
        print(self.__x)
        self. __m1()
        
s=A()
s. m2()
print(s._A__x)
s. _A__m1()
print()
class A:
    def __init__(self):
        self. _x=30
    def _m1(self):
        print("protected variable and method")
class x(A):
    def m2(self):
        print(self._x)
        self. _m1()
        
t=x()
t. m2()
print(t._x)