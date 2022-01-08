from match import Match
from computer import Computer
from user import User

class Computer_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players(Computer)
    
class Human_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players(User)

class Solo_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players()

    #right now mixed players switch back and forth between human and computer equally
    #TODO make it so users can specify how many computer/user players they want
    def init_players(self):    
        for i in range(self.num_players):
            if i % 2 == 0:
                self.players.append(Computer())
            else:
                self.players.append(User())