from gestures import GESTURES

class Player:
    def __init__(self):
        self.name = ''
        self.points = 0
        self.rounds_won = 0
        self.gestures = GESTURES
        self.current_gesture = ""
    
    def select_gesture(self):
        pass

    def score_point(self):
        self.points += 1

    def deduct_point(self):
        self.points -= 1

    def reset_points(self):
        self.points = 0

    def win_round(self):
        self.rounds_won += 1

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
        return opponent_gesture in self.gestures[self.current_gesture]

    def display_gesture(self):
        print(f"{self.name} chooses {self.current_gesture}")
    