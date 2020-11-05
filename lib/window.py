from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont


# creating game window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args)
        self.setWindowTitle('Project1')
        self.setWindowIcon(QIcon('assets\\window\\icon.png'))
        self.setGeometry(0, 0, kwargs['x'], kwargs['y'])
        self.board = Menu(self)
        self.setCentralWidget(self.board)
        if kwargs['borderless'] == 'True':
            self.windowed()
        self.show()

    def windowed(self):
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))


class Menu(QWidget):
    def __init__(self, parent):
        super(Menu, self).__init__(parent)
        self.QV = QVBoxLayout()
        self.QH = QHBoxLayout(self)
        self.label = QLabel("Main Menu", self)
        font = QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        # setting font to the head
        self.label.setFont(font)

        # setting alignment of the head
        self.label.setAlignment(Qt.AlignCenter)

        self.QV.addStretch(1)
        self.QV.addWidget(self.label)
        self.QV.addStretch(1)

        self.QH.addStretch(1)
        self.QH.addLayout(self.QV)
        self.QH.addStretch(1)
        self.setLayout(self.QH)
