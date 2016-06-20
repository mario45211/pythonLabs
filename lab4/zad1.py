import math

def sincos(x):
    return (math.sin(x),math.cos(x))

def zad1():
    for i in range(0,99,9):
        x,y=sincos(i*math.pi/180)
        print("Kąt: ",i,end="; ")
        print("sin:",x,end="; ")
        print("cos:",y)


zad1()
