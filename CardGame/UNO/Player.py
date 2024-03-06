from __future__ import annotations

import abc
from Platform import Platform
from ..Player import Player as IPlayer
from ..Card import Card
from ..Hand import Hand
from typing import List

class Player(IPlayer):

    def showCardCondition(self,platForm,cards)->bool:
        lastCard = platForm[-1]
        cards= []
        for index,card in enumerate(self.hand):
            if card.color==lastCard.color or card.number==lastCard.number:
                cards.append([index,card])
        return len(cards)>0

    @abc.abstractmethod
    def Show(self,cards)->Card:
        return
    