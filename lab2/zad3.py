import math

def printFx(f,xStart=-1,xStop=1,lPrzedzial=10):
    '''wyswietla wartosci funkcji z podanego przedzialu oraz okreslonej liczby podprzedzialow w tym przedziale'''
    x=xStart
    dx=(xStop-xStart)/lPrzedzial
    while x<=xStop:
        print(str(x)+'\t\t'+str(f(x)))
        #print(float(x),'\t\t',f(x))
        x+=dx
        #x=round(x,3)

printFx(lambda x:math.sin(x),lPrzedzial=8)