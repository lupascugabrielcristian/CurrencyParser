class HistoryObject:

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.timespan = 0

    def __repr__(self):
        return "Name: " + str(self.name) + " over " + str(self.timespan) + ", Points: " + str(self.points)