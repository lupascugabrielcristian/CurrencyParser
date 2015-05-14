import time
from Parser.Method_2_Parser import Method_2_Parser


class VariationFinder:

    def __init__(self):
        self.parser = Method_2_Parser()

    def findMaxVariation(self):
        repeats = int(input("Number of repeats: "))
        delay = int(input("Delay between repeats(seconds): "))

        listOfReadings = []
        for index in range(0, repeats):
            listOfReadings.append(self.parser.findInPage())
            time.sleep(delay)

        indexFound = self.processReadings(listOfReadings)

        for index in range(0, repeats):
            print(str(listOfReadings[index][indexFound]))
        print("Index is: " + str(indexFound))

    def processReadings(self, listOfReadings):
        variation = 0
        indexFoundCurrency = -1
        numberOfCurrencies = len(listOfReadings[0])

        for i in range(0, numberOfCurrencies):
            currencyValues = self.getCurrencyValueAllReadings(listOfReadings, i)
            thisCurrencyVariation = self.calculateVariationForCurrency(currencyValues)
            if thisCurrencyVariation > variation:
                variation = thisCurrencyVariation
                indexFoundCurrency = i

        return indexFoundCurrency



    def getCurrencyValueAllReadings(self, listOfReadings, indexOfCurrency):
        currencyValues = []
        numberOfReadings = len(listOfReadings)

        for i in range(0, numberOfReadings):
            currencyValues.append(listOfReadings[i][indexOfCurrency].value)

        return currencyValues

    def calculateVariationForCurrency(self, currencyValues):
        variation = 0

        for i in range(0, len(currencyValues) - 1):
            thisVariation = currencyValues[i + 1] - currencyValues[i]
            if thisVariation > variation:
                variation = thisVariation

        return variation