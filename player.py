from gestures import GESTURES

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.gestures = GESTURES
    
    def select_gesture(self):
        pass

    def win_round(self):
        self.score += 1

    def set_name(self):
        pass

    def validate_and_set_name(self, players, player_num):
        is_unique = False
        while not is_unique:
            self.set_name(player_num)
            for player in players:
                if player == self: continue
                elif player.name == self.name: is_unique = False
                else: is_unique = True