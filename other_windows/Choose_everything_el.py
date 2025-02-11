# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Choose_everything_el.ui'
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


class Ui_Dialog_choose(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 626)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 210, 567, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 310, 434, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_everything_el_no = QPushButton(self.layoutWidget)
        self.choose_everything_el_no.setObjectName(u"choose_everything_el_no")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(22)
        self.choose_everything_el_no.setFont(font1)

        self.horizontalLayout.addWidget(self.choose_everything_el_no)

        self.choose_everything_el_yes = QPushButton(self.layoutWidget)
        self.choose_everything_el_yes.setObjectName(
            u"choose_everything_el_yes")
        self.choose_everything_el_yes.setFont(font1)

        self.horizontalLayout.addWidget(self.choose_everything_el_yes)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u041d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435 n \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 ?", None))
        self.choose_everything_el_no.setText(
            QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.choose_everything_el_yes.setText(
            QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
    # retranslateUi
