from ShowDown import ShowDown
from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer
from Card import Card
from ..Deck import Deck 
from ..Hand import Hand
class Main:
    def __init__(self):
        return 
    def main(self):
        showDown = ShowDown(Deck(Card()),
                            [HumanPlayer("",Hand(0,[]),None),
                            AIPlayer("",Hand(0,[]),None),
                            AIPlayer("",Hand(0,[]),None),
                            AIPlayer("",Hand(0,[]),None)])
        showDown.GameStart()

main = Main()
main.main()z