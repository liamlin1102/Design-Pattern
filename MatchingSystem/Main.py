from Imdividual import Imdividual
from Distance import Distance
from Habbit import Habbit
from Reverse import Reverse 
from MatchmakingSystem import MatchmakingSystem
class Main:
    def __init__(self)->None:
        return 
    
    def Match(self)->None:
        strategy = input("請選擇策略:\n1. 距離\n2. 興趣\n")
        while(int(strategy)>2 or int(strategy)<1):
            strategy = input("請輸入數字1或是2來選擇策略\n")
        rerverse = input("請選擇正向還是反向:\n1. 正向\n2. 反向\n")
        while(int(rerverse)>2 or int(rerverse)<1):
            rerverse = input("請輸入數字1或是2來選擇策略方向\n")        
        if rerverse=="1":
            if strategy=="1":
                target = MatchmakingSystem(Distance()).Run()
                print(f"使用距離正向策略，最相近的玩家ID為 {target.id}，座標為{target.coord}")
            else:
                target = MatchmakingSystem(Habbit()).Run()
                print(f"使用興趣正向策略，最多共同興趣的玩家ID為 {target.id}，興趣數量為{len(target.habbits)}")
        else:
            if strategy=="1":
                target = MatchmakingSystem(Reverse(Distance())).Run()
                print(f"使用距離反向策略，最遙遠的玩家ID為 {target.id}，座標為{target.coord}")                
            else:
                target = MatchmakingSystem(Reverse(Habbit())).Run()   
                print(f"使用興趣反向策略，最少共同興趣的玩家ID為 {target.id}，興趣數量為{len(target.habbits)}")                
         

Main().Match()