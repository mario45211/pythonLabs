import time

def printCenter(tekst:str, width:int=80)->str:
    ileSpacji = (width-len(tekst))//2
    return ileSpacji*' '+tekst+ileSpacji*' '


def credits(szerl:int=80,*opis,**tworcy): #jak tu zrobic argument domyslny skoro jak tak jest to bierze pierwszy argument z parametru opis -
    # odp nie da się bo *opsi to lista i to 80 bedzie jako element listy, mozna o obejsc poprzez podanie dodatkowego leemtu do slownika ** tworcy
    # i sprawdzqc zcy ma jaką wartosc jesli nie ma to ustawimy mu jaką s odmylnsą wartosc a jesli ma to bierzemy podana wartosc
    for o in opis:
        for i in range(0,len(o)+1):
            print("\r"+printCenter(o[0:i],int(szerl)),end="")
            time.sleep(0.3)
        print("")

    for tw in sorted(tworcy.keys()):
        for i in range(0,len(tw)+1):
            print("\r"+printCenter(tw[0:i],szerl),end="")
            time.sleep(0.3)
        for j in range(0,len(tworcy[tw])+1):
            print("\r"+printCenter(tw+": "+tworcy[tw][0:j],szerl),end="")
            time.sleep(0.3)
        print("")


credits(80,"The Lord of the Ring"," ",
        "Podziekowania dla wszystkich ogladajacych",
        Scenariusz="John Mith",
        Scenografia="Mark Henn",
        Reżyseria="Olive Grown",
        System_Prezentacji_by="Python 3.5")

