from ShowDown.Player import Player
from Card import Card
import random

class AIPlayer(Player):

    def Show(self,cards)->Card:
        self.hand.count-=1        
        return self.hand.cards.pop(cards[random.randint(0,len(cards))][0])
