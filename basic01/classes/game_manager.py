from basic01.classes.words_manager import WordsManager


class GameManager:
    def __init__(self):
        self.tries_limit = 5
        self.words_manager = WordsManager()

    def start_game(self):
        if self.words_manager.check_user_guess():
            self.words_manager.print_success_message()
            return

        for i in range(self.tries_limit):
            self.words_manager.print_guesses_list()
            self.words_manager.get_user_guess()

            if self.words_manager.check_user_guess():
                self.words_manager.print_success_message()
                break
        else:
            self.words_manager.print_lose_message()
