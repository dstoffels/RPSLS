import time
from helpers import append_line

from player import Player

class Round:
    def __init__(self, players):
        self.players: list[Player] = players
        self.num_init_players = len(players)
        self.high_score: int = 0
        self.is_in_elimination = False

    def play(self) -> list[Player]:
        while len(self.players) > 1:
            self.reset_player_points()
            self.select_gestures()
            self.display_gestures()
            self.compare_gestures_and_award_points()
            self.set_high_score()
            self.eliminate_losers()
            self.results()
        return self.players

    def select_gestures(self):
        for player in self.players:
            player.select_gesture()

    def display_gestures(self):
        print("")
        for player in self.players:
            player.display_gesture()
            time.sleep(0.5)

    # each player compares its gesture with those of the other players
    # if the player in question has the winning gesture, they earn a point, if not they lose a point, no points for the same gestures
    def compare_gestures_and_award_points(self):
        for player in self.players:
            for other_player in self.players:
                if player.has_winning_gesture(other_player.current_gesture): 
                    player.score_point()
                    self.display_comparison(player, other_player)
                elif other_player.has_winning_gesture(player.current_gesture):
                    player.deduct_point()
        time.sleep(0.75)

    # only display gesture comparison if 2 players, otherwise screen clutters
    def display_comparison(self, winner, loser): 
        if len(self.players) == 2:
            print(f'\n{winner.current_gesture} beats {loser.current_gesture}!')

    def set_high_score(self):
        for player in self.players:
            if player.points > self.high_score:
                self.high_score = player.points

    # reduce the round's players list to only winners for elimination round
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

    def results(self):
        if len(self.players) == self.num_init_players:
            if self.is_in_elimination:
                print("It's a tie, repeat elimination round...")
            else:
                print(f"\nIt's a {len(self.players)}-way tie! Next round...")
                self.players.clear()
        elif len(self.players) > 1:
            self.activate_elimination_mode()
        else:
            winner = self.players[0]
            winner.win_round()
            print(f'\n*****{winner.name} wins the round!*****')

    def activate_elimination_mode(self):
        self.display_elimination_round()
        self.num_init_players = len(self.players)
        self.is_in_elimination = True

    def display_elimination_round(self):
        append_line(f"\nWe have a {len(self.players)}-way tie! ")
        for player in self.players:
            if player == self.players[-2]: append_line(player.name, ' and ')
            elif player == self.players[-1]: append_line(player.name, ' ')
            else: append_line(player.name, ', ')
        print('move onto an elimination round!')