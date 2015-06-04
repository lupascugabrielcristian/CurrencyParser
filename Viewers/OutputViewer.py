import threading
import tkinter as tk

class OutputViewer(tk.Frame):

    def __init__(self, debugflag):
        tk.Frame.__init__(self)
        self.debugflag = debugflag
        self.mainContainer = tk.Frame()
        self.mainContainer.grid(row=0, rowspan=2, column=0, columnspan=1)
        self.viewText = None
        self.createWidgets()
        windowThread = threading.Thread(target=self._showWindow)
        windowThread.setDaemon(True)
        windowThread.start()


    def createWidgets(self):
        scrollbar = tk.Scrollbar()
        viewText = tk.Text(self.mainContainer, bg='black', fg='white', height=50)
        viewText.grid(row=0, column=0, rowspan=1)
        viewText.config(yscrollcommand=scrollbar.set)

        self.viewText = viewText

    def showText(self, text):
        self.viewText.insert(0.0, text)

    def _showWindow(self):
        self.mainloop()