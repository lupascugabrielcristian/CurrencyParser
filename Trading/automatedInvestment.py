import sys

sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency'])

from Analysers.Predicter import Predicter
from time import sleep, gmtime, strftime
from Parser.Currency import Currency
from Parser.ValueParser import ValueParser

index = int(sys.argv[1])
name = sys.argv[2]
initialInterval = 10

parser = ValueParser(False)
predicter = Predicter(False, initialInterval)
sellEvents = predicter.sellEvents
buyEvents = predicter.buyEvents

def announceToSell():
    print("====\nSell!\n====")

def announceToBuy():
    print("====\nBuy!\n=====")

sellEvents.on_change += announceToSell
buyEvents.on_change += announceToBuy

currency = Currency(name)

def analyse():
    print("Analysing automated investment from: " + currency.fromName + ", to: " + currency.toName)

    while 1:
        interval = printDetails()
        sleep(interval)

def printDetails():
    currentTime = strftime("%H:%M:%S", gmtime())
    value = parser.getOnlineValueForCurrencyIndex(index)
    predicterResult = predicter.addData(value)

    print(str(currentTime) + '\t' + str(value) + "\t" + predicterResult[1])
    return predicterResult[0]




analyse()