from Player import Player
from Deck import Deck
from typing import List
from abc import ABC,abstractmethod
class CardGame(ABC):

    def __init__(self,deck:Deck,players:List[Player]):       
        self.deck = deck
        self.players = players

    def GameStart(self)->None:
        self.SetingGame()
        self.DrawCardTime(self.players[0])
        self.GameProcess()

    def SetingGame(self)->None:
        count=0
        for player in self.players:
            player.NameHimSelf()
            self.players[count-1].nextPlayer = player
            count+=1
        self.deck.Shuffle()
    
    @abstractmethod
    def DrawCardTime(self,player:Player)->None:
        return
    
    @abstractmethod
    def GameProcess(self)->None:
        return 