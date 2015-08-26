class PortofolioRemake:

	def __init__(self):
		self.portofolio = []

	def addMoney(self, money):
		for m in self.portofolio:
			if m.name == money.name:
				m.ammount += money.ammount
				return 1

		self.portofolio.append(money)
		return 0

	def haveEnough(self, money):
		for m in self.portofolio:
			if m.name == money.name:
				if m.ammount >= money.ammount:
					return True

		return False

	def extractMoney(self, money):
		for m in self.portofolio:
			if m.name == money.name:
				m.ammount -= money.ammount
				return 1

		return 0

	def __str__(self):
		representation = ""
		for money in self.portofolio:
			representation += str(money) + ", "

		return representation

	def __repr__(self):
		return str(self)