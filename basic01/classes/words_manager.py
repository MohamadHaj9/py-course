import random
import basic01.data.words as data


class WordsManager:
    def __init__(self):
        self.words = set(data.words_5_letters)
        self.colors = {"gray": "\033[90m", "yellow": "\033[93m", "green": "\033[92m", "red": "\033[91m"}
        self.random_word = self.select_random_word()
        self.user_guess = ""
        self.guesses_list = []
        self.get_user_guess()

    def select_random_word(self):
        random_word = random.choice(list(self.words))
        print(random_word.upper())
        return random_word

    def validate_user_guess(self, user_guess):
        return user_guess.lower() in self.words

    def get_user_guess(self, prompt="Enter your guess for the word: "):
        while True:
            user_guess = input(f"{self.colors['red']}{prompt}{self.colors['red']}")
            if self.validate_user_guess(user_guess):
                self.user_guess = user_guess.lower()
                break
            else:
                prompt = "Not in list. Please enter your guess for the word: "

    def check_user_guess(self):
        guesses = {}

        for index, g_letter in enumerate(self.user_guess):
            r_letter = self.random_word
            if g_letter == r_letter[index]:
                guesses[index] = (g_letter, self.colors["green"])
            elif g_letter != r_letter[index] and g_letter in self.random_word:
                guesses[index] = (g_letter, self.colors["yellow"])
            else:
                guesses[index] = (g_letter, self.colors['gray'])

        self.guesses_list.append(guesses)
        return self.user_guess == self.random_word

    def print_guesses_list(self):
        print("Previous Guesses")
        for guessed_word in self.guesses_list:
            for character in guessed_word.values():
                print(f"{character[1]}{character[0].upper()}{character[1]}", end="")
            print()

    def print_lose_message(self):
        print(f"You have no more tries. The target word was: {self.random_word.upper()}")

    def print_success_message(self):
        print(f"{self.colors['green']}Congratulations! You correctly guessed the target word: {self.random_word.upper()}{self.colors['green']}")
