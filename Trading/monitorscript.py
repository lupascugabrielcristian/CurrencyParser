from time import sleep
import sys
from Parser.ValueParser import ValueParser

repeats = int(sys.argv[1])
index = int(sys.argv[2])
initialPrice = int(sys.argv[3])

previousValue = 0


def monitor():
    global  repeats
    print("Monitoring")
    while True:
        if repeats == 0:
            end = input("stop or number of repeats: ")
            if "stop" in end:
                break
            if end.isnumeric():
                repeats = int(end)

        displayValues()
        sleep(10)
        repeats -= 1
    print("Monitoring is stoped")


def displayValues():
    parser = ValueParser(False)
    currentValue = parser.getOnlineValueForCurrencyIndex(index)

    if previousValue > 0:
        if currentValue > previousValue:
            mediumStatus = "RISING"
        elif currentValue < previousValue:
            mediumStatus = "LOWERING"
        else: mediumStatus = "STEADY"
    else: mediumStatus = "--"

    if currentValue > initialPrice:
        status = "UP"
    elif currentValue < initialPrice:
        status = "DOWN"
    else: status = "SAME"
    print("Current value = {}, {}, {}".format(currentValue, status, mediumStatus))

monitor()