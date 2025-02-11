# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Combination_repetitions.ui'
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


class Ui_Dialog_combination_repetitions(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 626)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 240, 457, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 300, 325, 32))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.Combination_repetitions_answer = QLineEdit(Dialog)
        self.Combination_repetitions_answer.setObjectName(
            u"Combination_repetitions_answer")
        self.Combination_repetitions_answer.setGeometry(
            QRect(470, 310, 113, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u044f c \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f\u043c\u0438", None))
        self.label_2.setText(QCoreApplication.translate(
            "Dialog", u"C = (n + m -1) / m! * (n - 1)! = ", None))
    # retranslateUi
