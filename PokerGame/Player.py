from __future__ import annotations
import abc
from Card import Card
from Hand import Hand
from typing import List
from ExchangePlayer import ExchangePlayer



class Player(abc.ABC):

    def __init__(self,name:str,point:int,exchange:bool,hand:Hand,exchangePlayer:ExchangePlayer,nextPlayer:Player)->None:
        self.name = name
        self.point = point
        self.exchange = exchange
        self.hand = hand
        self.exchangePlayer = exchangePlayer
        self.nextPlayer = nextPlayer
    

    @abc.abstractmethod
    def NameHimSelf(self)->None:
        return 

    def TakeTurn(self)->Player:
        return self.nextPlayer

    def ExchangeHands(self,players:List[Player])->bool:
        if(self.ExchangeDecide()):
            player = self.ExchangeChoose(players)
            self.exchangePlayer = ExchangePlayer(3,player)
            player.hand,self.hand = self.hand,player.hand
            self.exchange = False
            print(f"{self.name}選擇使用了換牌，換牌對象為{self.exchangePlayer.player.name}\n")

    @abc.abstractmethod
    def ExchangeDecide(self)->bool:
        return
    
    @abc.abstractmethod
    def ExchangeChoose(self,players:list[Player])->None:
        return
    
    def ReturnHands(self)->None:
        print(f"時間到了，{self.name}的牌要還給{self.exchangePlayer}")
        self.hand,self.exchangePlayer.player.hand = self.exchangePlayer.player.hand,self.hand
        return 
    
    @abc.abstractmethod
    def Show(self)->Card:
        return
    