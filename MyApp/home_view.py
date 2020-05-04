"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com

Choose location and other main functions
"""
import sys

from PySide2.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout


class HomeView(QWidget):
    def __init__(self):
        super(HomeView, self).__init__()
        self.setObjectName('HomeView')
        label = QLabel('Hello')

        layout = QHBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HomeView()
    win.show()

    sys.exit(app.exec_())
