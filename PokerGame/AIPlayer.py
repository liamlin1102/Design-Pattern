import Player
import Cards
import random
import OtherPlayerHands
class AIPlayer(Player.Player):
    def NameHimSelf(self,number)->None:
        self.name = f"AI{number}"
        return 
    def Show(self)->Cards.Cards:
        return self.hands.pop(random.randint(0,len(self.hands)-1))
    def ExchangeHands(self,players:list[Player.Player])->None:
        if(random.randint(1,3)==1):
            moveMyselfList = players[:]
            moveMyselfList.remove(self)
            pickNum = random.randint(0,len(moveMyselfList)-1)
            player = moveMyselfList[pickNum] 
            self.otherPlayerHands = OtherPlayerHands.OtherPlayerHands(3,player) 
            player.hands,self.hands = self.hands,player.hands
            self.exchange = False
            print(f"{self.name}選擇使用了換牌，換牌對象為{self.otherPlayerHands.otherPlayer.name}\n")
        return