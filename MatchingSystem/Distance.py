from Imdividual import Imdividual
from Strategy import Strategy
import sys,math
class Distance(Strategy) :
    def MatchStrategy(self,user:Imdividual,imdividuals:list[Imdividual])->Imdividual:
        minDistance = sys.maxsize
        matchUser = None
        for otherUser in imdividuals:
            otherUserDistance = math.sqrt(abs(otherUser.coord[0]-user.coord[0])+abs(otherUser.coord[1]-user.coord[1]))
            if(otherUserDistance<minDistance):
                matchUser = otherUser
                minDistance = otherUserDistance
            if(otherUserDistance==minDistance and otherUser.id<matchUser.id):
                matchUser = otherUser                
        return matchUser
        
    def MatchRerveseStrategy(self,user:Imdividual,imdividuals:[Imdividual])->Imdividual:
        maxDistance = 0
        matchUser = None
        for otherUser in imdividuals:
            otherUserDistance = math.sqrt(abs(otherUser.coord[0]-user.coord[0])+abs(otherUser.coord[1]-user.coord[1]))
            if(otherUserDistance>minDistance):
                matchUser = otherUser
                minDistance = otherUserDistance
            if(otherUserDistance==minDistance and otherUser.id<matchUser.id):
                matchUser = otherUser   
        return matchUser