# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'DialogSaveAs.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_DialogSaveAs(object):
    def setupUi(self, DialogSaveAs):
        if not DialogSaveAs.objectName():
            DialogSaveAs.setObjectName(u"DialogSaveAs")
        DialogSaveAs.resize(558, 99)
        DialogSaveAs.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(DialogSaveAs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(DialogSaveAs)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_SaveAsFolder = QLineEdit(DialogSaveAs)
        self.lineEdit_SaveAsFolder.setObjectName(u"lineEdit_SaveAsFolder")

        self.gridLayout.addWidget(self.lineEdit_SaveAsFolder, 1, 1, 1, 1)

        self.lineEdit_SaveAsFileName = QLineEdit(DialogSaveAs)
        self.lineEdit_SaveAsFileName.setObjectName(u"lineEdit_SaveAsFileName")

        self.gridLayout.addWidget(self.lineEdit_SaveAsFileName, 0, 1, 1, 1)

        self.label = QLabel(DialogSaveAs)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_selectPath = QPushButton(DialogSaveAs)
        self.pushButton_selectPath.setObjectName(u"pushButton_selectPath")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_selectPath.sizePolicy().hasHeightForWidth())
        self.pushButton_selectPath.setSizePolicy(sizePolicy)
        self.pushButton_selectPath.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.pushButton_selectPath, 1, 2, 1, 1)

        self.pushButton_OK = QPushButton(DialogSaveAs)
        self.pushButton_OK.setObjectName(u"pushButton_OK")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_OK.sizePolicy().hasHeightForWidth())
        self.pushButton_OK.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_OK, 2, 1, 1, 1)


        self.retranslateUi(DialogSaveAs)

        QMetaObject.connectSlotsByName(DialogSaveAs)
    # setupUi

    def retranslateUi(self, DialogSaveAs):
        DialogSaveAs.setWindowTitle(QCoreApplication.translate("DialogSaveAs", u"Save as", None))
        self.label_2.setText(QCoreApplication.translate("DialogSaveAs", u"Folder:", None))
        self.label.setText(QCoreApplication.translate("DialogSaveAs", u"File Name:", None))
        self.pushButton_selectPath.setText(QCoreApplication.translate("DialogSaveAs", u"select", None))
        self.pushButton_OK.setText(QCoreApplication.translate("DialogSaveAs", u"Save", None))
    # retranslateUi

