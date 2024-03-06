from ..Deck import Deck
class Platform:
    
    def __init__(self,deck):
        self.deck = deck

    def PutCardToDeck(self,deck):
        self.deck.Shuffle()
        for card in self.deck:
            deck.append(card)
        return deck
    