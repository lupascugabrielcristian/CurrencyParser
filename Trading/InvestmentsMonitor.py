import threading
from time import sleep

from Parser.ValueParser import ValueParser
from Trading.MonitorStarter import MonitorStarter


class InvestmentMonitor:

    def __init__(self, debugflag, portofolio):
        self.portofolio = portofolio
        self.debugflag = debugflag
        self.parser = ValueParser(debugflag)
        self.previousValues = []
        self.repeats = 0

    def monitor(self):
        if len(self.portofolio.investments) == 0:
            print("No investments to monitor")
            return

        print("Monitoring")

        for index in range(len(self.portofolio.investments)):
            MonitorStarter(self.debugflag,  self.portofolio.investments[index]).analyze()

        print("Monitoring is stoped")


    def getCurrentValuesForInvestments(self):

        for index in range(len(self.portofolio.investments)):
            investment = self.portofolio.investments[index]
            if investment.open:
                currentValue = self.parser.getOnlineValueForCurrencyIndex(investment.onlineindex)

                previousValue = self.previousValues[index]
                self.previousValues[index] = currentValue

                if previousValue > 0:
                    if currentValue > previousValue:
                        mediumStatus = "RISING"
                    elif currentValue < previousValue:
                        mediumStatus = "LOWERING"
                    else: mediumStatus = "STEADY"
                else: mediumStatus = "--"

                if currentValue > investment.initialPrice:
                    status = "UP"
                elif currentValue < investment.initialPrice:
                    status = "DOWN"
                else: status = "SAME"

                print(investment)
                print("Current value = {}, {}, {}".format(currentValue, status, mediumStatus))



    def initializePreviousVectorValues(self):
        for index in range(len(self.portofolio.investments)):
            self.previousValues.append(0)