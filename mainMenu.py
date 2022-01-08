from helpers import clear_console, validate_int_input
from match import Match
from match_variants import Computer_Match, Human_Match, Solo_Match

class MainMenu:

    def __init__(self):
        self.match: Match = None
        self.PROMPT = '''
    1) Solo Game
    2) Hotseat Game (2-humans)
    3) Watch the computer duke it out
    4) Exit Program

    Choose an option: '''

        self.run()

    def run(self):
        while True:
            clear_console()
            userInput = validate_int_input(self.PROMPT)
            match userInput:
                case 1: self.match = Solo_Match()
                case 2: self.match = Human_Match()
                case 3: self.match = Computer_Match()
                case 4: self.exit_progrum()
            self.match.run()

    def exit_progrum(self):
        print('Goodbye...\n')
        exit()