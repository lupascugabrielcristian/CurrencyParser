from Parser.AllCurrencyParser import AllCurrencyParser


class AllCurrencyList:
    def __init__(self):
        self.parser = AllCurrencyParser()

    def run(self):
        allCurrencies = self.parser.parse()

        for index in range(0, len(allCurrencies)):
            print(str(index) + ". " + str(allCurrencies[index]))

    def filter(self):
        currency = input("What currency to look for?")
        allCurrencies = self.parser.parse()
        results = 0

        for index in range(0, len(allCurrencies)):
            if currency in str(allCurrencies[index]):
                print(str(index) + ". " + str(allCurrencies[index]))
                results += 1

        if results == 0:
            print("No entry found!")