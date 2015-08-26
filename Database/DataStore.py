from pymongo import MongoClient
import time
from Trading.Money import Money

class DataStore:

	databasename = "bitcoinvalues"
	collectionname = 'values'
	collectionportofolio = 'portofolio'

	def __init__(self):
		client = MongoClient()
		self.db = client[self.databasename]


	def addToDataBase(self, value):
		collection = self.db[self.collectionname]

		return collection.insert_one(
			{
				"data": time.strftime("%d/%m/%Y %H:%M"),
				"value": value,
			}
		)



	def showData(self):
		collection = self.db[self.collectionname]
		cursor = collection.find()

		for document in cursor:
			print(document['value'] + " at " + document['data'])

	def getValues(self):
		collection = self.db[self.collectionname]
		cursor = collection.find()

		values =[]
		for document in cursor:
			values.append(document['value'])

		return values

	def getPortofolio(self):
		collection = self.db[self.collectionportofolio]
		from Trading.PortofolioRemake import PortofolioRemake
		portofolio = PortofolioRemake()

		cursor = collection.find()
		if cursor.count() > 0:
			for document in cursor:
				portofolio.addMoney(Money(document['name'], document['ammount']))
		else:
			portofolio.addMoney(Money("USD", 1000))
			print("No Portofolio found. Created a new one")

		return portofolio

	def savePortofolio(self, portofolio):
		collection = self.db[self.collectionportofolio]
		collection.remove({})

		for money in portofolio:
			collection.insert_one(
				{
					"name":money.name,
					"ammount": money.ammount
				}
			)

	def removeAllItems(self):
		collection = self.db[self.collectionname]
		return collection.remove({})