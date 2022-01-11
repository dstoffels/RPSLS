from match import Match
from human import Human
from computer import Computer

class Solo_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players()

    def init_players(self):    
        self.players.append(Human())
        self.players.append(Computer())