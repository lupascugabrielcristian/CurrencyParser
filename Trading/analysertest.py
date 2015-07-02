from time import sleep
import sys
from Analysers.Predicter import Predicter
from Parser.ValueParser import ValueParser

index = int(sys.argv[1])
initialPrice = float(sys.argv[2])
name = sys.argv[3]

readingInterval = 2.0

def analyze():
    global readingInterval
    print("Analizing " + name)
    print("Inital value: " + str(initialPrice))
    parser = ValueParser(False)
    predicter = Predicter(False, initialPrice, readingInterval)

    while 1:
        sleep(readingInterval)
        value = parser.getOnlineValueForCurrencyIndex(index)
        diff = value - initialPrice
        delta = abs(diff)

        if value > initialPrice:
            side = "UP"
        elif value < initialPrice:
            side = "DOWN"
        else: side = "SAME"

        print("Current Val: %.4f, D: %.4f # %s" %(value, diff, side))

        readingInterval = predicter.addData(value)

        if delta > 0.3:
            print("Diff: " + str(delta)) # log
            print("Delta exceeded(Max = 0.3)")
            print("Window will close in 20 seconds")
            sleep(20)
            return

analyze()