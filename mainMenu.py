from helpers import clear_console, validate_int_input
from match import Match
from mixedMultiplayerMatch import Mixed_Multiplayer
from soloMatch import Solo_Match
from humanMatch import Human_Match
from computerMatch import Computer_Match

# refactor idea: draw from a list to generate menu programatically
class MainMenu:

    def __init__(self):
        self.match: Match = None
        self.MENU = '''
[Rock, Paper, Scissors, Lizard, Spock]

MAIN MENU

    1) Solo Game
    2) Hotseat Game (2 Human Players)
    3) Mixed Multiplayer (3+ Players)
    4) Watch the computer duke it out
    5) Rules of the game
    6) Exit Program

'''

        self.run()

    def run(self):
        prompt = 'Choose an option: '
        while True:
            clear_console()
            userInput = validate_int_input(self.MENU + prompt)
            match userInput:
                case 1: self.match = Solo_Match()
                case 2: self.match = Human_Match()
                case 3: self.match = Mixed_Multiplayer()
                case 4: self.match = Computer_Match()
                case 5: self.display_rules()
                case 6: self.exit_progrum()
                case _: prompt = 'Please choose between 1-5: '
            if self.match: self.match.run()

    def display_rules(self):
        clear_console()
        print(GAME_RULES)
        input('Press enter to return to the main menu...')

    def exit_progrum(self):
        print('Goodbye...\n')
        exit()

GAME_RULES = '''
RULES

    As Sheldon explains, "Scissors cuts paper, paper covers rock, rock crushes lizard, 
    lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard 
    eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, 
    rock crushes scissors."
'''