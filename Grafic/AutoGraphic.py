import tkinter
from tkinter import Frame

from Grafic.AutoConvas import AutoCanvasCalculator
from Grafic.CadranCalculator import CadranCalculator
from Grafic.GridMaker import GridMaker
from Grafic.UnitCalculator import UnitCalculator
from Grafic.ValuesMarker import ValuesMarker


class AutoGraphic(Frame):

    def __init__(self, points, master=None):
        Frame.__init__(self, master)
        """
        Give the number of positive units on X, number of positive units on Y and the unit size
        """
        self.dimensions = None
        self.canvas = tkinter.Canvas()
        self.createAutoSizeGraphic(points)


    def createAutoSizeGraphic(self, listOfPoints):
        canvas = self.canvas

        if len(listOfPoints) == 0 or listOfPoints is None:
            return

        dimensions = AutoCanvasCalculator().createCanvasDimensions(listOfPoints)
        dimensions = CadranCalculator(dimensions).calculate()
        dimensions = UnitCalculator(dimensions, listOfPoints).calculateYUnitSize()

        self.dimensions = dimensions

        # Adjust canvas
        canvas["width"] = dimensions.xCanvasSize
        canvas["height"] = dimensions.yCanvasSize

        # Create cadran
        canvas.create_line(dimensions.horizontalLine[0], dimensions.horizontalLine[1],dimensions.horizontalLine[2],dimensions.horizontalLine[3])
        canvas.create_line(dimensions.verticalLine[0], dimensions.verticalLine[1],dimensions.verticalLine[2],dimensions.verticalLine[3])

        ValuesMarker(dimensions, canvas).showValues(listOfPoints)

        GridMaker(dimensions, canvas).makeGrid()

        canvas.pack(fill=tkinter.BOTH)
