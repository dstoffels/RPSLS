from gestures import FORFEIT
from helpers import validate_index, validate_yes_or_no
from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        self.offer_gestures()
        gesture_list = list(self.gestures)
        gesture_index = validate_index(f"{self.name}, enter the number of the gesture you would like to use: ", gesture_list)
        self.current_gesture = gesture_list[gesture_index]
        self.did_forfeit_match()

       
    def set_name(self, player_num):
        self.name = input(f'Enter a name for player {player_num}: ')

    def offer_gestures(self):
        i = 1
        for item in self.gestures.keys():
            print(f"{i}. {item}")
            i += 1
        
    def did_forfeit_match(self):
        if self.current_gesture == FORFEIT:
            if validate_yes_or_no('Are you sure you want to quit? '):
                exit() #TODO figure out how to return to main menu from match.py
            else: 
                self.select_gesture()

