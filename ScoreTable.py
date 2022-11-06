class ScoreTable:
    playersTable = {}
    
    def addPlayer(self,player):
        self.playersTable[player.getName()] = 0

    def addScore(self,player,amount):
        self.playersTable[player.getName()] += amount
    
    def __str__(self):
        keys = self.playersTable.keys()
        result = ""
        for key in keys:
            result = result + (f"{key}:{self.playersTable[key]},")    
        return result











  