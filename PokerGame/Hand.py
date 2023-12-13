from Card import Card
from typing import List
class Hand:
    def __init__(self,count:int,cards:List[Card]):
        self.count = count
        self.cards = cards
    
    