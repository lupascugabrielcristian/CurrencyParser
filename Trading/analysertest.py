from time import sleep
import sys
from Parser.ValueParser import ValueParser

index = int(sys.argv[1])
initialPrice = int(sys.argv[2])
name = sys.argv[3]

def testProcess():
    while 1:
        print("Anlysing ...")
        sleep(2)


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
            print(str(delta)) # log
            print("Delta exceeded")
            sleep(15)
            return

analyze()