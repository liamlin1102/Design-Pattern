from __future__ import annotations
from Suits import Suits
from Ranks import Ranks
from typing import List 
from ..Card import Card
from ..Deck import Deck

class Card(Card):  
    def __init__(self,suit:Suits=None,rank:Ranks=None)->None:
        self.rank = rank
        self.suit = suit
    
    def MakeDeck(self):
        deck = Deck()
        for _rank in range(len(Ranks)):
            for _suit in range(len(Suits)):
                deck.append(Card(_suit,_rank))
        return deck
        
