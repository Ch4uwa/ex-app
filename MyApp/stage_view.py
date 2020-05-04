"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com

Stage map and stage information
"""
from PySide2.QtWidgets import QWidget


class StageView(QWidget):
    """
    More specific information
    Stage map, Stage information
    """
    def __init__(self):
        super(StageView, self).__init__()
        self.setObjectName('StageView')
        pass
