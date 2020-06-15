class FantasyLeague:

    def __init__(self):
        self.openStatus = True

        self.teamList = []

        self.ratingSystem = "ELO"

    # accessible to tier 0 admins

    def open(self):
        self.openStatus = True

    def close(self):
        self.openStatus = False

    def submit_results(self, t1code, t2code, t1score, t2score):
        if self.ratingSystem == "ELO":
            pass
        elif self.ratingSystem == "ELOLinear":
            pass
        elif self.ratingSystem == "GLICKO":
            pass
        elif self.ratingSystem == "DWZ":
            pass

    # accessible to tier 1 admins
    def add_team(self, teamName, ticker, value):
        tm = new Team(teamName, ticker, value)
        self.teamList.append(tm)

    def setRatingSystem(self, rs):
        self.ratingSystem = rs
