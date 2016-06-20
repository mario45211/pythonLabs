def checkboard(n):
    return [[((i+j+1)%2) for i in range(0,n)] for j in range(0,n)]

print(checkboard(5))