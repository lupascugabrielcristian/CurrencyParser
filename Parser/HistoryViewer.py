import pickle
from Grafic.AutoSizeGraphic import AutoGraphic


class HistoryViewer:

    def __init__(self, debugflag):
        self.debugflag = debugflag
        self.historyObjects = []
        self.indexChosen = -1


    def view(self):
        historyFile = open("/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency/Parser/history", 'rb')


        try:
            while True:
                historyobject = pickle.load(historyFile)
                self.historyObjects.append(historyobject)
        except EOFError:
            print("File ended")

        historyFile.close()

        for index in range(0, len(self.historyObjects)):
            print(str(index) + ". " + self.historyObjects[index].name)

        self.indexChosen = int(input("Alege una: "))
        self.displayOne()


    def displayOne(self):
        print (self.historyObjects[self.indexChosen])
        AutoGraphic(self.historyObjects[self.indexChosen].points)
