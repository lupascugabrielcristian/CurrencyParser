import sys
from tkinter import Tk

sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency'])

from Grafic.AutoGraphic import AutoGraphic
from Parser.GraphicPointsBuilder import GraphicPointsBuilder


def buildGraphic():
    folder = "/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Trading/"
    file = "values" + ".num"
    path = folder + "graphic/" + file

    values = []
    with open(path) as f:
        for line in f:
            values.append(float(line.strip()))

    print(values)
    points = GraphicPointsBuilder(None).builFromValue(values)

    root = Tk()
    graphic = AutoGraphic(points, master=root)
    graphic.mainloop()

while 1:
    print("Showing graphic")
    buildGraphic()
