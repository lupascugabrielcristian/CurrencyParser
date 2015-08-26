from bs4 import BeautifulSoup
import urllib3
from Database.DataStore import DataStore


class BitcoinParserBig:

	webaddress = "https://bitcoinwisdom.com/"
	USD = 0
	CNY = 1
	EUR = 2
	CAD = 3
	RUR = 4

	NAME = 0
	PRICE = 1

	def __init__(self, currency=1):
		self.currency = currency
		print("Parsing bitcoinwisdom page")

	def findPrice(self):
		http = urllib3.PoolManager()
		webpage = http.request('GET', self.webaddress).read()
		soup = BeautifulSoup(webpage)
		table = soup.find('td', attrs={'class':'outer'})

		rows = []
		for el in table.find_all("tbody"):
			if el['class'][0] == "body":
				rows.append(el)

		rows = rows[0:5]

		marketRow = rows[self.currency]

		data = []
		for tabledata in marketRow.find_all("td"):
			data.append(tabledata.string)

		return data

	def getPrice(self):
			currentvalue = self.findPrice()[self.PRICE]
			result = DataStore().addToDataBase(currentvalue)

			if result is not None:
				print("Value added " + currentvalue)
			else:
				print("Cannot add value to database")

			return currentvalue