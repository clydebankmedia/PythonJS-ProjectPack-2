import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, \
    QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, \
    QLineEdit, QCheckBox

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
    lbl = QLabel("Game Screen")
    self.finish_button = QPushButton('Finish Game')
    self.finish_button.clicked.connect(self.finish_game)
  
    vbox = QVBoxLayout()
    vbox.addWidget(lbl)
    vbox.addWidget(self.finish_button)
  
    screen = QWidget()
    screen.setLayout(vbox)
    return screen
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = HangmanUI()
    ui.show()
    sys.exit(app.exec())
