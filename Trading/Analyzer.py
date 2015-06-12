from time import sleep
from Parser.ValueParser import ValueParser

class Analyzer:

    def __init__(self, debugflag, investment, viewer):
        self.debugflag = debugflag
        self.investment = investment
        self.parser = ValueParser(debugflag)
        self.viewer = viewer

    def analyze(self):
        while 1:
            sleep(5)
            value = self.parser.getOnlineValueForCurrencyIndex(self.investment.onlineindex)
            # print('\n' + self.investment.name + "Current value: " + str(value))
            self.viewer.showText('\n' + self.investment.name + "Current value: " + str(value))

            delta = abs(self.investment.initialPrice - value)
            if delta > 0.005:
                # print(str(delta)) # log
                self.viewer.showText(str(delta))
                return
