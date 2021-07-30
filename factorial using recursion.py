def fact(n):
    print('execution of factorial function for n:',n)
    if n==0:
        result=1
    else:
        result=n*fact(n-1) 
    print('returning factorial of ({}) is:{}'.format(n, result))
    return result
print(fact(6))