"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtWidgets import (QFrame, QApplication, QWidget, QPushButton,
                               QStackedLayout, QVBoxLayout, QHBoxLayout,
                               QLabel)


class MainFrame(QFrame):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.setWindowTitle('Main Window')
        self.setFixedSize(360, 720)

        try:
            self.setWindowIcon(QIcon(QPixmap('../MyApp/res/icon/jk_troll.png')))
        except Exception as e:
            print(e)

        self.frame_setup()

    def frame_setup(self):
        layout = QVBoxLayout()
        layout_btn = QHBoxLayout()

        # Buttons
        btn = QPushButton('Im a RED button')
        btn2 = QPushButton('Im a GREEN button')

        layout_btn.addWidget(btn)
        layout_btn.addWidget(btn2)

        # Add to layout
        layout.addLayout(layout_btn)

        # Set alignment
        layout.setAlignment(layout_btn, Qt.AlignBottom)

        # Set window layout
        self.setLayout(layout)


def run():
    app = QApplication(sys.argv)

    window = MainFrame()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
