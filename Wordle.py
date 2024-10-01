########################################
# Name: Flannery Sheets
# Collaborators (if any): Gavin Smith and Emma from the QUAD
# GenAI Transcript (if any): No
# Estimated time spent (hr): 8
# Description of any added extensions: No
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():

    def enter_action(): #when enter is pressed
        guess = word_from_row(0) #guess is equal to whatever is written in row
        row = gw.get_current_row() #get the row
        if guess.lower() in ENGLISH_WORDS:
            gw.show_message('Good Job!') #if english word prints message
            color_row(row,answer,guess) #colors row (checks row)
        else:
            gw.show_message('not word in list') #if not english word

    def set_row(guess): #function for when to end or first time win
        row = gw.get_current_row() #finds whatever the current row is
        if answer == guess: #if they are exactly the same
            gw.show_message("way to go buddy!") #prints message
            gw.set_current_row(N_ROWS) #ends the game
        elif row == N_ROWS - 1: #if all rows are filled
            gw.show_message("you lost, the answer was " + answer) #if answer is never reached
        else:
            gw.set_current_row(row+1) #moves on to next row

    def word_from_row(row:int) -> str: #shows that the guess is what is typed in the row
        string = gw.get_square_letter(row,0) + gw.get_square_letter(row,1) + gw.get_square_letter(row,2) + gw.get_square_letter(row,3) + gw.get_square_letter(row,4)
        return string
    
    def color_row(row:int,answer:str,guess:str):
        guess = word_from_row(row).lower()
        unmatched = answer
        for i in range(len(guess)): #in the first row, the guess
            if unmatched[i] == guess[i]: #if the answer and guess match, then green
                gw.set_square_color(row,i,CORRECT_COLOR) #letter green
                gw.set_key_color(guess[i],CORRECT_COLOR) #key green
                unmatched = unmatched[:i] + "-" + unmatched[i+1:] #removes correct letter from unmatched
        for i in range(len(guess)):    
            if guess[i] in unmatched: #if letter correspond
                color = gw.get_square_color(row,i) #color is the square color
                if color != CORRECT_COLOR: #if the color isnt green
                    gw.set_square_color(row,i,PRESENT_COLOR) # make the color yellow
                    color = gw.get_key_color(guess[i]) # color is equal to the color
                    if color != CORRECT_COLOR: # if color isnt green
                        gw.set_key_color(guess[i],PRESENT_COLOR) # make the key yellow
                    unmatched = unmatched.replace(guess[i],"-",1) #continuing to replace letters in unmatched so that the function can function
            else:
                color = gw.get_square_color(row,i) #color = whatever the color is
                if color == UNKNOWN_COLOR: # if its white
                    gw.set_square_color(row,i,MISSING_COLOR) #turn it to gray
                    colorb = gw.get_key_color(guess[i]) # but
                    if colorb == UNKNOWN_COLOR: # if the key is already a color   
                        gw.set_key_color(guess[i],MISSING_COLOR) # dont change it
        set_row(guess) # set the row so the game can continue

    def random_fiveletter_word() -> str: #sets the answer
        random.shuffle(ENGLISH_WORDS) #randomly pick an english word
        for word in ENGLISH_WORDS: #if that word
            if len(word) == 5: #is five characters
                return word #then return it



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    answer = random_fiveletter_word() #sets the answer









# Startup boilerplate
if __name__ == "__main__":
    wordle()
