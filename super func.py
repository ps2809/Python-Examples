class p:
    def m1(self):
        print('this is parent class')
class c(p):
    def m1(self):
        super().m1() #to call parent class explicitly
        print('child class')
        
        
c=c()
c.m1()
