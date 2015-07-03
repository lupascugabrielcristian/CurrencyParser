class Predicter:

    def __init__(self, debugflag, initialPice, readingInterval):
        self.debugflag = debugflag
        self.valuesSoFar = []
        self.initialPrice = initialPice
        self.notDecisiveReadings = 0
        self.readingInterval = readingInterval


    def addData(self, newValue):
        if len(self.valuesSoFar) == 0:
            self.valuesSoFar.append(newValue)
            return self.readingInterval

        self.__bubble_sort()
        minValue = self.valuesSoFar[0]

        if newValue < minValue:
            self.valuesSoFar.append(newValue)
            self.notDecisiveReadings = 0
            print(" ** Min Value found: %.4f"%newValue)

            if newValue < self.initialPrice:
                print("  *** Lower than bying price. Suggest SELL. IP: %.4f"%self.initialPrice)
        elif newValue == minValue:
            print("  * Reached bottom: %.4f"%newValue)
        else:
            self.valuesSoFar.append(newValue)
            self.notDecisiveReadings += 1

        self.__calculateGoodReadinngsDensity()
        return self.readingInterval


    def __bubble_sort(self):
        numbers = self.valuesSoFar
        #swap_test = False
        for i in range(0, len(numbers) - 1):
            swap_test = False
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # swap
                swap_test = True
            if not swap_test:
                break

    def __calculateGoodReadinngsDensity(self):
        if self.notDecisiveReadings > 10:
            self.notDecisiveReadings = 0
            self.readingInterval += 10
            print(" ++ Reading interval increased to %d seconds"%self.readingInterval)


    def calculateAverage(self):
        sum  = 0
        for x in self.valuesSoFar:
            sum += x
        return sum / len(self.valuesSoFar)