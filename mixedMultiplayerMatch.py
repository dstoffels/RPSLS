import time
from match import Match
from computer import Computer
from human import Human

from helpers import validate_int_input

class Mixed_Multiplayer(Match):
    def __init__(self):
        super().__init__()
        self.init_players()
        self.pause_time = 1
    
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

    def display_player_scores(self):  #overriding the original function to display the leaderboard
        super().display_player_scores()
        self.display_leader_board()

    def display_leader_board(self):
        self.leading_scorers = []
        num = 1
        if len(self.players) > 10:
            print("\nLeaderboard:\n")
            self.set_leader_board()
            for i in range(3):
                if self.leading_scorers[i].rounds_won > 0: print(f"{num}. {self.leading_scorers[i].name}: {self.leading_scorers[i].rounds_won}")
                num += 1
            if self.leading_scorers[0].rounds_won != self.score_to_win: input("\nPress enter to continue.... ")

    def set_leader_board(self):
        for player in self.players:
                if len(self.leading_scorers) == 0:
                    self.leading_scorers.append(player)
                else:
                    self.compare_leading_scores(player)

    def compare_leading_scores(self, player):
        for i in range(len(self.leading_scorers)):
            if player.rounds_won >= self.leading_scorers[i].rounds_won:
                self.leading_scorers.insert(i, player)
                break
            elif i == len(self.leading_scorers) - 1 and len(self.leading_scorers) < 3:
                self.leading_scorers.append(player)

    