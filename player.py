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
        print(f'\n{self.current_gesture} beats {opponent_gesture}. Point to {self.name}!')
        self.score += 1

    def set_name(self):
        pass

    # refactor??
    def validate_and_set_name(self, players, player_num): 
        prompt = f'Enter a name for player {player_num}: '
        is_unique = False
        while not is_unique:
            self.set_name(prompt)
            for player in players:
                if player != self: 
                    match self.name:
                        case '': prompt = 'Name cannot be blank, please re-enter: '
                        case player.name: prompt = 'Name must be unique, please re-enter: '
                        case _: is_unique = True
    

    def has_winning_gesture(self, opponent_gesture):
        return True if opponent_gesture in self.gestures[self.current_gesture] else False

    def display_gesture(self):
        print(f"{self.name} chooses {self.current_gesture}")
    