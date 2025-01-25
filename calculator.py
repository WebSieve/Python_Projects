import sys
from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QPushButton, QMainWindow, QVBoxLayout,
    QLineEdit, QWidget, QSizePolicy
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.userInput = ''
        
    def initUI(self):
        self.setWindowTitle('better calculator')
        self.setGeometry(300, 300, 500, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        vbox = QVBoxLayout(central_widget)
        
        self.display = QLineEdit(self)
        self.display.setFont(QFont('Roboto', 20))
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setGeometry(0, 0, 700, 300)
        self.display.setStyleSheet('padding: 4px; border: 2px solid black;')
        vbox.addWidget(self.display, stretch=1)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('=', 3, 3),
            ("+", 4, 0)
            ]
        
        grid = QGridLayout(self)
        
        for txt, rows, cols in buttons:
            btn = QPushButton(txt, self)
            btn.clicked.connect(self.on_number_btn_click)
            btn.setFont(QFont("Roboto", 14))
            btn.setStyleSheet("""
                              QPushButton{
                                    background-color: #3498db;
                                    color: white;
                                    padding: 10px;
                                    border-radius: 10px;
                                    border: 2px solid black;
                                }
                                QPushButton:hover {
                                    background-color: #2980b9;
                                }
                                QPushButton:pressed {
                                    background-color: #1abc9c;
                                }
                              """)
            grid.addWidget(btn, rows, cols,)
            
            vbox.addLayout(grid)

            
    def on_number_btn_click(self):
        
        sender = self.sender()
        text = sender.text()
        
        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error 404")
        elif text == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text()+text)
    
def main():
    app = QApplication(sys.argv)
    myApp = calculator()
    myApp.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    