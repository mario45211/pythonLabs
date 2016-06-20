def listDetail(L):
    min=L[0]
    max=L[0]
    sum=0
    for l in L:
        if min>l:min=l
        if max<l:max=l
        sum+=l
    print("Minimum = ",min)
    print("Maksimum =",max)
    print("Average = ",sum/len(L))

list=[1,9,3,4]
listDetail(list)