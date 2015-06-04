import threading
import time

from Parser.AllCurrenciesList import AllCurrencyList
from Parser.Currency import Currency
from Parser.OneCurrency import OneCurrency
from Parser.ValueParser import ValueParser
from Trading.Analyzer import Analyzer
from Trading.DataReaderWriter import DataReaderWriter
from Trading.Investment import Investment
from Watchers.WatchThread import WatchThread
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
        self.investments.append(newInvestment)
        print("Investment added") #log

        newThread = threading.Thread(target=self.runTransation, args=(newInvestment,))
        self.watchersManager.addWatch(newInvestment, newThread)


    @staticmethod
    def __findIndexOfCurrency__(currencyName):
        return AllCurrencyList().getIndexOfCurrency(currencyName)

    def runTransation(self, newInvestment):
        self.startTransaction(newInvestment)
        time.sleep(newInvestment.duration)
        self.endTransaction(newInvestment)


    def startTransaction(self, investment):
        investment.startTransaction()
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

    def startWatch(self):
        for investment in self.portofolio.investments:
            self.startIfOpen(investment)

    def startIfOpen(self, investment):
        if investment.open:
            remainingduration = investment.getRemainingDuration()
            # thread = threading.Thread(target=self.closeInvestmentAfter, args=(investment, remainingduration, ))
            thread = threading.Thread(target=self.analize, args=(investment, ))
            self.watchersManager.addWatch(investment, thread)


    def closeInvestmentAfter(self, investment, duration):
        time.sleep(duration)
        self.endTransaction(investment)


    def analize(self, investment):
        print("Investment found open - watching...") # log
        Analyzer(self.debugflag, investment).analyze()
        self.endTransaction(investment)
        print("Transaction ended because analyser") # log