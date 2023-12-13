from Player import Player
from Card import Card
from Hand import Hand
from Suits import Suits #是否可以
from Ranks import Ranks #是否可以
from ExchangePlayer import ExchangePlayer

class HumanPlayer(Player):
    def __init__(self,name:str,point:int,exchange:bool,hand:Hand,exchangePlayer:ExchangePlayer)->None:
        self.name = name
        self.point = point
        self.exchange = exchange
        self.hand = hand
        self.exchangePlayer = exchangePlayer

    def NameHimSelf(self)->None:
        self.name = input("使用者取名: ")

    def Show(self)->Card:
        count = 1
        print("目前持有的卡牌:\n")
        for card in self.hand.cards:
            print(f"{count}. {Suits(card.suit).name} {Ranks(card.rank).name}\n")
            count+=1
        try:
            pickNum = int(input("請選擇要出哪張牌\n"))
        except:
            print("請輸入數字\n")
            return self.Show()
        if (pickNum<1 or pickNum>self.hand.count):
            print("請輸入顯示的數字\n")
            return self.Show()
        self.hand.count-=1
        return self.hand.cards.pop(pickNum-1)
    
    def ExchangeDecide(self)->bool:
        agreeExchange= input("是否要交換別人的牌,要的話請輸入Y 或是 y\n")
        return agreeExchange=="Y" or agreeExchange=="y"
    
    def ExchangeChoose(self,players:list[Player])->Player:
        print("玩家對應編號\n")
        for index in range(len(players)):
            if index==0:
                continue
            player = players[index]
            print(f"{index}. {player.name}")
        try:
            pickNum = int(input("請選擇玩家\n"))
        except ValueError:
            print("你輸入的不是數字\n")
            return self.ExchangeHands()
        if (pickNum<1 or pickNum>len(players)):
            print("請輸入顯示的數字\n")
            return self.ExchangeHands()  
        return players[pickNum]
