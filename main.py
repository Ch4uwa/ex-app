"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""

import sys

from PySide2.QtWidgets import QApplication

from UI.mainwindow import MainWindow
from UI.expensesWindow import Widget


# class Widget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.items = 0
#
#         # Example data
#         self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
#                       "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
#                       "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}
#
#         # Left
#         self.table = QTableWidget()
#         self.table.setColumnCount(2)
#         self.table.setHorizontalHeaderLabels(['Description', 'Price'])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#
#         # Chart
#         self.chart_view = QtCharts.QChartView()
#         self.chart_view.setRenderHint(QPainter.Antialiasing)
#
#         # Right
#         self.description = QLineEdit()
#         self.price = QLineEdit()
#         self.btn_add = QPushButton('Add')
#         self.btn_clear = QPushButton('Clear')
#         self.btn_quit = QPushButton('Quit')
#         self.btn_plot = QPushButton('Plot')
#
#         # Disabling 'Add' button
#         self.btn_add.setEnabled(False)
#
#         self.side_right = QVBoxLayout()
#         self.side_right.setMargin(10)
#         self.side_right.addWidget(QLabel('Description'))
#         self.side_right.addWidget(self.description)
#         self.side_right.addWidget(QLabel('Price'))
#         self.side_right.addWidget(self.price)
#         self.side_right.addWidget(self.btn_add)
#         self.side_right.addWidget(self.btn_plot)
#         self.side_right.addWidget(self.chart_view)
#         self.side_right.addWidget(self.btn_clear)
#         self.side_right.addWidget(self.btn_quit)
#
#         # Widget Layout
#         self.layout = QHBoxLayout()
#
#         self.layout.addWidget(self.table)
#         self.layout.addLayout(self.side_right)
#
#         # Set Layout to Widget
#         self.setLayout(self.layout)
#
#         # Signals
#         self.btn_add.clicked.connect(self.add_element)
#         self.btn_quit.clicked.connect(self.close_application)
#         self.btn_clear.clicked.connect(self.clear_table)
#         self.btn_plot.clicked.connect(self.plot_data)
#         self.description.textChanged[str].connect(self.check_disable)
#         self.price.textChanged[str].connect(self.check_disable)
#
#         self.fill_table()
#
#     # Slots
#     @Slot()
#     def plot_data(self):
#         # Get table information
#         series = QtCharts.QPieSeries()
#         for i in range(self.table.rowCount()):
#             text = self.table.item(i, 0).text()
#             number = float(self.table.item(i, 1).text())
#             series.append(text, number)
#
#         chart = QtCharts.QChart()
#         chart.addSeries(series)
#         chart.legend().setAlignment(Qt.AlignLeft)
#         self.chart_view.setChart(chart)
#
#     @Slot()
#     def close_application(self):
#         QApplication.quit()
#
#     @Slot()
#     def clear_table(self):
#         self.table.setRowCount(0)
#         self.items = 0
#
#     @Slot()
#     def check_disable(self, s):
#         if not self.description.text() or not self.price.text():
#             self.btn_add.setEnabled(False)
#         else:
#             self.btn_add.setEnabled(True)
#
#     @Slot()
#     def add_element(self):
#         des = self.description.text()
#         price = self.price.text()
#
#         self.table.insertRow(self.items)
#         description_item = QTableWidgetItem(des)
#         price_item = QTableWidgetItem('{:.2f}'.format(float(price)))
#         price_item.setTextAlignment(Qt.AlignRight)
#
#         self.table.setItem(self.items, 0, description_item)
#         self.table.setItem(self.items, 1, price_item)
#
#         self.description.setText('')
#         self.price.setText('')
#
#         self.items += 1
#
#     def fill_table(self, data=None):
#         data = self._data if not data else data
#         for desc, price in data.items():
#             description_item = QTableWidgetItem(desc)
#             price_item = QTableWidgetItem('{:.2f}'.format(price))
#             price_item.setTextAlignment(Qt.AlignRight)
#             self.table.insertRow(self.items)
#             self.table.setItem(self.items, 0, description_item)
#             self.table.setItem(self.items, 1, price_item)
#             self.items += 1


# class MainWindow(QMainWindow):
#     def __init__(self, widget):
#         super(MainWindow, self).__init__()
#
#         # Menu
#         self.menu = self.menuBar()
#         self.main_menu = self.menu.addMenu('&Menu')
#
#         self.action_quit = QAction('&Quit', self)
#         self.action_quit.setShortcut('Ctrl+Q')
#         self.action_quit.triggered.connect(self.close_application)
#
#         self.main_menu.addAction(self.action_quit)
#         self.setCentralWidget(widget)
#
#     @Slot()
#     def close_application(self, checked):
#         QApplication.quit()


def run():
    app = QApplication(sys.argv)

    widget = Widget()
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
