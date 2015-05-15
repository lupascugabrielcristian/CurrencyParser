class HistoryObject:

    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __repr__(self):
        return "Name: " + str(self.name) + ", Points: " + str(self.points)