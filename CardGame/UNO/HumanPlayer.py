from Player import Player
from Card import Card
from Hand import Hand

class HumanPlayer(Player):

    def Show(self,cards)->Card:
        count = 1
        print("目前持有的卡牌:\n")
        for pair in cards:
            print(f"{count}. {pair[1].color} {(pair[1].number)}\n")
            count+=1
        try:
            pickNum = int(input("請選擇要出哪張牌\n"))
        except:
            print("請輸入數字\n")
            return self.Show(cards)
        if (pickNum<1 or pickNum>len(self.cards)):
            print("請輸入顯示的數字\n")
            return self.Show()
        self.hand.count-=1
        return self.hand.cards.pop(cards[pickNum-1][0])
    