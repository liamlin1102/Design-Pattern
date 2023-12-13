from ShowDown import ShowDown
from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer
from Deck import Deck 
from Hand import Hand

class Main:
    def __init__(self):
        return 
    def main(self):
        showDown = ShowDown(Deck([]),
                            HumanPlayer("",0,True,Hand(0,[]),None),
                            AIPlayer("",0,True,Hand(0,[]),None),
                            AIPlayer("",0,True,Hand(0,[]),None),
                            AIPlayer("",0,True,Hand(0,[]),None))
        showDown.Run()

main = Main()
main.main()