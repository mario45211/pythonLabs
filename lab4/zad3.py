import random

def blur(l,t):
    w1,w2,w3=t;
    newList = [l[0]]
    for i in range (1,len(l)-1):
        newList.insert(i,(l[i-1]*w1+l[i]*w2+l[i+1]*w3)/(w1+w2+w3))
    newList.insert(len(newList),l[len(l)-1])
    return newList

l=[random.randint(0,20) for i in range(20)]
print(l)
t=(random.randint(-2,3),random.randint(-2,3),random.randint(1,3))
print(t)

print(blur(l,t))
print(l)

l2=[3,1,2,0,4]
w=(1,1,1)
print(blur(l2,w))