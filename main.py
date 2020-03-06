import sys

from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QMainWindow, QApplication, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.action_quit = QAction('&Quit')

        self.menu = self.menuBar()
        self.main_menu = self.menu.addMenu('&Menu')
        self.main_menu.addAction(self.action_quit)

        self.action_quit.setShortcut('Ctrl+Q')

        self.action_quit.triggered.connect(self.close_application)

    @Slot()
    def close_application(self):
        sys.exit()


def run():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
