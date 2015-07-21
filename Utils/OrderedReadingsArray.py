class OrderedReadingsArray:

    def __init__(self):
        self.currentIndex = 0
        self.readings = []
        self.unOrderedReadings = []
        self.ponderi = []
        self.total = 0
        self.lastAddedValue = -1
        self.timeForLastValue = 0
        self.lastDerivative = 0
        self.timeUnitReference = 1

    def add(self, value, timeInterval):
        self.unOrderedReadings.append(value)
        self.calculateDerivative(value, timeInterval)

        self.lastAddedValue = value
        self.timeForLastValue = timeInterval
        pondere = self.timeIntervalToPondere(timeInterval)

        if len(self.readings) == 0:
            self.readings.append(value)
            self.ponderi.append(pondere)
        if len(self.readings) == 1:
            self.timeUnitReference = timeInterval
            if value > self.readings[0]:
                # daca e mai mare o adaug normal la lista
                self.readings.append(value)
                self.ponderi.append(pondere)
            if value < self.readings[0]:
                # daca e mai mica o pun pe index 0
                self.readings.append(self.readings[0])
                self.ponderi.append(pondere)
                self.readings[0] = value
                self.ponderi[0] = pondere
        else:
            self.putInList(value, pondere)

    def timeIntervalToPondere(self, timeInterval):
        self.adjustWeights()
        weight = int(timeInterval / self.timeUnitReference)
        return weight

    def adjustWeights(self):
        return 0

    def putInList(self, value, timeInterval):
        self.total += value
        index = -1
        for i in range(0, len(self.readings)):
            if value > self.readings[i]:
                index = i + 1

        if index > -1:
            self.readings.insert(index, value)
            self.ponderi.insert(index, timeInterval)
        else:
            self.readings.insert(0, value)
            self.ponderi.insert(0, timeInterval)

    def getMinValue(self):
        return self.readings[0]

    def getMaxValue(self):
        return self.readings[len(self.readings) - 1]


    def getArithmeticMean(self):
        return self.total / len(self.readings)

    def getGeometricMean(self):
        prod = 1
        for i in range(0, len(self.readings)):
            prod *= self.readings[i]
        return pow(prod, 1/len(self.readings))

    def getMediePonderata(self):
        s1 = 0
        s2 = 0
        for i in range(0, len(self.readings)):
            s1 += self.readings[i] * self.ponderi[i]
            s2 += self.ponderi[i]
        return s1 / s2

    def calculateDerivative(self, f2, t2):
        s1 = f2 - self.lastAddedValue
        s2 = t2 - self.timeForLastValue
        result = s1/s2
        self.lastDerivative = result * 100
        # print("s1: %.4f / s2: %.4f = %.5f"%(s1, s2, result))

    def size(self):
        return len(self.readings)
