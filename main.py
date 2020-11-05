from lib.logger import config
from lib.logger import logging
from lib.window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow(borderless=config['Window']['Borderless'], x=int(config['Window']['X']), y=int(config['Window']['Y']))
    sys.exit(app.exec_())
