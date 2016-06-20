def div(A,B):
    if(len(A)<=len(B)):
        return [round(A[i]/B[i],2) for i in range(0,len(A)) if B[i]!=0]
    else:
        return [round(A[i] / B[i], 2) for i in range(0, len(B)) if B[i] != 0]
a=[1,2,3]
b=[3,0,6]
print(div(a,b))