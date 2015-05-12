import sys
sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency'])

from Parser.InfoDesigner import InfoDesigner

designer = InfoDesigner()

delay = int( input("Time between reads: "))
indexOfCurrency = int( input("Currency index: ") )
repeats = int( input("Repeats: ") )


designer.currency_index = indexOfCurrency
designer.repeats = repeats
designer.interval = delay

designer.run()

