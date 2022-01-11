from os import name
from gestures import FORFEIT
from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.names = ['Bob', 'Scott', 'Lizzy', 'James', 'Tina', 'Nala']
        self.suffixes = ['-Bob', '-Sue', ' Cito', ' Earl Jones', ' Turner', ' Sr.', ' Jr.', ' esq. III', ' of York']
        self.new_names= []
    
    def select_gesture(self):
        gesture_list = list(self.gestures)
        gesture_list.remove(FORFEIT) # forfeit is only an option for Human players
        self.current_gesture = random.choice(gesture_list)

    # uses recursive random name generation by adding suffixes to computer.name
    def set_name(self, prompt):
        if len(self.names) == 0:
            self.names = self.new_names.copy()
            self.new_names.clear()
        self.name = random.choice(self.names)
        suffix = random.choice(self.suffixes)
        self.new_names.append(self.name + suffix)
        self.names.remove(self.name)