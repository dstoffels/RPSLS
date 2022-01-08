from gestures import GESTURES

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.gestures = GESTURES
        self.current_gesture = ""
    
    def select_gesture(self):
        pass

    def score_point(self, opponent_gesture):
        print(f'{self.current_gesture} beats {opponent_gesture}\nPoint to {self.name}!')
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

    def has_winning_gesture(self, opponent_gesture):
        return True if opponent_gesture in self.gestures[self.current_gesture] else False

    def display_gesture(self):
        print(f"{self.name} chooses {self.current_gesture}")
    