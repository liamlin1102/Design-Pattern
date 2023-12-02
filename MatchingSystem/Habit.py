from Imdividual import Imdividual
from Strategy import Strategy
class Distance(Strategy) :
    def MatchStrategy(self,user:Imdividual,imdividuals:list[Imdividual])->Imdividual:
        habbitCount = 0
        count =0
        habbitSet = set()
        matchUser = None
        for habbit in user.habbits:
            habbitSet.add(habbit)
        for otherUser in imdividuals:
            for habbit in otherUser.habbits:
                if(habbit in habbitSet):
                    count+=1
            if count>habbitCount:
                habbitCount = count
                matchUser = otherUser
            if (count==habbitCount and otherUser.id<matchUser.id):
                matchUser = otherUser
        return matchUser        
    def MatchRerveseStrategy(self,user:Imdividual,imdividuals:list[Imdividual])->Imdividual:
        habbitCount = 11
        count =0
        habbitSet = set()
        matchUser = None
        for habbit in user.habbits:
            habbitSet.add(habbit)
        for otherUser in imdividuals:
            for habbit in otherUser.habbits:
                if(habbit in habbitSet):
                    count+=1
            if count<habbitCount:
                habbitCount = count
                matchUser = otherUser
            if (count==habbitCount and otherUser.id<matchUser.id):
                matchUser = otherUser
        return matchUser      