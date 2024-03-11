from typing import Tuple,List
from Player import Player
from ..Deck import Deck
from Card import Card 
from ..CardGame import CardGame
class UNO(CardGame):  
    def DrawCardTime(self,players:List[Player])->None:
        for round in range(0,4):
            for player in players:
                self.deck.DrawCard(player)
                
    def GameProcess(self,player:Player)->None:
        cardList=[]
        winner = None
        for round in range(0,13):
            for count in range(len(self.players)):
                if player.hand.count>0:
                    cardList.append((player,player.Show()))
                player = player.TakeTurn()
            winner = self.CompareCard(winner,cardList)
        print(f"遊戲結束，勝利者是{winner.name}，他總計獲得了{winner.point}分")
            
