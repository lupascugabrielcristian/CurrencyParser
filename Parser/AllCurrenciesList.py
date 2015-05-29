from Parser.AllCurrencyParser import AllCurrencyParser


class AllCurrencyList:
    def __init__(self):
        self.parser = AllCurrencyParser()

    def run(self):
        allCurrencies = self.parser.parse()

        for index in range(0, len(allCurrencies)):
            text  = str(index) + ". " + str(allCurrencies[index])
            print(text)

    def filter(self):
        currency = input("What currency to look for?")
        allCurrencies = self.parser.parse()
        results = 0

        for index in range(0, len(allCurrencies)):
            if currency in str(allCurrencies[index]):
                text  = str(index) + ". " + str(allCurrencies[index])
                print(text)
                results += 1

        if results == 0:
            print("No entry found!")

    def getIndexOfCurrency(self, currencyName):
        allCurrencies = self.parser.parse()

        for index in range(0, len(allCurrencies)):
            if currencyName in str(allCurrencies[index]):
                return index