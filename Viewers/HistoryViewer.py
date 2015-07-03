import pickle
from Grafic.AutoSizeGraphic import AutoGraphic


class HistoryViewer:

    def __init__(self, debugflag):
        self.debugflag = debugflag
        self.historyObjects = []
        self.indexChosen = -1


    def askforOption(self):
        while True:
            print("1. View")
            print("2. Delete")
            print("3. Back")
            answer = int(input("Alege una: "))
            if answer == 1:
                self.view()
            if answer == 2:
                self.deleteOne()
            if answer == 3:
                print("All done")
                break


    def view(self):
        historyFile = open("/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency/Parser/history", 'rb')
        self.historyObjects.clear()

        try:
            while True:
                historyobject = pickle.load(historyFile)
                self.historyObjects.append(historyobject)
        except EOFError:
            print("File read")

        historyFile.close()

        for index in range(0, len(self.historyObjects)):
            try:
                print(str(index) + ". " + str(self.historyObjects[index]))
            except AttributeError:
                print(str(index) + ". " + self.historyObjects[index].name)

        self.indexChosen = int(input("Alege una: "))
        self.displayOne()


    def displayOne(self):
        try:
            print (self.historyObjects[self.indexChosen])
        except AttributeError:
            print("===> " + str(self.indexChosen) + ". " + self.historyObjects[self.indexChosen].name + " <=====")
        AutoGraphic(self.historyObjects[self.indexChosen].points)


    def deleteOne(self):
        historyFile = open("/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Parser/history", 'rb')
        self.historyObjects.clear()

        try:
            while True:
                historyobject = pickle.load(historyFile)
                self.historyObjects.append(historyobject)
        except EOFError:
            print("File read")

        historyFile.close()

        for index in range(0, len(self.historyObjects)):
            try:
                print(str(index) + ". " + str(self.historyObjects[index]))
            except AttributeError:
                print(str(index) + ". " + self.historyObjects[index].name)

        indexChosen = int(input("Alege una: "))
        self.historyObjects.pop(indexChosen)

        outputFile = open("/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Parser/history", 'wb')

        for historyobject in self.historyObjects:
            pickle.dump(historyobject, outputFile)

        outputFile.close()