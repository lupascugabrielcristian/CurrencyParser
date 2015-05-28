import signal
from pip.backwardcompat import raw_input
from Parser.ValueParser import ValueParser


class InvestmentMonitor:

    def __init__(self, debugflag, portofolio):
        self.portofolio = portofolio
        self.parser = ValueParser(debugflag)


    def monitor(self):
        print("Press any key to stop")
        self.input_or_timeout(5)


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

                print(investment + " Current value = " + str(currentValue) + ", " + status)

    def input_or_timeout(self, timeout):
        while True:
            def nothing():
                self.getCurrentValuesForInvestments()
            signal.signal(signal.SIGALRM, nothing)
            signal.alarm(timeout)
            try:
                userinput = raw_input()
                if userinput is not None:
                    break
                signal.alarm(0)
            except (IOError, EOFError): pass