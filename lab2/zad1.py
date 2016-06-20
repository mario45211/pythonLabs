def czyPierwsza(n) -> bool:
    '''zwraca komunikat i prawdę, czy liczba jest pierwsza'''
    for i in range(2, n):
        if n % i == 0:
            # print("Liczba nie jest pierwsza!")
            return 0
    else:
        # print("Liczba jest pierwsza.")
        return 1


# czyPierwsza(12)


def fMersennea(p) -> float:
    '''zwraca wartość funkcji Mersenne'a dla argumentu p'''
    return 2 ** p - 1


# print(fMersennea(1/2))

for i in range(1, 31):
    print("Wartosc funkcji Mersenna dla i= " + str(i) + " wynosi " + str(fMersennea(i)), end=" i")
    if czyPierwsza(fMersennea(i)):
        print(" jest liczbą pierwszą")
    else:
        print(" nie jest liczbą pierwszą")

# exit()
