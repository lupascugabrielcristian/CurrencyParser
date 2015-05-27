class InvesmentManger:

    def __init__(self):
        self.investments = []

    def makeInvestment(self):
        currencyName = input("Buy currency: ")
        ammount = int(input("Ammount: "))
        duration = int(input("(Optional)Seconds: "))

        # aici sa incep sa parsez sa aflu cat costa acum
        # sa fac un fel de monitor care imi arata cat costa treptat


