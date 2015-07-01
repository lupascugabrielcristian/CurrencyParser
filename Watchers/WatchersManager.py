from Trading.AnalyzeStarter import AnalyzeStarter


class WatchersManager:

    def __init__(self, debugflag):
        self.debugflag = debugflag
        self.watchers = []

    def addWatch(self, investment):
        if not self.__isInvestmentWatched(investment):
            self.watchers.append(investment)
            print("Starting watch for %s - %s" %(investment.name, investment.open))
            AnalyzeStarter(self.debugflag, investment).analyze()


    def __isInvestmentWatched(self, investment):
        for watcher in self.watchers:
            if watcher == investment:
                return True
        return False


    def empty(self):
        for watcher in self.watchers:
            watcher.stop()

        self.watchers.clear()
