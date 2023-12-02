import abc
import Cards
class Player(abc.ABC):
    def __init__(self)->None:
        self.name=""
        self.hand=0
        self.point=0
        self.nextPlayer = None
        self.exchange=True
        self.hands = []
        self.otherPlayerHands = None
    @abc.abstractmethod
    def NameHimSelf(self)->None:
        return 

    def TakesTurn(self,player:"Player")->"Player":
        self.nextPlayer = player
        return player
    
    @abc.abstractmethod
    def ExchangeHands(self,player:"Player")->bool:
        return 

    def ReturnHands(self)->None:
        print(f"時間到了，{self.name}的牌要還給{self.otherPlayerHands.otherPlayer.name}")
        self.hands,self.otherPlayerHands.otherPlayer.hands =self.otherPlayerHands.otherPlayer.hands,self.hands
        return 

    @abc.abstractmethod
    def Show(self)->Cards.Cards:
        return