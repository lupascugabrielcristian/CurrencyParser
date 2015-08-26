from bs4 import BeautifulSoup
import urllib3
from Database.DataStore import DataStore


class BitcoinParser:

	webaddress = "http://bitcoin-value-live.com/"
	BITFINEX = 0
	BITSTAMP = 1

	def __init__(self, marketindex=0):
		self.marketIndex = marketindex
		print("Parsing bitcoin page")


	def findPrice(self):
		http = urllib3.PoolManager()
		webpage = http.request('GET', self.webaddress).read()
		soup = BeautifulSoup(webpage)

		table = soup.find('table', attrs={'class': 'table table-hover table-striped table-values'})

		rows = []
		for el in table.tbody.find_all_next("tr"):
			rows.append(el)

		marketRow = rows[self.marketIndex]

		data = []
		for tabledata in marketRow.find_all("td"):
			data.append(tabledata.string)

		return data

	def getPrice(self):
		currentvalue = self.findPrice()[1]
		result = DataStore().addToDataBase(currentvalue)

		if result is not None:
			print("Value added " + currentvalue)
		else:
			print("Cannot add value to database")

		return currentvalue
