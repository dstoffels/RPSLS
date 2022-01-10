from helpers import clear_console, pause, validate_int_input
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
#TODO refactor 
    def init_players(self):    
        for i in range(self.num_players):
            if i % 2 == 0:
                self.players.append(Computer())
            else:
                self.players.append(Human())

class Mixed_Multiplayer(Match):
    def __init__(self):
        super().__init__()
        self.init_players()

    def init_players(self):     
        self.init_humans()
        self.init_computers()
        self.num_players = self.human_num + self.computer_num

    def init_humans(self):
        self.human_num = validate_int_input("How many humans are playing? ")
        for i in range(self.human_num):
            self.players.append(Human())

    def init_computers(self):    
        self.computer_num = validate_int_input("How many computer players would you like? ")
        for i in range(self.computer_num):
            self.players.append(Computer())
    