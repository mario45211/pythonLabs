def deleteSomeEl(L):
    i=0
    r=0
    while(i-r<len(L)):
        if (i + 1) % 3 == 0:
            del L[i-r]
            r+=1
        i += 1
    i=0
    r=0
    while(i-r<len(L)):
       if L[i-r]<0:
            del L[i-r]
            r+=1
       i+=1

    return L

list=[1,-2,5,-16,33,2,3,-9,0]
print(deleteSomeEl(list)) #[1,33,3]