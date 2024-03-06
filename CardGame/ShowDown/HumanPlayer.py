from Player import Player
from Card import Card
from Hand import Hand
from Suits import Suits 
from Ranks import Ranks 

class HumanPlayer(Player):

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
    