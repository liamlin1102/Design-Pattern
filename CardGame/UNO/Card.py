from __future__ import annotations
from ..Deck import Deck
from ..Card import Card as ICard

class Card(ICard):
    def __init__(self,color=None,number=None)->None:
        self.color = color
        self.number = number
    
    def MakeDeck(self) -> Deck:
        colors = ["BLUE","GREEN","YELLOW","RED"]
        deck = Deck()
        for color in colors:
            for num in range(0,10):
                deck.append(Card(color,num))
        return deck
        
