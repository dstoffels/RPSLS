from gestures import GESTURES
from helpers import validate_index, validate_int_input
from player import Player

class User(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        self.offer_gestures()
        gesture_list = list(self.gestures)
        gesture_index = validate_index("Enter the number of the gesture you would like to use: ", gesture_list)
        gesture = gesture_list[gesture_index]
        return gesture
        
    def set_name(self):
        self.name = input("What is your name? ")

    def offer_gestures(self):
        i = 1
        for item in self.gestures.keys():
            print(f"{i}. {item}")
            i += 1

