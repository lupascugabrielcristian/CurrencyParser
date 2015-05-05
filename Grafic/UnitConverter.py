class UnitConverter:

    def __init__(self, dimensions):
        self.dimensions = dimensions

    def convertXUnit(self, x):
        return self.dimensions.xOrigin + x * self.dimensions.xUnitSize

    def convertYUnit(self, y):
        return self.dimensions.yOrigin - ( ((y - self.dimensions.minYValue) * 10 ** (self.dimensions.yFactor - 1)) * self.dimensions.yUnitValue )

    def convertFromYDistance(self, dist):
        dimensions = self.dimensions
        return (dist / dimensions.yUnitValue) / 10 ** (dimensions.yFactor - 1) + dimensions.minYValue