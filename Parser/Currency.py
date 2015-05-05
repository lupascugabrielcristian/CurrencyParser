class Currency:

    name = "default name"
    value = 0

    def __init__(self, name, value):
        """
        This represents a currency
        :param name:
        :param value:
        :return:
        """
        self.name = name
        self.value = value

    def __str__(self):
        return "Name: " + self.name + "Value=" + self.value

    def __repr__(self):
        return "Name: " + str(self.name) + ", Value=" + str(self.value)