import PySimpleGUI as sg
from NewWord import *


def enter_game_data():
    """creates a gui window for user to input data..."""

    sg.theme('Dark Grey')
    layout = [
        [sg.Text("Wordle Assistant", text_color='white', font=('consolas', 30)), ],
        # [sg.Text("List of words that are still available:")],
        # TODO use threading to keep this list utd with entered data
        # [sg.Listbox(values=list_of_available_words, size=(20, 12), key='-LIST-', enable_events=True)],
        [sg.Text("Put any GREEN letters here:", text_color='green', font=('consolas', 30)),
         sg.InputText(size=(5, 1), background_color='green', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='green', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='green', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='green', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='green', text_color='black', font=('consolas', 20)), ],
        [sg.Text("Put any YELLOW letters here:", text_color='yellow', font=('consolas', 30)),
         sg.InputText(size=(5, 1), background_color='yellow', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='yellow', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='yellow', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='yellow', text_color='black', font=('consolas', 20)),
         sg.InputText(size=(5, 1), background_color='yellow', text_color='black', font=('consolas', 20)), ],
        [sg.Text("If you got a yellow R in position 1 at any point, you should put an r in position 1. If you also "
                 "got a yellow A in that position, you should put an a in that box as well. each yellow box should "
                 "hold all yellow letters that you have guessed in the appropriate index.")], # TODO clarify lol...
        [sg.Text("Put any BLACK letters in here:", text_color='black', font=('consolas', 30)),
         sg.InputText(size=(20, 1), background_color='grey', text_color='red', font=('consolas', 20)), ],
        [sg.Button("Submit")],
    ]

    window = sg.Window('Wordle Assistant', layout, keep_on_top=True)
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event in "Submit":
            list_of_green_letters = construct_green_letters_list(values)
            # make the chars in that string uppercase...
            list_of_green_letters = [each_string.upper() for each_string in list_of_green_letters]

            # should let in many letters per box.
            list_of_yellow_letter_lists = []
            yellow1 = str(values[5])  # these are yellows in position 1
            l1 = make_yellow_letter_list_element_list(yellow1, 0)
            yellow2 = str(values[6])
            l2 = make_yellow_letter_list_element_list(yellow2, 1)
            yellow3 = str(values[7])
            l3 = make_yellow_letter_list_element_list(yellow3, 2)
            yellow4 = str(values[8])
            l4 = make_yellow_letter_list_element_list(yellow4, 3)
            yellow5 = str(values[9])
            l5 = make_yellow_letter_list_element_list(yellow5, 4)
            if l1 is not None:
                list_of_yellow_letter_lists.append(l1)
            if l2 is not None:
                list_of_yellow_letter_lists.append(l2)
            if l3 is not None:
                list_of_yellow_letter_lists.append(l3)
            if l4 is not None:
                list_of_yellow_letter_lists.append(l4)
            if l5 is not None:
                list_of_yellow_letter_lists.append(l5)

            # accepts arbitrarily many letters
            black = values[10]
            black = black.upper()
            list_of_black_letters = split(black)

            # we also need to get good letters which is just a list of letters that appear in yellow or green.
            # put all the yellow ones in
            # smash all the yellow letters together into one long string
            long_string = yellow1 + yellow2 + yellow3 + yellow4 + yellow5
            # then split()
            long_string_split = split(long_string)
            # remove duplicates
            good_letters_list = []
            [good_letters_list.append(x) for x in long_string_split if x not in good_letters_list]
            # put all the green ones in
            # good_letters_list.append(item for item in list_of_green_letters)  # put all the green ones in

            return list_of_green_letters, list_of_yellow_letter_lists, list_of_black_letters, good_letters_list

    window.close()


def make_yellow_letter_list_element_list(yellow1, element):
    yellow1 = yellow1.upper()
    for letter in yellow1:
        new_list = ["", "", "", ""]
        new_list.insert(element, letter)
        return new_list


def construct_green_letters_list(values):
    green_letters = []
    for i in range(5):
        if len(values[i]) > 0:
            green_letters.append(values[i])
        else:
            green_letters.append("")
    return green_letters
