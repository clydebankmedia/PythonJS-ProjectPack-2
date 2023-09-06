import sys
from PySide2.QtWidgets import (
  QApplication, QWidget, QLabel, QLineEdit, QPushButton,
  QVBoxLayout, QHBoxLayout
)
from PySide2 import QtCore

class TemperatureConverterApp(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()

  def init_ui(self):
    self.setWindowTitle("Temperature Converter")
    self.setGeometry(100, 100, 400, 100) # x, y, width, height

    self.lbl_fahrenheit = QLabel("Fahrenheit:")
    self.edit_fahrenheit = QLineEdit()
    fahrenheit_layout = QVBoxLayout()
    fahrenheit_layout.addWidget(self.lbl_fahrenheit)
    fahrenheit_layout.addWidget(self.edit_fahrenheit)

    self.lbl_celsius = QLabel("Celsius:")
    self.edit_celsius = QLineEdit()
    celsius_layout = QVBoxLayout()
    celsius_layout.addWidget(self.lbl_celsius)
    celsius_layout.addWidget(self.edit_celsius)

    self.btn_to_celsius = QPushButton("\u2192")
    self.btn_to_celsius.setFixedWidth(50)
    self.btn_to_fahrenheit = QPushButton("\u2190")
    self.btn_to_fahrenheit.setFixedWidth(50)
    button_layout = QVBoxLayout()
    button_layout.addWidget(self.btn_to_celsius)
    button_layout.addWidget(self.btn_to_fahrenheit)

    top_layout = QHBoxLayout()
    top_layout.addLayout(fahrenheit_layout)
    top_layout.addLayout(button_layout)
    top_layout.addLayout(celsius_layout)
    
    self.error_label = QLabel("")
    self.error_label.setStyleSheet("color: red")

    main_layout = QVBoxLayout()
    main_layout.addLayout(top_layout)
    main_layout.addWidget(self.error_label, alignment=QtCore.Qt.AlignCenter)

    self.setLayout(main_layout)

    self.btn_to_celsius.clicked.connect(self.to_celsius)
    self.btn_to_fahrenheit.clicked.connect(self.to_fahrenheit)
    
  def to_celsius(self):
    try:
      text = self.edit_fahrenheit.text()
      fahrenheit = float(text)
      celsius = (fahrenheit - 32) * 5/9
      self.edit_celsius.setText(str(celsius))
      self.error_label.setText("")
    except ValueError:
      self.error_label.setText(f"Invalid input: {text}")

  def to_fahrenheit(self):
    try:
      text = self.edit_celsius.text()
      celsius = float(text)
      fahrenheit = celsius * 9/5 + 32
      self.edit_fahrenheit.setText(str(fahrenheit))
      self.error_label.setText("")
    except ValueError:
      self.error_label.setText(f"Invalid input: {text}")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  converter_app = TemperatureConverterApp()
  converter_app.show()
  sys.exit(app.exec_())
