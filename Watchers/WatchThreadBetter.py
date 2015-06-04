import threading


class WatchThreadBetter(threading.Thread):

    def __init__(self):
        super(WatchThreadBetter, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()