import sched
import time
from Grafic.AutoSizeGraphic import AutoGraphic
from Parser.GraphicPointsBuilder import GraphicPointsBuilder
from Parser.InfoDesigner import InfoDesigner

from Parser.Method_2_Parser import Method_2_Parser


designer = InfoDesigner()

indexOfCurrency = int( input("Currency index: ") )
repeats = int( input("Repeats: ") )


designer.currency_index = indexOfCurrency
designer.repeats = repeats

designer.run()
