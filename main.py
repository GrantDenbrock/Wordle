from NewWord import *
from GUI import *
import PySimpleGUI as sg

if __name__ == '__main__':
    # Open up the GUI
    GREEN_LETTERS, YELLOW_LETTERS, BAD_LETTERS, GOOD_LETTERS = enter_game_data()

    # I made an oopsie and need to make this list of strings all uppercase...
    GOOD_LETTERS = [each_string.upper() for each_string in GOOD_LETTERS]

    # pass this all to the engine
    word = NewWord(BAD_LETTERS, GOOD_LETTERS, GREEN_LETTERS, YELLOW_LETTERS)

    # get the list of possible words
    list_of_words = word.get_list_of_possible_words()
    sg.popup_scrolled(list_of_words, keep_on_top=True)

