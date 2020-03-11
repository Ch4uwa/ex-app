# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 547)
        icon = QIcon()
        icon.addFile(u"../res/img/jk_troll.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.actionPage_1 = QAction(Form)
        self.actionPage_1.setObjectName(u"actionPage_1")
        self.actionPage_2 = QAction(Form)
        self.actionPage_2.setObjectName(u"actionPage_2")
        self.actionQuit = QAction(Form)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionchange_page = QAction(Form)
        self.actionchange_page.setObjectName(u"actionchange_page")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.formLayout = QFormLayout(self.page)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(24, 24))
        self.toolButton.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.toolButton, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.retranslateUi(Form)
        self.stackedWidget.currentChanged.connect(self.label.setNum)
        self.actionQuit.triggered.connect(Form.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.actionPage_1.setText(QCoreApplication.translate("Form", u"Page 1", None))
        self.actionPage_2.setText(QCoreApplication.translate("Form", u"Page 2", None))
        self.actionQuit.setText(QCoreApplication.translate("Form", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("Form", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionchange_page.setText(QCoreApplication.translate("Form", u"change page", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Label 2", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.label.setText(QCoreApplication.translate("Form", u"Label 1", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"Menu", None))
    # retranslateUi

