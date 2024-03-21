from Hero import Hero
from Fire import Fire
from Water import Water
import random 

class World:
    def __init__(self,length:int=30):
        self.length = length
        self.sprites = self.makeSprite()

    def makeSprite(self):
        allPosition = [i for i in range(self.length)]
        lifePosition = random.shuffle(allPosition)[:10]
        answer = [None]*self.length
        for position in lifePosition:
            pick = random.randint(0,3)
            if pick==0:
                answer[position] = Hero("H",position)
            elif pick==1:
                answer[position] = Water("W",position)
            elif pick==2:
                answer[position] = Fire("F",position)
        return answer
    
    def moveSprite(self,startPosition:int,endPosition:int):
        startSprite = self.sprites[startPosition]
        remove = False
        if not startSprite:
            print("起始位置無目標")
        elif not endPosition or startSprite.collision(self.sprites[endPosition],remove):
              self.sprites[endPosition],self.sprites[startPosition] = startSprite,None  
              if(remove): self.removeSprite(startSprite)
        return 
    
    def removeSprite(self,position:int):
        self.sprites[position]=None