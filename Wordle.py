########################################
# Name: Flannery Sheets
# Collaborators (if any): Gavin Smith!!!
# GenAI Transcript (if any): No
# Estimated time spent (hr): 5
# Description of any added extensions: No
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():

    def enter_action():
        guess = word_from_row(0)
        row = gw.get_current_row()
        print(guess)
        if guess.lower() in ENGLISH_WORDS:
            gw.show_message('Good Job!')
            color_row(row,answer,guess)
            
        else:
            gw.show_message('not word in list')

    def word_to_row(row:int, word:str):
        gw.show_message("words")

    def set_row(guess):
        row = gw.get_current_row()
        if answer == guess:
            gw.show_message("way to go buddy!")
            gw.set_current_row(N_ROWS)
        elif row == N_ROWS - 1:
            gw.show_message("you lost, the answer was " + answer)
        else:
            gw.set_current_row(row+1)

    def word_from_row(row:int) -> str:
        string = gw.get_square_letter(row,0) + gw.get_square_letter(row,1) + gw.get_square_letter(row,2) + gw.get_square_letter(row,3) + gw.get_square_letter(row,4)
        print(type (string))
        return string
    
    def color_row(row:int,answer:str,guess:str):
        guess = word_from_row(row).lower()
        unmatched = answer
        
        print(len(unmatched))
        for i in range(len(guess)):
            if unmatched[i] == guess[i]:
                gw.set_square_color(row,i,CORRECT_COLOR)
                gw.set_key_color(guess[i],CORRECT_COLOR)
                #unmatched = remaining_letters(i,answer)
                unmatched = unmatched[:i] + "-" + unmatched[i+1:]
                print(unmatched)
        for i in range(len(guess)):    
            if guess[i] in unmatched:
                color = gw.get_square_color(row,i)
                if color != CORRECT_COLOR:
                    gw.set_square_color(row,i,PRESENT_COLOR)
                    color = gw.get_key_color(guess[i])
                    if color != CORRECT_COLOR:
                        gw.set_key_color(guess[i],PRESENT_COLOR)
                    #unmatched = remaining_letters(i,answer)
                    unmatched = unmatched.replace(guess[i],"-",1)
            else:
                color = gw.get_square_color(row,i)
                if color == UNKNOWN_COLOR:
                    gw.set_square_color(row,i,MISSING_COLOR)
                    colorb = gw.get_key_color(guess[i])
                    if colorb == UNKNOWN_COLOR:    
                        gw.set_key_color(guess[i],MISSING_COLOR)
        set_row(guess)
    
    def remaining_letters(letter:str, answer:str) -> str:
    # remove ONLY THE FIRST case of letter in word
        for index in range(len(answer)):
            if answer[index] == letter:
                return answer[:index] + '-' + answer[index+1:]
        return answer # if letter isn't present
    
    def random_fiveletter_word() -> str: 
        random.shuffle(ENGLISH_WORDS)
        for word in ENGLISH_WORDS:
            if len(word) == 5:
                return word



    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)

    
    answer = random_fiveletter_word()
    gw.show_message(answer)









# Startup boilerplate
if __name__ == "__main__":
    wordle()
