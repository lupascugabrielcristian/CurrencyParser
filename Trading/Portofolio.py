import time
from Trading.DataReaderWriter import DataReaderWriter
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
        self.investments.append(investment)

    def cleanup(self):
        for investment in self.investments:
            if investment.endTime < int(round(time.time())) and investment.open:
                investment.endTransaction()

        toRemove = []
        for investment in self.investments:
            if not investment.open:
                toRemove.append(investment)

        for investment in toRemove:
            self.investments.remove(investment)

        DataReaderWriter().savePorofolio(self)
