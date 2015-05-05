from Grafic.UnitConverter import UnitConverter


class GridMaker:
    def __init__(self, dimensions, canvas):
        self.dimensions = dimensions
        self.canvas = canvas

    def makeGrid(self):
        LABEL_OFFSET = -22
        dimensions = self.dimensions
        gridInterval = dimensions.yGraphSize / 10

        # First line
        currentGridPosition = dimensions.yOrigin - gridInterval
        valStr = "%0.3f" % dimensions.minYValue
        text = self.canvas.create_text(dimensions.xOrigin + LABEL_OFFSET, dimensions.yOrigin)
        self.canvas.insert(text, 12, valStr)

        while currentGridPosition >= dimensions.graphPadding:
            x1 = dimensions.xOrigin + 1
            y = currentGridPosition
            x2 = dimensions.xCanvasSize - dimensions.graphPadding
            currentGridPosition -= gridInterval
            self.canvas.create_line(x1, y, x2, y, fill="grey", dash=(5, 4))

            val = UnitConverter(dimensions).convertFromYDistance(dimensions.yOrigin - y)
            valStr = "%0.3f" % val
            text = self.canvas.create_text(x1 + LABEL_OFFSET, y)
            self.canvas.insert(text, 12, valStr)