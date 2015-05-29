import threading
from time import sleep

from Parser.ValueParser import ValueParser


class InvestmentMonitor:

    def __init__(self, debugflag, portofolio):
        self.portofolio = portofolio
        self.parser = ValueParser(debugflag)
        self.previousValues = []
        self.repeats = 0

    def monitor(self):
        print("Monitoring")
        self.initializePreviousVectorValues()

        while True:
            if self.repeats == 0:
                end = input("stop or number of repeats: ")
                if "stop" in end:
                    break
                if end.isnumeric():
                    self.repeats = int(end)

            myThread = threading.Thread(target=self.getCurrentValuesForInvestments(), args=())
            myThread.start()
            sleep(10)
            self.repeats -= 1
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