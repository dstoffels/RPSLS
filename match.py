import time
from helpers import clear_console, validate_int_input
from player import Player
from round import Round

class Match:
    def __init__(self):
        self.players: list[Player] = []
        self.score_to_win = 0
        self.round_num = 1
        self.num_players = 2
        self.match_winner = None
        
    def run(self):
        self.setup_match()
        while not self.match_winner:
            self.display_round()
            Round(self.players.copy()).play()
            self.display_player_scores()
            self.match_winner = self.has_winner()
            self.round_num += 1
        self.declare_winner(self.match_winner)
        input('\nPress return to continue...')
        
    def has_winner(self):
        for player in self.players:
            if player.rounds_won == self.score_to_win: return player
        return None

    def setup_match(self):
        clear_console()
        print("Match setup: ")
        self.choose_score_to_win()
        self.set_player_names()
        
    def set_player_names(self):
        i = 1
        for player in self.players:
            player.validate_and_set_name(self.players, i)
            i += 1

    def declare_winner(self, player):
        print(f"\n******{player.name.upper()} WINS!!******")

    def init_players(self, player_type):
        for i in range(self.num_players):
            self.players.append(player_type())

    def choose_score_to_win(self):
        prompt = "How many victories necessary to win the game? "
        while self.score_to_win <1:
            self.score_to_win = validate_int_input(prompt)
            prompt = "Score to win must be greater than 0."

    def display_round(self):
        clear_console()
        print(f"\nRound {self.round_num}")
        time.sleep(1)
    
    def display_player_scores(self):
        print("\nScoreboard:\n")
        for player in self.players:
            print(f"{player.name}: {player.rounds_won}")
        time.sleep(3)

    