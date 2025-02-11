# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Permutations_repetitions.ui'
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
                               QLineEdit, QSizePolicy, QWidget)


class Ui_Dialog_Permutations_repetitions(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 623)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 210, 513, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 310, 492, 34))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.Permutations_repetitions_answer = QLineEdit(self.widget)
        self.Permutations_repetitions_answer.setObjectName(
            u"Permutations_repetitions_answer")

        self.horizontalLayout.addWidget(self.Permutations_repetitions_answer)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u041f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0441 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f\u043c\u0438", None))
        self.label_2.setText(QCoreApplication.translate(
            "Dialog", u"Pn(m1,...,mk) = n! / m1!*...*mk! = ", None))
    # retranslateUi
