from Imdividual import Imdividual
from Strategy import Strategy
from MatchmakingSystem import MatchmakingSystem
class Main:
    def Run()->None:
        system = MatchmakingSystem(
            Imdividual(1,"FEMALE",20,"測試資料1",["釣魚","逛街","運動","玩遊戲","看電影","吃美食","閱讀","旅遊","寫作","烹飪"],[106,58],Strategy()),
            Imdividual(2,"FEMALE",27,"測試資料2",["釣魚","烹飪"],[17,12],Strategy()),  
            Imdividual(3,"FEMALE",34,"測試資料3",["釣魚","烹飪"],[46,58],Strategy()),            
            Imdividual(4,"MALE",19,"測試資料4",["釣魚","逛街"],[8,10],Strategy()),    
            Imdividual(5,"FEMALE",26,"測試資料5",["釣魚","逛街","運動","玩遊戲"],[58,27],Strategy()),    
            Imdividual(6,"MALE",52,"測試資料6",["釣魚","逛街","運動","玩遊戲","看電影","吃美食","閱讀","旅遊","寫作","烹飪"],[36,49],Strategy())    
        )
        system.Run()
Main.Run()