from CardGame.CardGame import ShowDown
from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer
from Deck import Deck 
from Hand import Hand

class Main:
    def __init__(self):
        return 
    def main(self):
        showDown = ShowDown(Deck([]),
                            [HumanPlayer("",0,True,Hand(0,[]),None,None),
                            AIPlayer("",0,True,Hand(0,[]),None,None),
                            AIPlayer("",0,True,Hand(0,[]),None,None),
                            AIPlayer("",0,True,Hand(0,[]),None,None)])
        showDown.GameStart()

main = Main()
main.main()