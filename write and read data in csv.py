import csv
x=input('what operation do you want to perform [read/write]:')
with open ('ex.csv','r+', newline='') as f:
    if x=='write':
        w=csv.writer(f)
        #print(type(w))
        w.writerow(['emp_no','emp_name','emp_sal','emp_addr'])
        while True:
            eno=int(input ('enter employee number :'))
            ename=input ('enter employee name :')
            esal=int(input ('enter employee salary :'))
            eaddr=input ('enter employee address :')
            w.writerow([eno,ename,esal,eaddr])
            y=input ('do you want to add more data [y/n]:').lower()
            if y=='n':
                break
    elif x=='read':
        r=csv.reader(f)
        data=list(r)
        print(data)  
        print()      
        for row in data:
            for column in row:
                print(column,'\t', end='')
            print()
        