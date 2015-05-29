import threading
from time import sleep

from Parser.ValueParser import ValueParser


class InvestmentMonitor:

    def __init__(self, debugflag, portofolio):
        self.portofolio = portofolio
        self.parser = ValueParser(debugflag)

    def monitor(self):
        print("Monitoring")
        while True:
            end = input("stop to end monitoring: ")
            if "stop" in end:
                break
            myThread = threading.Thread(target=self.getCurrentValuesForInvestments(), args=())
            myThread.start()
            sleep(10)
        print("Monitoring is stoped")


    def getCurrentValuesForInvestments(self):
        for investment in self.portofolio.investments:
            if investment.open:
                index = investment.onlineindex
                currentValue = self.parser.getOnlineValueForCurrencyIndex(index)

                if currentValue > investment.initialPrice:
                    status = "UP"
                elif currentValue < investment.initialPrice:
                    status = "DOWN"
                else: status = "SAME"

                print(investment)
                print("Current value = " + str(currentValue) + ", " + status)

