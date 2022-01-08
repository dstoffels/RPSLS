from gestures import FORFEIT
from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.names = ['Bob', 'Scott', 'Lizzy', 'James', 'Tina', 'Nala']
    
    def select_gesture(self):
        gesture_list = list(self.gestures)
        gesture_list.remove(FORFEIT)
        self.current_gesture = random.choice(gesture_list)

    def set_name(self, player_num):
        self.name = random.choice(self.names)
        
#change random choice to random int and just do length - 1
#add an if statement after selecting the gesture to make it do it again if it chooses forfeit
#or just create a second gesture list for the computer that doesn't include the forfeit option
#or just include something during the computer's select_gesture function that removes forfeit from the list