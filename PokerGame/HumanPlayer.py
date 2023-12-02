import Player
import Cards
import OtherPlayerHands

class HumanPlayer(Player.Player):
    def NameHimSelf(self)->None:
        self.name = input("使用者取名: ")

    def Show(self)->Cards.Cards:
        count = 1
        print("目前持有的卡牌:\n")
        for hand in self.hands:
            print(f"{count}. {hand.suit} {hand.rank}\n")
            count+=1
        try:
            pickNum = int(input("請選擇要出哪張牌\n"))
        except:
            print("請輸入數字\n")
            return self.Show()
        if (pickNum<1 or pickNum>len(self.hands)):
            print("請輸入顯示的數字\n")
            return self.Show()
        return self.hands.pop(pickNum-1)
    
    def ExchangeHands(self,players:list[Player.Player])->None:
        agreeExchange= input("是否要交換別人的牌,要的話請輸入Y 或是 y\n")
        if (agreeExchange!="Y" and agreeExchange!="y"):
            return
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
        player = players[pickNum] 
        self.otherPlayerHands = OtherPlayerHands.OtherPlayerHands(3,player)
        player.hands,self.hands = self.hands,player.hands
        self.exchange = False
        print(f"{self.name}選擇使用了換牌，換牌對象為{self.otherPlayerHands.otherPlayer.name}\n")
        return 
