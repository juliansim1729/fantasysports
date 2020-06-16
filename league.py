import re

class FantasyLeague:

    def __init__(self):
        self.openStatus = True

        self.teamList = []
        self.userList = []
        self.banList = []

        self.configNames = ["RatingSystem", "RatingSensitivity", "MatchOnlyResults", "FlatBuyTax", "PercentBuyTax", "FlatSellTax", "PercentSellTax", \
                            "PoolSystem", "AllowCashTransfer", "Dividends", "DividendPct", "BansAreWipes", "SuperAdmin"]
        self.configVals = ["ELO", 18, False, 0, 0, 0, 0, False, False, False, 1, True, False]
        self.configDesc = ["The rating system used to find and evaluate price changes depending on performance. [ELO, ELOLIN, GLICKO, DWZ]", \
                           "The value which indicates how sensitive the rating system is to recent events. [Positive Number]", \
                           "Results are entered as match scores (e.g. 1-0 or 0-1), instead of game scores (e.g. 4-2) [True/False]", \
                           "The flat amount taxed for every transaction where stocks are bought. [Positive Number]", \
                           "The percent amount of each transaction taxed when stocks are bought. [Percent 0 - 100]", \
                           "The flat amount taxed for every transaction where stocks are sold. [Positive Number]", \
                           "The percent amount of each transaction taxed when stocks are sold. [Percent 0 - 100]", \
                           "Taxes go into a pool, which gets evenly distributed amongst those that bought stocks of match winners. [True/False]", \
                           "Allow players to transfer cash between each other. [True/False]", \
                           "Stocks pay out dividends (manually), accessible to Tier 1 Admins. [True/False]", \
                           "The percentage of the stock price paid out in dividends to stockholders. [Percent 0 - 100]", \
                           "Bans wipe player stock data, while retaining their information on the banList. [True/False]", \
                           "Allow Tier 2 Admins to manually edit user information and team information. [True/False]"]
        self.configTypes = ["rs", "pos", "bin", "pos", "pct", "pos", "pct", "bin", "bin", "bin", "pct", "bin", "bin"]

        # implementation check: 0

    # accessible to tier 0 users

    def initPlayer(self, id, tag, liquidCash, adminTier = 0):
        newUser = User(id, tag, liquidCash, adminTier)
        if newUser not in self.banList:
            self.userList.append(User(id, tag, liquidCash, adminTier))

    # accessible to tier 1 admins, tier checks done in FantasyBot.py

    def open(self):
        self.openStatus = True

    def close(self):
        self.openStatus = False

    def submit_results(self, t1code, t2code, t1score, t2score):
        if self.configVals[0] == "ELO":
            pass
        elif self.configVals[0] == "ELOLIN":
            pass
        elif self.configVals[0] == "GLICKO":
            pass
        elif self.configVals[0] == "DWZ":
            pass

    # accessible to tier 2 admins, tier checks done in FantasyBot.py
    def add_team(self, teamName, ticker, value):
        tm = new Team(teamName, ticker, value)
        self.teamList.append(tm)

    def setRatingSystem(self, rs):
        self.ratingSystem = rs

    def accessConfigMenu(self, enableDesc = False):
        builtOutput = "Welcome to the bot settings menu. The following options and their current values are listed below."
        for i in range(len(self.configNames)):
            builtOutput += "\n{0}. {1:-20s}: {2:-7s}".format(i + 1, self.configNames[i], self.configVals[i])
            if enableDesc:
                builtOutput += " - {0}".format(self.configDesc[i])
        return builtOutput

    def updateConfigs(self, ind, newVal):
        if self.configTypes[ind] == "rs":
            if newVal.upper() in ["ELO", "ELOLIN", "GLICKO", "DWZ"]:
                self.configVals[ind] = newVal.upper()
            else:
                raise InvalidValueSubmissionError
        elif self.configTypes[ind] == "pos":
            if newVal.isdigit():
                self.configVals[ind] = int(newVal)
            else:
                raise InvalidValueSubmissionError
        elif self.configTypes[ind] == "pct":
            if newVal[-1] == '%': # remove ending percent sign if there
                newVal = newVal[:-1]
            if newVal.isdigit():
                self.configVals[ind] = int(newVal)
            else:
                raise InvalidValueSubmissionError
        elif self.configTypes[ind] == "bin":
            if newVal.upper() in ["TRUE", "T"]:
                self.configVals[ind] = True
            elif newVal.upper() in ["FALSE", "F"]:
                self.configVals[ind] = False
            else:
                raise InvalidValueSubmissionError

    def changeConfigSetting(self, configNo, newVal):
        if configNo.isdigit():
            ind = int(configNo) - 1
            self.updateConfigs(ind, newVal)
        else:
            try:
                ind = (names.upper() for names in self.configNames).index(newVal.upper())
                self.updateConfigs(ind, newVal)
            except ValueError:
                raise InvalidValueSubmissionError
