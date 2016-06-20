def name(dict):
    for i in sorted(dict):
        print(i)

def nameWithMarks(dict):
    for name,mark in dict.items():
        print(name,mark)

dict={'Marek':3,"Adam":4,"Jan":2.0,"Staś":5}

name(dict)
nameWithMarks(dict)
