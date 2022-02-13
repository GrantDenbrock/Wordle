from NewWord import *

if __name__ == '__main__':
    # Change the letters here accordingly.

    BAD_LETTERS = ["A", "T", "E", "U", "D"] # black letters
    GOOD_LETTERS = ["R", "O", "N", "B"] # yellow and green letters
    GREEN_LETTERS = ["R", "O", "", "", ""]
    YELLOW_LETTERS = [
        ["", "", "", "N", "B"],
    ]

    word = NewWord(BAD_LETTERS, GOOD_LETTERS, GREEN_LETTERS,YELLOW_LETTERS)
    word.get_list_of_possible_words()

