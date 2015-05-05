from Grafic.UnitConverter import UnitConverter


class ValuesMarker:

    def __init__(self, dimensions, canvas):
        self.dimensions = dimensions
        self.canvas = canvas
        self.calculator = UnitConverter(self.dimensions)

    def showValue(self, point):
        calculator = self.calculator
        x1 = calculator.convertXUnit(point.getX()) - 3
        y1 = calculator.convertYUnit(point.getY()) - 3
        x2 = calculator.convertXUnit(point.getX()) + 3
        y2 = calculator.convertYUnit(point.getY()) + 3
        self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline='red')


    def makeLine(self, point1, point2):
        calculator = self.calculator
        x1 = calculator.convertXUnit(point1.getX())
        y1 = calculator.convertYUnit(point1.getY())
        x2 = calculator.convertXUnit(point2.getX())
        y2 = calculator.convertYUnit(point2.getY())
        self.canvas.create_line(x1, y1, x2, y2)

    def showValues(self, values):
        for index in range (0, len(values)):
            self.showValue(values[index])

            if index > 0:
                self.makeLine(values[index - 1], values[index])

