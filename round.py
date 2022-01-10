import time
from helpers import append_line

from player import Player

class Round:
    def __init__(self, players):
        self.players: list[Player] = players
        self.num_init_players = len(players)
        self.high_score: int = 0

    def play(self) -> list[Player]:
        while len(self.players) > 1:
            self.reset_player_points()
            self.select_gestures()
            self.display_gestures()
            self.compare_gestures_and_award_points()
            self.set_high_score()
            self.eliminate_losers()
            self.display_results()
        return self.players

    def display_gestures(self):
        print("")
        for player in self.players:
            player.display_gesture()
            time.sleep(0.5)

    def select_gestures(self):
        for player in self.players:
            player.select_gesture()

    def compare_gestures_and_award_points(self):
        for player in self.players:
            for other_player in self.players:
                if player.has_winning_gesture(other_player.current_gesture): 
                    player.score_point()
                elif other_player.has_winning_gesture(player.current_gesture):
                    player.deduct_point()
        time.sleep(0.75)

    def set_high_score(self):
        for player in self.players:
            if player.points > self.high_score:
                self.high_score = player.points

    def eliminate_losers(self):
        winners = []
        for player in self.players:
            if player.points == self.high_score:
                winners.append(player)
        self.players = winners

    def reset_player_points(self):
        for player in self.players:
            player.reset_points()
        self.high_score = 0

    def display_results(self):
        if len(self.players) == self.num_init_players:
            print(f"It's a {len(self.players)}-way tie! Next round...")
            self.players.clear()
        elif len(self.players) > 1:
            self.display_elimination_round()
        else:
            winner = self.players[0]
            winner.win_round()
            print(f'{winner.name} wins the round!')

    def display_elimination_round(self):
        append_line(f"We have a {len(self.players)}-way tie! ")
        for player in self.players:
            if player == self.players[-2]: append_line(player.name, ' and ')
            elif player == self.players[-1]: append_line(player.name, ' ')
            else: append_line(player.name, ', ')
        print('move onto an elimination round!')
        self.num_init_players = len(self.players)

