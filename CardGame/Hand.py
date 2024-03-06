from Card import Card
from abc import ABC
from typing import List

class Hand(ABC):
    def __init__(self,count:int,cards:List[Card]):
        self.cards = cards
    
    