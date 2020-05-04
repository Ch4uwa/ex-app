"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
import sys

from PySide2.QtCore import Slot, Signal, Qt
from PySide2.QtWidgets import QWidget, QFormLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, \
    QVBoxLayout, QLayout, QApplication, QMessageBox
from MyApp.db_functions.database import DataBaseActions


class LoginView(QWidget):
    # Custom signals
    authenticated = Signal(str)

    def __init__(self):
        super(LoginView, self).__init__()
        self.setObjectName('LoginView')
        self.create_view()

        self.login_attempts = 0
        self.max_attempts = 5

        self.min_username_len = 3
        self.min_password_len = 4

    def create_view(self):
        grid_layout = QGridLayout()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.setSizeConstraint(QLayout.SetFixedSize)

        self.login_btn = QPushButton('Login')
        self.register_btn = QPushButton('Register')
        self.cancel_btn = QPushButton('Cancel')
        self.username_lbl = QLabel('Username')
        self.password_lbl = QLabel('Password')
        self.top_label = QLabel('Login')
        self.username_box = QLineEdit()
        self.password_box = QLineEdit()

        self.password_box.setEchoMode(QLineEdit.Password)
        self.password_box.setMaxLength(30)
        self.username_box.setMaxLength(20)

        self.login_btn.setEnabled(False)
        self.register_btn.setEnabled(False)

        grid_layout.addWidget(self.username_lbl, 1, 0)
        grid_layout.addWidget(self.username_box, 1, 1)
        grid_layout.addWidget(self.password_lbl, 2, 0)
        grid_layout.addWidget(self.password_box, 2, 1)

        v_layout.addStretch(1)
        v_layout.addWidget(self.top_label, alignment=Qt.AlignCenter)
        v_layout.addLayout(grid_layout)
        v_layout.addWidget(self.login_btn)
        v_layout.addWidget(self.register_btn)
        v_layout.addWidget(self.cancel_btn)
        v_layout.addStretch(1)

        h_layout.addStretch(1)
        h_layout.addLayout(v_layout)
        h_layout.addStretch(1)

        self.setLayout(h_layout)

        # Connect button
        self.login_btn.clicked.connect(self.authenticate)
        self.register_btn.clicked.connect(self.register_action)
        self.cancel_btn.clicked.connect(self.exit_application)

        self.username_box.textChanged.connect(self.check_enabled)
        self.password_box.textChanged.connect(self.check_enabled)

    def save_name_pass(self):
        print(self.username_box.text())
        print(self.password_box.text())

    def exit_application(self):
        QApplication.quit()

    @Slot()
    def check_enabled(self):
        if len(self.username_box.text()) > self.min_username_len and len(
                self.password_box.text()) > self.min_password_len:
            self.login_btn.setEnabled(True)
            self.register_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)
            self.register_btn.setEnabled(False)

    @Slot()
    def authenticate(self):
        if DataBaseActions().verify_user(username=self.username_box.text(), password=self.password_box.text()):
            self.authenticated.emit(self.username_box.text())
        else:
            self.top_label.setText('Wrong username or password')

    @Slot()
    def register_action(self):
        if DataBaseActions().insert_user(self.username_box.text(), self.password_box.text()):
            self.username_box.setText('')
            self.password_box.setText('')
        else:
            # Todo add messagebox to login instead
            pass
