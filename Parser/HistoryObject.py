class HistoryObject:

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.timespan = 0
        self.interval = 0

    def __repr__(self):
        return "Name: " + str(self.name) + " over " + str(self.timespan) + " seconds, at intervals of " + str(self.interval) + "seconds, Points: " + str(self.points)

    def __str__(self):
        return "Name: " + str(self.name) + " over " + str(self.timespan) + " seconds, at intervals of " + str(self.interval) + "seconds, Points: " + str(self.points)
