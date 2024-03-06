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

    @abstractmethod
    def SetingGame(self)->None:
        return
    
    @abstractmethod
    def DrawCardTime(self,player:Player)->None:
        return
    
    @abstractmethod
    def GameProcess(self)->None:
        return 