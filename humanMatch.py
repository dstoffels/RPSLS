from helpers import clear_console
from match import Match
from human import Human

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