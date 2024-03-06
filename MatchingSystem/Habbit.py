from Imdividual import Imdividual
from Strategy import Strategy
from typing import List
import heapq 
class Habbit(Strategy) :
    def MatchStrategy(self,user:Imdividual,imdividuals:List[Imdividual])->List[List[Imdividual]]:
        count =0
        matchUserList = []
        dictUser = {}
        strategySet = user.habbits
        habbitSet = set()
        for otherUser in imdividuals:
            for habbit in otherUser.habbits:
                if(habbit in strategySet):
                    count+=1
            if count not in dictUser:   
                dictUser[count] = []
                habbitSet.add(count)
            dictUser[count].append(otherUser)           
            count= 0
        sorted(habbitSet)
        for index in habbitSet:
            matchUserList.append(dictUser[index])
        return matchUserList        