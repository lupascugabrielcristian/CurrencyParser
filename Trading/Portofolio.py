from math import ceil
from Trading.Money import Money


class Portofolio:

    def __init__(self):
        # Asta vreau sa fie o lista cu toate valutele care le am
        self.currentBalance = []
        self.investments = []
        self.debt =[]

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
            print ("You don't have enough %s units" %investment.fromName)



    def sellInvestment(self, investment):
        currencytoSell = self.__haveCurrency(investment.toName)
        toPay = investment.endPrice * investment.units
        if currencytoSell >= toPay:
            self.__addCurrency(investment.units, investment.fromName)
            self.__removeCurrency(toPay, investment.toName)
            print("Vandut %d %s; Am cumparat %d %s" %(toPay, investment.toName, investment.units, investment.fromName) )
            self.__removeInvestmentWithId(investment.id)
            return True
        else :
            print("You need %d/You have %d of %s" %(toPay, currencytoSell, investment.toName))
            if self.askUser():
                print("Don't have enough money. Addind debt")
                newMoney = Money(investment.toName, toPay - currencytoSell)
                self.debt.append(newMoney)
                self.__setMoneyToThisValue(investment.toName, 0)
                self.__removeInvestmentWithId(investment.id)
                return False



    def __haveCurrency(self, currency):
        for i in range(0, len(self.currentBalance)):
            if currency in self.currentBalance[i].name:
                return self.currentBalance[i].sum
        return -1

    def __buyCurrency(self, investment):
        cost = ceil(investment.units * investment.initialPrice * 10) / 10
        self.__removeCurrency(investment.units, investment.fromName)
        self.__addCurrency(cost, investment.toName)
        print("Vandut %d %s; Am cumparat %d %s" %(investment.units, investment.fromName, cost, investment.toName) )


    def __removeInvestmentWithId(self, id):
        toRemove = []

        for i in range(0, len(self.investments)):
            if self.investments[i].id == id:
                toRemove.append(self.investments[i])

        self.investments.remove(toRemove[0])


    def __removeCurrency(self, quantity, name):
        for i in range(0, len(self.currentBalance)):
            if name in self.currentBalance[i].name:
                self.currentBalance[i].sum -= quantity


    def __addCurrency(self, quantity, name):
        for i in range(0, len(self.currentBalance)):
            if name in self.currentBalance[i].name:
                self.currentBalance[i].sum += quantity
                return
        newMoney = Money(name, quantity)
        self.currentBalance.append(newMoney)

    def __setMoneyToThisValue(self, name, value):
        for i in range(0, len(self.currentBalance)):
            if name in self.currentBalance[i].name:
                self.currentBalance[i].sum = value
                return True
        return False

    @staticmethod
    def askUser():
        answer = int(input("Force sell(Yes = 1, No = 0): "))
        if answer == 1:
            return True
        else:
            return False
