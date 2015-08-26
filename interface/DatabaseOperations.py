class DatabaseOperations:

	def __init__(self, datastore):
		self.datastore = datastore

	def menu(self):
		print("What operation?")
		print("1. Remove all items")
		answer = int(input("?"))

		if answer == 1:
			result = self.datastore.removeAllItems()
			print(str(result['n']) + " values removed")
