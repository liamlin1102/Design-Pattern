from typing import List
from Imdividual import Imdividual
from Strategy import Strategy
class Reverse(Strategy):
    def __init__(self,strategy : Strategy):
        self.strategy = strategy
        
    def MatchStrategy(self, user: Imdividual, imdividuals: List[Imdividual]) -> List[List[Imdividual]]:
        matchList = self.strategy.MatchStrategy(user,imdividuals)
        matchList.reverse()
        return matchList
    