"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
import sys
import time

from PySide2.QtWidgets import QStackedWidget, QLabel, QApplication, QPushButton, QHBoxLayout


class WidgetStack(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setCurrentIndex(0)

        btn1 = QPushButton('1')
        btn2 = QPushButton('2')
        btn3 = QPushButton('3')
        btn4 = QPushButton('4')

        layout = QHBoxLayout

        self.addWidget(btn1)
        self.addWidget(btn2)
        self.addWidget(btn3)
        self.addWidget(btn4)
        print(self.get_stack())

        btn1.clicked.connect(self.change_active_widget)
        btn2.clicked.connect(self.change_active_widget)
        btn3.clicked.connect(self.change_active_widget)
        btn4.clicked.connect(self.change_active_widget)

    def get_stack(self):
        return self.count()

    def change_active_widget(self):
        self.setCurrentIndex(self.currentIndex() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = WidgetStack()
    win.show()

    sys.exit(app.exec_())
