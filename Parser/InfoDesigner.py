import sched
import time
import pickle

from Grafic.AutoGraphic import AutoGraphic
from Grafic.GraphicPointsBuilder import GraphicPointsBuilder
from Parser.HistoryObject import HistoryObject
from Parser.Method_2_Parser import Method_2_Parser


class InfoDesigner:

    def __init__(self, debugflag):
        self.debugflag = debugflag
        self.interval = 10
        self.repeats = 5
        self.currency_index = 2
        self.currency_name = ""
        self.selectedCurrency = []


    def run(self):
        s = sched.scheduler(time.time, time.sleep)

        for i in range(self.repeats):
            print("====== " + str(i) + " =====")
            s.enter(self.interval, self.repeats, self.repeatFunction, ())
            s.run()

        points = GraphicPointsBuilder(self.selectedCurrency).build()
        print(points) # LOG
        self.saveToFile(points)
        AutoGraphic(points)


    def repeatFunction(self):
        allCurrencies = Method_2_Parser(self.debugflag).parse()
        currentCurrency = allCurrencies[self.currency_index]
        self.currency_name = currentCurrency.name
        self.selectedCurrency.append(currentCurrency)
        print(currentCurrency) # LOG


    def saveToFile(self, points):
        outputFile = open("/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Parser/history", 'ab')
        timespan = self.interval * self.repeats

        historyobject = HistoryObject(self.currency_name, points)
        historyobject.timespan = timespan
        historyobject.interval = self.interval
        pickle.dump(historyobject, outputFile)

        outputFile.close()