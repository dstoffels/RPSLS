from helpers import clear_console, validate_int_input
from match import Match
from match_variants import Computer_Match, Human_Match, Mixed_Multiplayer, Solo_Match


# refactor idea: draw from a list to generate menu programatically
class MainMenu:

    def __init__(self):
        self.match: Match = None
        self.MENU = '''
    1) Solo Game
    2) Hotseat Game (2 Human Players)
    3) Mixed Multiplayer (3+ Players)
    4) Watch the computer duke it out
    5) Exit Program

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
                case 5: self.exit_progrum()
                case _: prompt = 'Please choose between 1-5: '
            if self.match: self.match.run()

    def exit_progrum(self):
        print('Goodbye...\n')
        exit()