import os
import sys

from player import Player

from helpers import clear_console, validate_index, validate_yes_or_no
from gestures import FORFEIT

class Human(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        self.offer_gesture_options()
        gesture_list = list(self.gestures) # extract list of keys (str) from gestures dictionary
        gesture_index = validate_index(f"\n{self.name}, pick your move! ", gesture_list)
        self.current_gesture = gesture_list[gesture_index]
        self.did_forfeit_match()
        clear_console()
       
    def set_name(self, prompt):
        self.name = input(prompt)

    def offer_gesture_options(self):
        i = 1
        print("")
        for item in self.gestures.keys():
            print(f"{i}. {item}")
            i += 1
        
    def did_forfeit_match(self):
        if self.current_gesture == FORFEIT:
            if validate_yes_or_no('Are you sure you want to return to the main menu? '):
                os.execl(sys.executable, sys.executable)
            else: 
                self.select_gesture()