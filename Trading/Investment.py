import random
import time
from Parser.ValueParser import ValueParser


class Investment:

    def __init__(self, debugflag):
        self.parser = ValueParser(debugflag)
        self.name = "default name"
        self.onlineindex = 0
        self.investedMoney = 0
        self.units = 0.0
        self.initialPrice = 0.0
        self.startTime = 0 # in seconds from start of eopch
        self.endPrice = 0.0
        self.endTime = 0  # in seconds from start of eopch
        self.duration = 0
        self.open = False
        self.profit = 0.0
        self.id = random.randint(0, 10000)


    def startTransaction(self):
        self.initialPrice = self.parser.getOnlineValueForCurrencyIndex(self.onlineindex)
        self.startTime = int(round(time.time()))
        self.endTime = self.startTime + self.duration
        self.open = True


    def endTransaction(self):
        self.endPrice = self.parser.getOnlineValueForCurrencyIndex(self.onlineindex)
        self.open = False
        self.calculateProfit()

    def calculateProfit(self):
        delta = self.endPrice - self.initialPrice
        profit = delta * self.units * 1000
        self.profit = round(profit, 2)
        print("\n==========================") # log
        print("||Profit: " + str(self.profit))
        print("||Initial price: " + str(self.initialPrice))
        print("||Final price: " + str(self.endPrice))
        print("==========================") # log

    def getRemainingDuration(self):
        return self.endTime - int(round(time.time()))

    def __repr__(self):
        if self.open:
            open = "OPEN"
        else: open = "CLOSE"

        if self.endPrice != 0:
            endValue = "End Price: " + str(self.endPrice)
        else: endValue = ""

        if int(round(time.time())) > self.endTime:
            overtime = "EXCEEDED"
        else: overtime = "PENDING"

        reprs = "{} {} Initial price: {}, {}; time: {}".format(self.name, open, self.initialPrice, endValue, overtime)
        return reprs

    def __str__(self):
        if self.open:
            open = "OPEN"
        else: open = "CLOSE"

        if self.endPrice != 0:
            endValue = "End Price: " + str(self.endPrice)
        else: endValue = ""

        if int(round(time.time())) > self.endTime:
            overtime = "EXCEEDED"
        else: overtime = "PENDING"

        text = "{} {} Initial price: {}, {}; time: {}".format(self.name, open, self.initialPrice, endValue, overtime)
        return text