from Watchers.WatchThread import WatchThread


class WatchersManager:

    def __init__(self, debugflag):
        self.debuflag = debugflag
        self.watchers = []

    def addWatch(self, investment, thread):
        watcher = WatchThread(investment, thread)
        if not self.__isInvestmentWatched(investment):
            self.watchers.append(watcher)
            watcher.start()
        else:
            oldWatcher = self.__getWatcher(investment)
            if not oldWatcher.isAlive():
                oldWatcher.start()


    def __isInvestmentWatched(self, investment):
        for watcher in self.watchers:
            if watcher.investment == investment:
                return True
        return False

    def __getWatcher(self, investment):
        for watcher in self.watchers:
            if watcher.investment == investment:
                return watcher