Develop necessary classes/modules

gestures.py: stores list/dict of gestures, eventually gesture class(?)
-name = 'Rock'
-defeats_gestures = ['Scissors', 'Lizard']

def compare_gesture(opp_gesture):
for gest in self.defeats_gestures:
if gest == opp_gesture: return True
return False

p1_gest

-Player class
-name
-score: int
-gestures list

-select_gesture(): pass
-win_round(): rounds_won += 1

-User(Player) subclass
-player_menu = Menu(): display selecable list of gestures for round
-select_gesture(): player_menu.run() -> gesture

-AI(Player) subclass
-select_gesture(): Randomly select a gesture

-Menu class: displays menu strings and handles user selections
-prompt
-run()
-clearConsole()

-Match class: contains players, handles game logic
-player 1 = None
-player 2 = None
-total_rounds_for_win = 0
-round_num = 1

    -run():
      -setup_match()

    -setup_match():

      -set_player_names()
      -set total rounds for win()
      -display_rules()

    -round():
      -while both players rounds_won < total_rounds_for_win
        -print( round number and each players wins )
        -each player selects a gesture
        -if same gesture, display tie, rerun round
        -else: compare player.gesture to player2.gesture, +1 to round winner, +1 to round_num

    -declare_winner(): from # of player wins in players

-SoloMatch(Match):
-init
-player1 = user()
-player2 = AI()

-HotSeatMatch(Match):
-init
-player1 = user()
-player2 = user()

-AI_Match(Match):
-init:
-player1 = AI()
-player2 = AI()

-main.py
--match = None
--main_menu = Menu()
---1) Solo Game
----match = SoloMatch()
---2) Hot seat (2-player)
----match = HotSeatMatch()
---3) AI Only
----match = AI_Match()
---4) Exit Program
-----print 'goodbye'
-----exit()

      -match.run()
