from match import Match
from computer import Computer

class Computer_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players(Computer)