from Grafic.GraphicPoint import GraphicPoint


class GraphicPointsBuilder:

    def __init__(self, listOfCurrencies):
        self.currencies = listOfCurrencies
        self.increment = 1

    def build(self):
        graphicPoints = []
        increment = self.increment
        for currency in self.currencies:
            graphicPoints.append(GraphicPoint(increment, currency.value))
            increment += 1
        return graphicPoints