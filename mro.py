print('to check priority of the class #')

class a:pass
class b(a):pass
class c(a):pass
class d(b,c):pass
print(a.mro())
print(b.mro())
print(c.mro())
print(d.mro())