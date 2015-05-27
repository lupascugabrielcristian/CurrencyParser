import pickle


class DataReaderWriter:

    def __init__(self):
        self.portofolioFile = "/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency/Parser/portofolio"
        self.historyFile = "/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency/Parser/history"

    def getPortofolio(self):
        try:
            inputFile = open(self.portofolioFile, 'rb')
            portofolio = pickle.load(inputFile)
            return portofolio
        except FileNotFoundError:
            return None

    def savePorofolio(self, portofolio):
        outputFile = open(self.portofolioFile, 'wb')
        pickle.dump(portofolio, outputFile)
        outputFile.close()