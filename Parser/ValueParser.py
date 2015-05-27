from Parser.Method_2_Parser import Method_2_Parser


class ValueParser:

    def __init__(self, debugflag):
        self.debugflag = debugflag

    def getOnlineValueForCurrencyIndex(self, currencyIndex):
        allCurrencies = Method_2_Parser(self.debugflag).parse()
        currentCurrency = allCurrencies[currencyIndex]
        return currentCurrency.value