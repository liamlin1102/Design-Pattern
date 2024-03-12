from __future__ import annotations

import abc
from Platform import Platform
from ..Player import Player as IPlayer
from ..Card import Card
from ..Hand import Hand
from typing import List

class Player(IPlayer):
    def __init__(self, name: str, hand: Hand, nextPlayer: IPlayer,canShowCards:List[Card]) -> None:
        super().__init__(name, hand, nextPlayer)
        self.canShowCards = canShowCards

    def TakeTurn(self,deck,platForm)->Player:
        cards = []
        if(self.showCardCondition(platForm,cards)):
            self.show(cards)
        else:
            if(len(deck.cards)==0):
                platForm.PutCardToDeck(deck)
            deck.DrawCard(self)    
        return  self.nextPlayer,len(self.hand.cards)==0

    def showCardCondition(self,platForm,cards)->bool:
        lastCard = platForm[-1]
        for index,card in enumerate(self.hand):
            if card.color==lastCard.color or card.number==lastCard.number:
                cards.append([index,card])
        return len(cards)>0

    @abc.abstractmethod
    def Show(self,cards)->Card:
        return
    