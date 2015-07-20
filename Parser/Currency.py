class Currency:

    name = "default name"
    value = 0

    def __init__(self, name, value=0):
        """
        This represents a currency
        :param name:
        :param value:
        :return:
        """
        self.name = name
        self.value = value
        separation = name.index('/')
        self.fromName = name[:separation]
        self.toName = name[separation + 1:]


    def __str__(self):
        return "Name: {} Value = {}".format(self.name, self.value)

    def __repr__(self):
        return "Name: {} Value = {}".format(self.name, self.value)