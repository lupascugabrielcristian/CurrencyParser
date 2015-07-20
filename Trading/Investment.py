import random
import time
from Parser.ValueParser import ValueParser


class Investment:

    def __init__(self, debugflag):
        self.parser = ValueParser(debugflag)
        self.name = "default name"
        self.fromName = "from"
        self.toName = "to"
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
        self.type = "manual"


    def setName(self, currencyName):
        self.name = currencyName
        separation = currencyName.index('/')
        self.fromName = currencyName[:separation]
        self.toName = currencyName[separation + 1:]

    def startTransaction(self):
        self.initialPrice = self.parser.getOnlineValueForCurrencyIndex(self.onlineindex)
        self.startTime = int(round(time.time()))
        self.endTime = self.startTime + self.duration
        self.open = True


    def endTransaction(self):
        self.endPrice = self.parser.getOnlineValueForCurrencyIndex(self.onlineindex)
        self.open = False

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