import random

from events import Events

from Analysers.PredicterResult import PredicterResult
from Grafic.AutoSizeGraphic import AutoGraphic
from Parser.GraphicPointsBuilder import GraphicPointsBuilder
from Utils.OrderedReadingsArray import OrderedReadingsArray


class Predicter:

    UP_TENDENCY ="UP"
    DOWN_TENDENCY = "DOWN"
    NO_TENDENCY = "LEVEL"

    def __init__(self, debugflag, readingInterval, initialPice=0):
        self.debugflag = debugflag
        self.valuesSoFar = OrderedReadingsArray()
        self.initialPrice = initialPice
        self.notDecisiveReadings = 0
        self.readingInterval = readingInterval
        self.sellEvents = Events()
        self.buyEvents = Events()
        self.increasses = 0
        self.decreases = 0
        self.tendency = ""


    def addData(self, newValue, timeInterval):
        result = PredicterResult(self.readingInterval)

        if self.valuesSoFar.size() == 0:
            self.valuesSoFar.add(newValue, timeInterval)
            return result

        self.checkTendency(newValue)
        self.checkForMinimum(newValue, result)
        self.checkForMaximum(newValue, result)

        self.valuesSoFar.add(newValue, timeInterval)

        self.checkDerivative(result)
        self.__calculateGoodReadinngsDensity()

        result.readingInterval =  self.readingInterval
        result.tendency = self.tendency

        # self.showGraphic()

        return result

    def __calculateGoodReadinngsDensity(self):
        if self.notDecisiveReadings > 10:
            self.notDecisiveReadings = 0
            self.readingInterval += 5
            print(" ++ Reading interval increased to %d seconds"%self.readingInterval)


    def checkTendency(self, newValue):
        if newValue > self.valuesSoFar.lastAddedValue:
            self.increasses += 1
        if newValue < self.valuesSoFar.lastAddedValue:
            self.decreases += 1

        if self.decreases > self.increasses:
            self.tendency = self.DOWN_TENDENCY
        elif self.decreases < self.increasses:
            self.tendency = self.UP_TENDENCY
        else: self.tendency = self.NO_TENDENCY


    def checkForMinimum(self, newValue, result):
        minValue = self.valuesSoFar.getMinValue()

        if newValue < minValue:
            self.notDecisiveReadings = 0
            result.comment  = " ** Min Value found: %.4f"%newValue
            if newValue == minValue:
                self.sellEvents.on_change()
                result.comment = "  * Reached bottom: %.4f"%newValue
        else:
            self.notDecisiveReadings += 1


    def checkForMaximum(self, newValue, result):
        maxValue = self.valuesSoFar.getMaxValue()

        if newValue > maxValue:
            self.notDecisiveReadings = 0
            result.comment  = " ^^ Max Value found: %.4f"%newValue
            if newValue == maxValue:
                self.sellEvents.on_change()
                result.comment = "  ^ Reached top: %.4f"%newValue
        else:
            self.notDecisiveReadings += 1

    def checkOperation(self, result):
        result.comment2 = "I%d/D%d"%(self.increasses, self.decreases)

        if self.decreases - self.increasses > 5:
            result.operation = PredicterResult.OPERATION_SELL

        elif self.increasses - self.decreases > 5:
            result.operation = PredicterResult.OPERATION_BUY


    def checkDerivative(self, result):
        minimumDer = 0.2
        result.lastDerivative = self.valuesSoFar.lastDerivative

        if abs(result.lastDerivative) < minimumDer and result.lastDerivative < 0:
            result.operation = PredicterResult.OPERATION_BUY
            self.showGraphic()
        elif abs(result.lastDerivative) < minimumDer and result.lastDerivative > 0:
            result.operation = PredicterResult.OPERATION_SELL
            self.showGraphic()

    def showGraphic(self):
        points = GraphicPointsBuilder(None).builFromValue(self.valuesSoFar.unOrderedReadings)
        AutoGraphic(points)
