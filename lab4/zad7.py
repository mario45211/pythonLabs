import random

def generujMape()->[[]]:
    mapa=[[False for i in range(0,10)] for j in range(0,10)]
    #mapa=[[]]
    #for i in range(0,10):
   #     mapa[i].append(False)
   #     for j in range(0,10):
  #          mapa[i].insert(j,0) #sprawdz mapa[i[j]]
    for i in range(0,20):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while(mapa[x][y]==True):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        mapa[x][y]=True
    return mapa

def wyswietlMape(mapa):
    l=1
    for j in range(1, 11):
        print("   ",j, end="  ")
    print("")
    for i in mapa:
        print(l,end=") ")
        print(i)
        l+=1

def startGry():
    mapa=generujMape()
    historia=set()
    l=0
    while l<20:
        wyswietlMape(mapa)
        x=int(input("Podaj współrzędną x[1-10]: "));
        y=int(input("Podaj współrzędną y[1-10]: "));
        while (x,y) in historia:
            print("Tutaj już strzelano!")
            x = int(input("Podaj współrzędną x[1-10]: "));
            y = int(input("Podaj współrzędną y[1-10]: "));
        historia.add((x,y))

        if mapa[y-1][x-1]==True:
            print("Trafiono!")
            l += 1
            mapa[y-1][x-1]="XXX"
        else:
            print("Pudło!")
        #print(historia)
    print("Koniec gry!")
#wyswietlMape(generujMape())
startGry()