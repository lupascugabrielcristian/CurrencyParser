import sys

sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency'])

from Trading.InvestmentManager import InvestmentManger
from Trading.DataReaderWriter import DataReaderWriter
from Trading.Money import Money
from Trading.Portofolio import Portofolio
from Viewers.PortofoloiViewer import PortofolioViewer
from Parser.HistoryViewer import HistoryViewer
from Parser.VariationFinder import VariationFinder
from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency


def initializePortofolio():
    reader = DataReaderWriter()
    myPortofolio = reader.getPortofolio()
    if myPortofolio is None:
        myPortofolio = Portofolio()
        myPortofolio.add("USD", 10000)
        myPortofolio.addMoney(Money())
        reader.savePorofolio(myPortofolio)

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
    print("9. Portofolio")
    print("10. Make an investment")
    print("5. Debug ON")
    print("6. Debug OFF")
    print("7. Exit")

    answer = int(input("Choose your answer:"))

    if answer == 1:
        OneCurrency(debugflag).run()

    if answer == 2:
        AllCurrencyList().run()

    if answer == 3:
        AllCurrencyList().filter()

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

    if answer == 10:
        portofolio = initializePortofolio()
        InvestmentManger(debugflag).makeInvestment()


print("By by")