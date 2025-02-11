# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Placements.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
                               QSizePolicy, QWidget)


class Ui_Dialog_placement(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 626)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 220, 208, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 300, 196, 32))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.Placements_answer = QLineEdit(Dialog)
        self.Placements_answer.setObjectName(u"Placements_answer")
        self.Placements_answer.setGeometry(QRect(410, 310, 113, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate(
            "Dialog", u"A = n! / (n - m)! = ", None))
    # retranslateUi
