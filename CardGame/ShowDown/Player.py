from __future__ import annotations

import abc
from ..Player import Player as IPlayer
from ..Card import Card
from ..Hand import Hand
from typing import List

class Player(IPlayer):
    
    def TakeTurn(self,showCardList)->Player:
        if(self.showCardCondition()):
            showCardList.append(self.Show())
        return self.nextPlayer

    def showCardCondition(self)->bool:
        return len(self.hand)==0
    
    @abc.abstractmethod
    def Show(self)->Card:
        return