from Parser.ValueParser import ValueParser


class Investment:

    def __init__(self, debugflag):
        self.parser = ValueParser(debugflag)
        self.name = "default name"
        self.onlineindex = 0
        self.investedMoney = 0
        self.units = 0.0
        self.initialPrice = 0.0
        self.endPrice = 0.0
        self.duration = 0
        self.open = False
        self.profit = 0.0


    def startTransaction(self):
        self.initialPrice = self.parser.getOnlineValueForCurrencyIndex(self.onlineindex)
        self.open = True


    def endTransaction(self):
        self.endPrice = self.parser.getOnlineValueForCurrencyIndex(self.onlineindex)
        self.open = False
        self.calculateProfit()

    def calculateProfit(self):
        delta = self.endPrice - self.initialPrice
        self.profit = delta * self.units * 1000
        print ("==========================") # log
        print ("||Profit: " + str(self.profit))
        print("||Initial price: " + str(self.initialPrice))
        print("||Final price: " + str(self.endPrice))
        print ("==========================") # log

