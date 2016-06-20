class MoneyPocket:
    def __init__(self, denomination):
        self.denomination = denomination #lista przechowujaca dozwolone nominaly monet
        self._money = [] #lista monet przechowywanych w obiekcie

    def addCoin(self, coin):
        if coin in self.denomination:
            self._money.append(coin)
        else:
            print("Nie można przechować monety o podanym nominale")
            print("Przechowywacz moze przechować monety o nominale: ",end="")
            for i in self.denomination:
                print(i,end=",")
            print("")

    def _getTotalValue(self):
        sum = 0;
        for i in self._money:
            sum += i;
        return sum

    def _getCoin(self,denomination):
        if denomination not in self.denomination:
            print("Nie ma monet o podanym nominale")
            return None
        else:
            for i in self._money:
                if i==denomination:
                    coin = i
                    self._money.remove(i)
                    return coin


class TicketMachine(MoneyPocket):
    def __init__(self,denomination):
        super().__init__(denomination)
        self.pushedMoney = []

    def getPushedMoney(self):
        sum=0
        for i in self.pushedMoney:
            sum+=i
        return sum

    def pushCoin(self, coin):
        self.addCoin(coin)
        if coin in self.denomination:
            self.pushedMoney.append(coin)

    def _giveChange(self, amount):
        #w oparciu o algorytm zachłanny
        change=[]
        if amount<=0:
            return change

        for i in sorted(self._money, reverse=True):
            if amount<=0:
                break;
            if i<=amount:
                change.append(i)
                amount-=i

        if amount>0:
            return None
        else:
            for i in change:
                self._money.remove(i)
            return change

    def cancel(self):
        money = self._giveChange(self.getPushedMoney())
        self.pushedMoney=[]
        return money

    def buyTicket(self, price):
        if(price>self.getPushedMoney()):
            print("Cena biletu: ",price)
            print("Wrzucona kwota: ",self.getPushedMoney())
        else:
            change = self._giveChange(self.getPushedMoney()-price)
            if change is None:
                print("Tylko odliczona kwota")
                return self.cancel()
            else:
                self.pushedMoney=[]
                return change



ticketMachine=TicketMachine([1,2,5,10,20,50,100,200,500])

ticketMachine.pushCoin(500)
print(ticketMachine.buyTicket(230))
print("a",ticketMachine.cancel()) #wydal monete przy kupnie biletu, poniewaz nie bylo odliczonej kwoty a automat nie ma jak wydac reszty

ticketMachine.addCoin(1)
ticketMachine.addCoin(2)
ticketMachine.addCoin(5)
ticketMachine.addCoin(10)
ticketMachine.addCoin(20)
ticketMachine.addCoin(50)
ticketMachine.addCoin(100)
ticketMachine.addCoin(200)
ticketMachine.addCoin(500)

ticketMachine.pushCoin(500)
print(ticketMachine.buyTicket(230))

ticketMachine.pushCoin(200)
ticketMachine.pushCoin(100)
print(ticketMachine.buyTicket(300))

ticketMachine.pushCoin(100)
print(ticketMachine.buyTicket(200))
ticketMachine.pushCoin(100)
print("Anulowano:",ticketMachine.cancel())

ticketMachine.pushCoin(100)
ticketMachine.pushCoin(20)
ticketMachine.pushCoin(30)
ticketMachine.pushCoin(50)
ticketMachine.pushCoin(20)
ticketMachine.pushCoin(20)
print(ticketMachine.buyTicket(200))
ticketMachine.pushCoin(100)
print(ticketMachine.buyTicket(99))
ticketMachine.pushCoin(100)
print(ticketMachine.buyTicket(99))
ticketMachine.pushCoin(50)
ticketMachine.pushCoin(20)
ticketMachine.pushCoin(20)
print(ticketMachine.cancel())

print(ticketMachine._money)