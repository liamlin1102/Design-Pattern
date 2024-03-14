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
                answer[position] = Hero("H")
            elif pick==1:
                answer[position] = Water("W")
            elif pick==2:
                answer[position] = Fire("F")
        return answer
    
    def moveSprite(self,startPosition:int,endPosition:int):
        startSprite = self.sprites[startPosition]
        if(startSprite==None):
            return False
        if(startSprite.collision(self.sprites[endPosition])):
            self.sprites[endPosition] = startSprite
        return True