# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'oder.ui'
##
# Created by: Qt User Interface Compiler version 6.6.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QWidget)


class Ui_Dialog_oder(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 626)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 200, 286, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 290, 434, 43))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.oder_no = QPushButton(self.widget)
        self.oder_no.setObjectName(u"oder_no")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(22)
        self.oder_no.setFont(font1)

        self.horizontalLayout.addWidget(self.oder_no)

        self.oder_yes = QPushButton(self.widget)
        self.oder_yes.setObjectName(u"oder_yes")
        self.oder_yes.setFont(font1)

        self.horizontalLayout.addWidget(self.oder_yes)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0432\u0430\u0436\u0435\u043d ?", None))
        self.oder_no.setText(QCoreApplication.translate(
            "Dialog", u"\u041d\u0435\u0442", None))
        self.oder_yes.setText(QCoreApplication.translate(
            "Dialog", u"\u0414\u0430", None))
    # retranslateUi
