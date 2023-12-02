import Cards
import Player
import random 
class Deck:
    _suits = ["club","diamond","heart","spades"]
    _ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def __init__(self):
        self.cards = []
        for rank in self._ranks:
            for suit in self._suits:
                self.cards.append(Cards.Cards(suit,rank))
    def Shuffle(self):
        tempCards=[]
        for cardNum in range(51,-1,-1):
            index = random.randint(0,cardNum)
            tempCards.append(self.cards[index])
            del self.cards[index]
        self.cards = tempCards
    def DrawCard(self,player:Player.Player):
        player.hands.append(self.cards[0])
        player.hand += 1
        self.cards.pop(0)