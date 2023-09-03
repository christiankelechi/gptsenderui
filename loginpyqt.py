import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create buttons
        dark_theme_button = QPushButton("Dark Theme", self)
        dark_theme_button.clicked.connect(self.applyDarkTheme)

        light_theme_button = QPushButton("Light Theme", self)
        light_theme_button.clicked.connect(self.applyLightTheme)

        # Position buttons
        dark_theme_button.setGeometry(50, 50, 150, 30)
        light_theme_button.setGeometry(50, 100, 150, 30)

    def applyDarkTheme(self):
        # Set dark theme style sheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;
                color: white;
            }
            QPushButton {
                background-color: #333;
                color: white;
            }
        """)

    def applyLightTheme(self):
        # Set light theme style sheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
                color: black;
            }
            QPushButton {
                background-color: #DDD;
                color: black;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
