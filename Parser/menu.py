import sys

sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency'])

from Database.DataStore import DataStore
from Parser.BitcoinParserBig import BitcoinParserBig
from Utils.BitCoinGraphicBuilder import BitCoinGraphicBuilder
from interface.DatabaseOperations import DatabaseOperations
import subprocess
from UserInterface.MenuInterface import MenuInterface
from Viewers.HistoryViewer import HistoryViewer
from Parser.VariationFinder import VariationFinder
from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency


# def initializePortofolio():
#     reader = DataReaderWriter()
#     myPortofolio = reader.getPortofolio()
#     if myPortofolio is None:
#         myPortofolio = Portofolio()
#         myPortofolio.addMoney("EUR", 1000000)
#         reader.savePorofolio(myPortofolio)
#
#     return myPortofolio

# def prepareInvestmentManager():
#     manager = InvestmentManger(debugflag, portofolio)
#     manager.cleanup()
#     return manager


def cleanFiles():
	file = "/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency/Watchers/clean.sh"
	command = "gnome-terminal -x sh -c 'sh %s'" %file
	subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)


answer = 0
debugflag = False

# portofolio = initializePortofolio()
# investmentManager = prepareInvestmentManager()
datastore = DataStore()
portofolio = datastore.getPortofolio()

while answer != 7:
	print("Menu")
	print("=====")
	# print("1. One currency analyze")
	# print("2. List currencies")
	# print("3. Find a currency")
	# print("4. Find greatest change")
	# print("8. See history file")
	# print("9. View Portofolio")
	# print("12. Edit Portofolio")
	# print("10. Make an investment")
	# print("11. Monitor")
	# print("13. Test terminal")
	print("14. Check BitCoin value")
	print("15. View Bitcoin values")
	print("16. Graphic for Bitcoin values")
	print("17. Databse operations")
	print("18. Operations for BitCoin")
	print("19. Portofolio")
	# print("5. Debug ON")
	# print("6. Debug OFF")
	print("7. Exit")

	answer = int(input("Choose your answer:"))

	# investmentManager.cleanup()

	if answer == 1:
		OneCurrency(debugflag).run()

	if answer == 2:
		interface = MenuInterface(debugflag)
		AllCurrencyList().run()
		interface.destroy()

	if answer == 3:
		interface = MenuInterface(debugflag)
		AllCurrencyList().filter()
		interface.destroy()

	if answer == 4:
		VariationFinder(debugflag).findMaxVariation()

	if answer == 5:
		print("Debug Mode switched on. There will be al lot of printing!")
		debugflag = True

	if answer == 6:
		print("Debug Mode switched off. Printing to a minimum!")
		debugflag = False

	if answer == 8:
		HistoryViewer(debugflag).askforOption()

	# if answer == 9:
	#     PortofolioViewer(portofolio).view()
	#
	# if answer == 12:
	#     PortofolioEditor(portofolio, investmentManager, debugflag).edit()
	#
	# if answer == 10:
	#     investmentManager.makeInvestment("auto")
	#
	# if answer == 11:
	#     InvestmentMonitor(debugflag, portofolio).monitor()

	if answer == 14:
		BitcoinParserBig().getPrice()

	if answer == 15:
		datastore.showData()

	if answer == 16:
		BitCoinGraphicBuilder().showgraphic()

	if answer == 17:
		DatabaseOperations(datastore).menu()

	if answer == 18:
		print("Not implemented")

	if answer == 19:
		print(portofolio)


cleanFiles()
datastore.savePortofolio(portofolio)
print("By by")