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