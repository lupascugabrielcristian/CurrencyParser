import tkinter
from Grafic.GraphicPoint import *


class Graphic:

    def makecadrans(self):
        self.canvas.create_line(10, 5, 10, self.height - 5)
        self.canvas.create_line(5, self.height - 10, self.width - 5, self.height - 10)

    def __init__(self, unitswidth=10, unitsheight=10, unitSize=10):
        """
        Give the number of positive units on X, number of positive units on Y and the unit size
        """
        self.xUnitSize = unitSize
        self.yUnitSize = unitSize
        self.width = unitswidth * self.xUnitSize
        self.height = unitsheight * self.yUnitSize
        self.xOrigin = 10
        self.yOrigin = self.height - 10
        self.canvas = tkinter.Canvas(width=int(self.width), height=int(self.height))
        self.makecadrans()

    def display(self):
        global window
        self.canvas.pack(fill=tkinter.BOTH, expand=1)
        self.window.mainloop()

    def convertX(self, x):
        # return float(x) * self.xUnitSize + self.middle_x
        return float(x) * self.xUnitSize + 10

    def convertY(self, y):
        # return self.middle_y - float(y) * self.yUnitSize
        return self.yOrigin - float(y - self.minYValue) * self.yUnitSize

    def showpoint(self, p):
        self.canvas.create_line(self.xOrigin, self.yOrigin, self.convertX(p.getX()), self.convertY(p.getY()), fill='red', width=1.5)

    def showPointCircle(self, p):
        self.canvas.create_oval(self.convertX(p.getX()) - 3, self.convertY(p.getY()) - 3, self.convertX(p.getX()) + 3, self.convertY(p.getY()) + 3, fill='red', outline='red')

    def showpoints(self, lst):
        """
        Shows the line connecting all points in the list\n
        :param lst: a list of GraphicalPoints objects\n
        :return: None
        """
        for index in range(0, len(lst) - 1):
            origin = lst[index]
            final = lst[index + 1]
            self.showPointCircle(lst[index])
            self.canvas.create_line(self.convertX(origin.getX()), self.convertY(origin.getY()), self.convertX(final.getX()), self.convertY(final.getY()), fill='red', width=1.5)
        self.showPointCircle(lst[-1])

    @staticmethod
    def __f(x2coeficient, xcoeficient, x):
        return x2coeficient * x**2 + x * xcoeficient

    def showfunction(self, *args):
        """
        :param args: 1st should be the min range, 2nd should be the max range,
        3rd - the x2 coef, 4th - x coef, 5th - x0 coef
        :return:
        """
        rangeMin = args[0]
        rangeMax = args[1]
        points = []
        for x in range(rangeMin, rangeMax + 1):
            y = self.__f(args[2], args[3], x)
            points.append(GraphicPoint(x, y))
        self.showpoints(points)

    def giveSettings(self, arguments):
        if "xUnitSize" in arguments:
            self.xUnitSize = arguments['xUnitSize']
        if "yUnitSize" in arguments:
            self.yUnitSize = arguments['yUnitSize']
        if "minYValue" in arguments:
            self.minYValue = arguments['minYValue']

    window = tkinter.Tk()
    canvas = None
    width = 0
    minYValue = 0
    height = 0
    factor = 1
