class WatchThread:
    def __init__(self, investment, thread):
        self.investment = investment
        self.thread = thread

    def start(self):
        self.thread.start()