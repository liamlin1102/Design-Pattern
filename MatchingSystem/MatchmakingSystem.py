from Imdividual import Imdividual
from Distance import Distance
from Habbit import Habbit
from typing import List
from Coord import Coord
from Strategy import Strategy

class MatchmakingSystem:
    def __init__(self,strategy:Strategy)->None:
        self.strategy = strategy
        return 
    
    def Run(self)->Imdividual:
        return self.Match(self.MakeYourself())
         
    def Makehabbits(self) -> set[str]:
        _habbits = ["釣魚","逛街","運動","玩遊戲","看電影","吃美食","閱讀","旅遊","寫作","烹飪"]
        habbitSet=set()
        print("請輸入下方你要的興趣，輸入格式為 數字數字數字")
        for index in range(len(_habbits)):
            print(f"{index+1}. {_habbits[index]}")
        indexList = input()
        for index in indexList:
            habbitSet.add(_habbits[int(index)-1])  
        return habbitSet 
    
    def MakeYourself(self)->Imdividual:
        id = input("請輸入自己的ID:\n")
        gender = input("請選擇性別:\n1. 生理男\n2. 生理女\n")
        while(int(gender)>2 or int(gender)<1):
            gender = input("請輸入數字1或是2來選擇,請選擇性別:\n1. 生理男\n2. 生理女\n")
        gender = gender==1 if "MALE" else "FEMALE" 
        age = input("請輸入年紀")
        while(int(age)<17):
            age = input("年紀不可低於18歲，請再次輸入")
        intro = input("請輸入自我介紹")
        while(len(intro)>200 or len(intro)<1):
            intro = input("自傳長度不可為空白或是超過兩百次")
        habbits = self.Makehabbits()
        x = int(input("請輸入您所在的X座標\n"))
        y = int(input("請輸入您所在的Y座標\n"))
        coord = Coord(x,y)
        return Imdividual(id,gender,age,intro,habbits,coord)
    
    def Match(self,imdividual:Imdividual):
        matchList = self.strategy.MatchStrategy(imdividual,[Imdividual(1,"FEMALE",20,"測試資料1",set(["釣魚","逛街","運動","玩遊戲","看電影","吃美食","閱讀","旅遊","寫作","烹飪"]),Coord(106,58)),
            Imdividual(2,"FEMALE",27,"測試資料2",set(["釣魚","烹飪"]),Coord(17,12)),  
            Imdividual(3,"FEMALE",34,"測試資料3",set(["釣魚","烹飪"]),Coord(46,58)),            
            Imdividual(4,"MALE",19,"測試資料4",set(["釣魚","逛街"]),Coord(8,10)),    
            Imdividual(5,"FEMALE",26,"測試資料5",set(["釣魚","逛街","運動","玩遊戲"]),Coord(58,27)),    
            Imdividual(6,"MALE",52,"測試資料6",set(["釣魚","逛街","運動","玩遊戲","看電影","吃美食","閱讀","旅遊","寫作","烹飪"]),Coord(36,49))])
        return matchList[-1][0]