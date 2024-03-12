from typing import Tuple,List
from Player import Player
from ..Deck import Deck
from Suits import Suits
from Ranks import Ranks
from Card import Card 
from ..CardGame import CardGame

class ShowDown(CardGame):        
    def DrawCardTime(self)->None:
        player = self.players[0]
        while(len(self.deck.cards)!=0):
            self.deck.DrawCard(player)
            player = player.nextPlayer

    def GameProcess(self,player:Player)->None:
        cardList=[]
        winner = None
        for round in range(0,13):
            for player in self.players:
                player = player.TakeTurn(cardList)
            winner = self.CompareCard(winner,cardList)
        print(f"遊戲結束，勝利者是{winner.name}，他總計獲得了{winner.point}分")
            
    def CompareCard(self,winner:Player,cardList : List[Tuple[Player,Card]])->Player:
        if len(cardList)>0:
            maxCardTuple =None
            for cardTuple in cardList:
                print(f"{cardTuple[0].name}的牌是  {Suits(cardTuple[1].suit).name} {Ranks(cardTuple[1].rank).name}")
                if (not maxCardTuple):
                    maxCardTuple = cardTuple
                else :
                    if (maxCardTuple[1].rank<cardTuple[1].rank):maxCardTuple = cardTuple
                    if (maxCardTuple[1].rank==cardTuple[1].rank and maxCardTuple[1].suit>cardTuple[1].suit):maxCardTuple = cardTuple
            maxCardTuple[0].point +=1
            if(not winner):
                winner = maxCardTuple[0]
            elif(maxCardTuple[0].point>winner.point):
                winner = maxCardTuple[0]   
            cardList.clear()
            print(f"這局獲勝的是{maxCardTuple[0].name}") 
        return winner