from Parser.ValueParser import ValueParser
from Watchers.WatchersManager import WatchersManager


class InvestmentMonitor:

    def __init__(self, debugflag, portofolio):
        self.portofolio = portofolio
        self.debugflag = debugflag
        self.parser = ValueParser(debugflag)
        self.previousValues = []
        self.repeats = 0
        self.watchersManager = WatchersManager(debugflag)

    def monitor(self):
        if len(self.portofolio.investments) == 0:
            print("No investments to monitor")
            return

        print("Monitoring")

        for index in range(len(self.portofolio.investments)):
            self.watchersManager.addWatch(self.portofolio.investments[index])
            # MonitorStarter(self.debugflag,  self.portofolio.investments[index]).analyze()

        print("Monitoring is stoped")