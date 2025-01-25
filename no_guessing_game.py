import random
import sys
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QGridLayout, QPushButton, QMainWindow, QVBoxLayout,
    QLineEdit, QLabel, QWidget, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class no_guessing_game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()  # Initialize the user interface
        self.userInput = ""
        self.randomNumber = random.randint(1, 100)
        
    def initUI(self):
        # Set window title and dimensions
        self.setWindowTitle("Number Guessing Game")
        self.setGeometry(700, 450, 500, 400)

        # Create a central widget and set it as the central part of the window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: #20302b")
        
        # Create a vertical layout for better element arrangement
        vbox = QVBoxLayout(central_widget)

        # Label to give instructions to the user
        title_label = QLabel("Click 'Next' to generate a number!", self)
        title_label.setFont(QFont('Arial', 16))
        title_label.setStyleSheet("color: #4A90E2;")
        title_label.setAlignment(Qt.AlignCenter)  # Center align the label text
        vbox.addWidget(title_label)

        # Add some space above the input field for better spacing
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(spacer_top)

        # Input field (QLineEdit) to display the generated number
        self.display = QLineEdit(self)
        self.display.setPlaceholderText("Your Input?")
        self.display.setFont(QFont('Roboto', 14))
        self.display.setStyleSheet("background-color: #F0F0F0; padding: 10px; border: 2px solid #4A90E2;")
        self.display.setAlignment(Qt.AlignCenter)  # Align the text in the center of the box
        vbox.addWidget(self.display)
        
        # creating a grid layout to add to the vertical box.
        grid = QGridLayout()
        vbox.addLayout(grid)
        
        # displaying numbers so that the user is able to input the values in the input field.
        buttons = [("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
                   ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
                   ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
                                ("0", 3, 1)]
        for text, rows, cols in buttons:
            btn = QPushButton(text, self)
            btn.clicked.connect(self.on_number_button_click)
            btn.setFont(QFont("Roboto", 20))
            btn.setStyleSheet("""
                              QPushButton{
                                background-color: #2c5c4d;
                                color: white;
                                border: 2px solid black;
                                border-radius: 10px;
                                }
                              QPushButton:hover {
                                background-color: #8e44ad;
                                transform: scale(1.05);  
                                }
                                """)
            grid.addWidget(btn, rows, cols)

        # Add some space after the buttons.
        spacer_middle2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(spacer_middle2)
        
        # displaying if the user guess is correct of incorrect.
        self.result_label = QLabel("let's see if you guessed it", self)
        vbox.addWidget(self.result_label)
        self.result_label.setFont(QFont("Roboto", 16))
        self.result_label.setStyleSheet("color: white; border: 2px solid black; border-radius: 10px")
        self.result_label.setAlignment(Qt.AlignCenter) 
        
        
        # adding space after the result label
        result_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(result_spacer)
        
        # Create the "Next" button
        Nextbutton = QPushButton("Next", self)
        Nextbutton.setFont(QFont('Roboto', 20))
        Nextbutton.setStyleSheet(
            "background-color: #4A90E2; color: white; padding: 10px; border-radius: 5px;"
        )
        Nextbutton.clicked.connect(self.on_next_button_click)  # Connect button to method
        vbox.addWidget(Nextbutton)

        # Add a final spacer to create better margins at the bottom
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(spacer_bottom)
        
    def on_next_button_click(self):
        if self.userInput:
            if int(self.userInput) == self.randomNumber:
                self.result_label.setText("CONGRATULATIONS! YOU GUESSED IT.")
                self.result_label.setStyleSheet("color: green;")
            elif int(self.userInput) < self.randomNumber:
                self.result_label.setText("your guess is low")
                self.result_label.setStyleSheet("color: red;")
            elif int(self.userInput) > self.randomNumber:
                self.result_label.setText("your guess is high")
                self.result_label.setStyleSheet("color: red;")
                
            # self.randomNumber = random.randint(1, 100)
            self.userInput = ""
            self.display.clear()
            
    # getting the number is the user pressed the button.
    def on_number_button_click(self):
        sender = self.sender()
        text = sender.text()
        self.userInput += text
        self.display.setText(self.userInput)
        
def main():
    app = QApplication(sys.argv)
    myapp = no_guessing_game()  # Create the game window instance
    myapp.show()  # Show the window
    sys.exit(app.exec_())  # Exit application when the window is closed

if __name__ == "__main__":
    main()