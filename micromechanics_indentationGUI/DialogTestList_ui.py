# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'DialogTestList.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHeaderView, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_DialogTestList(object):
    def setupUi(self, DialogTestList):
        if not DialogTestList.objectName():
            DialogTestList.setObjectName(u"DialogTestList")
        DialogTestList.resize(795, 712)
        DialogTestList.setLayoutDirection(Qt.LeftToRight)
        DialogTestList.setAutoFillBackground(False)
        DialogTestList.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(DialogTestList)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_SelectAll = QPushButton(DialogTestList)
        self.pushButton_SelectAll.setObjectName(u"pushButton_SelectAll")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SelectAll.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectAll.setSizePolicy(sizePolicy)
        self.pushButton_SelectAll.setMinimumSize(QSize(0, 0))
        self.pushButton_SelectAll.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.pushButton_SelectAll, 6, 0, 1, 1)

        self.plainTextEdit_SelectTypedTest = QPlainTextEdit(DialogTestList)
        self.plainTextEdit_SelectTypedTest.setObjectName(u"plainTextEdit_SelectTypedTest")
        sizePolicy.setHeightForWidth(self.plainTextEdit_SelectTypedTest.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_SelectTypedTest.setSizePolicy(sizePolicy)
        self.plainTextEdit_SelectTypedTest.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_SelectTypedTest.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.plainTextEdit_SelectTypedTest, 3, 0, 1, 1)

        self.tableWidget = QTableWidget(DialogTestList)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font = QFont()
        font.setPointSize(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(9)
        self.tableWidget.setFont(font1)
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setInputMethodHints(Qt.ImhNone)
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(68)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 2, 1)

        self.pushButton_SelectTypedTest = QPushButton(DialogTestList)
        self.pushButton_SelectTypedTest.setObjectName(u"pushButton_SelectTypedTest")
        sizePolicy.setHeightForWidth(self.pushButton_SelectTypedTest.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectTypedTest.setSizePolicy(sizePolicy)
        self.pushButton_SelectTypedTest.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.pushButton_SelectTypedTest, 5, 0, 1, 1)


        self.retranslateUi(DialogTestList)

        QMetaObject.connectSlotsByName(DialogTestList)
    # setupUi

    def retranslateUi(self, DialogTestList):
        DialogTestList.setWindowTitle(QCoreApplication.translate("DialogTestList", u"Test list", None))
        self.pushButton_SelectAll.setText(QCoreApplication.translate("DialogTestList", u"Select/ Unselect all", None))
        self.plainTextEdit_SelectTypedTest.setPlaceholderText(QCoreApplication.translate("DialogTestList", u"e.g. 1-10, 12,15  ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogTestList", u"(use?) Test", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogTestList", u"Indentify?", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogTestList", u"Surface\n"
"Index", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogTestList", u"Frame\n"
"Compliance\n"
"[\u00b5m/mN]", None));
#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.pushButton_SelectTypedTest.setToolTip(QCoreApplication.translate("DialogTestList", u"How to select test(s)? see Q3 in Document from Help", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_SelectTypedTest.setText(QCoreApplication.translate("DialogTestList", u"Select the typed test(s)", None))
    # retranslateUi

