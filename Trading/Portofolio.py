from Trading.Money import Money


class Portofolio:

    def __init__(self):
        # Asta vreau sa fie o lista cu toate valutele care le am
        self.currentBalance = []
        self.investments = []

    def addMoney(self, name, ammount):
        newMoney = Money(name, ammount)
        self.currentBalance.append(newMoney)


    def addCurrency(self, money):
        """ :param - money A Currency object """
        self.currentBalance.append(money)


    def addInvestment(self, investment):
        currencytoSell = self.__haveCurrency(investment.fromName)
        if currencytoSell >= investment.units:
            self.__buyCurrency(investment)
            self.investments.append(investment)
        else:
            print ("You don't have enough money")


    def sellInvestment(self, investment):
        currencytoSell = self.__haveCurrency(investment.toName)
        if currencytoSell >= investment.endPrice * investment.units:
            self.__addCurrency(investment.units, investment.fromName)
            self.__removeCurrency(currencytoSell, investment.toName)
            print("Vandut %d %s; Am cumparat %d %s" %(currencytoSell, investment.toName, investment.units, investment.fromName) )
        else : print("Don't have enough money")



    def __haveCurrency(self, currency):
        for i in range(0, len(self.currentBalance)):
            if currency in self.currentBalance[i].name:
                return self.currentBalance[i].sum
        return -1

    def __buyCurrency(self, investment):
        cost = investment.units * investment.initialPrice
        self.__removeCurrency(investment.units, investment.fromName)
        self.__addCurrency(cost, investment.toName)
        print("Vandut %d %s; Am cumparat %d %s" %(investment.units, investment.fromName, cost, investment.toName) )


    def __removeCurrency(self, quantity, name):
        for i in range(0, len(self.currentBalance)):
            if name == self.currentBalance[i].name:
                self.currentBalance[i].sum -= quantity


    def __addCurrency(self, quantity, name):
        for i in range(0, len(self.currentBalance)):
            if name == self.currentBalance[i].name:
                self.currentBalance[i].sum += quantity
                return
        newMoney = Money(name, quantity)
        self.currentBalance.append(newMoney)
