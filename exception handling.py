import os
try:
    #risky code
  print('try')
#  os._exit(0)
  print()
except :
    #handling code
    print('error')
else:
    print('else')
finally:
   print ('finally')
   
class Error(Exception):
    def __init__(self):
        pass
x=10
y=12
if True:
    raise Error()

try:
    print(10/0)
except:
    print('handled')