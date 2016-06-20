def insert(L,odstep):
    i=0
    while(i<=len(L)):
        if (i+1)%(odstep+1) == 0:
            L.insert(i,0)
        i+=1
    return L

def insert2(L,odstep):
    i=odstep
    while(i<=len(L)):
        L.insert(i,0)
        i+=odstep+1
    return L

list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(insert(list,2))
list=[1,2,3,4,5,6,7,8,9,10]
print(insert2(list,3))