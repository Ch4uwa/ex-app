"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
import os
import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QStackedWidget, QWidget
from MyApp.view_manager import ViewManager


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super(MainWindow, self).__init__()
        self.setup_window(widget)

    def setup_window(self, widget):
        self.setGeometry(400, 400, 400, 700)
        self.setFixedSize(400, 700)
        self.setWindowTitle('My App')
        self.statusBar()

        self.setCentralWidget(widget)

        self.show()


def run():
    app = QApplication(sys.argv)
    stacked_widget = ViewManager()
    win = MainWindow(stacked_widget)

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
