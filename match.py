from player import Player

class Match:
    def __init__(self):
        self.players: list[Player] = []
        self.score_to_win = 2
        self.current_match = 0
        self.num_players = 2
        
    def run(self):
        pass

    def setup_match(self):
        self.set_player_names()
        
    def set_player_names(self):
        i = 1
        for player in self.players:
            player.validate_and_set_name(self.players, i)
            #print(player.name)
            i += 1

    def round(self):
        pass

    def declare_winner(self):
        pass

    def init_players(self, player_type):
        for i in range(self.num_players):
            self.players.append(player_type())