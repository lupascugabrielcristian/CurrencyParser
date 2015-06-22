import subprocess


class MonitorStarter:

    def __init__(self, debugflag, investment):
        self.debugflag = debugflag
        self.investment = investment


    def analyze(self):
        file  = self.__writeScriptFile()
        command = "gnome-terminal -x sh -c 'sh %s'" %file
        process = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)
        return process

    def __writeScriptFile(self):
        folder = "/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Trading/"

        repeats = self.askForRepeats()
        index = self.investment.onlineindex
        initialPrice = self.investment.initialPrice
        file = "monitor" + str(self.investment.id) + ".sh"
        path = folder + "watchers/" + file

        scriptFileObject = open(path, 'w')

        scriptFileObject.write("cd %s\n" %folder)
        scriptFileObject.write("python3.3 monitorscript.py %d %d %d\n" %(repeats, index, initialPrice))
        scriptFileObject.close()

        return path

    @staticmethod
    def askForRepeats():
        repeats = int(input("Repeats(for infinite put -1): "))
        return repeats