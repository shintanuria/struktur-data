class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    
    def addScore(self):
        self.score += 1
    
    def minScore(self):
        self.score -= 1

    def name(self):
        return self.name
    
    def score(self):
        return self.score