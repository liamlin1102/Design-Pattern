from __future__ import annotations
from abc import ABC,abstractmethod
from typing import TYPE_CHECKING
from typing import List
if TYPE_CHECKING:
    from Imdividual import Imdividual

class Strategy(ABC):
    def __init__(self):
        return 
    
    @abstractmethod
    def MatchStrategy(self,user:Imdividual,imdividuals:List[Imdividual])->List[List[Imdividual]]:
        return 
    