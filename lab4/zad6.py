import math

def ileSnu(dict):
    newDict={}
    for k in dict.keys():
        if dict[k]<=0:
            continue
        if k not in newDict:
            newDict[k]=0
        if dict[k]>200:
            newDict[k]='inf'
        else:
            newDict[k]=8/math.log10(dict[k])

    return newDict

def sleepTimeDictComp(dict):
    return {k:"inf" if dict[k]>200 else 8/math.log10(dict[k]) for k in dict.keys() if dict[k]>0}



osoby={"Maciek":357,"Jaś":20,"Michał":-345,"Olaf":34,"Stefan":2000,"Rysiek":45}

#print(ileSnu(osoby))
print(sleepTimeDictComp(osoby))