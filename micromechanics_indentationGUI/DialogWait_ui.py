# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'DialogWait.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_DialogWait(object):
    def setupUi(self, DialogWait):
        if not DialogWait.objectName():
            DialogWait.setObjectName(u"DialogWait")
        DialogWait.resize(395, 204)
        DialogWait.setLayoutDirection(Qt.LeftToRight)
        DialogWait.setAutoFillBackground(False)
        DialogWait.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(DialogWait)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_OK_DialogWait = QPushButton(DialogWait)
        self.pushButton_OK_DialogWait.setObjectName(u"pushButton_OK_DialogWait")

        self.gridLayout.addWidget(self.pushButton_OK_DialogWait, 4, 0, 1, 1)

        self.textBrowser_Info = QTextBrowser(DialogWait)
        self.textBrowser_Info.setObjectName(u"textBrowser_Info")

        self.gridLayout.addWidget(self.textBrowser_Info, 3, 0, 1, 1)


        self.retranslateUi(DialogWait)

        QMetaObject.connectSlotsByName(DialogWait)
    # setupUi

    def retranslateUi(self, DialogWait):
        DialogWait.setWindowTitle(QCoreApplication.translate("DialogWait", u"Waiting", None))
        self.pushButton_OK_DialogWait.setText(QCoreApplication.translate("DialogWait", u"OK", None))
    # retranslateUi

