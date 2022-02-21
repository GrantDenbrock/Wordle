# This is the dictionary that exists in your machine (if you are on macOS)
filename = "/usr/share/dict/words"


def split(word):
    return list(word)


def better_check_chars(words, correct_letters):
    result = []
    indices_to_check = []

    for index, value in enumerate(correct_letters):
        if value != '':
            indices_to_check.append((index, value))

    number_of_indices = len(indices_to_check)

    for word in words:
        flag = True
        word = split(word)
        for i in range(number_of_indices):
            if indices_to_check[i][1] == word[indices_to_check[i][0]]:
                pass
            else:
                flag = False
        if flag:
            result.append(word)

    return result


def check_for_letters_in_wrong_place(words, letter_not_positions):
    result = []

    for word in words:
        flag = True
        # check for letter in wrong place()
        word = split(word)
        for i in range(len(word)):
            for thing in letter_not_positions:
                if word[i] == thing[i]:
                    # that means we have detected a letter in the wrong place...
                    flag = False
                else:
                    pass
        if flag:
            result.append(word)
    return result


class NewWord:
    def __init__(self, bad_letters, good_letters, list_of_correct_letters_in_correct_places, letter_not_positions):
        self.list_of_correct_letters_in_correct_places = list_of_correct_letters_in_correct_places
        self.good_letters = list(good_letters)
        self.word = None
        self.words = None
        self.bad_letters = list(bad_letters)
        self.letter_not_positions = letter_not_positions
        self.green_letter_list = ["", "", "", "", ""]
        self.yellow_letter_list = ["", "", "", "", ""]
        self.yellow_letter_list_of_lists = []

    def get_new_bad_letters(self):
        yes_no = None
        while yes_no != "N":
            yes_no = input("is there another letter we can rule out? Enter Y for yes, or N for no.")
            if yes_no == "Y":
                new_bad_letter = input("Enter the new letter to be ruled out: ")
                self.bad_letters.append(str(new_bad_letter.upper()))
            else:
                print("Ok moving on then...")

    def get_new_good_letters(self):
        yes_no = None
        while yes_no != "N":
            yes_no = input("Are there any letters we know for sure are in the word? (i.e. yellow or green) Enter Y for yes, or N for no.")
            if yes_no == "Y":
                new_bad_letter = input("Enter the new letter to be ruled in: ")
                self.bad_letters.append(str(new_bad_letter.upper()))
            else:
                print("Ok moving on then...")

    def get_green_letters(self):
        yes_no = input("Another green letter to add? Enter Y for yes, or N for no.")
        while yes_no != "N":
            index = input("What index was the correct letter(s) in? (STARTING WITH 0)")
            value = input("What letter goes there?")
            self.green_letter_list[int(index)] = str(value.upper())
            yes_no = input("Is there another green letter to add? Enter Y for yes, or N for no.")

    def get_yellow_letters(self):
        print("Another yellow letter? Enter Y for yes, or N for no.")
        yes_no = None
        while yes_no != "N":
            value = input("What letter is it?")
            index = input("What index does it not go into? (STARTING WITH 0)")
            self.yellow_letter_list[int(index)] = str(value.upper())
            self.yellow_letter_list_of_lists.append(self.yellow_letter_list)
            yes_no = input("Is there another yellow letter to add? Enter Y for yes, or N for no.")

    def find_right_letters_in_right_position(self):
        wordle_list = split(self.wordle)
        user_guess_list = split(self.user_guess)
        for i in range(5):
            if user_guess_list[i] == wordle_list[i]:
                print("in position", i + 1, ", ", user_guess_list[i], "was the correct letter")

    def get_list_of_possible_words(self):
        # get all 5-letter words
        self.words = list(x.strip().upper() for x in open(filename) if len(x) == 6)

        # remove words that contain letters that we aren't interested in
        # Remove words containing list characters
        # using loop
        self.remove_words_with_letters_we_arent_interested_in()

        # remove words that don't contain letters that we are interested in
        # Remove words not containing list characters
        # using loop
        self.remove_words_that_dont_contain_letters_that_we_are_interested_in()

        self.words = better_check_chars(self.words, self.list_of_correct_letters_in_correct_places)

        self.words = check_for_letters_in_wrong_place(self.words, self.letter_not_positions)
        print("There are %s possibilities" % len(self.words))
        print("The list of possible words is: ", self.words)
        return self.words

    def remove_words_that_dont_contain_letters_that_we_are_interested_in(self):
        result = []
        flag = 1
        for word in self.words:
            for idx in self.good_letters:
                if idx in word:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                result.append(word)
        self.words = result

    def remove_words_with_letters_we_arent_interested_in(self):
        result = []
        flag = 1
        for word in self.words:
            for idx in self.bad_letters:
                if idx not in word:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                result.append(word)
        self.words = result
