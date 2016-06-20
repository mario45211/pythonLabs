

class MoneyPocket:
    def __init__(self, denomination):
        self.denomination = denomination
        self.money = []

    def addCoin(self, coin):
        if coin in self.denomination:
            self.money.append(coin)
        else:
            print("Nie można przechować monety o podanym nominale")
            print("Przechowywacz moze przechować moenty o nominale: ",end="")
            for i in self.denomination:
                print(i,end=",")
            print("")

    def getTotalValue(self):
        sum = 0;
        for i in self.money:
            sum += i;
        return sum

    def getCoin(self,denomination):
        if denomination not in self.denomination:
            print("Nie ma monet o podanym nominale")
            return None
        else:
            for i in self.money:
                if i==denomination:
                    coin = i
                    self.money.remove(i)
                    return coin


class MoneyBox(MoneyPocket):
    def getCoin(self,a):
        print("Nie można wyciągnąć pojedyńczej monety")


myPocket=MoneyPocket([1,2,100])

myPocket.addCoin(1)
myPocket.addCoin(20)
myPocket.addCoin(100)

print("łączna wartość przechowywacza = ",myPocket.getTotalValue(),"groszy (",myPocket.getTotalValue()/100," zł)")

print("Pobralem monetę = ",myPocket.getCoin(1))
print("Pobralem monetę = ",myPocket.getCoin(20))

print("łączna wartość przechowywacza po pobraniu monet = ",myPocket.getTotalValue(),"groszy (",myPocket.getTotalValue()/100," zł)")

myMoneyBox=MoneyBox([1,2,100,500])

for i in range(5):
    myMoneyBox.addCoin(2)

myMoneyBox.addCoin(50)

print("łączna wartość skarbonki = ",myMoneyBox.getTotalValue(),"groszy (",myMoneyBox.getTotalValue()/100," zł)")

print(myMoneyBox.getCoin(2))