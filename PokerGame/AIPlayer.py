from Player import Player
from Card import Card
import random
from Hand import Hand
from ExchangePlayer import ExchangePlayer

class AIPlayer(Player):
    def __init__(self,name:str,point:int,exchange:bool,hand:Hand,exchangePlayer:ExchangePlayer)->None:
        self.name = name
        self.point = point
        self.exchange = exchange
        self.hand = hand
        self.exchangePlayer = exchangePlayer

    def NameHimSelf(self,number)->None:
        self.name = f"AI{number}"
        return 
    
    def Show(self)->Card:
        self.hand.count-=1
        return self.hand.cards.pop(random.randint(0,self.hand.count))

    def ExchangeDecide(self) -> bool:
        return random.randint(1,3)==1

    def ExchangeChoose(self,players:list[Player])->Player:     
        moveMyselfList = players[:]
        moveMyselfList.remove(self)
        pickNum = random.randint(0,len(moveMyselfList)-1)
        return moveMyselfList[pickNum] 
        
        