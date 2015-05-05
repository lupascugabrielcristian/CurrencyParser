from bs4 import BeautifulSoup
import urllib3
from Grafic.AutoSizeGraphic import AutoGraphic

from Grafic.GraphicPoint import *
from Parser.Currency import Currency


# Sa parsez si pagina asta "http://www.fxstreet.com/rates-charts/currency-rates/"
# pentru live currency


def makeAddress(minDate, maxDate):
    result = []
    for zi in range(minDate, maxDate + 1):
        day = "%02d" % (zi,)
        result.append("http://www.cursbnr.ro/arhiva-curs-bnr-2015-04-" + day)
    return result

def getGraphPoints(listOfValues):
    result = []
    for index in range(len(listOfValues)):
        x = index + 1
        y = listOfValues[index].value
        result.append(GraphicPoint(x, y))
    return result


currencies = []
http = urllib3.PoolManager()
addresses = makeAddress(1, 30)
for address in addresses:
    webpage = http.request('GET', address).read()
    soup = BeautifulSoup(webpage)

    data = []

    table = soup.find(id="tabel_valute_arhiva")
    for el in table.tbody.find_all_next("tr"):
        if "USD" in el.get_text():
            data = el.findAll("b")
            currencies.append(Currency(data[0].string, data[2].string))


grafic = AutoGraphic(getGraphPoints(currencies))

