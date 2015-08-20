from pymongo import MongoClient
import time


class DataStore:


	databasename = "bitcoinvalues"
	collectionname = 'values'

	def __init__(self):
		client = MongoClient()
		self.db = client[self.databasename]


	def addToDataBase(self, value):
		collection = self.db[self.collectionname]

		return collection.insert_one(
			{
				"data": time.strftime("%d/%m/%Y"),
				"value": value,
				"value_id": "some id"
			}
		)



	def showData(self):
		print(self.db[self.databasename])