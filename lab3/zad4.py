def add(A,B):
    if(len(A)<=len(B)):
        return [A[i]+B[i] for i in range (0,len(A))]
    else:
        return [A[i] + B[i] for i in range(0, len(B))]

a=[1,2,3,7]
b=[3,4,5,5]
c=add(a,b)
print(c)