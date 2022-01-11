from match import Match
from computer import Computer
from human import Human

from helpers import validate_int_input

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
    