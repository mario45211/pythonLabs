def samogloski(str):
    samogloski="aeiouy"
    ilosc=0
    for i in range(0,len(str)):
        if str[i] in samogloski:
            ilosc+=1
    return ilosc

def listaSamogloski(L):
    return [i for i in L[:] if samogloski(i)%2==0]

print(listaSamogloski(["Robot","Matjasy","Metal","Python","Metal Gear","Jaś"]))