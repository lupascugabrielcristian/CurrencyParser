from Trading.Money import Money


class Portofolio:

    def __init__(self):
        # Asta vreau sa fie o lista cu toate valutele care le am
        self.currentBalance = []

    def add(self, name, ammount):
        newMoney = Money(name, ammount)
        self.currentBalance.append(newMoney)

    def addMoney(self, money):
        self.currentBalance.append(money)
