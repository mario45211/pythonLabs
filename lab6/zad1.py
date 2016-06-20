class Coin:
    def __init__(self, value):
        if (value in [1, 2, 5, 10, 20, 50, 100, 200, 500]):
            self.value = value
        else:
            self.value = 0

    def getValue(self):
        return self.value

myCoin = Coin(2);
#print("Moneta o nominale =", myCoin.getValue()/100,"zł");