from bs4 import BeautifulSoup
import urllib3

from Grafic.GraphicPoint import GraphicPoint
from Trading.Currency import Currency


class Method_1_Parser:

    def __init__(self):
        self.currencies = []

    def makeAddress(self, minDate, maxDate):
        result = []
        for zi in range(minDate, maxDate + 1):
            day = "%02d" % (zi,)
            result.append("http://www.cursbnr.ro/arhiva-curs-bnr-2015-04-" + day)
        return result

    def getGraphPoints(self, listOfValues):
        result = []
        for index in range(len(listOfValues)):
            x = index + 1
            y = listOfValues[index].value
            result.append(GraphicPoint(x, y))
        return result

    def findInPage(self):
        http = urllib3.PoolManager()
        addresses = self.makeAddress(1, 30)
        for address in addresses:
            webpage = http.request('GET', address).read()
            soup = BeautifulSoup(webpage)

            table = soup.find(id="tabel_valute_arhiva")
            for el in table.tbody.find_all_next("tr"):
                if "USD" in el.get_text():
                    data = el.findAll("b")
                    self.currencies.append(Currency(data[0].string, data[2].string))


    def parse(self):
        self.findInPage()
        return self.getGraphPoints(self.currencies)