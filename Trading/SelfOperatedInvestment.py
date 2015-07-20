from Trading.AbstractInvestment import AbstractInvestment


class SelfOperatedInvestment(AbstractInvestment):

    def __init__(self, debugflag):
        self.type = "auto"
        AbstractInvestment.__init__(self, debugflag)


    def setName(self, currencyName):
        self.name = currencyName
        separation = currencyName.index('/')
        self.fromName = currencyName[:separation]
        self.toName = currencyName[separation + 1:]
