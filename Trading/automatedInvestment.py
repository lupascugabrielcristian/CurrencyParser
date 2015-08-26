import sys

sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte_personale/Python/project_currency'])

from Analysers.PredicterResult import PredicterResult
from Analysers.Predicter import Predicter
from time import sleep, gmtime, strftime
from Trading.Currency import Currency
from Parser.ValueParser import ValueParser
import time

index = int(sys.argv[1])
name = sys.argv[2]
initialInterval = 5

beginingOfTime = time.time()
parser = ValueParser(False)
predicter = Predicter(False, initialInterval)
sellEvents = predicter.sellEvents
buyEvents = predicter.buyEvents

def announceToSell():
    print("====\nSell!\n====")

def announceToBuy():
    print("====\nBuy!\n=====")

# sellEvents.on_change += announceToSell
# buyEvents.on_change += announceToBuy

currency = Currency(name)

def analyse():
    print("Analysing automated investment from: " + currency.fromName + ", to: " + currency.toName)
    printHeader()

    while 1:
        value = parser.getOnlineValueForCurrencyIndex(index)
        timeInterval = time.time() - beginingOfTime
        predicterResult = predicter.addData(value, timeInterval)
        printDetails(value, predicterResult)
        sleep(predicterResult.readingInterval)

def printHeader():
    print("Time\t\tValue\t\tDerivata\t\tOperation\tTendency\tComment")

def printDetails(value, predicterResult):
    currentTime = strftime("%H:%M:%S", gmtime())
    operation = "\t\t" + predicterResult.operation
    comment = "\t\t\t" + str(predicterResult.comment)
    tendency = "\t\t\t" + str(predicterResult.tendency)
    derivata = "\t\t\t%.4f"%predicterResult.lastDerivative

    if PredicterResult.OPERATION_NONE in predicterResult.operation:
        operation = "\t\t---"

    print(str(currentTime) + '\t' + str(value) + derivata + operation + tendency + comment)


analyse()