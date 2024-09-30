class Command:
    sign = None
    # arguments = [] #for later implementation

    def __init__(self, sign, arguments):
        self.sign = sign
        self.arguments = arguments

    def checkCall(self, call):
        return self.sign == call