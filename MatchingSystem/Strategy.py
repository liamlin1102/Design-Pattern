from abc import ABC,abstractmethod
from Imdividual import Imdividual
class Strategy(ABC):
    def __init__(self)->None:
        return 
    @abstractmethod
    def MatchStrategy(self,imdividuals:[Imdividual])->Imdividual:
        return
    @abstractmethod
    def MatchRerveseStrategy(self,imdividuals:[Imdividual])->Imdividual:
        return