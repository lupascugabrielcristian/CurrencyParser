from tkinter import Tk

from Database.DataStore import DataStore
from Grafic.AutoGraphic import AutoGraphic
from Grafic.GraphicPointsBuilder import GraphicPointsBuilder


class BitCoinGraphicBuilder:

	def __init__(self):
		self.values = DataStore().getValues()

	def showgraphic(self):
		points = GraphicPointsBuilder(None).builFromValue(self.values)
		root = Tk()
		graphic = AutoGraphic(points, master=root)
		graphic.mainloop()