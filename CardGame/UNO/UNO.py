from typing import Tuple,List
from CardGame.Player import Player
from Player import Player
from ..Deck import Deck
from Platform import Platform
from Card import Card 
from ..CardGame import CardGame

class UNO(CardGame):  

    def __init__(self, deck: Deck, players: List[Player],platForm:Platform):
        super().__init__(deck, players)
        self.platForm = platForm

    def DrawCardTime(self,players:List[Player])->None:
        for round in range(0,4):
            for player in players:
                self.deck.DrawCard(player)

    def GameProcess(self,player:Player)->None:
        cardList=[]
        winner = None
        while(True):
            nextPlayer,isFinish= player.TakeTurn(self.deck,self.platForm)
            if(isFinish):
                print(f"遊戲結束，勝利者是{player.name}")
                return 
            player = nextPlayer

            
