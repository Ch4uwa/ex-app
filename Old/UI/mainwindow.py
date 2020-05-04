"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""

from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QAction, QApplication


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Thing')
        self.set_icon()

        # Menu
        self.menu = self.menuBar()
        self.main_menu = self.menu.addMenu('&Menu')

        self.action_quit = QAction('&Quit', self)
        self.action_quit.setShortcut('Ctrl+Q')
        self.action_quit.triggered.connect(self.close_application)

        self.main_menu.addAction(self.action_quit)
        self.setCentralWidget(widget)

    @Slot()
    def close_application(self, checked):
        QApplication.quit()

    def set_icon(self):
        app_icon = QIcon("../MyApp/res/icon/jk_troll24x24.png")
        try:
            self.setWindowIcon(app_icon)
        except Exception as e:
            print('Exception:', e)
