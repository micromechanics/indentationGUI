# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'DialogPathList.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_DialogPathList(object):
    def setupUi(self, DialogPathList):
        if not DialogPathList.objectName():
            DialogPathList.setObjectName(u"DialogPathList")
        DialogPathList.resize(1114, 712)
        DialogPathList.setLayoutDirection(Qt.LeftToRight)
        DialogPathList.setAutoFillBackground(False)
        DialogPathList.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(DialogPathList)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_path = QTableWidget(DialogPathList)
        if (self.tableWidget_path.columnCount() < 1):
            self.tableWidget_path.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_path.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_path.rowCount() < 1):
            self.tableWidget_path.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_path.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setCheckState(Qt.Unchecked);
        self.tableWidget_path.setItem(0, 0, __qtablewidgetitem2)
        self.tableWidget_path.setObjectName(u"tableWidget_path")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_path.sizePolicy().hasHeightForWidth())
        self.tableWidget_path.setSizePolicy(sizePolicy)
        self.tableWidget_path.setMinimumSize(QSize(350, 100))
        self.tableWidget_path.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_path.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_path.setShowGrid(True)
        self.tableWidget_path.setSortingEnabled(False)
        self.tableWidget_path.horizontalHeader().setVisible(False)
        self.tableWidget_path.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_path.horizontalHeader().setMinimumSectionSize(57)
        self.tableWidget_path.horizontalHeader().setDefaultSectionSize(600)
        self.tableWidget_path.horizontalHeader().setHighlightSections(True)
        self.tableWidget_path.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_path.verticalHeader().setVisible(True)
        self.tableWidget_path.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget_path.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_path.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget_path, 0, 0, 6, 1)

        self.pushButton_addFile = QPushButton(DialogPathList)
        self.pushButton_addFile.setObjectName(u"pushButton_addFile")
        self.pushButton_addFile.setMinimumSize(QSize(36, 26))
        self.pushButton_addFile.setMaximumSize(QSize(36, 16777215))
#if QT_CONFIG(tooltip)
        self.pushButton_addFile.setToolTip(u" Add a new test  file to the list")
#endif // QT_CONFIG(tooltip)
        icon = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_addFile.setIcon(icon)
        self.pushButton_addFile.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_addFile, 0, 1, 1, 1)

        self.pushButton_MoveFileUp = QPushButton(DialogPathList)
        self.pushButton_MoveFileUp.setObjectName(u"pushButton_MoveFileUp")
        self.pushButton_MoveFileUp.setMinimumSize(QSize(36, 26))
        self.pushButton_MoveFileUp.setMaximumSize(QSize(36, 16777215))
#if QT_CONFIG(tooltip)
        self.pushButton_MoveFileUp.setToolTip(u" Add a new test  file to the list")
#endif // QT_CONFIG(tooltip)
        icon1 = QIcon()
        iconThemeName = u"go-up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_MoveFileUp.setIcon(icon1)
        self.pushButton_MoveFileUp.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_MoveFileUp, 1, 1, 1, 1)

        self.pushButton_changeFile = QPushButton(DialogPathList)
        self.pushButton_changeFile.setObjectName(u"pushButton_changeFile")
        self.pushButton_changeFile.setMinimumSize(QSize(36, 26))
        self.pushButton_changeFile.setMaximumSize(QSize(36, 16777215))
        icon2 = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_changeFile.setIcon(icon2)
        self.pushButton_changeFile.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_changeFile, 2, 1, 1, 1)

        self.pushButton_MoveFileDown = QPushButton(DialogPathList)
        self.pushButton_MoveFileDown.setObjectName(u"pushButton_MoveFileDown")
        self.pushButton_MoveFileDown.setMinimumSize(QSize(36, 26))
        self.pushButton_MoveFileDown.setMaximumSize(QSize(36, 16777215))
#if QT_CONFIG(tooltip)
        self.pushButton_MoveFileDown.setToolTip(u" Add a new test  file to the list")
#endif // QT_CONFIG(tooltip)
        icon3 = QIcon()
        iconThemeName = u"go-down"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_MoveFileDown.setIcon(icon3)
        self.pushButton_MoveFileDown.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_MoveFileDown, 3, 1, 1, 1)

        self.pushButton_deleteFile = QPushButton(DialogPathList)
        self.pushButton_deleteFile.setObjectName(u"pushButton_deleteFile")
        self.pushButton_deleteFile.setMinimumSize(QSize(36, 26))
        self.pushButton_deleteFile.setMaximumSize(QSize(36, 16777215))
        icon4 = QIcon()
        iconThemeName = u"list-remove"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_deleteFile.setIcon(icon4)
        self.pushButton_deleteFile.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_deleteFile, 4, 1, 1, 1)


        self.retranslateUi(DialogPathList)

        self.pushButton_addFile.setDefault(False)
        self.pushButton_MoveFileUp.setDefault(False)
        self.pushButton_MoveFileDown.setDefault(False)


        QMetaObject.connectSlotsByName(DialogPathList)
    # setupUi

    def retranslateUi(self, DialogPathList):
        DialogPathList.setWindowTitle(QCoreApplication.translate("DialogPathList", u"Test files selection", None))
        ___qtablewidgetitem = self.tableWidget_path.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogPathList", u"Path1", None));

        __sortingEnabled = self.tableWidget_path.isSortingEnabled()
        self.tableWidget_path.setSortingEnabled(False)
        self.tableWidget_path.setSortingEnabled(__sortingEnabled)

        self.pushButton_addFile.setText("")
        self.pushButton_MoveFileUp.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_changeFile.setToolTip(QCoreApplication.translate("DialogPathList", u"Edit the selected test file", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_changeFile.setText("")
        self.pushButton_MoveFileDown.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_deleteFile.setToolTip(QCoreApplication.translate("DialogPathList", u"Remove the selected test file from the list", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_deleteFile.setText("")
    # retranslateUi

