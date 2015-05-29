import sys
from Editors.PprtofolioEditor import PortofolioEditor

sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency'])

from UserInterface.MenuInterface import MenuInterface
from Trading.InvestmentsMonitor import InvestmentMonitor
from Viewers.HistoryViewer import HistoryViewer
from Trading.InvestmentManager import InvestmentManger
from Trading.DataReaderWriter import DataReaderWriter
from Trading.Money import Money
from Trading.Portofolio import Portofolio
from Viewers.PortofoloiViewer import PortofolioViewer
from Parser.VariationFinder import VariationFinder
from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency



def initializePortofolio():
    reader = DataReaderWriter()
    myPortofolio = reader.getPortofolio()
    if myPortofolio is None:
        myPortofolio = Portofolio()
        myPortofolio.addMoney("USD", 10000)
        myPortofolio.addCurrency(Money())
        reader.savePorofolio(myPortofolio)
    else:
        myPortofolio.cleanup()
        myPortofolio.startWatch()

    return myPortofolio

answer = 0
debugflag = False

while answer != 7:
    print("Menu")
    print("=====")
    print("1. One currency analyze")
    print("2. List currencies")
    print("3. Find a currency")
    print("4. Find greatest change")
    print("8. See history file")
    print("9. View Portofolio")
    print("12. Edit Portofolio")
    print("10. Make an investment")
    print("11. Monitor")
    print("5. Debug ON")
    print("6. Debug OFF")
    print("7. Exit")

    answer = int(input("Choose your answer:"))

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

    if answer == 9:
        portofolio = initializePortofolio()
        PortofolioViewer(portofolio).view()

    if answer == 12:
        portofolio = initializePortofolio()
        PortofolioEditor(portofolio, debugflag).edit()

    if answer == 10:
        portofolio = initializePortofolio()
        InvestmentManger(debugflag, portofolio).makeInvestment()

    if answer == 11:
        portofolio = initializePortofolio()
        InvestmentMonitor(debugflag, portofolio).monitor()


print("By by")