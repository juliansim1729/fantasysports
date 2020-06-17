class Stock:

    def __init__(self, teamName, ticker, value):
        self.teamName = teamName
        self.ticker = ticker
        self.value = value

    def editTeamName(self, newName):
        self.teamName = newName

    def editTicker(self, newTick):
        self.ticker = newTicker

    def editPrice(self, delta):
        self.value += delta
