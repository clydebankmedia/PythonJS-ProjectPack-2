import sys
from enum import Enum, auto
import requests # for random word generation
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, \
    QPushButton, QVBoxLayout, QMessageBox, QCheckBox, QMainWindow, QStackedWidget
from PySide2.QtGui import QRegExpValidator
from PySide2.QtCore import QRegExp

class HangmanGame:
    class GameStatus(Enum):
        IN_PROGRESS = auto()
        WON = auto()
        LOST = auto()
    
    def __init__(self, word, num_guesses):
        self.word = word
        self.guess_so_far = ['_'] * len(word)
        self.num_guesses = num_guesses
        self.guessed_letters = set()
        self.guessed_words = set() 
        self.remaining_guesses = num_guesses
        self.status = self.GameStatus.IN_PROGRESS

    def get_display(self):
        return ''.join(self.guess_so_far)

    def alreadyGuessed(self, guess):
        return guess in self.guessed_letters or guess in self.guessed_words

    def guess_letter(self, letter):
        assert self.status == self.GameStatus.IN_PROGRESS
        self.guessed_letters.add(letter)
        if letter in self.word:
            for i, c in enumerate(self.word):
                if c == letter:
                    self.guess_so_far[i] = letter
        return self.finish_guess()

    def guess_word(self, word):
        assert self.status == self.GameStatus.IN_PROGRESS
        self.guessed_words.add(word)
        if word == self.word:
            self.guess_so_far = list(self.word)
        return self.finish_guess()
    
    def finish_guess(self):
        self.remaining_guesses -= 1
        if ''.join(self.guess_so_far) == self.word:
            self.status = self.GameStatus.WON
        elif self.remaining_guesses == 0:
            self.status = self.GameStatus.LOST
        return self.status, self.get_display(), self.remaining_guesses

class HangmanUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hangman')
        self.setup_screen = self.make_setup_screen()
        self.game_screen = self.make_game_screen()

        self.main_widget = QStackedWidget(self)
        self.main_widget.addWidget(self.setup_screen)
        self.main_widget.addWidget(self.game_screen)
        self.setCentralWidget(self.main_widget)

    def make_setup_screen(self):
        header_lbl = QLabel("Setup")
        header_lbl.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.num_guesses_input = QLineEdit()
        self.num_guesses_input.setValidator(QRegExpValidator(QRegExp(r'^\d{1,2}$')))
        self.prevent_dup_chk = QCheckBox("Prevent &Duplicate Guesses")
        self.prevent_dup_chk.setChecked(True)
        self.show_prev_chk = QCheckBox("Show &Previous Guesses")
        self.show_prev_chk.setChecked(True)

        self.chosen_word_input = QLineEdit()
        self.chosen_word_input.setPlaceholderText('Leave blank for random word')
        self.chosen_word_input.setValidator(QRegExpValidator(QRegExp(r'^[a-zA-Z]+$')))
        self.word_length_input = QLineEdit()
        self.word_length_input.setPlaceholderText('Leave blank to use chosen word above')
        self.word_length_input.setValidator(QRegExpValidator(QRegExp(r'^\d{1,2}$')))
        
        self.start_button = QPushButton('Start Game')
        self.start_button.clicked.connect(self.start_game)
        
        vbox = QVBoxLayout()
        vbox.addWidget(header_lbl)
        vbox.addWidget(QLabel('Number of Guesses Allowed:'))
        vbox.addWidget(self.num_guesses_input)
        vbox.addWidget(self.prevent_dup_chk)
        vbox.addWidget(self.show_prev_chk)
        
        vbox.addWidget(QLabel('Word to Guess:'))
        vbox.addWidget(self.chosen_word_input)
        vbox.addWidget(QLabel('Word Length (for random generation):'))
        vbox.addWidget(self.word_length_input)

        vbox.addWidget(self.start_button)
        screen = QWidget()
        screen.setLayout(vbox)
        return screen
        
    def make_game_screen(self):
        self.remaining_guesses_label = QLabel()
        self.word_label = QLabel()

        self.guessed_letters_label = QLabel()
        self.guessed_words_label = QLabel()

        self.guess_input = QLineEdit()
        self.guess_input.returnPressed.connect(self.guess)
        self.guess_input.setValidator(QRegExpValidator(QRegExp('[a-zA-Z]+')))
        self.guess_btn = QPushButton('Guess Letter')
        self.guess_btn.clicked.connect(self.guess)
        
        self.restart_btn = QPushButton('Restart')
        self.restart_btn.clicked.connect(self.restart_game)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.restart_btn)
        vbox.addWidget(self.remaining_guesses_label)
        vbox.addWidget(self.word_label)

        vbox.addWidget(QLabel('Guessed Letters:')) 
        vbox.addWidget(self.guessed_letters_label)
        vbox.addWidget(QLabel('Guessed Words:'))
        vbox.addWidget(self.guessed_words_label)

        vbox.addWidget(QLabel('Guess:'))
        vbox.addWidget(self.guess_input)
        vbox.addWidget(self.guess_btn)

        screen = QWidget()
        screen.setLayout(vbox)
        return screen

    def generate_random_word(self, length):
        if length < 1:
            return ''
        url = 'https://random-word-api.herokuapp.com/word'
        response = requests.get(url, params={'length': length})
        if response.status_code != 200:
            # at first, just raise Exception.
            QMessageBox.warning(self, "Error", "Failed to generate a random word.")
            raise Exception('Failed to generate random word')
        return response.json()[0]
        
    def start_game(self):
        # clear any error styling
        self.num_guesses_input.setStyleSheet("")
        self.word_length_input.setStyleSheet("")
        self.chosen_word_input.setStyleSheet("")

        num_guesses = self.num_guesses_input.text()
        if not num_guesses.isnumeric():
            self.num_guesses_input.setStyleSheet("border: 1px solid red;")
            return
        num_guesses = int(num_guesses)

        word_length = self.word_length_input.text()
        word = self.chosen_word_input.text()
        if not (word_length or word): # user didn't provide either
            self.word_length_input.setStyleSheet("border: 1px solid red;")
            self.chosen_word_input.setStyleSheet("border: 1px solid red;")
            return
        if not word:
            try:
                word = self.generate_random_word(int(word_length))
            except Exception as e:
                print(e)
                return # stay at setup screen 
        
        self.game = HangmanGame(word.lower(), num_guesses)
        self.update_display(self.game.GameStatus.IN_PROGRESS, self.game.get_display(), num_guesses)
        self.main_widget.setCurrentWidget(self.game_screen)

    def guess(self):
        self.guess_input.setStyleSheet("") # clear old error styling
        guess = self.guess_input.text().strip().lower()
        self.guess_input.clear() # clear old input
        
        if self.prevent_dup_chk.isChecked() and self.game.alreadyGuessed(guess):
            self.guess_input.setStyleSheet("border: 1px solid red;")
            return
        
        method = self.game.guess_letter if len(guess) == 1 else self.game.guess_word
        status, display, remaining_guesses = method(guess)
        self.update_display(status, display, remaining_guesses)

    def update_display(self, status, display, remaining_guesses):
        self.remaining_guesses_label.setText(f"Remaining Guesses: {remaining_guesses}")
        self.word_label.setText(' '.join(display))
        self.guessed_letters_label.setText(', '.join(self.game.guessed_letters))
        self.guessed_words_label.setText(', '.join(self.game.guessed_words))
        if status == HangmanGame.GameStatus.IN_PROGRESS:
            return
        if status == HangmanGame.GameStatus.WON:
            QMessageBox.information(self, "You Won!", "You guessed the word!")
        elif status == HangmanGame.GameStatus.LOST:
            self.word_label.setText(' '.join(self.game.word))
            QMessageBox.information(self, "You Lost!", f"You ran out of guesses! The word was {self.game.word}")
        self.restart_game()

    def restart_game(self):
        self.main_widget.setCurrentWidget(self.setup_screen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = HangmanUI()
    ui.show()
    sys.exit(app.exec_())
