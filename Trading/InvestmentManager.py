import time

from Parser.AllCurrenciesList import AllCurrencyList
from Parser.Currency import Currency
from Parser.OneCurrency import OneCurrency
from Parser.ValueParser import ValueParser
from Trading.AnalyzeStarter import AnalyzeStarter
from Trading.DataReaderWriter import DataReaderWriter
from Trading.Investment import Investment
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


        self.startTransaction(newInvestment)
        self.startWatch(newInvestment)

        print("Investment added") #log



    def cleanup(self):
        for investment in self.portofolio.investments:
            if investment.endTime < int(round(time.time())) and investment.open:
                self.endTransaction(investment)

        toRemove = []
        for investment in self.portofolio.investments:
            if not investment.open:
                toRemove.append(investment)

        for investment in toRemove:
            self.portofolio.investments.remove(investment)
            print("Investment sold") #log

        DataReaderWriter().savePorofolio(self.portofolio)

        for investment in self.portofolio.investments:
            self.startWatch(investment)


    # def startWatch(self):
    #     self.watchersManager.empty()
    #     for investment in self.portofolio.investments:
    #         self.startIfOpen(investment)


    @staticmethod
    def __findIndexOfCurrency__(currencyName):
        return AllCurrencyList().getIndexOfCurrency(currencyName)

    # def runTransation(self, newInvestment):
    #     self.startTransaction(newInvestment)
    #     time.sleep(newInvestment.duration)
    #     self.endTransaction(newInvestment)


    def startTransaction(self, investment):
        investment.startTransaction()
        self.investments.append(investment)
        self.portofolio.addInvestment(investment)
        DataReaderWriter().savePorofolio(self.portofolio)

    def endTransaction(self, investment):
        investment.endTransaction()
        self.portofolio.addCurrency(Currency(investment.name, investment.profit))
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


    def startWatch(self, investment):
        self.watchersManager.addWatch(investment)