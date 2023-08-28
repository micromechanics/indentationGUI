# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'DialogExport.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_DialogExport(object):
    def setupUi(self, DialogExport):
        if not DialogExport.objectName():
            DialogExport.setObjectName(u"DialogExport")
        DialogExport.resize(558, 153)
        self.gridLayout = QGridLayout(DialogExport)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(DialogExport)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_ExportTab = QComboBox(DialogExport)
        self.comboBox_ExportTab.addItem("")
        self.comboBox_ExportTab.addItem("")
        self.comboBox_ExportTab.setObjectName(u"comboBox_ExportTab")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ExportTab.sizePolicy().hasHeightForWidth())
        self.comboBox_ExportTab.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.comboBox_ExportTab, 0, 1, 1, 1)

        self.label_4 = QLabel(DialogExport)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_ExportFileName = QLineEdit(DialogExport)
        self.lineEdit_ExportFileName.setObjectName(u"lineEdit_ExportFileName")

        self.gridLayout.addWidget(self.lineEdit_ExportFileName, 1, 1, 1, 1)

        self.label = QLabel(DialogExport)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_ExportFolder = QLineEdit(DialogExport)
        self.lineEdit_ExportFolder.setObjectName(u"lineEdit_ExportFolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_ExportFolder.sizePolicy().hasHeightForWidth())
        self.lineEdit_ExportFolder.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lineEdit_ExportFolder, 2, 1, 1, 1)

        self.pushButton_selectPath = QPushButton(DialogExport)
        self.pushButton_selectPath.setObjectName(u"pushButton_selectPath")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_selectPath.sizePolicy().hasHeightForWidth())
        self.pushButton_selectPath.setSizePolicy(sizePolicy2)
        self.pushButton_selectPath.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.pushButton_selectPath, 2, 2, 1, 1)

        self.label_3 = QLabel(DialogExport)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.comboBox_ExportFormat = QComboBox(DialogExport)
        self.comboBox_ExportFormat.addItem("")
        self.comboBox_ExportFormat.addItem("")
        self.comboBox_ExportFormat.addItem("")
        self.comboBox_ExportFormat.setObjectName(u"comboBox_ExportFormat")
        sizePolicy.setHeightForWidth(self.comboBox_ExportFormat.sizePolicy().hasHeightForWidth())
        self.comboBox_ExportFormat.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.comboBox_ExportFormat, 3, 1, 1, 1)

        self.pushButton_OK = QPushButton(DialogExport)
        self.pushButton_OK.setObjectName(u"pushButton_OK")
        self.pushButton_OK.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_OK.sizePolicy().hasHeightForWidth())
        self.pushButton_OK.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_OK, 4, 1, 1, 1)


        self.retranslateUi(DialogExport)

        QMetaObject.connectSlotsByName(DialogExport)
    # setupUi

    def retranslateUi(self, DialogExport):
        DialogExport.setWindowTitle(QCoreApplication.translate("DialogExport", u"Export Results", None))
        self.label_2.setText(QCoreApplication.translate("DialogExport", u"Tab:", None))
        self.comboBox_ExportTab.setItemText(0, QCoreApplication.translate("DialogExport", u"Hardness and Young's Modulus", None))
        self.comboBox_ExportTab.setItemText(1, QCoreApplication.translate("DialogExport", u"Analyse Pop-in Effect", None))

        self.label_4.setText(QCoreApplication.translate("DialogExport", u"File Name:", None))
        self.lineEdit_ExportFileName.setText(QCoreApplication.translate("DialogExport", u"Ouput.xlsx", None))
        self.label.setText(QCoreApplication.translate("DialogExport", u"Folder:", None))
        self.pushButton_selectPath.setText(QCoreApplication.translate("DialogExport", u"select", None))
        self.label_3.setText(QCoreApplication.translate("DialogExport", u"Format:", None))
        self.comboBox_ExportFormat.setItemText(0, QCoreApplication.translate("DialogExport", u"Each Test in one Sheet", None))
        self.comboBox_ExportFormat.setItemText(1, QCoreApplication.translate("DialogExport", u"All Tests in one Sheet", None))
        self.comboBox_ExportFormat.setItemText(2, "")

        self.pushButton_OK.setText(QCoreApplication.translate("DialogExport", u"Export", None))
    # retranslateUi

