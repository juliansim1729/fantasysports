from math import comb

class BinomCalc:
    # using for method storage mainly

    # ends up as a bernoulli method for only 1 'game'/match played

    def __init__(self):
        pass

    def firstToNBinom(self, pWin, tmWins, tmLosses): # calculates bernoulli probabilities when stopping when one team hits a specific amount of games won
        return comb(tmWins + tmLosses - 1, min(tmWins, tmLosses)) * (pWin ** tmWins) * ((1 - pWin) ** tmLosses)

    def bestOfNBinom(self, pWin, tmWins, tmLosses):
        # symmetric, so can just use tmWins in coeff
        return comb(tmWins + tmLosses, tmWins) * (pWin ** tmWins) * ((1 - pWin) ** tmLosses)
