from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
    #TODO add a list of random names for the computer to choose from
    
    def select_gesture(self):
        gesture_list = list(self.gestures)
        gesture = random.choice(gesture_list)
        return gesture

    def set_name(self):
        self.name = "Computer"
