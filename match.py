from player import Player
from computer import Computer
from user import User

class Match:
    def __init__(self):
        self.players: list[Player] = []
        self.score_to_win = 2
        self.current_match = 0
        
    def run(self):
        pass

    def setup_match(self):
        self.set_player_names()
        
    def set_player_names(self):
        i = 1
        for player in self.players:
            player.validate_and_set_name(self.players, i)
            i += 1

    def round(self):
        pass

    def declare_winner(self):
        pass