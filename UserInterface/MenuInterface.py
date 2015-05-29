import tkinter as tk
from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency
from Trading.DataReaderWriter import DataReaderWriter
from Trading.InvestmentsMonitor import InvestmentMonitor
from Trading.Money import Money
from Trading.Portofolio import Portofolio


class MenuInterface(tk.Frame):

    def __init__(self, debugflag):
        tk.Frame.__init__(self)
        self.debugflag = debugflag
        self.mainContainer = tk.Frame()
        self.mainContainer.grid(row=0, rowspan=5, column=0, columnspan=2)
        self.viewText = None
        self.inputText = None
        self.createWidgets()
        self.mainloop()

    def createWidgets(self):
        # Buttons
        oneCurrencyAnalyse = tk.Button(self.mainContainer, text="One CurrencyAnalyse", command= OneCurrency(self.debugflag).run)
        oneCurrencyAnalyse.grid(row=0, column=0)

        listButton = tk.Button(self.mainContainer, text="List Currencies", command=AllCurrencyList().run)
        listButton.grid(row=1, column=0)

        filterButton = tk.Button(self.mainContainer, text="Filter", command=AllCurrencyList().filter)
        filterButton.grid(row=2, column=0)

        monitorButton = tk.Button(self.mainContainer, text="Monitor", command=self.startMonitor )
        monitorButton.grid(row=3, column=0)

        testButton = tk.Button(self.mainContainer, text="Test", command=lambda: self.showText("Test") )
        testButton.grid(row=4, column=0)


        # Text widgets
        scrollbar = tk.Scrollbar()

        viewText = tk.Text(self.mainContainer, bg='black', fg='white', height=20)
        viewText.grid(row=0, column=1, rowspan=4)
        viewText.config(yscrollcommand=scrollbar.set)

        inputText = tk.Text(self.mainContainer, bg='black', fg='green', height=1, width=40)
        inputText.grid(row=4, column=1)

        self.viewText = viewText
        self.inputText = inputText


    def showText(self, text):
        self.viewText.insert(0.0, text)

    def startMonitor(self):
        reader = DataReaderWriter()
        myPortofolio = reader.getPortofolio()
        if myPortofolio is None:
            myPortofolio = Portofolio()
            myPortofolio.addMoney("USD", 10000)
            myPortofolio.addCurrency(Money())
            reader.savePorofolio(myPortofolio)
        else:
            myPortofolio.cleanup()

        InvestmentMonitor(self.debugflag, myPortofolio, self).monitor()