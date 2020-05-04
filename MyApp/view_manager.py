"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QFormLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, \
    QVBoxLayout, QLayout, QStackedWidget
from MyApp.login_view import LoginView
from MyApp.home_view import HomeView
from MyApp.location_view import LocationView
from MyApp.stage_view import StageView


class ViewManager(QStackedWidget):
    """
    Handle view stack
    """

    def __init__(self):
        super(ViewManager, self).__init__()
        self.setObjectName('ViewManager')
        self.cur_index = 0
        self.cur_user = None
        self.setCurrentIndex(self.cur_index)

        self.login_view = LoginView()
        self.home_view = HomeView()

        self.insertWidget(0, self.login_view)
        self.insertWidget(1, self.home_view)

        self.login_view.authenticated.connect(self._logged_in)

    @Slot(str)
    def _logged_in(self, username):
        self.cur_user = username

        if self.cur_user:
            self.switch_view(1)

    @Slot(int)
    def switch_view(self, i):
        self.cur_index = i
        try:
            self.setCurrentIndex(self.cur_index)
        except Exception as e:
            print(e)
            # Todo add popup window
