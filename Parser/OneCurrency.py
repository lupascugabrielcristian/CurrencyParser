from Parser.InfoDesigner import InfoDesigner

class OneCurrency:

    def __init__(self):
        self.designer = InfoDesigner()

    def run(self):
        delay = int( input("Time between reads: "))
        indexOfCurrency = int( input("Currency index: ") )
        repeats = int( input("Repeats: ") )


        self.designer.currency_index = indexOfCurrency
        self.designer.repeats = repeats
        self.designer.interval = delay

        self.designer.run()

