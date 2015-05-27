class PortofolioViewer:

    def __init__(self, portofolio):
        self.portofolio = portofolio


    def view(self):
        print("This is current portofolio: ")
        print("============================")
        for item in self.portofolio.currentBalance:
            print(item)