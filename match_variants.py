from helpers import clear_console, pause
from match import Match
from computer import Computer
from human import Human

class Computer_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players(Computer)
    
class Human_Match(Match):
    def __init__(self):
        super().__init__()
        self.init_players(Human)
    
    def select_gestures(self):
        for player in self.players:
            player.select_gesture()
            self.switch_player()

    def switch_player(self):
        clear_console()
        input('Press return to continue...')
        clear_console()

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
                self.players.append(Human())