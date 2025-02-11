# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'start_ui.ui'
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
                               QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Dialog_start(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 577)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 140, 199, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.next_step_button = QPushButton(Dialog)
        self.next_step_button.setObjectName(u"next_step_button")
        self.next_step_button.setGeometry(QRect(250, 390, 213, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(22)
        self.next_step_button.setFont(font1)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 250, 567, 94))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(24)
        self.layoutWidget.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2)

        self.nn = QLineEdit(self.layoutWidget)
        self.nn.setObjectName(u"nn")
        self.nn.setFont(font2)

        self.horizontalLayout.addWidget(self.nn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.mm = QLineEdit(self.layoutWidget)
        self.mm.setObjectName(u"mm")
        self.mm.setFont(font2)

        self.horizontalLayout_2.addWidget(self.mm)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435", None))
        self.next_step_button.setText(QCoreApplication.translate(
            "Dialog", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0448\u0430\u0433", None))
        self.label_2.setText(QCoreApplication.translate(
            "Dialog", u"n - \u043e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 = ", None))
        self.label_3.setText(QCoreApplication.translate(
            "Dialog", u"m - \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0432\u044b\u0431\u0438\u0440\u0430\u0435\u043c = ", None))
    # retranslateUi
