from UNO import UNO
from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer
from Deck import Deck 
from Hand import Hand
from Card import Card
from Platform import Platform

class Main:
    def __init__(self):
        return 
    def main(self):
        uno = UNO(Deck(Card()),
                            [HumanPlayer("",Hand(0,[]),None),
                            AIPlayer("",Hand(0,[]),None),
                            AIPlayer("",Hand(0,[]),None),
                            AIPlayer("",Hand(0,[]),None)],Platform())
        uno.GameStart()

main = Main()
main.main()