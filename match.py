from random import choice
from player import Player

class Match:
    def __init__(self):
        self.players: list[Player] = []
        self.score_to_win = 2
        self.current_round = 1
        self.num_players = 2
        
    def run(self):
        self.setup_match()
        while not self.has_winner():
            self.round()
        
    def has_winner(self):
        for player in self.players:
            if player.score == self.score_to_win:
                self.declare_winner(player)
                return True
        return False

    def setup_match(self):
        self.set_player_names()
        
    def set_player_names(self):
        i = 1
        for player in self.players:
            player.validate_and_set_name(self.players, i)
            #print(player.name)
            i += 1

    def round(self):
        self.select_gestures()
        self.display_gestures()
        self.compare_gestures_and_award_point ()
        # display score

    def display_gestures(self):
        for player in self.players:
            player.display_gesture()

    def select_gestures(self):
        for player in self.players:
            player.select_gesture()

    def declare_winner(self, player): #good place to implement slow crawl
        print(f"Winner: {player.name}")

    def init_players(self, player_type):
        for i in range(self.num_players):
            self.players.append(player_type())

    def compare_gestures_and_award_point(self):
        if len(self.players) == 2:
            player1, player2 = self.players
            if player1.has_winning_gesture(player2.current_gesture): player1.score_point(player2.current_gesture)
            elif player2.has_winning_gesture(player1.current_gesture): player2.score_point(player1.current_gesture)
            else: print("It's a tie!")
        else: pass ## run logic for 3+ players (see below)

    #     for player in self.players:
    #         for compared_player in self.players:
    #             if player != compared_player:
    #                 self.check_for_point_scored(player, compared_player)
    #     self.current_round += 1

    # def print_point_scored(self, winner, loser):
    #     print(f"{winner.gesture} beats {loser.gesture}! {winner.name} wins this round!")

    # def check_for_tie(self, player, compared_player):
    #     if player.gesture == compared_player.gesture:
    #         print(f"Both {player.name} and {compared_player.name} played {player.gesture}! It's a tie!")
    #         return True
    #     else:
    #         return False

    # def check_for_point_scored(self, player, compared_player):
    #     if not self.check_for_tie(player, compared_player):
    #         if compared_player.gesture in player.gestures[player.gesture]:
    #             winner = player
    #             loser = compared_player
    #         else:
    #             winner = compared_player
    #             loser = player
    #         self.print_point_scored(winner, loser)
    #         winner.score_point()


