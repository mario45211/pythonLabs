import time

def printCenter(tekst:str, width:int=80):
    ileSpacji = (width-len(tekst))//2
    print(ileSpacji*' '+tekst+ileSpacji*' ')


def credits(*opis,**tworcy):
    for o in opis:
        printCenter(o)
        time.sleep(1)

    for tw in sorted(tworcy.keys()): #sorted sortuje po nazwie parametru, nie jego wartosci
        printCenter(tw+": "+tworcy[tw])
        time.sleep(1)


credits("The Lurd of the Rung"," ",
        "Podziekowania dla wszystkich ogladajacych",
        Scenariusz="John Mith",
        Scenografia="Mark Henn",
        Reżyseria="Olive Grown",
        System_Prezentacji="Python 3.5")