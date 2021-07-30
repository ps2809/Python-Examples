from time import *
f=open('log.txt','rb')
with open('log.txt','r') as f:
    print('current position of curser',f.tell())
    print('file is opened at index no:',f.seek(999))
    line=f.read()
    while line!='':
        print(line, end='')
       # sleep(1.2)
        line=f.readline()
    print('curent position of curser',f.tell())
print(f.closed)
#f.write('hello \n')
#l=['hii ','welcome ','this is list\n']
#k={'hii ','welcome ','this is set\n'}
#m={'greet':'hi'}
#f.writelines('hello ''writeline example\n')
#f.writelines(l)
#f.writelines(k)
#f.writelines(m.values())
#print(f.name)
#print()
#print(f.readlines())
#f. close()
