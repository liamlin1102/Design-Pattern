from abc import ABC,abstractmethod
from typing import List 
from Card import Card
from Player import Player
import random 

class Deck(ABC):
    def __init__(self,card:Card)->None:
        self.card = card
        self.cards = card.MakeDeck()
        
    def Shuffle(self)->None:
        tempCard=[]
        for cardNum in range(len(self.cards)-1,-1,-1):
            index = random.randint(0,cardNum)
            tempCard.append(self.cards[index])
            del self.cards[index]
        self.cards = tempCard
    
    def DrawCard(self,player:Player)->None:
        if(len(self.cards)>=1):
            player.hand.cards.append(self.cards[0])
            player.hand.count += 1
            self.cards.pop(0)
        else:
            print("Deck is empty.")
        
