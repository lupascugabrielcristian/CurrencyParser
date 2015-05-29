import threading
import time

from Parser.AllCurrenciesList import AllCurrencyList
from Parser.Currency import Currency
from Parser.OneCurrency import OneCurrency
from Parser.ValueParser import ValueParser
from Trading.DataReaderWriter import DataReaderWriter
from Trading.Investment import Investment


class InvestmentManger:
    DELAY_BETWEEN_READS = 10

    def __init__(self, debugflag, portofolio):
        self.investments = []
        self.portofolio = portofolio
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
        print("Investment added") #log

        myThread = threading.Thread(target=self.runTransation, args=(newInvestment,))
        myThread.start()


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
        self.investments.remove(investment)
        self.portofolio.addCurrency(Currency(investment.name, investment.profit))
        DataReaderWriter().savePorofolio(self.portofolio)



    def __getOnlineData__(self, duration, currencyName):
        currencyIndex = self.__findIndexOfCurrency__(currencyName)
        repeats = int(duration / self.DELAY_BETWEEN_READS)
        OneCurrency(self.debugflag).runwiththisparameters(self.DELAY_BETWEEN_READS, currencyIndex, repeats)
