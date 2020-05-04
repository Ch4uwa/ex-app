"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com

More information about location
and choose stage from location
"""
from PySide2.QtWidgets import QWidget


class LocationView(QWidget):
    """
    General information of location
    """
    def __init__(self):
        super(LocationView, self).__init__()
        self.setObjectName('LocationView')
        self.name = []
