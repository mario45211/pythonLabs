import random

def blur(L):
    list=[L[0]]
    for i in range(1,len(L)-1):
        list.append(round((L[i-1]+L[i]+L[i+1])/3,2))
    list.append(L[len(L)-1])
    return list

lista = []
for i in range (1,21):
    lista.append(random.randint(1,20))

print("lista = ",lista)
print("lista rozmyta", blur(lista))
print("Jeszcze raz lista = ",lista)
print(blur([3,1,2,0,4]))