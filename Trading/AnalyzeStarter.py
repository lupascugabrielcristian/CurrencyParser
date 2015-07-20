import subprocess

from Parser.ValueParser import ValueParser


class AnalyzeStarter:

    def __init__(self, debugflag, investment):
        self.debugflag = debugflag
        self.investment = investment
        self.parser = ValueParser(debugflag)

    def analyze(self):
        if "auto" in self.investment.type:
            file = self.__writeScriptFileForAuto()
        else: file  = self.__writeScriptFile()

        command = "gnome-terminal -x sh -c 'sh %s'" %file
        process = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)
        return process

    def __writeScriptFile(self):
        folder = "/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Trading/"

        index = self.investment.onlineindex
        initialPrice = self.investment.initialPrice
        name = self.investment.name
        file = "watch" + str(self.investment.id) + ".sh"
        path = folder + "watchers/" + file

        scriptFileObject = open(path, 'w')

        scriptFileObject.write("cd %s\n" %folder)
        scriptFileObject.write("python3.3 analysertest.py %d %.4f %s\n" %(index, initialPrice,name))
        scriptFileObject.close()

        return path

    def __writeScriptFileForAuto(self):
        folder = "/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Trading/"

        index = self.investment.onlineindex
        name = self.investment.name
        file = "watch" + str(self.investment.id) + ".sh"
        path = folder + "watchers/" + file

        scriptFileObject = open(path, 'w')

        scriptFileObject.write("cd %s\n" %folder)
        scriptFileObject.write("python3.3 automatedInvestment.py %d %s\n" %(index, name))
        scriptFileObject.write("clac")
        scriptFileObject.close()

        return path