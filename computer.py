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

    def set_name(self, prompt):
        self.name = random.choice(self.names)
        
        
