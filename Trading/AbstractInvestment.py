import random


class AbstractInvestment:

    def __init__(self, debugflag):
        self.debugFlag = debugflag
        self.name = "default name"
        self.fromName = "from"
        self.toName = "to"
        self.onlineindex = 0
        self.units = 0.0
        self.id = random.randint(0, 10000)
