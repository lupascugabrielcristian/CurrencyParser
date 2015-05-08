class GraphicPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return float(self.x)

    def getY(self):
        return float(self.y)

    def __str__(self):
        return "X = " + str(self.x) + " Y = " + str(self.y)

    def __repr__(self):
        return "X = " + str(self.x) + " Y = " + str(self.y)

    def __lt__(self, other):
        if other.getY() < self.y:
            return True
        else: return False

    def __gt__(self, other):
        if other.getY() >= self.y:
            return True
        else: return False