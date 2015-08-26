from Trading.Money import Money
from Utils.CurrenciesEnum import CurrenciesEnum


class PortofolioOperations:

	def __init__(self, portofolio):
		self.portofolio = portofolio


	def buyBitCoin(self, ammount, rate):
		self.makeTransaction(CurrenciesEnum.BTC, rate, CurrenciesEnum.USD, ammount)


	def buyUsd(self, ammount, rate):
		self.makeTransaction(CurrenciesEnum.USD, rate, CurrenciesEnum.BTC, ammount)


	"""
	whatToBuy = the name of the currency you want to buy
	buyPrice = is the rate of conversion whatToBuy/whatToPay'
	whatToPay = the name of currency in which the paiment is to be made
	ammountToBuy = ammount of whatToBuy currency you want to aquire
	"""
	def makeTransaction(self, whatToBuy, buyPrice, whatToPay, ammountToBuy):
		ammountToPay = buyPrice * ammountToBuy

		toPayMoney = Money(whatToPay, ammountToPay)
		toBuyMoney = Money(whatToBuy, ammountToBuy)

		if self.portofolio.haveEnough(toPayMoney):
			self.portofolio.extractMoney(toPayMoney)
			self.portofolio.addMoney(toBuyMoney)
			print("Transaction completted")
		else:
			print("Not enough money")