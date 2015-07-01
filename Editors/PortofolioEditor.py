from Trading.DataReaderWriter import DataReaderWriter


class PortofolioEditor:

    def __init__(self, portofolio, investmentManager, debugflag):
        self.debugflag = debugflag
        self.portofolio = portofolio
        self.investmentManager = investmentManager
        self.exitFlag = False


    def edit(self):
        while True:
            if self.exitFlag:
                break
            userinput = self.show()
            self.findItemToRemove(userinput)

    def show(self):
        print("Ccurrent portofolio: ")
        print("============================")
        print("Money:")
        for index in range(len(self.portofolio.currentBalance)):
            print("{}. {}".format(index, self.portofolio.currentBalance[index]))

        print("Invesments:")
        for index in range(len(self.portofolio.investments)):
            print("{}. {}".format(index, self.portofolio.investments[index]))

        print("To delete money write: m[index]. To delete investment write i[index]. "
              "To sell an investment: s[index]. To exit write e:")
        userinput = input("=>")
        return userinput


    def findItemToRemove(self, userinput):
        if len(userinput) < 1:
            print("Wrong input")
            return

        if userinput[0] == 'e':
            self.exitFlag = True
            return
        elif userinput[0] == 'm':
            self.removeMoney(userinput)
        elif userinput[0] == 'i':
            self.removeInvestment(userinput)
        elif userinput[0] == 's':
            self.sellInvestment(userinput)


    def removeMoney(self, userinput):
        index = int(userinput[1:])
        try:
            self.portofolio.currentBalance.pop(index)
            DataReaderWriter().savePorofolio(self.portofolio)
            print("Money at index " + str(index) + " was removed")
        except IndexError:
            print("Wrong command")

    def removeInvestment(self, userinput):
        index = int(userinput[1:])
        try:
            self.portofolio.investments.pop(index)
            DataReaderWriter().savePorofolio(self.portofolio)
            print("Investment at index " + str(index) + " was removed")
        except IndexError:
            print("Wrong command")

    def sellInvestment(self, userinput):
        index = int(userinput[1:])
        try:
            investment = self.portofolio.investments[index]
            self.investmentManager.closeInvestment(investment)

            print("Investment at index " + str(index) + " was sold")
        except IndexError:
            print("Wrong command")

