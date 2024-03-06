from Imdividual import Imdividual
from Strategy import Strategy
from typing import List
import sys,math

class Distance(Strategy) :
    def MatchStrategy(self,user:Imdividual,imdividuals:List[Imdividual])->List[List[Imdividual]]:
        matchUserList = []
        dictUser = {}
        strategySet = set()
        for otherUser in imdividuals:
            otherUserDistance = math.sqrt(abs(otherUser.coord.x-user.coord.x)+abs(otherUser.coord.y-user.coord.y))
            if otherUserDistance not in dictUser:
                dictUser[otherUserDistance] = []
                strategySet.add(otherUserDistance)
            dictUser[otherUserDistance].append(otherUser)        
        sorted(strategySet)  
        for distance in strategySet:
            matchUserList.append(dictUser[distance])
        return matchUserList     
