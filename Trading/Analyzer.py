from time import sleep
from Parser.ValueParser import ValueParser


class Analyzer:

    def __init__(self, debugflag, investment):
        self.debugflag = debugflag
        self.investment = investment
        self.parser = ValueParser(debugflag)

    def analyze(self):
        while 1:
            sleep(5)
            value = self.parser.getOnlineValueForCurrencyIndex(self.investment.onlineindex)
            print(self.investment.name + "Current value: " + str(value))

            delta = abs(self.investment.initialPrice - value)
            if delta > 0.005:
                print(str(delta)) # log
                return