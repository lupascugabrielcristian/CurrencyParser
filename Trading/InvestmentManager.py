import sched
import time
from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency
from Parser.ValueParser import ValueParser
from Trading.Investment import Investment


class InvestmentManger:
    DELAY_BETWEEN_READS = 10

    def __init__(self, debugflag):
        self.investments = []
        self.debugflag = debugflag
        self.parser = ValueParser(debugflag)
        self.endTransactionPending = []

    def makeInvestment(self):
        currencyName = input("Buy currency: ")
        ammount = int(input("Ammount: "))
        duration = int(input("(Optional)Seconds: "))

        newInvestment = Investment(self.debugflag)
        newInvestment.name = currencyName
        index = self.__findIndexOfCurrency__(currencyName)

        if index is None or index < 0:
            print("Currency was not found")
            return

        newInvestment.onlineindex = index
        newInvestment.units = ammount
        newInvestment.duration = duration
        self.investments.append(newInvestment)

        indexOfNewInvestment = len(self.investments) - 1
        schedueledTask = sched.scheduler(time.time, time.sleep)
        self.startTransaction(indexOfNewInvestment)
        schedueledTask.enter(duration, 1, self.endTransaction, (indexOfNewInvestment,))
        schedueledTask.run()


    def __getOnlineData__(self, duration, currencyName):
        currencyIndex = self.__findIndexOfCurrency__(currencyName)
        repeats = int(duration / self.DELAY_BETWEEN_READS)
        OneCurrency(self.debugflag).runwiththisparameters(self.DELAY_BETWEEN_READS, currencyIndex, repeats)


    def __findIndexOfCurrency__(self, currencyName):
        return AllCurrencyList().getIndexOfCurrency(currencyName)

    def startTransaction(self, investmentIndex):
        self.investments[investmentIndex].startTransaction()

    def endTransaction(self, investmentIndex):
        self.investments[investmentIndex].endTransaction()
