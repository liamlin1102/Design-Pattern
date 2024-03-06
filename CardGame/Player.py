from __future__ import annotations
import abc
from Hand import Hand
from Card import Card
from typing import List

class Player(abc.ABC):

    def __init__(self,name:str,hand:Hand,nextPlayer:Player)->None:
        self.name = name
        self.hand = hand
        self.nextPlayer = nextPlayer
    
    def NameHimSelf(self)->None:
        self.name = input("請在下方輸入該玩家的名字")
        return 

    def TakeTurn(self,showCardList)->Player:
        if(self.showCardCondition()):
            showCardList.append(self.Show())
        return self.nextPlayer
    
    @abc.abstractmethod
    def showCardCondition(self)->bool:
        return 

    @abc.abstractmethod
    def Show(self)->Card:
        return
    