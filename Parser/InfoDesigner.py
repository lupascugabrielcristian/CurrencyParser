import sched
import time
from Grafic.AutoSizeGraphic import AutoGraphic
from Parser.GraphicPointsBuilder import GraphicPointsBuilder
from Parser.Method_2_Parser import Method_2_Parser


class InfoDesigner:

    def __init__(self):
        self.interval = 10
        self.repeats = 5
        self.currency_index = 2
        self.selectedCurrency = []


    def repeatFunction(self):
        allCurrencies = Method_2_Parser().parse()
        currentCurrency = allCurrencies[self.currency_index]
        self.selectedCurrency.append(currentCurrency)
        print(currentCurrency)




    def run(self):
        s = sched.scheduler(time.time, time.sleep)

        for i in range(5):
            s.enter(self.interval, self.repeats, self.repeatFunction, ())
            s.run()

        points = GraphicPointsBuilder(self.selectedCurrency).build()
        print(points)
        AutoGraphic(points)