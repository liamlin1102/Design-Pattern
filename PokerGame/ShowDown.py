from Player import Player
from Deck import Deck
from typing import Tuple,List
from Suits import Suits
from Ranks import Ranks
from Card import Card #這裡是否能import card
class ShowDown:
    def __init__(self,deck:Deck,player:Player,ai1:Player,ai2:Player,ai3:Player):       
        self.deck = deck
        self.player = player
        self.ai1 = ai1
        self.ai2 = ai2
        self.ai3 = ai3
        self.playerList : List[Player] = [self.player,self.ai1,self.ai2,self.ai3] #這麼做好嗎
    def Run(self)->None:
        self.PrepareTime()
        self.DrawCardTime()
        self.ShowCardTime()

    def PrepareTime(self)->None:
        count=0
        self.deck.MakeDeck()
        for player in self.playerList:
            if count==0:
                player.NameHimSelf()
                count+=1
            else:
                player.NameHimSelf(count)
        self.deck.Shuffle()
                
    def DrawCardTime(self)->None:
        while(len(self.deck.cards)!=0):
            for player in self.playerList:
                self.deck.DrawCard(player)

    def ShowCardTime(self)->None:
        cardList=[]
        winner = None
        for round in range(0,13):
            for player in self.playerList:
                if (player.exchangePlayer):
                    player.exchangePlayer.round-=1
                    if(player.exchangePlayer.round==0):
                        player.ReturnHands()
                if (player.exchange):
                    player.ExchangeHands(self.playerList)
                if player.hand.count>0:
                    cardList.append((player,player.Show()))
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