from Parser.InfoDesigner import InfoDesigner

class OneCurrency:

    def __init__(self, debugflag):
        self.debugflag = debugflag
        self.designer = InfoDesigner(debugflag)

    def run(self):
        delay = int( input("Time between reads: "))
        indexOfCurrency = int( input("Currency index: ") )
        repeats = int( input("Repeats: ") )


        self.designer.currency_index = indexOfCurrency
        self.designer.repeats = repeats
        self.designer.interval = delay

        self.designer.run()


    def runwiththisparameters(self, delay, currencyIndex, repeats):
        self.designer.currency_index = currencyIndex
        self.designer.repeats = repeats
        self.designer.interval = delay

        self.designer.run()

