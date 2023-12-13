from __future__ import annotations
from Suits import Suits
from Ranks import Ranks
from typing import List 
class Card:
    def __init__(self,suit:Suits,rank:Ranks)->None:
        self.rank = rank
        self.suit = suit

        
