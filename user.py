class User:

    def __init__(self, id, tag, liquidCash, adminTier):
        self.id = id
        self.tag = tag
        self.adminTier = adminTier
        self.portfolio = []
        self.liquidCash = liquidCash
        self.netWorth = liquidCash

    def __repr__(self):
        return 'fantasy.player({0}, {1}, {2}, {3}, {4}, {5})'.format(self.id, self.tag, self.portfolio, self.liquidCash, self.adminTier, self.netWorth)

    def __str__(self):
        builtOutput = 'Player {1} with ID {0} has ${2:.2f} free, with the following items in his portfolio, culminating in a final net worth of ${3:.2f}.'.format(self.id, self.tag, self.liquidCash, self.netWorth)
        for itemGrouping in portfolio:
            builtOutput += '\n\t {0}\u00d7 {1}'.format(itemGrouping[0], itemGrouping[1])
        return builtOutput

    def updateTag(self, tag):
        self.tag = tag

    def updateNetWorth(self):
        self.netWorth = self.liquidCash
        for i in self.portfolio:
            self.netWorth += i[0] * i[1].value

    def buy(self, stock, stockPrice, amount = "MAX", flatTax = 0, pctTax = 0):
        if amount == "MAX":
            amount = self.liquidCash % stockPrice
        taxPaid = flatTax + pctTax * amount * stockPrice
        if amount * stockPrice + taxPaid < liquidCash:
            raise NotEnoughLiquidCashError
        else:
            liquidCash -= amount * stockPrice + taxPaid
        if any(stock in item for item in self.portfolio): # if any amount of that stock is currently held
            for i in self.portfolio:
                if i[1] == stock:
                    i[0] += amount
        else:
            self.portfolio.append([amount, stock])
        return taxPaid

    def sell(self, stock, stockPrice, amount = "MAX", flatTax = 0, pctTax = 0):
        ind = -1
        for i in self.portfolio:
            if i[1] == stock:
                ind = i
        if ind == -1: # if not found
            raise StockNotFoundError
        if amount == "MAX":
            amount = self.portfolio[ind][0]
        if amount > self.portfolio[ind][0]: # if not enough to sell
            raise NotEnoughAssetsError
        else:
            if self.portfolio[ind][0] == amount:
                del self.portfolio[ind]
            else:
                self.portfolio[ind][0] -= amount
            taxPaid = flatTax + pctTax * amount * stockPrice
            if self.liquidCash + amount * stockPrice < taxPaid: # if taxes would cause the player's bal to go neg
                raise NotEnoughLiquidCashError
            else:
                self.liquidCash += amount * stockPrice - taxPaid
            return taxPaid

    def sendCash(self, destUser, amount):
        if self.liquidCash < amount:
            raise NotEnoughLiquidCashError
        else:
            self.liquidCash -= amount
            destUser.liquidCash += amount
