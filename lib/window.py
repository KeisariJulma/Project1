from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont


# creating game window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Project1')
        self.setWindowIcon(QIcon('assets\\window\\icon.png'))
        self.setGeometry(0, 0, kwargs['x'], kwargs['y'])
        self.mainmenu(x=kwargs['x'], y=kwargs['y'])
        self.show()

    def windowed(self):
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))

    def mainmenu(self, **kwargs):
        head = QLabel("Main Menu", self)
        head.setGeometry(kwargs['x'] / 2.4, kwargs['y'] / 2.5, 300, 60)
        font = QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        # setting font to the head
        head.setFont(font)

        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)
