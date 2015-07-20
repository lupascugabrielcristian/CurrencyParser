import time

from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency
from Parser.ValueParser import ValueParser
from Trading.DataReaderWriter import DataReaderWriter
from Trading.Investment import Investment
from Trading.SelfOperatedInvestment import SelfOperatedInvestment
from Watchers.WatchersManager import WatchersManager


class InvestmentManger:
    DELAY_BETWEEN_READS = 10

    def __init__(self, debugflag, portofolio):
        self.investments = []
        self.portofolio = portofolio
        self.debugflag = debugflag
        self.endTransactionPending = []
        self.parser = ValueParser(debugflag)
        self.watchersManager = WatchersManager(debugflag)

    def makeInvestment(self, type):
        if "normal" in type:
            self.__makeNormalInvestment()

        if "auto" in type:
            self.__makeSelfOperatedInvestment()


    def __makeNormalInvestment(self):
        currencyName = input("Buy currency: ")
        ammount = int(input("Ammount: "))

        newInvestment = Investment(self.debugflag)
        newInvestment.setName(currencyName)
        index = self.__findIndexOfCurrency__(currencyName)

        if index is None or index < 0:
            print("Currency was not found")
            return

        newInvestment.onlineindex = index
        newInvestment.units = ammount

        self.startTransaction(newInvestment)
        self.startWatch(newInvestment)

        print("Investment added") #log


    def __makeSelfOperatedInvestment(self):
        currencyName = input("Currency: ")
        ammount = int(input("Ammount: "))

        newInvestment = SelfOperatedInvestment(self.debugflag)
        newInvestment.setName(currencyName)
        index = self.__findIndexOfCurrency__(currencyName)

        if index is None or index < 0:
            print("Currency was not found")
            return

        newInvestment.onlineindex = index
        newInvestment.units = ammount

        self.startWatch(newInvestment)

        return 0

    def cleanup(self):

        toRemove = []
        for investment in self.portofolio.investments:
            if not investment.open:
                toRemove.append(investment)

        for investment in toRemove:
            self.portofolio.sellInvestment(investment)

        DataReaderWriter().savePorofolio(self.portofolio)

        for investment in self.portofolio.investments:
            self.startWatch(investment)


    @staticmethod
    def __findIndexOfCurrency__(currencyName):
        return AllCurrencyList().getIndexOfCurrency(currencyName)

    def startTransaction(self, investment):
        investment.startTransaction()
        self.investments.append(investment)
        self.portofolio.addInvestment(investment)
        DataReaderWriter().savePorofolio(self.portofolio)

    def endTransaction(self, investment):
        investment.endTransaction()
        self.portofolio.sellInvestment(investment)
        DataReaderWriter().savePorofolio(self.portofolio)

    def __getOnlineData__(self, duration, currencyName):
        currencyIndex = self.__findIndexOfCurrency__(currencyName)
        repeats = int(duration / self.DELAY_BETWEEN_READS)
        OneCurrency(self.debugflag).runwiththisparameters(self.DELAY_BETWEEN_READS, currencyIndex, repeats)

    def startIfOpen(self, investment):
        if investment.open:
            self.watchersManager.addWatch(investment)


    def closeInvestmentAfter(self, investment, duration):
        time.sleep(duration)
        self.endTransaction(investment)

    def closeInvestment(self, investment):
        self.endTransaction(investment)

    def startWatch(self, investment):
        self.watchersManager.addWatch(investment)