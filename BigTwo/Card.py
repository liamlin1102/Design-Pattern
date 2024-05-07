from __future__ import annotations
from Suit import Suit
from Rank import Rank
from typing import List 

class Card():  
    def __init__(self,suit:Suit=None,rank:Rank=None)->None:
        self.rank = rank
        self.suit = suit