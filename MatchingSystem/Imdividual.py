from Strategy import Strategy

class Imdividual():
    def __init__(self,id:int,gender:str,age:int,intro:str,habbits:set[str],coord:list[int],strategy:Strategy)->None:
        self.id = id
        self.gender = gender
        self.age =age
        self.intro = intro
        self.habbits = habbits
        self.coord = coord 
        self.strategy = strategy
    def MatchStrategy(self,imdividuals:list["Imdividual"])->"Imdividual":
        return self.strategy.MatchStrategy(self,imdividuals)
    def MatchReverseStrategy(self,imdividuals:list["Imdividual"])->"Imdividual": 
        return self.strategy.MatchRerveseStrategy(self,imdividuals)