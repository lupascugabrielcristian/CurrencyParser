from Grafic.Dimensions import Dimensions


class AutoCanvasCalculator:

    def __init__(self):
        self.xCanvasSize = 0
        self.yCanvasSize = 0
        self.xUnitSize = 0

    def createCanvasDimensions(self, listOfPoints):
        self.yCanvasSize = 400
        self.xUnitSize = 30
        self.xCanvasSize = (len(listOfPoints) + 3) * self.xUnitSize

        dimensions = Dimensions()
        dimensions.xCanvasSize = self.xCanvasSize
        dimensions.xUnitSize = self.xUnitSize
        dimensions.yCanvasSize = self.yCanvasSize

        return dimensions