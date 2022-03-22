#1261번 알고스팟

class solution:
    
    def __init__(self):
        self.N,self.M = map(int,input().split())
        self.room = [list(map(int, input())) for _ in range(self.M)]


    def countOne(self,x:int, y:int) -> int:        
        if x+1 < self.N or y+1 < self.M:
            
            if x+1 >= self.N:
                return self.room[y][x] + self.countOne(x,y+1)
            elif y+1 >= self.M:
                return self.room[y][x] + self.countOne(x+1,y)
            else:
                return self.room[y][x] + min(self.countOne(x+1,y), self.countOne(x,y+1))
        else:
            return self.room[y][x]
        
        
s = solution()

print(s.countOne(0,0))