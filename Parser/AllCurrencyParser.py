from bs4 import BeautifulSoup
import requests


class AllCurrencyParser:

    def parse(self):
        listOfCurrencies = self.findInPage()
        return listOfCurrencies

    def findInPage(self):
        address = "http://www.fxstreet.com/rates-charts/currency-rates/"
        webpage = requests.get(address)
        data = webpage.text

        soup = BeautifulSoup(data)

        table = soup.find(style="cursor:pointer")

        currencies = []
        for el in table.find_all_next("tr"):
            name = ""
            for td in el.find_all_next("td"):
                parsedname = self.trygetname(td)

                if parsedname != "":
                    name = parsedname

                if name != "":
                    currencies.append(name)
                    name = ""

        return currencies

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