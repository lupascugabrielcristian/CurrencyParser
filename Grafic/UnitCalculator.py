class UnitCalculator:

    PRECISION = 100

    def __init__(self, dimensions, listOfPoints):
        self.dimensions = dimensions
        self.listOfPoints = listOfPoints

    def calculateYUnitSize(self):
        dimensions = self.dimensions

        minYValue = self.findMinim(self.listOfPoints)
        maxValue = self.findMaxim(self.listOfPoints)
        gHeight = dimensions.yCanvasSize - 2 * dimensions.graphPadding

        dimensions.minYValue = minYValue
        dimensions.yGraphSize = gHeight


        # Numar unitati
        if len(self.listOfPoints) > 1:
            N = maxValue - minYValue

            if N == 0:
                N = 1

            while N < self.PRECISION:
                dimensions.yFactor +=1
                N *= 10
        else: N = 3
        dimensions.verticalUnits = N

        # Marime unitate
        dimensions.yUnitValue =float(gHeight / N)

        return dimensions

    @staticmethod
    def findMinim(listOfPoints):
        yValues = []
        for i in range(len(listOfPoints)):
            yValues.append(listOfPoints[i].getY())
        return min(yValues)

    @staticmethod
    def findMaxim(listOfPoints):
        yValues = []
        for i in range(len(listOfPoints)):
            yValues.append(listOfPoints[i].getY())
        return max(yValues)