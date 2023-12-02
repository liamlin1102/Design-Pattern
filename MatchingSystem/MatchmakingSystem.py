from Imdividual import Imdividual
from Strategy import Strategy

class MatchmakingSystem:
    def __init__(self,imdividual1,imdividual2,imdividual3,imdividual4,imdividual5,imdividual6)->None:
        self.imdividuals = [imdividual1,imdividual2,imdividual3,imdividual4,imdividual5,imdividual6]

    def MakeHabbits(self) -> set[str]:
        _habbits = ["釣魚","逛街","運動","玩遊戲","看電影","吃美食","閱讀","旅遊","寫作","烹飪"]
        habbitSet=set()
        print("請輸入下方你要的興趣，輸入格式為 數字+^隔開+數字")
        for index in range(_habbits):
            print(f"{index+1}. {_habbits[index]}")
        indexList = input().split("^")
        for index in indexList:
            habbitSet.add(_habbits[int(index)])  
        return habbitSet 
    
    def MakeYourself(self)->Imdividual:
        coard=[]
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
        habbits = self.MakeHabbits()
        coard[0] = input("請輸入您所在的X座標\n")
        coard[1] = input("請輸入您所在的Y座標\n")
        return Imdividual(int(id),gender,int(age),intro,habbits,coard,Strategy())

    def Run(self)->None:
        user = self.MakeYourself()
        strategy = input("請選擇策略:\n1. 距離\n2. 興趣\n")
        while(int(strategy)>2 or int(strategy)<1):
            strategy = input("請輸入數字1或是2來選擇策略\n")
        rerverse = input("請選擇正向還是反向:\n1. 正向\n2. 反向\n")
        while(int(rerverse)>2 or int(rerverse)<1):
            rerverse = input("請輸入數字1或是2來選擇策略方向\n")        
        if rerverse==1:
            return user.MatchStrategy(self.imdividuals)     
        else:
            return user.MatchReverseStrategy(self.imdividuals)                
    





        

