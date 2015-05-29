from Trading.DataReaderWriter import DataReaderWriter


class PortofolioEditor:

    def __init__(self, portofolio, debugflag):
        self.debugflag = debugflag
        self.portofolio = portofolio
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

        print("To delete money write: m[index]. To delete investment write i[index]. To exit write e:")
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
            index = int(userinput[1:])
            try:
                self.portofolio.currentBalance.pop(index)
                DataReaderWriter().savePorofolio(self.portofolio)
                print("Money at index " + str(index) + " was removed")
            except IndexError:
                print("Wrong index")
        elif userinput[0] == 'i':
            index = int(userinput[1:])
            try:
                self.portofolio.investments.pop(index)
                DataReaderWriter().savePorofolio(self.portofolio)
                print("Investment at index " + str(index) + " was removed")
            except IndexError:
                print("Wrong index")



