import HumanPlayer;
import AIPlayer;
import Deck;

deck = Deck.Deck()
player = HumanPlayer.HumanPlayer()
winner = AIPlayer.AIPlayer()
plyayerList = []
cardList=[]
_suits = ["club","diamond","heart","spades"]
_ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suitsMap = {}
ranksMap = {}
playerNum = 4
rounds = 13

def Run()->None:
    player.NameHimSelf()
    plyayerList.append(player)
    count = 1   
    MakeAIPlayer()
    GameSetting()
    GameStart()

def MakeAIPlayer()->None:
    global player
    for count in range(1,playerNum+1):
        if(count!=4):
            newPlayer = AIPlayer.AIPlayer()
            newPlayer.NameHimSelf(count)
            plyayerList.append(newPlayer)
            player.TakesTurn(newPlayer)       
        else:
            player.TakesTurn(plyayerList[0])
        player = player.nextPlayer

def GameSetting()->None:
    global player
    for num in range(len(_suits)):
        suitsMap[_suits[num]] = num
    for num in range(len(_ranks)):
        ranksMap[_ranks[num]] = num
    deck.Shuffle()
    while(len(deck.cards)!=0):
        deck.DrawCard(player)
        player = player.nextPlayer

def GameStart()->None:
    global player
    for round in range(0,rounds):
        for playerCount in range(playerNum):
            if (player.otherPlayerHands):
                player.otherPlayerHands.round-=1
                if(player.otherPlayerHands.round==0):
                    player.ReturnHands()
            if (player.exchange):
                player.ExchangeHands(plyayerList)
            if len(player.hands)>0:
                cardList.append((player,player.Show()))
            player = player.nextPlayer
        CompareCard()
    print(f"遊戲結束，勝利者是{winner.name}，他總計獲得了{winner.point}分")
        

def CompareCard()->None:
    global winner
    if len(cardList)>0:
        maxCardTuple =None
        for cardTuple in cardList:
            print(f"{cardTuple[0].name}的牌是  {cardTuple[1].suit}{cardTuple[1].rank}")
            if (not maxCardTuple):
                maxCardTuple = cardTuple
            else :
                if (ranksMap[maxCardTuple[1].rank]<ranksMap[cardTuple[1].rank]):maxCardTuple = cardTuple
                if (ranksMap[maxCardTuple[1].rank]==ranksMap[cardTuple[1].rank] and suitsMap[maxCardTuple[1].suit]>suitsMap[cardTuple[1].suit]):maxCardTuple = cardTuple
        maxCardTuple[0].point +=1
        if(maxCardTuple[0].point>winner.point):
            winner = maxCardTuple[0]   
        cardList.clear()
        print(f"這局獲勝的是{maxCardTuple[0].name}")                 
Run()