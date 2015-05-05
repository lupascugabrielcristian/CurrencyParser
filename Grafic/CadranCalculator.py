class CadranCalculator:

    GRAPH_PADDING = 10

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.GRAPH_PADDING = dimensions.graphPadding


    def calculate(self):
        x = self.GRAPH_PADDING + self.dimensions.labelsSpace
        y1 = self.GRAPH_PADDING
        y2 = self.dimensions.yCanvasSize - self.GRAPH_PADDING
        self.dimensions.verticalLine = (x,y1,x, y2)


        x1 = self.GRAPH_PADDING + self.dimensions.labelsSpace
        y = self.dimensions.yCanvasSize - self.GRAPH_PADDING
        x2 = self.dimensions.xCanvasSize - self.GRAPH_PADDING
        self.dimensions.horizontalLine = (x1,y,x2,y)

        self.dimensions.xOrigin = x
        self.dimensions.yOrigin = y

        return self.dimensions