# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'DialogError.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_DialogError(object):
    def setupUi(self, DialogError):
        if not DialogError.objectName():
            DialogError.setObjectName(u"DialogError")
        DialogError.resize(395, 342)
        DialogError.setLayoutDirection(Qt.LeftToRight)
        DialogError.setAutoFillBackground(False)
        DialogError.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(DialogError)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser_Error = QTextBrowser(DialogError)
        self.textBrowser_Error.setObjectName(u"textBrowser_Error")

        self.gridLayout.addWidget(self.textBrowser_Error, 4, 0, 1, 1)

        self.pushButton_OK_DialogError = QPushButton(DialogError)
        self.pushButton_OK_DialogError.setObjectName(u"pushButton_OK_DialogError")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OK_DialogError.sizePolicy().hasHeightForWidth())
        self.pushButton_OK_DialogError.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_OK_DialogError, 7, 0, 1, 1)

        self.textBrowser_Suggestion = QTextBrowser(DialogError)
        self.textBrowser_Suggestion.setObjectName(u"textBrowser_Suggestion")

        self.gridLayout.addWidget(self.textBrowser_Suggestion, 6, 0, 1, 1)

        self.label = QLabel(DialogError)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(DialogError)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)


        self.retranslateUi(DialogError)

        QMetaObject.connectSlotsByName(DialogError)
    # setupUi

    def retranslateUi(self, DialogError):
        DialogError.setWindowTitle(QCoreApplication.translate("DialogError", u"Error", None))
        self.textBrowser_Error.setMarkdown("")
        self.textBrowser_Error.setHtml(QCoreApplication.translate("DialogError", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_OK_DialogError.setText(QCoreApplication.translate("DialogError", u"OK", None))
        self.label.setText(QCoreApplication.translate("DialogError", u"[Error]", None))
        self.label_2.setText(QCoreApplication.translate("DialogError", u"[Suggestion to solve the error]", None))
    # retranslateUi

