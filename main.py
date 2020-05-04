"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""

import sys

from PySide2.QtWidgets import QApplication

from Old.UI import MainWindow
from Old.UI import Widget


def run():
    app = QApplication(sys.argv)

    widget = Widget()
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
