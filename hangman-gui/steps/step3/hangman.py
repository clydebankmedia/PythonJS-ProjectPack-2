import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, \
    QMainWindow, QStackedWidget, QPushButton, QVBoxLayout

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
    lbl = QLabel("Setup Screen")
    self.start_button = QPushButton('Start Game')
    self.start_button.clicked.connect(self.start_game)
  
    vbox = QVBoxLayout()
    vbox.addWidget(lbl)
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
