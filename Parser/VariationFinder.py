import time
from Parser.Method_2_Parser import Method_2_Parser


class VariationFinder:

    def __init__(self, debugFlag):
        self.parser = Method_2_Parser(debugFlag)
        self.debugflag = debugFlag

    def findMaxVariation(self):
        repeats = int(input("Number of repeats: "))
        delay = int(input("Delay between repeats(seconds): "))

        listOfReadings = []
        for index in range(0, repeats):
            listOfReadings.append(self.parser.findInPage())
            print("Reading no " + str(index))
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

            if self.debugflag:
                print(str(listOfReadings[0][i].name) + ": " + str(currencyValues))

            thisCurrencyVariation = self.calculateVariationForCurrency(currencyValues)

            if self.debugflag:
                print("Variation: " + str(thisCurrencyVariation))

            if thisCurrencyVariation > variation:
                variation = thisCurrencyVariation
                indexFoundCurrency = i

        return indexFoundCurrency



    def getCurrencyValueAllReadings(self, listOfReadings, indexOfCurrency):
        currencyValues = []
        numberOfReadings = len(listOfReadings)

        for i in range(0, numberOfReadings):
            value = listOfReadings[i][indexOfCurrency].value
            currencyValues.append(value)

        return currencyValues

    def calculateVariationForCurrency(self, currencyValues):
        variation = 0

        for i in range(0, len(currencyValues) - 1):
            thisVariation = abs(currencyValues[i + 1] - currencyValues[i])

            if self.debugflag:
                print("Local variation: " + str(thisVariation))

            if thisVariation > variation:
                variation = thisVariation

        return variation