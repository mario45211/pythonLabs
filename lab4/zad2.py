def secondSum(x,y):
    return (y,x+y)

def fib(n):
    x,y=1,2
    for i in range(3,n):
        x,y=secondSum(x,y)
    print(y)

def fib2(n):
    t=secondSum(1,1)
    for i in range(3,n):
        t=secondSum(*t)
    return t

fib(7)
x,y=fib2(7)
print(y)