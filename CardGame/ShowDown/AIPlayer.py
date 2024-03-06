from ShowDown.Player import Player
from Card import Card
from typing import List
import random
from Hand import Hand

class AIPlayer(Player):
    
    def Show(self)->Card:
        self.hand.count-=1
        return self.hand.cards.pop(random.randint(0,self.hand.count))

