class Coin:
    def __init__(self, value):
        if (value in [1, 2, 5, 10, 20, 50, 100, 200, 500]):
            self.value = value
        else:
            self.value = 0

    def getValue(self):
        return self.value



#zad2
class MoneyBox:
    def __init__(self):
        self.moneyBox = []

    def addCoin(self,coin):
        self.moneyBox.append(coin);

    def getTotalValue(self):
        sum=0
        for i in self.moneyBox[:]: #for i in self.moneyBox
            sum+=i
        return sum


myMoneyBox = MoneyBox()

for i in range(5):
    myMoneyBox.addCoin(Coin(20).getValue())
    myMoneyBox.addCoin(Coin(1).getValue())

#print("Zawartość skarbonki = ",myMoneyBox.getTotalValue(),"groszy (",myMoneyBox.getTotalValue()/100," zł)")v