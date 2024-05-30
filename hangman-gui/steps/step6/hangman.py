import sys
from enum import Enum, auto
from PySide6.QtWidgets import QApplication, QWidget, QLabel, \
    QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, \
    QLineEdit, QCheckBox

class HangmanGame:
  class GameStatus(Enum):
    IN_PROGRESS = auto()
    WON = auto()
    LOST = auto()
        
  def __init__(self, word, num_guesses):
    assert len(word) > 0 and word.islower() and word.isalpha() and num_guesses > 0
    self.word = word
    self.display_word = ['_'] * len(word)
    self.num_guesses = num_guesses
    self.guessed_letters = set()
    self.guessed_words = set() 
    self.remaining_guesses = num_guesses
    self.status = self.GameStatus.IN_PROGRESS

  def get_display(self):
    return ''.join(self.display_word)

  def already_guessed(self, guess):
    return guess in self.guessed_letters or guess in self.guessed_words

  def guess_letter(self, letter):
    assert self.status == self.GameStatus.IN_PROGRESS
    self.guessed_letters.add(letter)
    if letter in self.word:
      for i, c in enumerate(self.word):
        if c == letter:
          self.display_word[i] = letter
    return self.finish_guess()

  def guess_word(self, word):
    assert self.status == self.GameStatus.IN_PROGRESS
    self.guessed_words.add(word)
    if word == self.word:
      self.display_word = list(self.word)
    return self.finish_guess()
    
  def finish_guess(self):
    self.remaining_guesses -= 1
    current_progress = self.get_display()
    if current_progress == self.word:
      self.status = self.GameStatus.WON
    elif self.remaining_guesses <= 0:
      self.status = self.GameStatus.LOST
    return self.status, current_progress, self.remaining_guesses

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
  

  def start_game(self):
    self.main_widget.setCurrentWidget(self.game_screen)

  def finish_game(self):
    self.main_widget.setCurrentWidget(self.setup_screen)

  def make_setup_screen(self):
    header_lbl = QLabel("Setup")
    header_lbl.setStyleSheet("font-size: 24px; font-weight: bold;")
      
    self.num_guesses_input = QLineEdit("6")
    self.prevent_dup_chk = QCheckBox("Prevent &Duplicate Guesses")
    self.prevent_dup_chk.setChecked(True)
    self.show_prev_chk = QCheckBox("Show &Previous Guesses")
    self.show_prev_chk.setChecked(True)
  
    self.chosen_word_input = QLineEdit("quickstart")
    self.chosen_word_input.setPlaceholderText('Leave blank for random word')
    self.word_length_input = QLineEdit()
    self.word_length_input.setPlaceholderText('Leave blank to use chosen word above')
          
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
  
    self.guess_button = QPushButton('Guess')
    self.guess_button.clicked.connect(self.guess)
          
    self.finish_button = QPushButton('Finish')
    self.finish_button.clicked.connect(self.finish_game)
          
    vbox = QVBoxLayout()
    vbox.addWidget(self.finish_button)
    vbox.addWidget(self.remaining_guesses_label)
    vbox.addWidget(self.word_label)
  
    vbox.addWidget(QLabel('Guessed Letters:')) 
    vbox.addWidget(self.guessed_letters_label)
    vbox.addWidget(QLabel('Guessed Words:'))
    vbox.addWidget(self.guessed_words_label)
  
    vbox.addWidget(QLabel('Guess:'))
    vbox.addWidget(self.guess_input)
    vbox.addWidget(self.guess_button)
  
    screen = QWidget()
    screen.setLayout(vbox)
    return screen

  def guess(self):
    pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = HangmanUI()
    ui.show()
    sys.exit(app.exec())
