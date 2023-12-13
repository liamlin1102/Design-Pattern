from typing import List 
from Card import Card
from Player import Player
from Suits import Suits #這樣做好嗎?
from Ranks import Ranks #這樣做好嗎?
import random 

class Deck:
    def __init__(self,cards:List[Card])->None:
        self.cards = cards #這樣做好嗎?

    #這樣做好嗎?
    def MakeDeck(self)->List[Card]:
        for _rank in range(len(Ranks)):
            for _suit in range(len(Suits)):
                self.cards.append(Card(_suit,_rank))
        return self.cards    

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
        
