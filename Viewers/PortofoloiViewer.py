class PortofolioViewer:

    def __init__(self, portofolio):
        self.portofolio = portofolio


    def view(self):
        print("This is current portofolio: ")
        print("============================")
        print("Money:")
        print("======")
        for item in self.portofolio.currentBalance:
            print(item)

        print("Invesments:")
        print("===========")
        for item in self.portofolio.investments:
            print(item)