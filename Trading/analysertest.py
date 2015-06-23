from time import sleep
import sys
from Parser.ValueParser import ValueParser

index = int(sys.argv[1])
initialPrice = float(sys.argv[2])
name = sys.argv[3]

def analyze():
    print("Analizing " + name)
    print("Inital value: " + str(initialPrice))
    parser = ValueParser(False)

    while 1:
        sleep(2)
        value = parser.getOnlineValueForCurrencyIndex(index)

        delta = abs(initialPrice - value)

        if value > initialPrice:
            side = "UP"
        elif value < initialPrice:
            side = "DOWN"
        else: side = "SAME"

        print("Current Val: %.4f, D: %.4f - %s" %(value, delta, side))

        if delta > 0.3:
            print("Diff: " + str(delta)) # log
            print("Delta exceeded(Max = 0.3)")
            print("Window will close in 20 seconds")
            sleep(20)
            return

analyze()