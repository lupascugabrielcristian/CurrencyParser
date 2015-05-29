class Money:

    def __init__(self, name="RON", ammount=100):
        self.name = name
        self.sum = ammount

    def __repr__(self):
        return "{} Value = {}".format(self.name, self.sum)

    def __str__(self):
        return "{} Value = {}".format(self.name, self.sum)