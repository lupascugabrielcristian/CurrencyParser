class PredicterResult:

    OPERATION_SELL = "sell"
    OPERATION_BUY = "buy"
    OPERATION_NONE = "none"

    def __init__(self, readingInterval):
        self.comment = ""
        self.comment2 = ""
        self.readingInterval = readingInterval
        self.operation = "none"
        self.tendency  = ""
        self.lastDerivative = 1
