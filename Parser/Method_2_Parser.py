from bs4 import BeautifulSoup
import requests

from Parser.Currency import Currency


class Method_2_Parser:

    # Sa parsez si pagina asta "http://www.fxstreet.com/rates-charts/currency-rates/"
    # pentru live currency

    def _init_(self):
        self.test = "tst"


    def findInPage(self):
        address = "http://www.fxstreet.com/rates-charts/currency-rates/"
        webpage = requests.get(address)
        data = webpage.text

        soup = BeautifulSoup(data)

        table = soup.find(style="cursor:pointer")

        currencies = []
        for el in table.find_all_next("tr"):
            value = 0
            name = ""
            for td in el.find_all_next("td"):
                parsedname = self.trygetname(td)

                if parsedname != "":
                    name = parsedname

                parsedvalue = self.trygetvalue(td)
                if parsedvalue > 0:
                    value = parsedvalue

                if value > 0 and name != "":
                    currencies.append(Currency(name, value))
                    value = 0
                    name = ""

        return currencies


    def parse(self):
        listOfCurrencies = self.findInPage()
        print("Currencies: " + str(listOfCurrencies))
        return listOfCurrencies

    def trygetname(self, tdelement):
        name = ""
        try:
            if tdelement['class'] is not None:
                name = tdelement.get_text()

        except TypeError:
            name = ""

        except KeyError:
            name = ""

        return name

    def trygetvalue(self, tdelement):
        value = 0
        try:
             if tdelement['id'] is not None:
                idstring  = tdelement['id']
                if "last" in idstring:
                    value = float(tdelement.get_text())
        except TypeError:
            value = -1

        except KeyError:
            value = -1

        return value
