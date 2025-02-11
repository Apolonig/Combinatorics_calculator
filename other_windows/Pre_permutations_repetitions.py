# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Pre_permutations_repetitions.ui'
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
                               QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_Dialog_pre_permutation(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(831, 577)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 658, 17))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.counting_button = QPushButton(Dialog)
        self.counting_button.setObjectName(u"counting_button")
        self.counting_button.setGeometry(QRect(290, 500, 213, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(22)
        self.counting_button.setFont(font1)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 70, 361, 43))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(24)
        self.label_12.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.nn = QLineEdit(self.layoutWidget)
        self.nn.setObjectName(u"nn")
        self.nn.setFont(font2)

        self.horizontalLayout_11.addWidget(self.nn)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 179, 401, 43))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.m4 = QLineEdit(self.layoutWidget1)
        self.m4.setObjectName(u"m4")
        self.m4.setFont(font2)

        self.horizontalLayout_7.addWidget(self.m4)

        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 351, 401, 43))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.m8 = QLineEdit(self.layoutWidget2)
        self.m8.setObjectName(u"m8")
        self.m8.setFont(font2)

        self.horizontalLayout_10.addWidget(self.m8)

        self.layoutWidget3 = QWidget(Dialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 394, 401, 43))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_10)

        self.m9 = QLineEdit(self.layoutWidget3)
        self.m9.setObjectName(u"m9")
        self.m9.setFont(font2)

        self.horizontalLayout_9.addWidget(self.m9)

        self.layoutWidget4 = QWidget(Dialog)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(30, 93, 401, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2)

        self.m2 = QLineEdit(self.layoutWidget4)
        self.m2.setObjectName(u"m2")
        self.m2.setFont(font2)

        self.horizontalLayout.addWidget(self.m2)

        self.layoutWidget5 = QWidget(Dialog)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(30, 437, 401, 43))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.m10 = QLineEdit(self.layoutWidget5)
        self.m10.setObjectName(u"m10")
        self.m10.setFont(font2)

        self.horizontalLayout_5.addWidget(self.m10)

        self.layoutWidget6 = QWidget(Dialog)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(30, 136, 401, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.m3 = QLineEdit(self.layoutWidget6)
        self.m3.setObjectName(u"m3")
        self.m3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.m3)

        self.layoutWidget7 = QWidget(Dialog)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(30, 265, 401, 43))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.m6 = QLineEdit(self.layoutWidget7)
        self.m6.setObjectName(u"m6")
        self.m6.setFont(font2)

        self.horizontalLayout_8.addWidget(self.m6)

        self.layoutWidget8 = QWidget(Dialog)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(30, 222, 401, 43))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.m5 = QLineEdit(self.layoutWidget8)
        self.m5.setObjectName(u"m5")
        self.m5.setFont(font2)

        self.horizontalLayout_3.addWidget(self.m5)

        self.layoutWidget9 = QWidget(Dialog)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(30, 308, 401, 43))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.m7 = QLineEdit(self.layoutWidget9)
        self.m7.setObjectName(u"m7")
        self.m7.setFont(font2)

        self.horizontalLayout_4.addWidget(self.m7)

        self.layoutWidget10 = QWidget(Dialog)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(31, 51, 401, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.m1 = QLineEdit(self.layoutWidget10)
        self.m1.setObjectName(u"m1")
        self.m1.setFont(font2)

        self.horizontalLayout_6.addWidget(self.m1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u043c\u043e\u0436\u043d\u043e \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u0432\u0438\u0442\u044c m \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432, \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 1", None))
        self.counting_button.setText(QCoreApplication.translate(
            "Dialog", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.label_12.setText(
            QCoreApplication.translate("Dialog", u"n = ", None))
        self.label_8.setText(
            QCoreApplication.translate("Dialog", u"m4 = ", None))
        self.label_6.setText(
            QCoreApplication.translate("Dialog", u"m8 = ", None))
        self.label_10.setText(
            QCoreApplication.translate("Dialog", u"m9 = ", None))
        self.label_2.setText(
            QCoreApplication.translate("Dialog", u"m2 = ", None))
        self.label_11.setText(
            QCoreApplication.translate("Dialog", u"m10 = ", None))
        self.label_3.setText(
            QCoreApplication.translate("Dialog", u"m3 = ", None))
        self.label_9.setText(
            QCoreApplication.translate("Dialog", u"m6 = ", None))
        self.label_4.setText(
            QCoreApplication.translate("Dialog", u"m5 = ", None))
        self.label_5.setText(
            QCoreApplication.translate("Dialog", u"m7 = ", None))
        self.label_7.setText(
            QCoreApplication.translate("Dialog", u"m1 = ", None))
    # retranslateUi
