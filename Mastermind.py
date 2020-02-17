#methods imports
from Mastermind_methods import *

class mm_guess:
    def __init__(self,guess_input,valid_range,valid_length,pattern):
        self.guess_input = guess_input
        self.pattern = pattern
        self.valid = guess_is_valid(self.guess_input,valid_range,valid_length)
        if self.valid:
            self.guess = parse_guess(self.guess_input)
        else:
            self.guess = [0 for i in range(0,valid_length)]
        self.correctness = analyse_guess(self.guess,self.pattern)
        self.b_score = self.correctness.count(2)    #black score = correctness 2
        self.w_score = self.correctness.count(1)    #white score = correctness 1

#individual mm game
class mm_game:
    def __init__(self,max_guesses=12,pattern_range=6,pattern_length=4):
        self.max_guesses = max_guesses
        self.pattern_length = pattern_length
        self.pattern_range = pattern_range
        self.guess_list = []

    def start_game(self):
        print("\nNew game started")
        print("Black = correct colour, correct position. White = correct colour, wrong position\n")
        self.pattern = gen_pattern(self.pattern_range,self.pattern_length)
        self.guess_number = 1
        while(self.guess_number <= self.max_guesses):
            print("\nGuess number ",self.guess_number,"/",self.max_guesses)
            example_input = ''.join(str(i) for i in range(1,self.pattern_length+1))
            guess_raw = input("Enter guess in form "+example_input+": ")
            new_guess = mm_guess(guess_raw,self.pattern_range,self.pattern_length,self.pattern)
            if new_guess.valid:
                print("Valid guess. Black score: ",new_guess.b_score,", White score: ",new_guess.w_score)
                self.guess_list.append(new_guess)
                self.guess_number = self.guess_number+1
                if new_guess.b_score == self.pattern_length:
                    break
        self.end_game()
        

    def end_game(self):
        if self.guess_list[-1].b_score == self.pattern_length:
            print("\nCongratulations! You correctly guess the pattern!")
        elif self.guess_number > self.max_guesses:
            print("\nSorry, you ran out of guesses!")

#overall game session - various text input commands, can start new games etc.
class mm_session:
    def __init__(self,max_guesses=12,pattern_range=6,pattern_length=4):
        self.max_guesses = max_guesses
        self.pattern_length = pattern_length
        self.pattern_range = pattern_range
        self.session_active = True

    def main_loop(self):
        print("Welcome to Mastermind!")
        while self.session_active:
            print("Default settings are: ",self.max_guesses," guesses, ",self.pattern_length," \"pegs\", ",self.pattern_range," \"colours\"")
            text = "a"
            while (text not in ["y","n"]):
                text = input("Would you like to change the settings before starting? (y/n) ")
            if text == "y":
                self.change_settings()
            self.current_game = mm_game(self.max_guesses,self.pattern_range,self.pattern_length)
            self.current_game.start_game()
            text = "a"
            while (text not in ["y","n"]):
                text = input("\nWould you like to play again? (y/n) ")
            if text == "n":
                print("Session over")
                self.session_active = False

    def change_settings(self):
        print("Sorry this feature is not yet supported")

new_mm = mm_session(3,4,4)
new_mm.main_loop()

