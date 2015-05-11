from Parser.InfoDesigner import InfoDesigner


designer = InfoDesigner()

indexOfCurrency = int( input("Currency index: ") )
repeats = int( input("Repeats: ") )


designer.currency_index = indexOfCurrency
designer.repeats = repeats

designer.run()
