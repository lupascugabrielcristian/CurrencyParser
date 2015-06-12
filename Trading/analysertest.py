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
        print("Current value: " + str(value))

        delta = abs(initialPrice - value)
        if delta > 0.01:
            print(str(delta)) # log
            print("Delta exceeded")
            sleep(15)
            return

analyze()