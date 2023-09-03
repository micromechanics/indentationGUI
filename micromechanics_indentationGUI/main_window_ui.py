# -*- coding: utf-8 -*-
# pylint: skip-file
################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QGraphicsView, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1485, 834)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setCheckable(False)
        self.actionNew.setEnabled(True)
        self.actionNew.setVisible(True)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(True)
        self.actionSave.setShortcutContext(Qt.WidgetShortcut)
        self.actionSave.setShortcutVisibleInContextMenu(True)
        self.actionSave.setPriority(QAction.HighPriority)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionRecent1 = QAction(MainWindow)
        self.actionRecent1.setObjectName(u"actionRecent1")
        self.actionAAA = QAction(MainWindow)
        self.actionAAA.setObjectName(u"actionAAA")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_30 = QGridLayout(self.centralwidget)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tab_calibration = QWidget()
        self.tab_calibration.setObjectName(u"tab_calibration")
        sizePolicy.setHeightForWidth(self.tab_calibration.sizePolicy().hasHeightForWidth())
        self.tab_calibration.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.tab_calibration)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_59 = QGroupBox(self.tab_calibration)
        self.groupBox_59.setObjectName(u"groupBox_59")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_59.sizePolicy().hasHeightForWidth())
        self.groupBox_59.setSizePolicy(sizePolicy1)
        self.groupBox_59.setMinimumSize(QSize(460, 0))
        self.groupBox_59.setMaximumSize(QSize(460, 69))
        self.gridLayout_112 = QGridLayout(self.groupBox_59)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.comboBox_CalculationMethod_tabTAF = QComboBox(self.groupBox_59)
        self.comboBox_CalculationMethod_tabTAF.addItem("")
        self.comboBox_CalculationMethod_tabTAF.addItem("")
        self.comboBox_CalculationMethod_tabTAF.setObjectName(u"comboBox_CalculationMethod_tabTAF")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_CalculationMethod_tabTAF.sizePolicy().hasHeightForWidth())
        self.comboBox_CalculationMethod_tabTAF.setSizePolicy(sizePolicy2)
        self.comboBox_CalculationMethod_tabTAF.setEditable(False)

        self.gridLayout_112.addWidget(self.comboBox_CalculationMethod_tabTAF, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_59, 2, 0, 1, 2)

        self.pushButton_SelectAll_tabTAF = QPushButton(self.tab_calibration)
        self.pushButton_SelectAll_tabTAF.setObjectName(u"pushButton_SelectAll_tabTAF")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectAll_tabTAF.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectAll_tabTAF.setSizePolicy(sizePolicy1)
        self.pushButton_SelectAll_tabTAF.setMinimumSize(QSize(200, 0))
        self.pushButton_SelectAll_tabTAF.setMaximumSize(QSize(200, 1000))

        self.gridLayout_2.addWidget(self.pushButton_SelectAll_tabTAF, 3, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_calibration)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(224, 0))
        self.groupBox_5.setMaximumSize(QSize(224, 100))
        self.gridLayout_12 = QGridLayout(self.groupBox_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.spinBox_DataFilterSize_tabTAF = QSpinBox(self.groupBox_5)
        self.spinBox_DataFilterSize_tabTAF.setObjectName(u"spinBox_DataFilterSize_tabTAF")
        self.spinBox_DataFilterSize_tabTAF.setValue(5)

        self.gridLayout_12.addWidget(self.spinBox_DataFilterSize_tabTAF, 2, 1, 1, 1)

        self.doubleSpinBox_Rate2findSurface_tabTAF = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_Rate2findSurface_tabTAF.setObjectName(u"doubleSpinBox_Rate2findSurface_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabTAF.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabTAF.setValue(1.000000000000000)

        self.gridLayout_12.addWidget(self.doubleSpinBox_Rate2findSurface_tabTAF, 1, 1, 1, 1)

        self.label_87 = QLabel(self.groupBox_5)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_87, 2, 0, 1, 1)

        self.checkBox_UsingRate2findSurface_tabTAF = QCheckBox(self.groupBox_5)
        self.checkBox_UsingRate2findSurface_tabTAF.setObjectName(u"checkBox_UsingRate2findSurface_tabTAF")
        sizePolicy1.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabTAF.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabTAF.setSizePolicy(sizePolicy1)
        self.checkBox_UsingRate2findSurface_tabTAF.setChecked(True)

        self.gridLayout_12.addWidget(self.checkBox_UsingRate2findSurface_tabTAF, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_5, 4, 1, 1, 1)

        self.groupBox_48 = QGroupBox(self.tab_calibration)
        self.groupBox_48.setObjectName(u"groupBox_48")
        sizePolicy1.setHeightForWidth(self.groupBox_48.sizePolicy().hasHeightForWidth())
        self.groupBox_48.setSizePolicy(sizePolicy1)
        self.groupBox_48.setMinimumSize(QSize(200, 0))
        self.groupBox_48.setMaximumSize(QSize(200, 100))
        self.gridLayout_98 = QGridLayout(self.groupBox_48)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.checkBox_UsingDriftUnloading_tabTAF = QCheckBox(self.groupBox_48)
        self.checkBox_UsingDriftUnloading_tabTAF.setObjectName(u"checkBox_UsingDriftUnloading_tabTAF")
        self.checkBox_UsingDriftUnloading_tabTAF.setEnabled(True)
        self.checkBox_UsingDriftUnloading_tabTAF.setChecked(True)

        self.gridLayout_98.addWidget(self.checkBox_UsingDriftUnloading_tabTAF, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_48, 4, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_calibration)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(460, 0))
        self.groupBox_2.setMaximumSize(QSize(460, 69))
        self.gridLayout_9 = QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.spinBox_max_size_fluctuation_tabTAF = QSpinBox(self.groupBox_2)
        self.spinBox_max_size_fluctuation_tabTAF.setObjectName(u"spinBox_max_size_fluctuation_tabTAF")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabTAF.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabTAF.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabTAF.setValue(1)

        self.gridLayout_9.addWidget(self.spinBox_max_size_fluctuation_tabTAF, 1, 6, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.label_9, 1, 5, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.label_8, 1, 1, 1, 1)

        self.doubleSpinBox_relForceRateNoise_tabTAF = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_relForceRateNoise_tabTAF.setObjectName(u"doubleSpinBox_relForceRateNoise_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabTAF.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabTAF.setSingleStep(0.000100000000000)
        self.doubleSpinBox_relForceRateNoise_tabTAF.setValue(0.003000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_relForceRateNoise_tabTAF, 1, 4, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.progressBar_tabTAF = QProgressBar(self.tab_calibration)
        self.progressBar_tabTAF.setObjectName(u"progressBar_tabTAF")
        sizePolicy1.setHeightForWidth(self.progressBar_tabTAF.sizePolicy().hasHeightForWidth())
        self.progressBar_tabTAF.setSizePolicy(sizePolicy1)
        self.progressBar_tabTAF.setMinimumSize(QSize(200, 0))
        self.progressBar_tabTAF.setMaximumSize(QSize(200, 55))
        self.progressBar_tabTAF.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar_tabTAF, 5, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab_calibration)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(460, 0))
        self.groupBox.setMaximumSize(QSize(460, 16777215))
        self.groupBox.setFont(font)
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.doubleSpinBox_E_tabTAF = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_E_tabTAF.setObjectName(u"doubleSpinBox_E_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_E_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_E_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_E_tabTAF.setDecimals(3)
        self.doubleSpinBox_E_tabTAF.setMaximum(1000.000000000000000)
        self.doubleSpinBox_E_tabTAF.setSingleStep(0.001000000000000)
        self.doubleSpinBox_E_tabTAF.setValue(72.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBox_E_tabTAF, 2, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_33, 1, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_32, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_4, 2, 0, 1, 1)

        self.doubleSpinBox_Poisson_tabTAF = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Poisson_tabTAF.setObjectName(u"doubleSpinBox_Poisson_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Poisson_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Poisson_tabTAF.setDecimals(4)
        self.doubleSpinBox_Poisson_tabTAF.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_tabTAF.setValue(0.179000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBox_Poisson_tabTAF, 2, 3, 1, 1)

        self.lineEdit_path_tabTAF = QLineEdit(self.groupBox)
        self.lineEdit_path_tabTAF.setObjectName(u"lineEdit_path_tabTAF")
        sizePolicy2.setHeightForWidth(self.lineEdit_path_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabTAF.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.lineEdit_path_tabTAF, 1, 1, 1, 3)

        self.lineEdit_MaterialName_tabTAF = QLineEdit(self.groupBox)
        self.lineEdit_MaterialName_tabTAF.setObjectName(u"lineEdit_MaterialName_tabTAF")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_MaterialName_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_MaterialName_tabTAF.setSizePolicy(sizePolicy5)
        self.lineEdit_MaterialName_tabTAF.setMinimumSize(QSize(0, 0))

        self.gridLayout_7.addWidget(self.lineEdit_MaterialName_tabTAF, 0, 1, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab_calibration)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(230, 0))
        self.groupBox_3.setMaximumSize(QSize(230, 100))
        self.gridLayout_10 = QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.label_2, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout_10.addWidget(self.label, 2, 1, 1, 1)

        self.comboBox_equipment_tabTAF = QComboBox(self.groupBox_3)
        self.comboBox_equipment_tabTAF.addItem("")
        self.comboBox_equipment_tabTAF.addItem("")
        self.comboBox_equipment_tabTAF.setObjectName(u"comboBox_equipment_tabTAF")
        self.comboBox_equipment_tabTAF.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabTAF.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabTAF.setSizePolicy(sizePolicy2)
        self.comboBox_equipment_tabTAF.setMaximumSize(QSize(3000, 16777215))
        self.comboBox_equipment_tabTAF.setMaxVisibleItems(20)

        self.gridLayout_10.addWidget(self.comboBox_equipment_tabTAF, 2, 2, 1, 1)

        self.comboBox_method_tabTAF = QComboBox(self.groupBox_3)
        self.comboBox_method_tabTAF.addItem("")
        self.comboBox_method_tabTAF.addItem("")
        self.comboBox_method_tabTAF.addItem("")
        self.comboBox_method_tabTAF.setObjectName(u"comboBox_method_tabTAF")
        self.comboBox_method_tabTAF.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabTAF.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabTAF.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabTAF.setMinimumSize(QSize(0, 0))
        self.comboBox_method_tabTAF.setEditable(False)
        self.comboBox_method_tabTAF.setModelColumn(0)

        self.gridLayout_10.addWidget(self.comboBox_method_tabTAF, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction = QTabWidget(self.tab_calibration)
        self.graphicsView_tab_TipAreaFunction.setObjectName(u"graphicsView_tab_TipAreaFunction")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction.setUsesScrollButtons(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget_3 = QTabWidget(self.tab_3)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness = QPushButton(self.tab_5)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness, 4, 0, 1, 2)

        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF = QCheckBox(self.tab_5)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF.sizePolicy().hasHeightForWidth())
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF.setSizePolicy(sizePolicy7)

        self.gridLayout_6.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF, 2, 0, 1, 1)

        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF = QGraphicsView(self.tab_5)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setSizePolicy(sizePolicy)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setMinimumSize(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setMaximumSize(QSize(16777215, 16777215))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setSizeIncrement(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setBaseSize(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_6.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTAF, 1, 0, 1, 4)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabTAF = QCheckBox(self.tab_5)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTAF.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabTAF")
        sizePolicy7.setHeightForWidth(self.checkBox_iLHU_inclusive_frame_stiffness_tabTAF.sizePolicy().hasHeightForWidth())
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTAF.setSizePolicy(sizePolicy7)

        self.gridLayout_6.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabTAF, 2, 1, 1, 1)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF = QCheckBox(self.tab_5)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF")
        sizePolicy1.setHeightForWidth(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF.sizePolicy().hasHeightForWidth())
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF, 2, 2, 1, 1)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF = QGraphicsView(self.tab_6)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_6, "")

        self.gridLayout_5.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.graphicsView_FrameStiffness_tabTAF = QGraphicsView(self.tab)
        self.graphicsView_FrameStiffness_tabTAF.setObjectName(u"graphicsView_FrameStiffness_tabTAF")

        self.gridLayout.addWidget(self.graphicsView_FrameStiffness_tabTAF, 4, 0, 1, 7)

        self.lineEdit_FrameStiffness_tabTAF = QLineEdit(self.tab)
        self.lineEdit_FrameStiffness_tabTAF.setObjectName(u"lineEdit_FrameStiffness_tabTAF")
        self.lineEdit_FrameStiffness_tabTAF.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameStiffness_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameStiffness_tabTAF.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameStiffness_tabTAF.setFrame(True)
        self.lineEdit_FrameStiffness_tabTAF.setDragEnabled(False)
        self.lineEdit_FrameStiffness_tabTAF.setReadOnly(True)
        self.lineEdit_FrameStiffness_tabTAF.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_FrameStiffness_tabTAF, 2, 1, 1, 1)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)

        self.lineEdit_FrameCompliance_tabTAF = QLineEdit(self.tab)
        self.lineEdit_FrameCompliance_tabTAF.setObjectName(u"lineEdit_FrameCompliance_tabTAF")
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameCompliance_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameCompliance_tabTAF.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameCompliance_tabTAF.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_FrameCompliance_tabTAF, 2, 3, 1, 1)

        self.graphicsView_tab_TipAreaFunction.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_13 = QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.graphicsView_TAF_tabTAF = QGraphicsView(self.tab_2)
        self.graphicsView_TAF_tabTAF.setObjectName(u"graphicsView_TAF_tabTAF")
        sizePolicy.setHeightForWidth(self.graphicsView_TAF_tabTAF.sizePolicy().hasHeightForWidth())
        self.graphicsView_TAF_tabTAF.setSizePolicy(sizePolicy)

        self.gridLayout_13.addWidget(self.graphicsView_TAF_tabTAF, 2, 0, 1, 12)

        self.groupBox_22 = QGroupBox(self.tab_2)
        self.groupBox_22.setObjectName(u"groupBox_22")
        sizePolicy1.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy1)
        self.groupBox_22.setMinimumSize(QSize(0, 0))
        self.gridLayout_42 = QGridLayout(self.groupBox_22)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_30 = QLabel(self.groupBox_22)
        self.label_30.setObjectName(u"label_30")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy8)

        self.gridLayout_42.addWidget(self.label_30, 0, 8, 1, 1)

        self.label_26 = QLabel(self.groupBox_22)
        self.label_26.setObjectName(u"label_26")
        sizePolicy8.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy8)

        self.gridLayout_42.addWidget(self.label_26, 0, 0, 1, 1)

        self.lineEdit_TAF3_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF3_tabTAF.setObjectName(u"lineEdit_TAF3_tabTAF")
        sizePolicy1.setHeightForWidth(self.lineEdit_TAF3_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF3_tabTAF.setSizePolicy(sizePolicy1)
        self.lineEdit_TAF3_tabTAF.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF3_tabTAF.setReadOnly(True)

        self.gridLayout_42.addWidget(self.lineEdit_TAF3_tabTAF, 0, 5, 1, 1)

        self.lineEdit_TAF2_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF2_tabTAF.setObjectName(u"lineEdit_TAF2_tabTAF")
        self.lineEdit_TAF2_tabTAF.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF2_tabTAF.setReadOnly(True)

        self.gridLayout_42.addWidget(self.lineEdit_TAF2_tabTAF, 0, 3, 1, 1)

        self.lineEdit_TAF4_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF4_tabTAF.setObjectName(u"lineEdit_TAF4_tabTAF")
        self.lineEdit_TAF4_tabTAF.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF4_tabTAF.setReadOnly(True)

        self.gridLayout_42.addWidget(self.lineEdit_TAF4_tabTAF, 0, 7, 1, 1)

        self.lineEdit_TAF1_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF1_tabTAF.setObjectName(u"lineEdit_TAF1_tabTAF")
        sizePolicy1.setHeightForWidth(self.lineEdit_TAF1_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF1_tabTAF.setSizePolicy(sizePolicy1)
        self.lineEdit_TAF1_tabTAF.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF1_tabTAF.setReadOnly(True)

        self.gridLayout_42.addWidget(self.lineEdit_TAF1_tabTAF, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_22)
        self.label_29.setObjectName(u"label_29")
        sizePolicy8.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy8)

        self.gridLayout_42.addWidget(self.label_29, 0, 6, 1, 1)

        self.label_28 = QLabel(self.groupBox_22)
        self.label_28.setObjectName(u"label_28")
        sizePolicy8.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy8)

        self.gridLayout_42.addWidget(self.label_28, 0, 4, 1, 1)

        self.label_27 = QLabel(self.groupBox_22)
        self.label_27.setObjectName(u"label_27")
        sizePolicy8.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy8)

        self.gridLayout_42.addWidget(self.label_27, 0, 2, 1, 1)

        self.lineEdit_TAF5_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF5_tabTAF.setObjectName(u"lineEdit_TAF5_tabTAF")
        self.lineEdit_TAF5_tabTAF.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF5_tabTAF.setReadOnly(True)

        self.gridLayout_42.addWidget(self.lineEdit_TAF5_tabTAF, 0, 9, 1, 1)

        self.label_31 = QLabel(self.groupBox_22)
        self.label_31.setObjectName(u"label_31")
        sizePolicy8.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy8)

        self.gridLayout_42.addWidget(self.label_31, 0, 10, 1, 1)

        self.lineEdit_TAF6_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF6_tabTAF.setObjectName(u"lineEdit_TAF6_tabTAF")
        self.lineEdit_TAF6_tabTAF.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_42.addWidget(self.lineEdit_TAF6_tabTAF, 1, 3, 1, 1)

        self.label_139 = QLabel(self.groupBox_22)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_42.addWidget(self.label_139, 1, 4, 1, 1)

        self.lineEdit_TAF7_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF7_tabTAF.setObjectName(u"lineEdit_TAF7_tabTAF")
        sizePolicy1.setHeightForWidth(self.lineEdit_TAF7_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF7_tabTAF.setSizePolicy(sizePolicy1)
        self.lineEdit_TAF7_tabTAF.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_42.addWidget(self.lineEdit_TAF7_tabTAF, 1, 5, 1, 1)

        self.label_140 = QLabel(self.groupBox_22)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_42.addWidget(self.label_140, 1, 6, 1, 1)

        self.lineEdit_TAF8_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF8_tabTAF.setObjectName(u"lineEdit_TAF8_tabTAF")
        self.lineEdit_TAF8_tabTAF.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_42.addWidget(self.lineEdit_TAF8_tabTAF, 1, 7, 1, 1)

        self.label_141 = QLabel(self.groupBox_22)
        self.label_141.setObjectName(u"label_141")

        self.gridLayout_42.addWidget(self.label_141, 1, 8, 1, 1)

        self.lineEdit_TAF9_tabTAF = QLineEdit(self.groupBox_22)
        self.lineEdit_TAF9_tabTAF.setObjectName(u"lineEdit_TAF9_tabTAF")
        self.lineEdit_TAF9_tabTAF.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_42.addWidget(self.lineEdit_TAF9_tabTAF, 1, 9, 1, 1)

        self.label_142 = QLabel(self.groupBox_22)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_42.addWidget(self.label_142, 1, 10, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_22, 1, 0, 1, 12)

        self.graphicsView_tab_TipAreaFunction.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.graphicsView_tab_TipAreaFunction, 0, 3, 8, 1)

        self.groupBox_7 = QGroupBox(self.tab_calibration)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setMinimumSize(QSize(460, 285))
        self.groupBox_7.setMaximumSize(QSize(460, 285))
        self.gridLayout_15 = QGridLayout(self.groupBox_7)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_34 = QLabel(self.groupBox_7)
        self.label_34.setObjectName(u"label_34")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy9)
        font1 = QFont()
        font1.setPointSize(10)
        self.label_34.setFont(font1)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_34, 2, 0, 1, 2)

        self.comboBox_TipType_tabTAF = QComboBox(self.groupBox_7)
        self.comboBox_TipType_tabTAF.addItem("")
        self.comboBox_TipType_tabTAF.addItem("")
        self.comboBox_TipType_tabTAF.addItem("")
        self.comboBox_TipType_tabTAF.setObjectName(u"comboBox_TipType_tabTAF")
        sizePolicy7.setHeightForWidth(self.comboBox_TipType_tabTAF.sizePolicy().hasHeightForWidth())
        self.comboBox_TipType_tabTAF.setSizePolicy(sizePolicy7)

        self.gridLayout_15.addWidget(self.comboBox_TipType_tabTAF, 0, 5, 1, 1)

        self.doubleSpinBox_Poisson_Tip_tabTAF = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_Poisson_Tip_tabTAF.setObjectName(u"doubleSpinBox_Poisson_Tip_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Poisson_Tip_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_Tip_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Poisson_Tip_tabTAF.setDecimals(3)
        self.doubleSpinBox_Poisson_Tip_tabTAF.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_Tip_tabTAF.setValue(0.070000000000000)

        self.gridLayout_15.addWidget(self.doubleSpinBox_Poisson_Tip_tabTAF, 2, 5, 1, 1)

        self.groupBox_63 = QGroupBox(self.groupBox_7)
        self.groupBox_63.setObjectName(u"groupBox_63")
        sizePolicy1.setHeightForWidth(self.groupBox_63.sizePolicy().hasHeightForWidth())
        self.groupBox_63.setSizePolicy(sizePolicy1)
        self.gridLayout_111 = QGridLayout(self.groupBox_63)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.label_21 = QLabel(self.groupBox_63)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_111.addWidget(self.label_21, 0, 0, 1, 1)

        self.doubleSpinBox_half_includedAngle_tabTAF = QDoubleSpinBox(self.groupBox_63)
        self.doubleSpinBox_half_includedAngle_tabTAF.setObjectName(u"doubleSpinBox_half_includedAngle_tabTAF")
        self.doubleSpinBox_half_includedAngle_tabTAF.setValue(30.000000000000000)

        self.gridLayout_111.addWidget(self.doubleSpinBox_half_includedAngle_tabTAF, 0, 1, 1, 1)

        self.label_138 = QLabel(self.groupBox_63)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_111.addWidget(self.label_138, 0, 2, 1, 1)

        self.doubleSpinBox_idealRadiusSphere_tabTAF = QDoubleSpinBox(self.groupBox_63)
        self.doubleSpinBox_idealRadiusSphere_tabTAF.setObjectName(u"doubleSpinBox_idealRadiusSphere_tabTAF")
        self.doubleSpinBox_idealRadiusSphere_tabTAF.setDecimals(3)
        self.doubleSpinBox_idealRadiusSphere_tabTAF.setValue(2.000000000000000)

        self.gridLayout_111.addWidget(self.doubleSpinBox_idealRadiusSphere_tabTAF, 0, 3, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_63, 5, 0, 1, 6)

        self.doubleSpinBox_E_Tip_tabTAF = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_E_Tip_tabTAF.setObjectName(u"doubleSpinBox_E_Tip_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_E_Tip_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_E_Tip_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_E_Tip_tabTAF.setDecimals(3)
        self.doubleSpinBox_E_Tip_tabTAF.setMaximum(99999.990000000005239)
        self.doubleSpinBox_E_Tip_tabTAF.setSingleStep(0.001000000000000)
        self.doubleSpinBox_E_Tip_tabTAF.setValue(1141.000000000000000)

        self.gridLayout_15.addWidget(self.doubleSpinBox_E_Tip_tabTAF, 2, 2, 1, 2)

        self.label_137 = QLabel(self.groupBox_7)
        self.label_137.setObjectName(u"label_137")
        sizePolicy3.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy3)
        self.label_137.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_137, 0, 4, 1, 1)

        self.label_64 = QLabel(self.groupBox_7)
        self.label_64.setObjectName(u"label_64")
        sizePolicy9.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy9)
        self.label_64.setFont(font)
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_64, 2, 4, 1, 1)

        self.label_63 = QLabel(self.groupBox_7)
        self.label_63.setObjectName(u"label_63")
        sizePolicy9.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy9)
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_63, 0, 0, 1, 2)

        self.lineEdit_TipName_tabTAF = QLineEdit(self.groupBox_7)
        self.lineEdit_TipName_tabTAF.setObjectName(u"lineEdit_TipName_tabTAF")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.lineEdit_TipName_tabTAF.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabTAF.setSizePolicy(sizePolicy10)

        self.gridLayout_15.addWidget(self.lineEdit_TipName_tabTAF, 0, 2, 1, 2)

        self.groupBox_64 = QGroupBox(self.groupBox_7)
        self.groupBox_64.setObjectName(u"groupBox_64")
        sizePolicy1.setHeightForWidth(self.groupBox_64.sizePolicy().hasHeightForWidth())
        self.groupBox_64.setSizePolicy(sizePolicy1)
        self.groupBox_64.setMinimumSize(QSize(0, 102))
        self.gridLayout_113 = QGridLayout(self.groupBox_64)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.label_14 = QLabel(self.groupBox_64)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.label_14, 0, 0, 1, 1)

        self.spinBox_number_of_TAFterms_tabTAF = QSpinBox(self.groupBox_64)
        self.spinBox_number_of_TAFterms_tabTAF.setObjectName(u"spinBox_number_of_TAFterms_tabTAF")
        sizePolicy9.setHeightForWidth(self.spinBox_number_of_TAFterms_tabTAF.sizePolicy().hasHeightForWidth())
        self.spinBox_number_of_TAFterms_tabTAF.setSizePolicy(sizePolicy9)
        self.spinBox_number_of_TAFterms_tabTAF.setMinimum(2)
        self.spinBox_number_of_TAFterms_tabTAF.setMaximum(9)
        self.spinBox_number_of_TAFterms_tabTAF.setValue(3)

        self.gridLayout_113.addWidget(self.spinBox_number_of_TAFterms_tabTAF, 0, 1, 1, 1)

        self.checkBox_IfTermsGreaterThanZero_tabTAF = QCheckBox(self.groupBox_64)
        self.checkBox_IfTermsGreaterThanZero_tabTAF.setObjectName(u"checkBox_IfTermsGreaterThanZero_tabTAF")
        self.checkBox_IfTermsGreaterThanZero_tabTAF.setChecked(True)

        self.gridLayout_113.addWidget(self.checkBox_IfTermsGreaterThanZero_tabTAF, 0, 2, 1, 1)

        self.label_45 = QLabel(self.groupBox_64)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_113.addWidget(self.label_45, 1, 0, 1, 1)

        self.doubleSpinBox_minhc_Tip_tabTAF = QDoubleSpinBox(self.groupBox_64)
        self.doubleSpinBox_minhc_Tip_tabTAF.setObjectName(u"doubleSpinBox_minhc_Tip_tabTAF")
        sizePolicy7.setHeightForWidth(self.doubleSpinBox_minhc_Tip_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_minhc_Tip_tabTAF.setSizePolicy(sizePolicy7)
        self.doubleSpinBox_minhc_Tip_tabTAF.setDecimals(3)

        self.gridLayout_113.addWidget(self.doubleSpinBox_minhc_Tip_tabTAF, 1, 1, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_64, 6, 0, 1, 6)


        self.gridLayout_2.addWidget(self.groupBox_7, 1, 0, 1, 2)

        self.tableWidget_tabTAF = QTableWidget(self.tab_calibration)
        if (self.tableWidget_tabTAF.columnCount() < 2):
            self.tableWidget_tabTAF.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTAF.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTAF.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_tabTAF.rowCount() < 1):
            self.tableWidget_tabTAF.setRowCount(1)
        self.tableWidget_tabTAF.setObjectName(u"tableWidget_tabTAF")
        sizePolicy1.setHeightForWidth(self.tableWidget_tabTAF.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabTAF.setSizePolicy(sizePolicy1)
        self.tableWidget_tabTAF.setMinimumSize(QSize(200, 100))
        self.tableWidget_tabTAF.setMaximumSize(QSize(200, 543))
        self.tableWidget_tabTAF.setAutoScroll(True)
        self.tableWidget_tabTAF.setRowCount(1)
        self.tableWidget_tabTAF.setColumnCount(2)
        self.tableWidget_tabTAF.horizontalHeader().setVisible(True)
        self.tableWidget_tabTAF.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_tabTAF.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget_tabTAF.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_tabTAF.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_2.addWidget(self.tableWidget_tabTAF, 0, 2, 3, 1)

        self.OK_path_tabTAF = QPushButton(self.tab_calibration)
        self.OK_path_tabTAF.setObjectName(u"OK_path_tabTAF")
        sizePolicy8.setHeightForWidth(self.OK_path_tabTAF.sizePolicy().hasHeightForWidth())
        self.OK_path_tabTAF.setSizePolicy(sizePolicy8)
        self.OK_path_tabTAF.setMinimumSize(QSize(200, 0))
        self.OK_path_tabTAF.setMaximumSize(QSize(200, 46))

        self.gridLayout_2.addWidget(self.OK_path_tabTAF, 6, 2, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_calibration)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy8.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy8)
        self.groupBox_6.setMinimumSize(QSize(224, 0))
        self.groupBox_6.setMaximumSize(QSize(224, 300))
        self.gridLayout_14 = QGridLayout(self.groupBox_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)

        self.gridLayout_14.addWidget(self.label_12, 0, 1, 1, 1)

        self.doubleSpinBox_critForceStiffness_tabTAF = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_critForceStiffness_tabTAF.setObjectName(u"doubleSpinBox_critForceStiffness_tabTAF")
        self.doubleSpinBox_critForceStiffness_tabTAF.setMaximum(999.000000000000000)
        self.doubleSpinBox_critForceStiffness_tabTAF.setSingleStep(1.000000000000000)
        self.doubleSpinBox_critForceStiffness_tabTAF.setValue(15.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_critForceStiffness_tabTAF, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")
        sizePolicy8.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy8)

        self.gridLayout_14.addWidget(self.label_13, 1, 1, 1, 1)

        self.doubleSpinBox_critDepthStiffness_tabTAF = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_critDepthStiffness_tabTAF.setObjectName(u"doubleSpinBox_critDepthStiffness_tabTAF")
        self.doubleSpinBox_critDepthStiffness_tabTAF.setSingleStep(0.010000000000000)
        self.doubleSpinBox_critDepthStiffness_tabTAF.setValue(0.100000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_critDepthStiffness_tabTAF, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_6, 5, 1, 2, 1)

        self.groupBox_55 = QGroupBox(self.tab_calibration)
        self.groupBox_55.setObjectName(u"groupBox_55")
        sizePolicy1.setHeightForWidth(self.groupBox_55.sizePolicy().hasHeightForWidth())
        self.groupBox_55.setSizePolicy(sizePolicy1)
        self.groupBox_55.setMinimumSize(QSize(230, 0))
        self.groupBox_55.setMaximumSize(QSize(230, 300))
        self.gridLayout_52 = QGridLayout(self.groupBox_55)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_6 = QLabel(self.groupBox_55)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(110, 0))

        self.gridLayout_52.addWidget(self.label_6, 0, 0, 1, 1)

        self.doubleSpinBox_Start_Pmax_tabTAF = QDoubleSpinBox(self.groupBox_55)
        self.doubleSpinBox_Start_Pmax_tabTAF.setObjectName(u"doubleSpinBox_Start_Pmax_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabTAF.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabTAF.setValue(0.980000000000000)

        self.gridLayout_52.addWidget(self.doubleSpinBox_Start_Pmax_tabTAF, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_55)
        self.label_7.setObjectName(u"label_7")
        sizePolicy9.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy9)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_7, 1, 0, 1, 1)

        self.doubleSpinBox_End_Pmax_tabTAF = QDoubleSpinBox(self.groupBox_55)
        self.doubleSpinBox_End_Pmax_tabTAF.setObjectName(u"doubleSpinBox_End_Pmax_tabTAF")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabTAF.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabTAF.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabTAF.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabTAF.setValue(0.500000000000000)

        self.gridLayout_52.addWidget(self.doubleSpinBox_End_Pmax_tabTAF, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_55, 5, 0, 2, 1)

        self.tabWidget.addTab(self.tab_calibration, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_16 = QGridLayout(self.tab_4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.tabWidget_2 = QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_19 = QGridLayout(self.tab_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_10 = QGroupBox(self.tab_7)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.groupBox_10.setMinimumSize(QSize(460, 0))
        self.groupBox_10.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_18 = QGridLayout(self.groupBox_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_18 = QLabel(self.groupBox_10)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(0, 0))

        self.gridLayout_18.addWidget(self.label_18, 0, 5, 1, 1)

        self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness.setObjectName(u"doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness.setSingleStep(0.000100000000000)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness.setValue(0.010000000000000)

        self.gridLayout_18.addWidget(self.doubleSpinBox_relForceRateNoise_tabTipRadius_FrameStiffness, 0, 4, 1, 1)

        self.spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness = QSpinBox(self.groupBox_10)
        self.spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness.setObjectName(u"spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness.setValue(1)

        self.gridLayout_18.addWidget(self.spinBox_max_size_fluctuation_tabTipRadius_FrameStiffness, 0, 6, 1, 1)

        self.label_17 = QLabel(self.groupBox_10)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_17, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_10, 2, 0, 1, 2)

        self.pushButton_SelectAll_tabTipRadius_FrameStiffness = QPushButton(self.tab_7)
        self.pushButton_SelectAll_tabTipRadius_FrameStiffness.setObjectName(u"pushButton_SelectAll_tabTipRadius_FrameStiffness")
        self.pushButton_SelectAll_tabTipRadius_FrameStiffness.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_19.addWidget(self.pushButton_SelectAll_tabTipRadius_FrameStiffness, 6, 2, 1, 1)

        self.groupBox_57 = QGroupBox(self.tab_7)
        self.groupBox_57.setObjectName(u"groupBox_57")
        sizePolicy1.setHeightForWidth(self.groupBox_57.sizePolicy().hasHeightForWidth())
        self.groupBox_57.setSizePolicy(sizePolicy1)
        self.groupBox_57.setMinimumSize(QSize(460, 0))
        self.groupBox_57.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_106 = QGridLayout(self.groupBox_57)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness = QComboBox(self.groupBox_57)
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.addItem("")
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.addItem("")
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.setObjectName(u"comboBox_CalculationMethod_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.setEditable(False)

        self.gridLayout_106.addWidget(self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness, 1, 0, 1, 1)

        self.groupBox_61 = QGroupBox(self.groupBox_57)
        self.groupBox_61.setObjectName(u"groupBox_61")
        sizePolicy4.setHeightForWidth(self.groupBox_61.sizePolicy().hasHeightForWidth())
        self.groupBox_61.setSizePolicy(sizePolicy4)
        self.groupBox_61.setMinimumSize(QSize(0, 0))
        self.groupBox_61.setMaximumSize(QSize(44000, 16777215))
        self.gridLayout_109 = QGridLayout(self.groupBox_61)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.lineEdit_TAF4_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF4_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF4_tabTipRadius_FrameStiffness")
        self.lineEdit_TAF4_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF4_tabTipRadius_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF4_tabTipRadius_FrameStiffness.setReadOnly(True)

        self.gridLayout_109.addWidget(self.lineEdit_TAF4_tabTipRadius_FrameStiffness, 2, 7, 1, 1)

        self.label_128 = QLabel(self.groupBox_61)
        self.label_128.setObjectName(u"label_128")
        sizePolicy8.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy8)

        self.gridLayout_109.addWidget(self.label_128, 2, 2, 1, 1)

        self.label_126 = QLabel(self.groupBox_61)
        self.label_126.setObjectName(u"label_126")
        sizePolicy8.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy8)

        self.gridLayout_109.addWidget(self.label_126, 2, 6, 1, 1)

        self.lineEdit_TAF2_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF2_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF2_tabTipRadius_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF2_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF2_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF2_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF2_tabTipRadius_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF2_tabTipRadius_FrameStiffness.setReadOnly(True)

        self.gridLayout_109.addWidget(self.lineEdit_TAF2_tabTipRadius_FrameStiffness, 2, 3, 1, 1)

        self.label_84 = QLabel(self.groupBox_61)
        self.label_84.setObjectName(u"label_84")
        sizePolicy8.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy8)
        self.label_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_109.addWidget(self.label_84, 2, 0, 1, 1)

        self.lineEdit_TAF3_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF3_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF3_tabTipRadius_FrameStiffness")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lineEdit_TAF3_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF3_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy11)
        self.lineEdit_TAF3_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF3_tabTipRadius_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF3_tabTipRadius_FrameStiffness.setReadOnly(True)

        self.gridLayout_109.addWidget(self.lineEdit_TAF3_tabTipRadius_FrameStiffness, 2, 5, 1, 1)

        self.lineEdit_TAF1_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF1_tabTipRadius_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF1_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setReadOnly(True)

        self.gridLayout_109.addWidget(self.lineEdit_TAF1_tabTipRadius_FrameStiffness, 2, 1, 1, 1)

        self.lineEdit_TAF5_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF5_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF5_tabTipRadius_FrameStiffness")
        self.lineEdit_TAF5_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF5_tabTipRadius_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF5_tabTipRadius_FrameStiffness.setReadOnly(True)

        self.gridLayout_109.addWidget(self.lineEdit_TAF5_tabTipRadius_FrameStiffness, 2, 9, 1, 1)

        self.label_129 = QLabel(self.groupBox_61)
        self.label_129.setObjectName(u"label_129")
        sizePolicy9.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy9)
        self.label_129.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_109.addWidget(self.label_129, 0, 0, 1, 2)

        self.label_124 = QLabel(self.groupBox_61)
        self.label_124.setObjectName(u"label_124")
        sizePolicy8.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy8)

        self.gridLayout_109.addWidget(self.label_124, 2, 8, 1, 1)

        self.label_127 = QLabel(self.groupBox_61)
        self.label_127.setObjectName(u"label_127")
        sizePolicy8.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy8)
        self.label_127.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_109.addWidget(self.label_127, 2, 4, 1, 1)

        self.label_125 = QLabel(self.groupBox_61)
        self.label_125.setObjectName(u"label_125")
        sizePolicy8.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy8)

        self.gridLayout_109.addWidget(self.label_125, 2, 10, 1, 1)

        self.lineEdit_TAF9_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF9_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF9_tabTipRadius_FrameStiffness")
        self.lineEdit_TAF9_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_109.addWidget(self.lineEdit_TAF9_tabTipRadius_FrameStiffness, 3, 9, 1, 1)

        self.lineEdit_TAF8_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF8_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF8_tabTipRadius_FrameStiffness")
        self.lineEdit_TAF8_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_109.addWidget(self.lineEdit_TAF8_tabTipRadius_FrameStiffness, 3, 7, 1, 1)

        self.lineEdit_TAF7_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF7_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF7_tabTipRadius_FrameStiffness")
        self.lineEdit_TAF7_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_109.addWidget(self.lineEdit_TAF7_tabTipRadius_FrameStiffness, 3, 5, 1, 1)

        self.lineEdit_TAF6_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TAF6_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TAF6_tabTipRadius_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF6_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF6_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF6_tabTipRadius_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_109.addWidget(self.lineEdit_TAF6_tabTipRadius_FrameStiffness, 3, 3, 1, 1)

        self.label_143 = QLabel(self.groupBox_61)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_109.addWidget(self.label_143, 3, 4, 1, 1)

        self.label_144 = QLabel(self.groupBox_61)
        self.label_144.setObjectName(u"label_144")

        self.gridLayout_109.addWidget(self.label_144, 3, 6, 1, 1)

        self.label_145 = QLabel(self.groupBox_61)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_109.addWidget(self.label_145, 3, 8, 1, 1)

        self.label_146 = QLabel(self.groupBox_61)
        self.label_146.setObjectName(u"label_146")

        self.gridLayout_109.addWidget(self.label_146, 3, 10, 1, 1)

        self.Copy_TAF_tabTipRadius_FrameStiffness = QPushButton(self.groupBox_61)
        self.Copy_TAF_tabTipRadius_FrameStiffness.setObjectName(u"Copy_TAF_tabTipRadius_FrameStiffness")
        sizePolicy3.setHeightForWidth(self.Copy_TAF_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.Copy_TAF_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy3)
        self.Copy_TAF_tabTipRadius_FrameStiffness.setMinimumSize(QSize(110, 0))

        self.gridLayout_109.addWidget(self.Copy_TAF_tabTipRadius_FrameStiffness, 6, 0, 1, 11)

        self.lineEdit_TipName_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_61)
        self.lineEdit_TipName_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_TipName_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.lineEdit_TipName_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_109.addWidget(self.lineEdit_TipName_tabTipRadius_FrameStiffness, 0, 2, 1, 9)


        self.gridLayout_106.addWidget(self.groupBox_61, 2, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_57, 1, 0, 1, 2)

        self.graphicsView_tab_TipAreaFunction_2 = QTabWidget(self.tab_7)
        self.graphicsView_tab_TipAreaFunction_2.setObjectName(u"graphicsView_tab_TipAreaFunction_2")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction_2.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction_2.setUsesScrollButtons(True)
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_20 = QGridLayout(self.tab_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tabWidget_4 = QTabWidget(self.tab_9)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_21 = QGridLayout(self.tab_10)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness = QGraphicsView(self.tab_10)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness")
        sizePolicy6.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy6)

        self.gridLayout_21.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness, 1, 0, 1, 5)

        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness = QCheckBox(self.tab_10)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)

        self.gridLayout_21.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness, 2, 0, 1, 1)

        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness = QPushButton(self.tab_10)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy1)

        self.gridLayout_21.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness, 4, 0, 1, 4)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness = QCheckBox(self.tab_10)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)

        self.gridLayout_21.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness, 2, 1, 1, 1)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness = QCheckBox(self.tab_10)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy1)

        self.gridLayout_21.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness, 2, 2, 1, 1)

        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_22 = QGridLayout(self.tab_11)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_2 = QGraphicsView(self.tab_11)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_2.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_2")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_2.setSizePolicy(sizePolicy)

        self.gridLayout_22.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_2, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_11, "")

        self.gridLayout_20.addWidget(self.tabWidget_4, 1, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_2.addTab(self.tab_9, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_23 = QGridLayout(self.tab_12)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness = QLineEdit(self.tab_12)
        self.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_FrameCompliance_tabTipRadius_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness.setReadOnly(True)

        self.gridLayout_23.addWidget(self.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness, 1, 3, 1, 1)

        self.label_20 = QLabel(self.tab_12)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_23.addWidget(self.label_20, 1, 0, 1, 1)

        self.graphicsView_tabTipRadius_FrameStiffness = QGraphicsView(self.tab_12)
        self.graphicsView_tabTipRadius_FrameStiffness.setObjectName(u"graphicsView_tabTipRadius_FrameStiffness")
        self.graphicsView_tabTipRadius_FrameStiffness.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_23.addWidget(self.graphicsView_tabTipRadius_FrameStiffness, 3, 0, 1, 6)

        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness = QLineEdit(self.tab_12)
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_FrameStiffness_tabTipRadius_FrameStiffness")
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setFrame(True)
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setDragEnabled(False)
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setReadOnly(True)
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setClearButtonEnabled(False)

        self.gridLayout_23.addWidget(self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness, 1, 1, 1, 1)

        self.label_19 = QLabel(self.tab_12)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_23.addWidget(self.label_19, 1, 2, 1, 1)

        self.graphicsView_tab_TipAreaFunction_2.addTab(self.tab_12, "")

        self.gridLayout_19.addWidget(self.graphicsView_tab_TipAreaFunction_2, 0, 5, 18, 1)

        self.tableWidget_tabTipRadius_FrameStiffness = QTableWidget(self.tab_7)
        if (self.tableWidget_tabTipRadius_FrameStiffness.columnCount() < 2):
            self.tableWidget_tabTipRadius_FrameStiffness.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTipRadius_FrameStiffness.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTipRadius_FrameStiffness.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        if (self.tableWidget_tabTipRadius_FrameStiffness.rowCount() < 1):
            self.tableWidget_tabTipRadius_FrameStiffness.setRowCount(1)
        self.tableWidget_tabTipRadius_FrameStiffness.setObjectName(u"tableWidget_tabTipRadius_FrameStiffness")
        sizePolicy12 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.tableWidget_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy12)
        self.tableWidget_tabTipRadius_FrameStiffness.setMinimumSize(QSize(200, 0))
        self.tableWidget_tabTipRadius_FrameStiffness.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_tabTipRadius_FrameStiffness.setAutoScroll(True)
        self.tableWidget_tabTipRadius_FrameStiffness.setRowCount(1)
        self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeader().setVisible(True)
        self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeader().setHighlightSections(True)
        self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_19.addWidget(self.tableWidget_tabTipRadius_FrameStiffness, 0, 2, 6, 1)

        self.groupBox_8 = QGroupBox(self.tab_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.groupBox_8.setMinimumSize(QSize(224, 0))
        self.groupBox_8.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_24 = QGridLayout(self.groupBox_8)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness = QCheckBox(self.groupBox_8)
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.setObjectName(u"checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy1)
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.setMinimumSize(QSize(0, 0))
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.setChecked(True)

        self.gridLayout_24.addWidget(self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness, 0, 0, 1, 1)

        self.label_86 = QLabel(self.groupBox_8)
        self.label_86.setObjectName(u"label_86")
        sizePolicy9.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy9)
        self.label_86.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_86, 1, 0, 1, 1)

        self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness.setObjectName(u"doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness.setValue(1.000000000000000)

        self.gridLayout_24.addWidget(self.doubleSpinBox_Rate2findSurface_tabTipRadius_FrameStiffness, 0, 1, 1, 1)

        self.spinBox_DataFilterSize_tabTipRadius_FrameStiffness = QSpinBox(self.groupBox_8)
        self.spinBox_DataFilterSize_tabTipRadius_FrameStiffness.setObjectName(u"spinBox_DataFilterSize_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.spinBox_DataFilterSize_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.spinBox_DataFilterSize_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.spinBox_DataFilterSize_tabTipRadius_FrameStiffness.setValue(5)

        self.gridLayout_24.addWidget(self.spinBox_DataFilterSize_tabTipRadius_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_8, 3, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.tab_7)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.groupBox_11.setMinimumSize(QSize(230, 0))
        self.groupBox_11.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_25 = QGridLayout(self.groupBox_11)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_23 = QLabel(self.groupBox_11)
        self.label_23.setObjectName(u"label_23")
        sizePolicy9.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy9)
        self.label_23.setMaximumSize(QSize(16777215, 16777215))
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_23, 1, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_11)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)

        self.gridLayout_25.addWidget(self.label_22, 2, 1, 1, 1)

        self.comboBox_equipment_tabTipRadius_FrameStiffness = QComboBox(self.groupBox_11)
        self.comboBox_equipment_tabTipRadius_FrameStiffness.addItem("")
        self.comboBox_equipment_tabTipRadius_FrameStiffness.setObjectName(u"comboBox_equipment_tabTipRadius_FrameStiffness")
        self.comboBox_equipment_tabTipRadius_FrameStiffness.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_25.addWidget(self.comboBox_equipment_tabTipRadius_FrameStiffness, 2, 2, 1, 1)

        self.comboBox_method_tabTipRadius_FrameStiffness = QComboBox(self.groupBox_11)
        self.comboBox_method_tabTipRadius_FrameStiffness.addItem("")
        self.comboBox_method_tabTipRadius_FrameStiffness.addItem("")
        self.comboBox_method_tabTipRadius_FrameStiffness.addItem("")
        self.comboBox_method_tabTipRadius_FrameStiffness.setObjectName(u"comboBox_method_tabTipRadius_FrameStiffness")
        self.comboBox_method_tabTipRadius_FrameStiffness.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabTipRadius_FrameStiffness.setMinimumSize(QSize(120, 0))
        self.comboBox_method_tabTipRadius_FrameStiffness.setEditable(False)

        self.gridLayout_25.addWidget(self.comboBox_method_tabTipRadius_FrameStiffness, 1, 2, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_11, 3, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.tab_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy1.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy1)
        self.groupBox_9.setMinimumSize(QSize(460, 0))
        self.groupBox_9.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_17 = QGridLayout(self.groupBox_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lineEdit_path_tabTipRadius_FrameStiffness = QLineEdit(self.groupBox_9)
        self.lineEdit_path_tabTipRadius_FrameStiffness.setObjectName(u"lineEdit_path_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.lineEdit_path_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_17.addWidget(self.lineEdit_path_tabTipRadius_FrameStiffness, 0, 1, 1, 1)

        self.label_77 = QLabel(self.groupBox_9)
        self.label_77.setObjectName(u"label_77")
        sizePolicy8.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy8)

        self.gridLayout_17.addWidget(self.label_77, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_9, 0, 0, 1, 2)

        self.groupBox_50 = QGroupBox(self.tab_7)
        self.groupBox_50.setObjectName(u"groupBox_50")
        sizePolicy1.setHeightForWidth(self.groupBox_50.sizePolicy().hasHeightForWidth())
        self.groupBox_50.setSizePolicy(sizePolicy1)
        self.groupBox_50.setMinimumSize(QSize(230, 0))
        self.groupBox_50.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_100 = QGridLayout(self.groupBox_50)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.label_16 = QLabel(self.groupBox_50)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMinimumSize(QSize(110, 0))

        self.gridLayout_100.addWidget(self.label_16, 0, 0, 1, 1)

        self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness = QDoubleSpinBox(self.groupBox_50)
        self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness.setObjectName(u"doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness.setValue(0.980000000000000)

        self.gridLayout_100.addWidget(self.doubleSpinBox_Start_Pmax_tabTipRadius_FrameStiffness, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_50)
        self.label_15.setObjectName(u"label_15")
        sizePolicy9.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy9)
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_100.addWidget(self.label_15, 1, 0, 1, 1)

        self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness = QDoubleSpinBox(self.groupBox_50)
        self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness.setObjectName(u"doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness.setValue(0.500000000000000)

        self.gridLayout_100.addWidget(self.doubleSpinBox_End_Pmax_tabTipRadius_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_50, 4, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_7)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy1.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy1)
        self.groupBox_12.setMinimumSize(QSize(224, 0))
        self.groupBox_12.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_26 = QGridLayout(self.groupBox_12)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness.setObjectName(u"doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness")
        sizePolicy5.setHeightForWidth(self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy5)
        self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness.setValue(0.100000000000000)

        self.gridLayout_26.addWidget(self.doubleSpinBox_critDepthStiffness_tabTipRadius_FrameStiffness, 0, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_12)
        self.label_24.setObjectName(u"label_24")
        sizePolicy8.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy8)

        self.gridLayout_26.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_12)
        self.label_25.setObjectName(u"label_25")
        sizePolicy9.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy9)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_25, 1, 0, 1, 1)

        self.doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness.setObjectName(u"doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness")
        self.doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness.setMaximum(999.000000000000000)
        self.doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness.setValue(15.000000000000000)

        self.gridLayout_26.addWidget(self.doubleSpinBox_critForceStiffness_tabTipRadius_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_12, 4, 1, 1, 1)

        self.progressBar_tabTipRadius_FrameStiffness = QProgressBar(self.tab_7)
        self.progressBar_tabTipRadius_FrameStiffness.setObjectName(u"progressBar_tabTipRadius_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.progressBar_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.progressBar_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy1)
        self.progressBar_tabTipRadius_FrameStiffness.setMinimumSize(QSize(224, 0))
        self.progressBar_tabTipRadius_FrameStiffness.setMaximumSize(QSize(224, 16777215))
        self.progressBar_tabTipRadius_FrameStiffness.setValue(0)

        self.gridLayout_19.addWidget(self.progressBar_tabTipRadius_FrameStiffness, 5, 1, 1, 1)

        self.pushButton_Calculate_tabTipRadius_FrameStiffness = QPushButton(self.tab_7)
        self.pushButton_Calculate_tabTipRadius_FrameStiffness.setObjectName(u"pushButton_Calculate_tabTipRadius_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_Calculate_tabTipRadius_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate_tabTipRadius_FrameStiffness.setSizePolicy(sizePolicy1)
        self.pushButton_Calculate_tabTipRadius_FrameStiffness.setMinimumSize(QSize(224, 0))
        self.pushButton_Calculate_tabTipRadius_FrameStiffness.setMaximumSize(QSize(224, 16777215))

        self.gridLayout_19.addWidget(self.pushButton_Calculate_tabTipRadius_FrameStiffness, 6, 1, 1, 1)

        self.groupBox_45 = QGroupBox(self.tab_7)
        self.groupBox_45.setObjectName(u"groupBox_45")
        sizePolicy1.setHeightForWidth(self.groupBox_45.sizePolicy().hasHeightForWidth())
        self.groupBox_45.setSizePolicy(sizePolicy1)
        self.groupBox_45.setMinimumSize(QSize(230, 0))
        self.groupBox_45.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_95 = QGridLayout(self.groupBox_45)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness = QCheckBox(self.groupBox_45)
        self.checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness.setObjectName(u"checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness")
        self.checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness.setEnabled(True)
        self.checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness.setChecked(True)

        self.gridLayout_95.addWidget(self.checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_45, 5, 0, 2, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_58 = QGridLayout(self.tab_8)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.groupBox_29 = QGroupBox(self.tab_8)
        self.groupBox_29.setObjectName(u"groupBox_29")
        sizePolicy1.setHeightForWidth(self.groupBox_29.sizePolicy().hasHeightForWidth())
        self.groupBox_29.setSizePolicy(sizePolicy1)
        self.groupBox_29.setMinimumSize(QSize(460, 0))
        self.groupBox_29.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_60 = QGridLayout(self.groupBox_29)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.label_75 = QLabel(self.groupBox_29)
        self.label_75.setObjectName(u"label_75")
        sizePolicy3.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy3)
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_60.addWidget(self.label_75, 0, 0, 1, 1)

        self.doubleSpinBox_Poisson_tabTipRadius = QDoubleSpinBox(self.groupBox_29)
        self.doubleSpinBox_Poisson_tabTipRadius.setObjectName(u"doubleSpinBox_Poisson_tabTipRadius")
        sizePolicy5.setHeightForWidth(self.doubleSpinBox_Poisson_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_tabTipRadius.setSizePolicy(sizePolicy5)
        self.doubleSpinBox_Poisson_tabTipRadius.setDecimals(3)
        self.doubleSpinBox_Poisson_tabTipRadius.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_tabTipRadius.setValue(0.280000000000000)

        self.gridLayout_60.addWidget(self.doubleSpinBox_Poisson_tabTipRadius, 3, 3, 1, 1)

        self.label_83 = QLabel(self.groupBox_29)
        self.label_83.setObjectName(u"label_83")
        sizePolicy1.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy1)

        self.gridLayout_60.addWidget(self.label_83, 3, 0, 1, 1)

        self.label_73 = QLabel(self.groupBox_29)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_60.addWidget(self.label_73, 1, 0, 1, 1)

        self.doubleSpinBox_E_tabTipRadius = QDoubleSpinBox(self.groupBox_29)
        self.doubleSpinBox_E_tabTipRadius.setObjectName(u"doubleSpinBox_E_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_E_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_E_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_E_tabTipRadius.setDecimals(3)
        self.doubleSpinBox_E_tabTipRadius.setMaximum(9999.000000000000000)
        self.doubleSpinBox_E_tabTipRadius.setSingleStep(0.001000000000000)
        self.doubleSpinBox_E_tabTipRadius.setValue(390.000000000000000)

        self.gridLayout_60.addWidget(self.doubleSpinBox_E_tabTipRadius, 3, 1, 1, 1)

        self.label_74 = QLabel(self.groupBox_29)
        self.label_74.setObjectName(u"label_74")
        sizePolicy8.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy8)

        self.gridLayout_60.addWidget(self.label_74, 3, 2, 1, 1)

        self.lineEdit_path_tabTipRadius = QLineEdit(self.groupBox_29)
        self.lineEdit_path_tabTipRadius.setObjectName(u"lineEdit_path_tabTipRadius")
        sizePolicy10.setHeightForWidth(self.lineEdit_path_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabTipRadius.setSizePolicy(sizePolicy10)
        self.lineEdit_path_tabTipRadius.setMinimumSize(QSize(0, 0))
        self.lineEdit_path_tabTipRadius.setMaximumSize(QSize(292, 16777215))

        self.gridLayout_60.addWidget(self.lineEdit_path_tabTipRadius, 1, 1, 1, 3)

        self.lineEdit_MaterialName_tabTipRadius = QLineEdit(self.groupBox_29)
        self.lineEdit_MaterialName_tabTipRadius.setObjectName(u"lineEdit_MaterialName_tabTipRadius")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.lineEdit_MaterialName_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.lineEdit_MaterialName_tabTipRadius.setSizePolicy(sizePolicy13)

        self.gridLayout_60.addWidget(self.lineEdit_MaterialName_tabTipRadius, 0, 1, 1, 3)


        self.gridLayout_58.addWidget(self.groupBox_29, 0, 0, 1, 2)

        self.groupBox_17 = QGroupBox(self.tab_8)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy1.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy1)
        self.groupBox_17.setMinimumSize(QSize(460, 0))
        self.groupBox_17.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_36 = QGridLayout(self.groupBox_17)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_70 = QLabel(self.groupBox_17)
        self.label_70.setObjectName(u"label_70")
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy14)
        self.label_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_70, 0, 0, 1, 1)

        self.label_38 = QLabel(self.groupBox_17)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)

        self.gridLayout_36.addWidget(self.label_38, 2, 0, 1, 1)

        self.doubleSpinBox_Poisson_Tip_tabTipRadius = QDoubleSpinBox(self.groupBox_17)
        self.doubleSpinBox_Poisson_Tip_tabTipRadius.setObjectName(u"doubleSpinBox_Poisson_Tip_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Poisson_Tip_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_Tip_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Poisson_Tip_tabTipRadius.setDecimals(3)
        self.doubleSpinBox_Poisson_Tip_tabTipRadius.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_Tip_tabTipRadius.setValue(0.070000000000000)

        self.gridLayout_36.addWidget(self.doubleSpinBox_Poisson_Tip_tabTipRadius, 2, 3, 1, 1)

        self.label_71 = QLabel(self.groupBox_17)
        self.label_71.setObjectName(u"label_71")
        sizePolicy1.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy1)

        self.gridLayout_36.addWidget(self.label_71, 2, 2, 1, 1)

        self.lineEdit_TipName_tabTipRadius = QLineEdit(self.groupBox_17)
        self.lineEdit_TipName_tabTipRadius.setObjectName(u"lineEdit_TipName_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.lineEdit_TipName_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabTipRadius.setSizePolicy(sizePolicy2)
        self.lineEdit_TipName_tabTipRadius.setMinimumSize(QSize(0, 0))

        self.gridLayout_36.addWidget(self.lineEdit_TipName_tabTipRadius, 0, 1, 1, 3)

        self.doubleSpinBox_E_Tip_tabTipRadius = QDoubleSpinBox(self.groupBox_17)
        self.doubleSpinBox_E_Tip_tabTipRadius.setObjectName(u"doubleSpinBox_E_Tip_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_E_Tip_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_E_Tip_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_E_Tip_tabTipRadius.setDecimals(3)
        self.doubleSpinBox_E_Tip_tabTipRadius.setMaximum(99999.990000000005239)
        self.doubleSpinBox_E_Tip_tabTipRadius.setSingleStep(0.001000000000000)
        self.doubleSpinBox_E_Tip_tabTipRadius.setValue(1141.000000000000000)

        self.gridLayout_36.addWidget(self.doubleSpinBox_E_Tip_tabTipRadius, 2, 1, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_17, 1, 0, 1, 2)

        self.groupBox_15 = QGroupBox(self.tab_8)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy9.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy9)
        self.groupBox_15.setMinimumSize(QSize(460, 0))
        self.groupBox_15.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_65 = QGridLayout(self.groupBox_15)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.doubleSpinBox_relForceRateNoise_tabTipRadius = QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius.setObjectName(u"doubleSpinBox_relForceRateNoise_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius.setSingleStep(0.000100000000000)
        self.doubleSpinBox_relForceRateNoise_tabTipRadius.setValue(0.030000000000000)

        self.gridLayout_65.addWidget(self.doubleSpinBox_relForceRateNoise_tabTipRadius, 0, 1, 1, 1)

        self.label_79 = QLabel(self.groupBox_15)
        self.label_79.setObjectName(u"label_79")
        sizePolicy1.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy1)

        self.gridLayout_65.addWidget(self.label_79, 0, 0, 1, 1)

        self.label_78 = QLabel(self.groupBox_15)
        self.label_78.setObjectName(u"label_78")
        sizePolicy1.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy1)
        self.label_78.setMinimumSize(QSize(128, 0))

        self.gridLayout_65.addWidget(self.label_78, 0, 2, 1, 1)

        self.spinBox_max_size_fluctuation_tabTipRadius = QSpinBox(self.groupBox_15)
        self.spinBox_max_size_fluctuation_tabTipRadius.setObjectName(u"spinBox_max_size_fluctuation_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabTipRadius.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabTipRadius.setValue(5)

        self.gridLayout_65.addWidget(self.spinBox_max_size_fluctuation_tabTipRadius, 0, 3, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_15, 2, 0, 1, 2)

        self.graphicsView_tab_TipAreaFunction_5 = QTabWidget(self.tab_8)
        self.graphicsView_tab_TipAreaFunction_5.setObjectName(u"graphicsView_tab_TipAreaFunction_5")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction_5.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction_5.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction_5.setUsesScrollButtons(True)
        self.tab_29 = QWidget()
        self.tab_29.setObjectName(u"tab_29")
        self.gridLayout_61 = QGridLayout(self.tab_29)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.tabWidget_9 = QTabWidget(self.tab_29)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        sizePolicy6.setHeightForWidth(self.tabWidget_9.sizePolicy().hasHeightForWidth())
        self.tabWidget_9.setSizePolicy(sizePolicy6)
        self.tab_30 = QWidget()
        self.tab_30.setObjectName(u"tab_30")
        self.gridLayout_62 = QGridLayout(self.tab_30)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius = QPushButton(self.tab_30)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.setSizePolicy(sizePolicy1)

        self.gridLayout_62.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius, 3, 0, 1, 4)

        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius = QGraphicsView(self.tab_30)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius")
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setSizePolicy(sizePolicy3)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setMinimumSize(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setMaximumSize(QSize(10000, 10000))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setSizeIncrement(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setBaseSize(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setInteractive(True)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setDragMode(QGraphicsView.NoDrag)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius.setTransformationAnchor(QGraphicsView.NoAnchor)

        self.gridLayout_62.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabTipRadius, 1, 0, 1, 4)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius = QCheckBox(self.tab_30)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius")
        sizePolicy7.setHeightForWidth(self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius.setSizePolicy(sizePolicy7)

        self.gridLayout_62.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius, 2, 1, 1, 1)

        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius = QCheckBox(self.tab_30)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius")
        sizePolicy7.setHeightForWidth(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius.setSizePolicy(sizePolicy7)

        self.gridLayout_62.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius, 2, 0, 1, 1)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius = QCheckBox(self.tab_30)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius.setSizePolicy(sizePolicy1)

        self.gridLayout_62.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius, 2, 2, 1, 1)

        self.tabWidget_9.addTab(self.tab_30, "")
        self.tab_31 = QWidget()
        self.tab_31.setObjectName(u"tab_31")
        self.gridLayout_63 = QGridLayout(self.tab_31)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_2 = QGraphicsView(self.tab_31)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_2.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_2")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_2.setSizePolicy(sizePolicy)

        self.gridLayout_63.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_2, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_31, "")

        self.gridLayout_61.addWidget(self.tabWidget_9, 0, 1, 1, 1)

        self.graphicsView_tab_TipAreaFunction_5.addTab(self.tab_29, "")
        self.tab_32 = QWidget()
        self.tab_32.setObjectName(u"tab_32")
        self.gridLayout_64 = QGridLayout(self.tab_32)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius = QPushButton(self.tab_32)
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.setObjectName(u"pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.setSizePolicy(sizePolicy1)

        self.gridLayout_64.addWidget(self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius, 2, 0, 1, 1)

        self.graphicsView_HertzianFitting_tabTipRadius = QGraphicsView(self.tab_32)
        self.graphicsView_HertzianFitting_tabTipRadius.setObjectName(u"graphicsView_HertzianFitting_tabTipRadius")
        sizePolicy3.setHeightForWidth(self.graphicsView_HertzianFitting_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.graphicsView_HertzianFitting_tabTipRadius.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.graphicsView_HertzianFitting_tabTipRadius, 1, 0, 1, 2)

        self.graphicsView_tab_TipAreaFunction_5.addTab(self.tab_32, "")
        self.tab_33 = QWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.gridLayout_66 = QGridLayout(self.tab_33)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.label_80 = QLabel(self.tab_33)
        self.label_80.setObjectName(u"label_80")
        sizePolicy1.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy1)

        self.gridLayout_66.addWidget(self.label_80, 0, 0, 1, 1)

        self.lineEdit_TipRadius_tabTipRadius = QLineEdit(self.tab_33)
        self.lineEdit_TipRadius_tabTipRadius.setObjectName(u"lineEdit_TipRadius_tabTipRadius")
        sizePolicy7.setHeightForWidth(self.lineEdit_TipRadius_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipRadius_tabTipRadius.setSizePolicy(sizePolicy7)
        self.lineEdit_TipRadius_tabTipRadius.setReadOnly(True)

        self.gridLayout_66.addWidget(self.lineEdit_TipRadius_tabTipRadius, 0, 1, 1, 1)

        self.lineEdit_reducedModulus_tabTipRadius = QLineEdit(self.tab_33)
        self.lineEdit_reducedModulus_tabTipRadius.setObjectName(u"lineEdit_reducedModulus_tabTipRadius")
        sizePolicy7.setHeightForWidth(self.lineEdit_reducedModulus_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.lineEdit_reducedModulus_tabTipRadius.setSizePolicy(sizePolicy7)
        self.lineEdit_reducedModulus_tabTipRadius.setReadOnly(True)

        self.gridLayout_66.addWidget(self.lineEdit_reducedModulus_tabTipRadius, 0, 3, 1, 1)

        self.graphicsView_CalculatedTipRadius_tabTipRadius = QGraphicsView(self.tab_33)
        self.graphicsView_CalculatedTipRadius_tabTipRadius.setObjectName(u"graphicsView_CalculatedTipRadius_tabTipRadius")
        sizePolicy.setHeightForWidth(self.graphicsView_CalculatedTipRadius_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.graphicsView_CalculatedTipRadius_tabTipRadius.setSizePolicy(sizePolicy)

        self.gridLayout_66.addWidget(self.graphicsView_CalculatedTipRadius_tabTipRadius, 1, 0, 2, 8)

        self.label_81 = QLabel(self.tab_33)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_66.addWidget(self.label_81, 0, 2, 1, 1)

        self.graphicsView_tab_TipAreaFunction_5.addTab(self.tab_33, "")

        self.gridLayout_58.addWidget(self.graphicsView_tab_TipAreaFunction_5, 0, 3, 19, 1)

        self.groupBox_4 = QGroupBox(self.tab_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy15 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy15)
        self.groupBox_4.setMinimumSize(QSize(230, 0))
        self.groupBox_4.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_57 = QGridLayout(self.groupBox_4)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.comboBox_method_tabTipRadius = QComboBox(self.groupBox_4)
        self.comboBox_method_tabTipRadius.addItem("")
        self.comboBox_method_tabTipRadius.addItem("")
        self.comboBox_method_tabTipRadius.addItem("")
        self.comboBox_method_tabTipRadius.setObjectName(u"comboBox_method_tabTipRadius")
        self.comboBox_method_tabTipRadius.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabTipRadius.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabTipRadius.setMinimumSize(QSize(120, 0))
        self.comboBox_method_tabTipRadius.setEditable(False)

        self.gridLayout_57.addWidget(self.comboBox_method_tabTipRadius, 1, 2, 1, 1)

        self.comboBox_equipment_tabTipRadius = QComboBox(self.groupBox_4)
        self.comboBox_equipment_tabTipRadius.addItem("")
        self.comboBox_equipment_tabTipRadius.setObjectName(u"comboBox_equipment_tabTipRadius")
        self.comboBox_equipment_tabTipRadius.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabTipRadius.setSizePolicy(sizePolicy2)

        self.gridLayout_57.addWidget(self.comboBox_equipment_tabTipRadius, 2, 2, 1, 1)

        self.label_72 = QLabel(self.groupBox_4)
        self.label_72.setObjectName(u"label_72")
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy16)
        self.label_72.setMaximumSize(QSize(16777215, 16777215))
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.label_72, 1, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox_4)
        self.label_37.setObjectName(u"label_37")
        sizePolicy8.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy8)

        self.gridLayout_57.addWidget(self.label_37, 2, 1, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.groupBox_49 = QGroupBox(self.tab_8)
        self.groupBox_49.setObjectName(u"groupBox_49")
        sizePolicy15.setHeightForWidth(self.groupBox_49.sizePolicy().hasHeightForWidth())
        self.groupBox_49.setSizePolicy(sizePolicy15)
        self.groupBox_49.setMinimumSize(QSize(230, 0))
        self.groupBox_49.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_99 = QGridLayout(self.groupBox_49)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.label_82 = QLabel(self.groupBox_49)
        self.label_82.setObjectName(u"label_82")
        sizePolicy1.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy1)
        self.label_82.setMinimumSize(QSize(0, 0))

        self.gridLayout_99.addWidget(self.label_82, 0, 0, 1, 1)

        self.doubleSpinBox_Start_Pmax_tabTipRadius = QDoubleSpinBox(self.groupBox_49)
        self.doubleSpinBox_Start_Pmax_tabTipRadius.setObjectName(u"doubleSpinBox_Start_Pmax_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabTipRadius.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabTipRadius.setValue(0.980000000000000)

        self.gridLayout_99.addWidget(self.doubleSpinBox_Start_Pmax_tabTipRadius, 0, 1, 1, 1)

        self.label_76 = QLabel(self.groupBox_49)
        self.label_76.setObjectName(u"label_76")
        sizePolicy9.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy9)
        self.label_76.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_99.addWidget(self.label_76, 1, 0, 1, 1)

        self.doubleSpinBox_End_Pmax_tabTipRadius = QDoubleSpinBox(self.groupBox_49)
        self.doubleSpinBox_End_Pmax_tabTipRadius.setObjectName(u"doubleSpinBox_End_Pmax_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabTipRadius.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabTipRadius.setValue(0.500000000000000)

        self.gridLayout_99.addWidget(self.doubleSpinBox_End_Pmax_tabTipRadius, 1, 1, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_49, 4, 0, 1, 1)

        self.groupBox_27 = QGroupBox(self.tab_8)
        self.groupBox_27.setObjectName(u"groupBox_27")
        sizePolicy15.setHeightForWidth(self.groupBox_27.sizePolicy().hasHeightForWidth())
        self.groupBox_27.setSizePolicy(sizePolicy15)
        self.groupBox_27.setMinimumSize(QSize(0, 0))
        self.groupBox_27.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_27)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_UsingRate2findSurface_tabTipRadius = QCheckBox(self.groupBox_27)
        self.checkBox_UsingRate2findSurface_tabTipRadius.setObjectName(u"checkBox_UsingRate2findSurface_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabTipRadius.setSizePolicy(sizePolicy1)
        self.checkBox_UsingRate2findSurface_tabTipRadius.setMinimumSize(QSize(150, 0))
        self.checkBox_UsingRate2findSurface_tabTipRadius.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_UsingRate2findSurface_tabTipRadius, 0, 0, 1, 1)

        self.doubleSpinBox_Rate2findSurface_tabTipRadius = QDoubleSpinBox(self.groupBox_27)
        self.doubleSpinBox_Rate2findSurface_tabTipRadius.setObjectName(u"doubleSpinBox_Rate2findSurface_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabTipRadius.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabTipRadius.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabTipRadius.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_Rate2findSurface_tabTipRadius, 0, 1, 1, 1)

        self.label_85 = QLabel(self.groupBox_27)
        self.label_85.setObjectName(u"label_85")
        sizePolicy3.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy3)
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_85, 1, 0, 1, 1)

        self.spinBox_DataFilterSize_tabTipRadius = QSpinBox(self.groupBox_27)
        self.spinBox_DataFilterSize_tabTipRadius.setObjectName(u"spinBox_DataFilterSize_tabTipRadius")
        sizePolicy2.setHeightForWidth(self.spinBox_DataFilterSize_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.spinBox_DataFilterSize_tabTipRadius.setSizePolicy(sizePolicy2)
        self.spinBox_DataFilterSize_tabTipRadius.setValue(5)

        self.gridLayout_3.addWidget(self.spinBox_DataFilterSize_tabTipRadius, 1, 1, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_27, 3, 1, 1, 1)

        self.groupBox_28 = QGroupBox(self.tab_8)
        self.groupBox_28.setObjectName(u"groupBox_28")
        sizePolicy1.setHeightForWidth(self.groupBox_28.sizePolicy().hasHeightForWidth())
        self.groupBox_28.setSizePolicy(sizePolicy1)
        self.groupBox_28.setMinimumSize(QSize(0, 0))
        self.groupBox_28.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_59 = QGridLayout(self.groupBox_28)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.lineEdit_FrameCompliance_tabTipRadius = QLineEdit(self.groupBox_28)
        self.lineEdit_FrameCompliance_tabTipRadius.setObjectName(u"lineEdit_FrameCompliance_tabTipRadius")
        self.lineEdit_FrameCompliance_tabTipRadius.setReadOnly(True)

        self.gridLayout_59.addWidget(self.lineEdit_FrameCompliance_tabTipRadius, 0, 1, 1, 1)

        self.Copy_FrameCompliance_tabTipRadius = QPushButton(self.groupBox_28)
        self.Copy_FrameCompliance_tabTipRadius.setObjectName(u"Copy_FrameCompliance_tabTipRadius")

        self.gridLayout_59.addWidget(self.Copy_FrameCompliance_tabTipRadius, 1, 1, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_28, 4, 1, 1, 1)

        self.progressBar_tabTipRadius = QProgressBar(self.tab_8)
        self.progressBar_tabTipRadius.setObjectName(u"progressBar_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.progressBar_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.progressBar_tabTipRadius.setSizePolicy(sizePolicy1)
        self.progressBar_tabTipRadius.setMinimumSize(QSize(0, 0))
        self.progressBar_tabTipRadius.setMaximumSize(QSize(224, 16777215))
        self.progressBar_tabTipRadius.setValue(0)

        self.gridLayout_58.addWidget(self.progressBar_tabTipRadius, 5, 1, 1, 1)

        self.pushButton_Calculate_tabTipRadius = QPushButton(self.tab_8)
        self.pushButton_Calculate_tabTipRadius.setObjectName(u"pushButton_Calculate_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.pushButton_Calculate_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate_tabTipRadius.setSizePolicy(sizePolicy1)
        self.pushButton_Calculate_tabTipRadius.setMinimumSize(QSize(0, 0))
        self.pushButton_Calculate_tabTipRadius.setMaximumSize(QSize(224, 16777215))

        self.gridLayout_58.addWidget(self.pushButton_Calculate_tabTipRadius, 6, 1, 1, 1)

        self.groupBox_46 = QGroupBox(self.tab_8)
        self.groupBox_46.setObjectName(u"groupBox_46")
        sizePolicy15.setHeightForWidth(self.groupBox_46.sizePolicy().hasHeightForWidth())
        self.groupBox_46.setSizePolicy(sizePolicy15)
        self.groupBox_46.setMinimumSize(QSize(230, 0))
        self.groupBox_46.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_96 = QGridLayout(self.groupBox_46)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.checkBox_UsingDriftUnloading_tabTipRadius = QCheckBox(self.groupBox_46)
        self.checkBox_UsingDriftUnloading_tabTipRadius.setObjectName(u"checkBox_UsingDriftUnloading_tabTipRadius")

        self.gridLayout_96.addWidget(self.checkBox_UsingDriftUnloading_tabTipRadius, 0, 0, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_46, 5, 0, 2, 1)

        self.tableWidget_tabTipRadius = QTableWidget(self.tab_8)
        if (self.tableWidget_tabTipRadius.columnCount() < 3):
            self.tableWidget_tabTipRadius.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTipRadius.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTipRadius.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabTipRadius.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        if (self.tableWidget_tabTipRadius.rowCount() < 1):
            self.tableWidget_tabTipRadius.setRowCount(1)
        self.tableWidget_tabTipRadius.setObjectName(u"tableWidget_tabTipRadius")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.tableWidget_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabTipRadius.setSizePolicy(sizePolicy17)
        self.tableWidget_tabTipRadius.setMinimumSize(QSize(205, 500))
        self.tableWidget_tabTipRadius.setMaximumSize(QSize(205, 16777215))
        self.tableWidget_tabTipRadius.setAutoScroll(True)
        self.tableWidget_tabTipRadius.setRowCount(1)
        self.tableWidget_tabTipRadius.setColumnCount(3)
        self.tableWidget_tabTipRadius.horizontalHeader().setVisible(True)
        self.tableWidget_tabTipRadius.horizontalHeader().setMinimumSectionSize(65)
        self.tableWidget_tabTipRadius.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_tabTipRadius.horizontalHeader().setHighlightSections(True)
        self.tableWidget_tabTipRadius.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_58.addWidget(self.tableWidget_tabTipRadius, 0, 2, 6, 1)

        self.pushButton_SelectAll_tabTipRadius = QPushButton(self.tab_8)
        self.pushButton_SelectAll_tabTipRadius.setObjectName(u"pushButton_SelectAll_tabTipRadius")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectAll_tabTipRadius.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectAll_tabTipRadius.setSizePolicy(sizePolicy1)
        self.pushButton_SelectAll_tabTipRadius.setMaximumSize(QSize(205, 16777215))

        self.gridLayout_58.addWidget(self.pushButton_SelectAll_tabTipRadius, 6, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.gridLayout_16.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_27 = QGridLayout(self.tab_13)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.tabWidget_5 = QTabWidget(self.tab_13)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_37 = QGridLayout(self.tab_14)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.groupBox_16 = QGroupBox(self.tab_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy1.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy1)
        self.groupBox_16.setMinimumSize(QSize(460, 0))
        self.groupBox_16.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_35 = QGridLayout(self.groupBox_16)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_42 = QLabel(self.groupBox_16)
        self.label_42.setObjectName(u"label_42")
        sizePolicy1.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy1)

        self.gridLayout_35.addWidget(self.label_42, 1, 4, 1, 1)

        self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness = QDoubleSpinBox(self.groupBox_16)
        self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness.setObjectName(u"doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness.setSingleStep(0.000100000000000)
        self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness.setValue(0.010000000000000)

        self.gridLayout_35.addWidget(self.doubleSpinBox_relForceRateNoise_tabHE_FrameStiffness, 1, 3, 1, 1)

        self.label_43 = QLabel(self.groupBox_16)
        self.label_43.setObjectName(u"label_43")
        sizePolicy1.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy1)

        self.gridLayout_35.addWidget(self.label_43, 1, 0, 1, 1)

        self.spinBox_max_size_fluctuation_tabHE_FrameStiffness = QSpinBox(self.groupBox_16)
        self.spinBox_max_size_fluctuation_tabHE_FrameStiffness.setObjectName(u"spinBox_max_size_fluctuation_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabHE_FrameStiffness.setValue(1)

        self.gridLayout_35.addWidget(self.spinBox_max_size_fluctuation_tabHE_FrameStiffness, 1, 5, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_16, 2, 0, 1, 2)

        self.graphicsView_tab_TipAreaFunction_3 = QTabWidget(self.tab_14)
        self.graphicsView_tab_TipAreaFunction_3.setObjectName(u"graphicsView_tab_TipAreaFunction_3")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction_3.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction_3.setUsesScrollButtons(True)
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_31 = QGridLayout(self.tab_16)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.tabWidget_6 = QTabWidget(self.tab_16)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.gridLayout_32 = QGridLayout(self.tab_17)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness = QGraphicsView(self.tab_17)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness")
        sizePolicy18 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy18.setHorizontalStretch(100)
        sizePolicy18.setVerticalStretch(100)
        sizePolicy18.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setSizePolicy(sizePolicy18)

        self.gridLayout_32.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness, 1, 0, 1, 5)

        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness = QCheckBox(self.tab_17)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setSizePolicy(sizePolicy7)

        self.gridLayout_32.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness, 2, 0, 1, 1)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE_FrameStiffness = QCheckBox(self.tab_17)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE_FrameStiffness.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabHE_FrameStiffness")

        self.gridLayout_32.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabHE_FrameStiffness, 2, 1, 1, 1)

        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness = QPushButton(self.tab_17)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setSizePolicy(sizePolicy1)

        self.gridLayout_32.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness, 3, 0, 1, 3)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE_FrameStiffness = QCheckBox(self.tab_17)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE_FrameStiffness")

        self.gridLayout_32.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE_FrameStiffness, 2, 2, 1, 1)

        self.tabWidget_6.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.gridLayout_33 = QGridLayout(self.tab_18)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_3 = QGraphicsView(self.tab_18)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_3.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_3")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_3.setSizePolicy(sizePolicy)

        self.gridLayout_33.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_3, 0, 0, 1, 1)

        self.tabWidget_6.addTab(self.tab_18, "")

        self.gridLayout_31.addWidget(self.tabWidget_6, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_3.addTab(self.tab_16, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_34 = QGridLayout(self.tab_19)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_40 = QLabel(self.tab_19)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_34.addWidget(self.label_40, 1, 0, 1, 1)

        self.lineEdit_FrameStiffness_tabHE_FrameStiffness = QLineEdit(self.tab_19)
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setObjectName(u"lineEdit_FrameStiffness_tabHE_FrameStiffness")
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameStiffness_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setFrame(True)
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setDragEnabled(False)
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setReadOnly(True)
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setClearButtonEnabled(False)

        self.gridLayout_34.addWidget(self.lineEdit_FrameStiffness_tabHE_FrameStiffness, 1, 1, 1, 1)

        self.label_39 = QLabel(self.tab_19)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_34.addWidget(self.label_39, 1, 2, 1, 1)

        self.graphicsView_tabHE_FrameStiffness = QGraphicsView(self.tab_19)
        self.graphicsView_tabHE_FrameStiffness.setObjectName(u"graphicsView_tabHE_FrameStiffness")
        self.graphicsView_tabHE_FrameStiffness.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_34.addWidget(self.graphicsView_tabHE_FrameStiffness, 3, 0, 1, 7)

        self.lineEdit_FrameCompliance_tabHE_FrameStiffness = QLineEdit(self.tab_19)
        self.lineEdit_FrameCompliance_tabHE_FrameStiffness.setObjectName(u"lineEdit_FrameCompliance_tabHE_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameCompliance_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameCompliance_tabHE_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameCompliance_tabHE_FrameStiffness.setReadOnly(True)

        self.gridLayout_34.addWidget(self.lineEdit_FrameCompliance_tabHE_FrameStiffness, 1, 3, 1, 1)

        self.graphicsView_tab_TipAreaFunction_3.addTab(self.tab_19, "")

        self.gridLayout_37.addWidget(self.graphicsView_tab_TipAreaFunction_3, 0, 3, 22, 1)

        self.groupBox_56 = QGroupBox(self.tab_14)
        self.groupBox_56.setObjectName(u"groupBox_56")
        sizePolicy1.setHeightForWidth(self.groupBox_56.sizePolicy().hasHeightForWidth())
        self.groupBox_56.setSizePolicy(sizePolicy1)
        self.groupBox_56.setMinimumSize(QSize(460, 0))
        self.groupBox_56.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_105 = QGridLayout(self.groupBox_56)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.comboBox_CalculationMethod_tabHE_FrameStiffness = QComboBox(self.groupBox_56)
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.addItem("")
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.addItem("")
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.setObjectName(u"comboBox_CalculationMethod_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.comboBox_CalculationMethod_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.setEditable(False)

        self.gridLayout_105.addWidget(self.comboBox_CalculationMethod_tabHE_FrameStiffness, 0, 0, 1, 1)

        self.groupBox_60 = QGroupBox(self.groupBox_56)
        self.groupBox_60.setObjectName(u"groupBox_60")
        sizePolicy4.setHeightForWidth(self.groupBox_60.sizePolicy().hasHeightForWidth())
        self.groupBox_60.setSizePolicy(sizePolicy4)
        self.groupBox_60.setMinimumSize(QSize(0, 0))
        self.groupBox_60.setMaximumSize(QSize(44000, 16777215))
        self.gridLayout_108 = QGridLayout(self.groupBox_60)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.label_116 = QLabel(self.groupBox_60)
        self.label_116.setObjectName(u"label_116")
        sizePolicy8.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy8)

        self.gridLayout_108.addWidget(self.label_116, 2, 3, 1, 1)

        self.lineEdit_TAF1_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF1_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF1_tabHE_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF1_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF1_tabHE_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF1_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF1_tabHE_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF1_tabHE_FrameStiffness.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_TAF1_tabHE_FrameStiffness.setReadOnly(True)

        self.gridLayout_108.addWidget(self.lineEdit_TAF1_tabHE_FrameStiffness, 2, 2, 1, 1)

        self.label_59 = QLabel(self.groupBox_60)
        self.label_59.setObjectName(u"label_59")
        sizePolicy9.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy9)
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_108.addWidget(self.label_59, 0, 0, 1, 3)

        self.lineEdit_TAF5_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF5_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF5_tabHE_FrameStiffness")
        self.lineEdit_TAF5_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF5_tabHE_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF5_tabHE_FrameStiffness.setReadOnly(True)

        self.gridLayout_108.addWidget(self.lineEdit_TAF5_tabHE_FrameStiffness, 2, 10, 1, 1)

        self.label_122 = QLabel(self.groupBox_60)
        self.label_122.setObjectName(u"label_122")
        sizePolicy8.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy8)
        self.label_122.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_108.addWidget(self.label_122, 2, 5, 1, 1)

        self.lineEdit_TAF3_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF3_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF3_tabHE_FrameStiffness")
        sizePolicy11.setHeightForWidth(self.lineEdit_TAF3_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF3_tabHE_FrameStiffness.setSizePolicy(sizePolicy11)
        self.lineEdit_TAF3_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF3_tabHE_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF3_tabHE_FrameStiffness.setReadOnly(True)

        self.gridLayout_108.addWidget(self.lineEdit_TAF3_tabHE_FrameStiffness, 2, 6, 1, 1)

        self.lineEdit_TAF2_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF2_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF2_tabHE_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF2_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF2_tabHE_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF2_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF2_tabHE_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF2_tabHE_FrameStiffness.setReadOnly(True)

        self.gridLayout_108.addWidget(self.lineEdit_TAF2_tabHE_FrameStiffness, 2, 4, 1, 1)

        self.label_123 = QLabel(self.groupBox_60)
        self.label_123.setObjectName(u"label_123")
        sizePolicy8.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy8)

        self.gridLayout_108.addWidget(self.label_123, 2, 7, 1, 1)

        self.lineEdit_TAF4_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF4_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF4_tabHE_FrameStiffness")
        self.lineEdit_TAF4_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF4_tabHE_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF4_tabHE_FrameStiffness.setReadOnly(True)

        self.gridLayout_108.addWidget(self.lineEdit_TAF4_tabHE_FrameStiffness, 2, 8, 1, 1)

        self.label_98 = QLabel(self.groupBox_60)
        self.label_98.setObjectName(u"label_98")
        sizePolicy8.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy8)

        self.gridLayout_108.addWidget(self.label_98, 2, 9, 1, 1)

        self.label_121 = QLabel(self.groupBox_60)
        self.label_121.setObjectName(u"label_121")
        sizePolicy8.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy8)

        self.gridLayout_108.addWidget(self.label_121, 2, 11, 1, 1)

        self.lineEdit_TAF6_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF6_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF6_tabHE_FrameStiffness")
        self.lineEdit_TAF6_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_108.addWidget(self.lineEdit_TAF6_tabHE_FrameStiffness, 3, 4, 1, 1)

        self.lineEdit_TAF7_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF7_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF7_tabHE_FrameStiffness")
        self.lineEdit_TAF7_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_108.addWidget(self.lineEdit_TAF7_tabHE_FrameStiffness, 3, 6, 1, 1)

        self.lineEdit_TAF8_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF8_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF8_tabHE_FrameStiffness")
        self.lineEdit_TAF8_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_108.addWidget(self.lineEdit_TAF8_tabHE_FrameStiffness, 3, 8, 1, 1)

        self.lineEdit_TAF9_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TAF9_tabHE_FrameStiffness.setObjectName(u"lineEdit_TAF9_tabHE_FrameStiffness")
        self.lineEdit_TAF9_tabHE_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_108.addWidget(self.lineEdit_TAF9_tabHE_FrameStiffness, 3, 10, 1, 1)

        self.label_147 = QLabel(self.groupBox_60)
        self.label_147.setObjectName(u"label_147")

        self.gridLayout_108.addWidget(self.label_147, 3, 5, 1, 1)

        self.label_148 = QLabel(self.groupBox_60)
        self.label_148.setObjectName(u"label_148")

        self.gridLayout_108.addWidget(self.label_148, 3, 7, 1, 1)

        self.label_149 = QLabel(self.groupBox_60)
        self.label_149.setObjectName(u"label_149")

        self.gridLayout_108.addWidget(self.label_149, 3, 9, 1, 1)

        self.label_150 = QLabel(self.groupBox_60)
        self.label_150.setObjectName(u"label_150")

        self.gridLayout_108.addWidget(self.label_150, 3, 11, 1, 1)

        self.label_60 = QLabel(self.groupBox_60)
        self.label_60.setObjectName(u"label_60")
        sizePolicy8.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy8)
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_108.addWidget(self.label_60, 2, 0, 1, 2)

        self.Copy_TAF_tabHE_FrameStiffness = QPushButton(self.groupBox_60)
        self.Copy_TAF_tabHE_FrameStiffness.setObjectName(u"Copy_TAF_tabHE_FrameStiffness")
        sizePolicy3.setHeightForWidth(self.Copy_TAF_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.Copy_TAF_tabHE_FrameStiffness.setSizePolicy(sizePolicy3)
        self.Copy_TAF_tabHE_FrameStiffness.setMinimumSize(QSize(110, 0))

        self.gridLayout_108.addWidget(self.Copy_TAF_tabHE_FrameStiffness, 6, 0, 1, 12)

        self.lineEdit_TipName_tabHE_FrameStiffness = QLineEdit(self.groupBox_60)
        self.lineEdit_TipName_tabHE_FrameStiffness.setObjectName(u"lineEdit_TipName_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.lineEdit_TipName_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_108.addWidget(self.lineEdit_TipName_tabHE_FrameStiffness, 0, 3, 1, 9)


        self.gridLayout_105.addWidget(self.groupBox_60, 1, 0, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_56, 1, 0, 1, 2)

        self.groupBox_14 = QGroupBox(self.tab_14)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy1.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy1)
        self.groupBox_14.setMinimumSize(QSize(230, 0))
        self.groupBox_14.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_29 = QGridLayout(self.groupBox_14)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_36 = QLabel(self.groupBox_14)
        self.label_36.setObjectName(u"label_36")
        sizePolicy9.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy9)
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_36, 1, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_14)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)

        self.gridLayout_29.addWidget(self.label_35, 2, 1, 1, 1)

        self.comboBox_method_tabHE_FrameStiffness = QComboBox(self.groupBox_14)
        self.comboBox_method_tabHE_FrameStiffness.addItem("")
        self.comboBox_method_tabHE_FrameStiffness.addItem("")
        self.comboBox_method_tabHE_FrameStiffness.addItem("")
        self.comboBox_method_tabHE_FrameStiffness.setObjectName(u"comboBox_method_tabHE_FrameStiffness")
        self.comboBox_method_tabHE_FrameStiffness.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabHE_FrameStiffness.setMinimumSize(QSize(120, 0))
        self.comboBox_method_tabHE_FrameStiffness.setEditable(False)

        self.gridLayout_29.addWidget(self.comboBox_method_tabHE_FrameStiffness, 1, 2, 1, 1)

        self.comboBox_equipment_tabHE_FrameStiffness = QComboBox(self.groupBox_14)
        self.comboBox_equipment_tabHE_FrameStiffness.addItem("")
        self.comboBox_equipment_tabHE_FrameStiffness.setObjectName(u"comboBox_equipment_tabHE_FrameStiffness")
        self.comboBox_equipment_tabHE_FrameStiffness.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_29.addWidget(self.comboBox_equipment_tabHE_FrameStiffness, 2, 2, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_14, 3, 0, 3, 1)

        self.groupBox_25 = QGroupBox(self.tab_14)
        self.groupBox_25.setObjectName(u"groupBox_25")
        sizePolicy1.setHeightForWidth(self.groupBox_25.sizePolicy().hasHeightForWidth())
        self.groupBox_25.setSizePolicy(sizePolicy1)
        self.groupBox_25.setMinimumSize(QSize(224, 0))
        self.groupBox_25.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_55 = QGridLayout(self.groupBox_25)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness = QDoubleSpinBox(self.groupBox_25)
        self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness.setObjectName(u"doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness.setValue(1.000000000000000)

        self.gridLayout_55.addWidget(self.doubleSpinBox_Rate2findSurface_tabHE_FrameStiffness, 0, 1, 1, 1)

        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness = QCheckBox(self.groupBox_25)
        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.setObjectName(u"checkBox_UsingRate2findSurface_tabHE_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.setSizePolicy(sizePolicy7)
        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.setMinimumSize(QSize(0, 0))
        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.setChecked(True)

        self.gridLayout_55.addWidget(self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness, 0, 0, 1, 1)

        self.label_89 = QLabel(self.groupBox_25)
        self.label_89.setObjectName(u"label_89")
        sizePolicy9.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy9)
        self.label_89.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_89, 1, 0, 1, 1)

        self.spinBox_DataFilterSize_tabHE_FrameStiffness = QSpinBox(self.groupBox_25)
        self.spinBox_DataFilterSize_tabHE_FrameStiffness.setObjectName(u"spinBox_DataFilterSize_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.spinBox_DataFilterSize_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.spinBox_DataFilterSize_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.spinBox_DataFilterSize_tabHE_FrameStiffness.setValue(5)

        self.gridLayout_55.addWidget(self.spinBox_DataFilterSize_tabHE_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_25, 3, 1, 3, 1)

        self.groupBox_13 = QGroupBox(self.tab_14)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.groupBox_13.setMinimumSize(QSize(460, 0))
        self.gridLayout_28 = QGridLayout(self.groupBox_13)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_5 = QLabel(self.groupBox_13)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_path_tabHE_FrameStiffness = QLineEdit(self.groupBox_13)
        self.lineEdit_path_tabHE_FrameStiffness.setObjectName(u"lineEdit_path_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.lineEdit_path_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_28.addWidget(self.lineEdit_path_tabHE_FrameStiffness, 0, 1, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_13, 0, 0, 1, 2)

        self.pushButton_SelectAll_tabHE_FrameStiffness = QPushButton(self.tab_14)
        self.pushButton_SelectAll_tabHE_FrameStiffness.setObjectName(u"pushButton_SelectAll_tabHE_FrameStiffness")
        self.pushButton_SelectAll_tabHE_FrameStiffness.setMinimumSize(QSize(200, 0))
        self.pushButton_SelectAll_tabHE_FrameStiffness.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_37.addWidget(self.pushButton_SelectAll_tabHE_FrameStiffness, 8, 2, 1, 1)

        self.groupBox_26 = QGroupBox(self.tab_14)
        self.groupBox_26.setObjectName(u"groupBox_26")
        sizePolicy1.setHeightForWidth(self.groupBox_26.sizePolicy().hasHeightForWidth())
        self.groupBox_26.setSizePolicy(sizePolicy1)
        self.groupBox_26.setMinimumSize(QSize(224, 0))
        self.groupBox_26.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_56 = QGridLayout(self.groupBox_26)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness = QDoubleSpinBox(self.groupBox_26)
        self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness.setObjectName(u"doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness")
        sizePolicy5.setHeightForWidth(self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness.setSizePolicy(sizePolicy5)
        self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness.setSingleStep(0.100000000000000)
        self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness.setValue(0.100000000000000)

        self.gridLayout_56.addWidget(self.doubleSpinBox_critDepthStiffness_tabHE_FrameStiffness, 0, 1, 1, 1)

        self.label_68 = QLabel(self.groupBox_26)
        self.label_68.setObjectName(u"label_68")
        sizePolicy8.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy8)

        self.gridLayout_56.addWidget(self.label_68, 0, 0, 1, 1)

        self.label_69 = QLabel(self.groupBox_26)
        self.label_69.setObjectName(u"label_69")
        sizePolicy9.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy9)
        self.label_69.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_56.addWidget(self.label_69, 1, 0, 1, 1)

        self.doubleSpinBox_critForceStiffness_tabHE_FrameStiffness = QDoubleSpinBox(self.groupBox_26)
        self.doubleSpinBox_critForceStiffness_tabHE_FrameStiffness.setObjectName(u"doubleSpinBox_critForceStiffness_tabHE_FrameStiffness")
        self.doubleSpinBox_critForceStiffness_tabHE_FrameStiffness.setMaximum(999.000000000000000)
        self.doubleSpinBox_critForceStiffness_tabHE_FrameStiffness.setValue(15.000000000000000)

        self.gridLayout_56.addWidget(self.doubleSpinBox_critForceStiffness_tabHE_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_26, 6, 1, 1, 1)

        self.groupBox_51 = QGroupBox(self.tab_14)
        self.groupBox_51.setObjectName(u"groupBox_51")
        sizePolicy1.setHeightForWidth(self.groupBox_51.sizePolicy().hasHeightForWidth())
        self.groupBox_51.setSizePolicy(sizePolicy1)
        self.groupBox_51.setMinimumSize(QSize(230, 0))
        self.groupBox_51.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_101 = QGridLayout(self.groupBox_51)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness = QDoubleSpinBox(self.groupBox_51)
        self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness.setObjectName(u"doubleSpinBox_Start_Pmax_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness.setValue(0.980000000000000)

        self.gridLayout_101.addWidget(self.doubleSpinBox_Start_Pmax_tabHE_FrameStiffness, 0, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_51)
        self.label_41.setObjectName(u"label_41")
        sizePolicy1.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy1)

        self.gridLayout_101.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_44 = QLabel(self.groupBox_51)
        self.label_44.setObjectName(u"label_44")
        sizePolicy9.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy9)
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_101.addWidget(self.label_44, 1, 0, 1, 1)

        self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness = QDoubleSpinBox(self.groupBox_51)
        self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness.setObjectName(u"doubleSpinBox_End_Pmax_tabHE_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness.setValue(0.500000000000000)

        self.gridLayout_101.addWidget(self.doubleSpinBox_End_Pmax_tabHE_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_51, 6, 0, 1, 1)

        self.progressBar_tabHE_FrameStiffness = QProgressBar(self.tab_14)
        self.progressBar_tabHE_FrameStiffness.setObjectName(u"progressBar_tabHE_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.progressBar_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.progressBar_tabHE_FrameStiffness.setSizePolicy(sizePolicy1)
        self.progressBar_tabHE_FrameStiffness.setMinimumSize(QSize(224, 0))
        self.progressBar_tabHE_FrameStiffness.setMaximumSize(QSize(224, 16777215))
        self.progressBar_tabHE_FrameStiffness.setValue(0)

        self.gridLayout_37.addWidget(self.progressBar_tabHE_FrameStiffness, 7, 1, 1, 1)

        self.pushButton_Calculate_tabHE_FrameStiffness = QPushButton(self.tab_14)
        self.pushButton_Calculate_tabHE_FrameStiffness.setObjectName(u"pushButton_Calculate_tabHE_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_Calculate_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate_tabHE_FrameStiffness.setSizePolicy(sizePolicy1)
        self.pushButton_Calculate_tabHE_FrameStiffness.setMinimumSize(QSize(224, 0))
        self.pushButton_Calculate_tabHE_FrameStiffness.setMaximumSize(QSize(224, 16777215))
        self.pushButton_Calculate_tabHE_FrameStiffness.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_37.addWidget(self.pushButton_Calculate_tabHE_FrameStiffness, 8, 1, 1, 1)

        self.groupBox_41 = QGroupBox(self.tab_14)
        self.groupBox_41.setObjectName(u"groupBox_41")
        sizePolicy1.setHeightForWidth(self.groupBox_41.sizePolicy().hasHeightForWidth())
        self.groupBox_41.setSizePolicy(sizePolicy1)
        self.groupBox_41.setMinimumSize(QSize(230, 0))
        self.groupBox_41.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_91 = QGridLayout(self.groupBox_41)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.checkBox_UsingDriftUnloading_tabHE_FrameStiffness = QCheckBox(self.groupBox_41)
        self.checkBox_UsingDriftUnloading_tabHE_FrameStiffness.setObjectName(u"checkBox_UsingDriftUnloading_tabHE_FrameStiffness")
        self.checkBox_UsingDriftUnloading_tabHE_FrameStiffness.setEnabled(True)
        self.checkBox_UsingDriftUnloading_tabHE_FrameStiffness.setChecked(True)

        self.gridLayout_91.addWidget(self.checkBox_UsingDriftUnloading_tabHE_FrameStiffness, 0, 0, 1, 1)


        self.gridLayout_37.addWidget(self.groupBox_41, 7, 0, 2, 1)

        self.tableWidget_tabHE_FrameStiffness = QTableWidget(self.tab_14)
        if (self.tableWidget_tabHE_FrameStiffness.columnCount() < 2):
            self.tableWidget_tabHE_FrameStiffness.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabHE_FrameStiffness.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabHE_FrameStiffness.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        if (self.tableWidget_tabHE_FrameStiffness.rowCount() < 1):
            self.tableWidget_tabHE_FrameStiffness.setRowCount(1)
        self.tableWidget_tabHE_FrameStiffness.setObjectName(u"tableWidget_tabHE_FrameStiffness")
        sizePolicy.setHeightForWidth(self.tableWidget_tabHE_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabHE_FrameStiffness.setSizePolicy(sizePolicy)
        self.tableWidget_tabHE_FrameStiffness.setMinimumSize(QSize(200, 0))
        self.tableWidget_tabHE_FrameStiffness.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_tabHE_FrameStiffness.setAutoScroll(True)
        self.tableWidget_tabHE_FrameStiffness.setRowCount(1)
        self.tableWidget_tabHE_FrameStiffness.setColumnCount(2)
        self.tableWidget_tabHE_FrameStiffness.horizontalHeader().setVisible(True)
        self.tableWidget_tabHE_FrameStiffness.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_tabHE_FrameStiffness.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_tabHE_FrameStiffness.horizontalHeader().setHighlightSections(True)
        self.tableWidget_tabHE_FrameStiffness.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_37.addWidget(self.tableWidget_tabHE_FrameStiffness, 0, 2, 8, 1)

        self.tabWidget_5.addTab(self.tab_14, "")
        self.graphicsView_tab_TipAreaFunction_3.raise_()
        self.groupBox_16.raise_()
        self.groupBox_13.raise_()
        self.groupBox_56.raise_()
        self.groupBox_14.raise_()
        self.groupBox_25.raise_()
        self.groupBox_41.raise_()
        self.pushButton_SelectAll_tabHE_FrameStiffness.raise_()
        self.groupBox_26.raise_()
        self.groupBox_51.raise_()
        self.tableWidget_tabHE_FrameStiffness.raise_()
        self.progressBar_tabHE_FrameStiffness.raise_()
        self.pushButton_Calculate_tabHE_FrameStiffness.raise_()
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_48 = QGridLayout(self.tab_15)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.groupBox_19 = QGroupBox(self.tab_15)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy9.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy9)
        self.groupBox_19.setMinimumSize(QSize(230, 0))
        self.groupBox_19.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_39 = QGridLayout(self.groupBox_19)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_47 = QLabel(self.groupBox_19)
        self.label_47.setObjectName(u"label_47")
        sizePolicy9.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy9)
        self.label_47.setMaximumSize(QSize(16777215, 16777215))
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_39.addWidget(self.label_47, 1, 1, 1, 1)

        self.label_46 = QLabel(self.groupBox_19)
        self.label_46.setObjectName(u"label_46")
        sizePolicy1.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy1)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_39.addWidget(self.label_46, 2, 1, 1, 1)

        self.comboBox_method_tabHE = QComboBox(self.groupBox_19)
        self.comboBox_method_tabHE.addItem("")
        self.comboBox_method_tabHE.addItem("")
        self.comboBox_method_tabHE.addItem("")
        self.comboBox_method_tabHE.setObjectName(u"comboBox_method_tabHE")
        self.comboBox_method_tabHE.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabHE.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabHE.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabHE.setMinimumSize(QSize(120, 0))
        self.comboBox_method_tabHE.setEditable(False)

        self.gridLayout_39.addWidget(self.comboBox_method_tabHE, 1, 2, 1, 1)

        self.comboBox_equipment_tabHE = QComboBox(self.groupBox_19)
        self.comboBox_equipment_tabHE.addItem("")
        self.comboBox_equipment_tabHE.addItem("")
        self.comboBox_equipment_tabHE.addItem("")
        self.comboBox_equipment_tabHE.setObjectName(u"comboBox_equipment_tabHE")
        self.comboBox_equipment_tabHE.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabHE.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabHE.setSizePolicy(sizePolicy2)

        self.gridLayout_39.addWidget(self.comboBox_equipment_tabHE, 2, 2, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_19, 3, 0, 1, 1)

        self.groupBox_52 = QGroupBox(self.tab_15)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_102 = QGridLayout(self.groupBox_52)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.label_48 = QLabel(self.groupBox_52)
        self.label_48.setObjectName(u"label_48")
        sizePolicy1.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy1)

        self.gridLayout_102.addWidget(self.label_48, 0, 0, 1, 1)

        self.doubleSpinBox_Start_Pmax_tabHE = QDoubleSpinBox(self.groupBox_52)
        self.doubleSpinBox_Start_Pmax_tabHE.setObjectName(u"doubleSpinBox_Start_Pmax_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabHE.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabHE.setValue(0.980000000000000)

        self.gridLayout_102.addWidget(self.doubleSpinBox_Start_Pmax_tabHE, 0, 1, 1, 1)

        self.label_51 = QLabel(self.groupBox_52)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_102.addWidget(self.label_51, 1, 0, 1, 1)

        self.doubleSpinBox_End_Pmax_tabHE = QDoubleSpinBox(self.groupBox_52)
        self.doubleSpinBox_End_Pmax_tabHE.setObjectName(u"doubleSpinBox_End_Pmax_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabHE.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabHE.setValue(0.500000000000000)

        self.gridLayout_102.addWidget(self.doubleSpinBox_End_Pmax_tabHE, 1, 1, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_52, 6, 0, 2, 1)

        self.groupBox_18 = QGroupBox(self.tab_15)
        self.groupBox_18.setObjectName(u"groupBox_18")
        sizePolicy9.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy9)
        self.groupBox_18.setMinimumSize(QSize(460, 0))
        self.groupBox_18.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_38 = QGridLayout(self.groupBox_18)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_65 = QLabel(self.groupBox_18)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_38.addWidget(self.label_65, 1, 0, 1, 1)

        self.label_66 = QLabel(self.groupBox_18)
        self.label_66.setObjectName(u"label_66")
        sizePolicy8.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy8)

        self.gridLayout_38.addWidget(self.label_66, 0, 0, 1, 1)

        self.lineEdit_path_tabHE = QLineEdit(self.groupBox_18)
        self.lineEdit_path_tabHE.setObjectName(u"lineEdit_path_tabHE")
        sizePolicy2.setHeightForWidth(self.lineEdit_path_tabHE.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabHE.setSizePolicy(sizePolicy2)

        self.gridLayout_38.addWidget(self.lineEdit_path_tabHE, 1, 1, 1, 4)

        self.lineEdit_MaterialName_tabHE = QLineEdit(self.groupBox_18)
        self.lineEdit_MaterialName_tabHE.setObjectName(u"lineEdit_MaterialName_tabHE")
        sizePolicy2.setHeightForWidth(self.lineEdit_MaterialName_tabHE.sizePolicy().hasHeightForWidth())
        self.lineEdit_MaterialName_tabHE.setSizePolicy(sizePolicy2)
        self.lineEdit_MaterialName_tabHE.setMinimumSize(QSize(0, 0))

        self.gridLayout_38.addWidget(self.lineEdit_MaterialName_tabHE, 0, 1, 1, 1)

        self.label_67 = QLabel(self.groupBox_18)
        self.label_67.setObjectName(u"label_67")
        sizePolicy3.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy3)
        self.label_67.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_38.addWidget(self.label_67, 0, 2, 1, 1)

        self.doubleSpinBox_Poisson_tabHE = QDoubleSpinBox(self.groupBox_18)
        self.doubleSpinBox_Poisson_tabHE.setObjectName(u"doubleSpinBox_Poisson_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Poisson_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Poisson_tabHE.setDecimals(3)
        self.doubleSpinBox_Poisson_tabHE.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_tabHE.setValue(0.179000000000000)

        self.gridLayout_38.addWidget(self.doubleSpinBox_Poisson_tabHE, 0, 3, 1, 2)


        self.gridLayout_48.addWidget(self.groupBox_18, 0, 0, 1, 3)

        self.groupBox_42 = QGroupBox(self.tab_15)
        self.groupBox_42.setObjectName(u"groupBox_42")
        sizePolicy3.setHeightForWidth(self.groupBox_42.sizePolicy().hasHeightForWidth())
        self.groupBox_42.setSizePolicy(sizePolicy3)
        self.groupBox_42.setMinimumSize(QSize(224, 0))
        self.groupBox_42.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_92 = QGridLayout(self.groupBox_42)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.checkBox_UsingDriftUnloading_tabHE = QCheckBox(self.groupBox_42)
        self.checkBox_UsingDriftUnloading_tabHE.setObjectName(u"checkBox_UsingDriftUnloading_tabHE")

        self.gridLayout_92.addWidget(self.checkBox_UsingDriftUnloading_tabHE, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_42, 6, 1, 2, 1)

        self.groupBox_23 = QGroupBox(self.tab_15)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy1.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy1)
        self.groupBox_23.setMinimumSize(QSize(460, 0))
        self.groupBox_23.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_43 = QGridLayout(self.groupBox_23)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.lineEdit_TAF6_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF6_tabHE.setObjectName(u"lineEdit_TAF6_tabHE")
        self.lineEdit_TAF6_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF6_tabHE.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_43.addWidget(self.lineEdit_TAF6_tabHE, 5, 3, 1, 2)

        self.Copy_TAF_tabHE = QPushButton(self.groupBox_23)
        self.Copy_TAF_tabHE.setObjectName(u"Copy_TAF_tabHE")
        sizePolicy3.setHeightForWidth(self.Copy_TAF_tabHE.sizePolicy().hasHeightForWidth())
        self.Copy_TAF_tabHE.setSizePolicy(sizePolicy3)
        self.Copy_TAF_tabHE.setMinimumSize(QSize(110, 0))

        self.gridLayout_43.addWidget(self.Copy_TAF_tabHE, 9, 0, 1, 18)

        self.doubleSpinBox_Poisson_Tip_tabHE = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_Poisson_Tip_tabHE.setObjectName(u"doubleSpinBox_Poisson_Tip_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Poisson_Tip_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_Tip_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Poisson_Tip_tabHE.setDecimals(3)
        self.doubleSpinBox_Poisson_Tip_tabHE.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_Tip_tabHE.setValue(0.070000000000000)

        self.gridLayout_43.addWidget(self.doubleSpinBox_Poisson_Tip_tabHE, 1, 14, 1, 3)

        self.lineEdit_TAF4_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF4_tabHE.setObjectName(u"lineEdit_TAF4_tabHE")
        self.lineEdit_TAF4_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF4_tabHE.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_TAF4_tabHE.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_TAF4_tabHE, 3, 11, 1, 1)

        self.label_153 = QLabel(self.groupBox_23)
        self.label_153.setObjectName(u"label_153")

        self.gridLayout_43.addWidget(self.label_153, 5, 13, 1, 2)

        self.label_57 = QLabel(self.groupBox_23)
        self.label_57.setObjectName(u"label_57")
        sizePolicy8.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy8)

        self.gridLayout_43.addWidget(self.label_57, 3, 3, 1, 1)

        self.lineEdit_TAF8_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF8_tabHE.setObjectName(u"lineEdit_TAF8_tabHE")
        self.lineEdit_TAF8_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF8_tabHE.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_43.addWidget(self.lineEdit_TAF8_tabHE, 5, 11, 1, 1)

        self.label_151 = QLabel(self.groupBox_23)
        self.label_151.setObjectName(u"label_151")

        self.gridLayout_43.addWidget(self.label_151, 5, 5, 1, 2)

        self.label_54 = QLabel(self.groupBox_23)
        self.label_54.setObjectName(u"label_54")
        sizePolicy8.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy8)

        self.gridLayout_43.addWidget(self.label_54, 3, 9, 1, 2)

        self.label_152 = QLabel(self.groupBox_23)
        self.label_152.setObjectName(u"label_152")

        self.gridLayout_43.addWidget(self.label_152, 5, 9, 1, 2)

        self.label_55 = QLabel(self.groupBox_23)
        self.label_55.setObjectName(u"label_55")
        sizePolicy8.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy8)
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_55, 3, 6, 1, 1)

        self.lineEdit_TAF3_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF3_tabHE.setObjectName(u"lineEdit_TAF3_tabHE")
        sizePolicy11.setHeightForWidth(self.lineEdit_TAF3_tabHE.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF3_tabHE.setSizePolicy(sizePolicy11)
        self.lineEdit_TAF3_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF3_tabHE.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_TAF3_tabHE.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_TAF3_tabHE, 3, 7, 1, 1)

        self.lineEdit_TAF7_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF7_tabHE.setObjectName(u"lineEdit_TAF7_tabHE")
        self.lineEdit_TAF7_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF7_tabHE.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_43.addWidget(self.lineEdit_TAF7_tabHE, 5, 7, 1, 1)

        self.lineEdit_TAF9_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF9_tabHE.setObjectName(u"lineEdit_TAF9_tabHE")
        self.lineEdit_TAF9_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF9_tabHE.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_43.addWidget(self.lineEdit_TAF9_tabHE, 5, 15, 1, 1)

        self.label_62 = QLabel(self.groupBox_23)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setScaledContents(True)
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_62, 1, 9, 1, 5)

        self.label_154 = QLabel(self.groupBox_23)
        self.label_154.setObjectName(u"label_154")

        self.gridLayout_43.addWidget(self.label_154, 5, 17, 1, 1)

        self.label_56 = QLabel(self.groupBox_23)
        self.label_56.setObjectName(u"label_56")
        sizePolicy8.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy8)
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_56, 3, 0, 1, 1)

        self.lineEdit_TAF5_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF5_tabHE.setObjectName(u"lineEdit_TAF5_tabHE")
        self.lineEdit_TAF5_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF5_tabHE.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF5_tabHE.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_TAF5_tabHE, 3, 15, 1, 1)

        self.lineEdit_TAF1_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF1_tabHE.setObjectName(u"lineEdit_TAF1_tabHE")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF1_tabHE.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF1_tabHE.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF1_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF1_tabHE.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_TAF1_tabHE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_TAF1_tabHE.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_TAF1_tabHE, 3, 1, 1, 2)

        self.label_58 = QLabel(self.groupBox_23)
        self.label_58.setObjectName(u"label_58")
        sizePolicy8.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy8)

        self.gridLayout_43.addWidget(self.label_58, 3, 17, 1, 1)

        self.label_61 = QLabel(self.groupBox_23)
        self.label_61.setObjectName(u"label_61")
        sizePolicy3.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy3)
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_61, 1, 0, 1, 5)

        self.doubleSpinBox_E_Tip_tabHE = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_E_Tip_tabHE.setObjectName(u"doubleSpinBox_E_Tip_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_E_Tip_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_E_Tip_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_E_Tip_tabHE.setMinimumSize(QSize(80, 0))
        self.doubleSpinBox_E_Tip_tabHE.setDecimals(3)
        self.doubleSpinBox_E_Tip_tabHE.setMaximum(99999.990000000005239)
        self.doubleSpinBox_E_Tip_tabHE.setSingleStep(0.001000000000000)
        self.doubleSpinBox_E_Tip_tabHE.setValue(1141.000000000000000)

        self.gridLayout_43.addWidget(self.doubleSpinBox_E_Tip_tabHE, 1, 5, 1, 4)

        self.label_52 = QLabel(self.groupBox_23)
        self.label_52.setObjectName(u"label_52")
        sizePolicy9.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy9)
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_43.addWidget(self.label_52, 0, 0, 1, 3)

        self.label_53 = QLabel(self.groupBox_23)
        self.label_53.setObjectName(u"label_53")
        sizePolicy8.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy8)

        self.gridLayout_43.addWidget(self.label_53, 3, 14, 1, 1)

        self.lineEdit_TAF2_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TAF2_tabHE.setObjectName(u"lineEdit_TAF2_tabHE")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF2_tabHE.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF2_tabHE.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF2_tabHE.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF2_tabHE.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_TAF2_tabHE.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_TAF2_tabHE, 3, 4, 1, 2)

        self.lineEdit_TipName_tabHE = QLineEdit(self.groupBox_23)
        self.lineEdit_TipName_tabHE.setObjectName(u"lineEdit_TipName_tabHE")
        sizePolicy2.setHeightForWidth(self.lineEdit_TipName_tabHE.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabHE.setSizePolicy(sizePolicy2)

        self.gridLayout_43.addWidget(self.lineEdit_TipName_tabHE, 0, 3, 1, 15)


        self.gridLayout_48.addWidget(self.groupBox_23, 1, 0, 1, 3)

        self.groupBox_24 = QGroupBox(self.tab_15)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy1.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy1)
        self.groupBox_24.setMinimumSize(QSize(224, 0))
        self.groupBox_24.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_49 = QGridLayout(self.groupBox_24)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.lineEdit_FrameCompliance_tabHE = QLineEdit(self.groupBox_24)
        self.lineEdit_FrameCompliance_tabHE.setObjectName(u"lineEdit_FrameCompliance_tabHE")
        self.lineEdit_FrameCompliance_tabHE.setReadOnly(True)

        self.gridLayout_49.addWidget(self.lineEdit_FrameCompliance_tabHE, 0, 0, 1, 1)

        self.Copy_FrameCompliance_tabHE = QPushButton(self.groupBox_24)
        self.Copy_FrameCompliance_tabHE.setObjectName(u"Copy_FrameCompliance_tabHE")

        self.gridLayout_49.addWidget(self.Copy_FrameCompliance_tabHE, 1, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_24, 3, 1, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_15)
        self.groupBox_20.setObjectName(u"groupBox_20")
        sizePolicy9.setHeightForWidth(self.groupBox_20.sizePolicy().hasHeightForWidth())
        self.groupBox_20.setSizePolicy(sizePolicy9)
        self.groupBox_20.setMinimumSize(QSize(460, 0))
        self.groupBox_20.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_40 = QGridLayout(self.groupBox_20)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.doubleSpinBox_relForceRateNoise_tabHE = QDoubleSpinBox(self.groupBox_20)
        self.doubleSpinBox_relForceRateNoise_tabHE.setObjectName(u"doubleSpinBox_relForceRateNoise_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabHE.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabHE.setSingleStep(0.000100000000000)
        self.doubleSpinBox_relForceRateNoise_tabHE.setValue(0.010000000000000)

        self.gridLayout_40.addWidget(self.doubleSpinBox_relForceRateNoise_tabHE, 1, 4, 1, 1)

        self.spinBox_max_size_fluctuation_tabHE = QSpinBox(self.groupBox_20)
        self.spinBox_max_size_fluctuation_tabHE.setObjectName(u"spinBox_max_size_fluctuation_tabHE")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabHE.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabHE.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabHE.setValue(1)

        self.gridLayout_40.addWidget(self.spinBox_max_size_fluctuation_tabHE, 1, 6, 1, 1)

        self.label_49 = QLabel(self.groupBox_20)
        self.label_49.setObjectName(u"label_49")
        sizePolicy1.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy1)

        self.gridLayout_40.addWidget(self.label_49, 1, 5, 1, 1)

        self.label_50 = QLabel(self.groupBox_20)
        self.label_50.setObjectName(u"label_50")
        sizePolicy1.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy1)

        self.gridLayout_40.addWidget(self.label_50, 1, 1, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_20, 2, 0, 1, 3)

        self.progressBar_tabHE = QProgressBar(self.tab_15)
        self.progressBar_tabHE.setObjectName(u"progressBar_tabHE")
        sizePolicy3.setHeightForWidth(self.progressBar_tabHE.sizePolicy().hasHeightForWidth())
        self.progressBar_tabHE.setSizePolicy(sizePolicy3)
        self.progressBar_tabHE.setMinimumSize(QSize(200, 0))
        self.progressBar_tabHE.setMaximumSize(QSize(200, 16777215))
        self.progressBar_tabHE.setValue(0)

        self.gridLayout_48.addWidget(self.progressBar_tabHE, 6, 3, 1, 1)

        self.graphicsView_tab_TipAreaFunction_4 = QTabWidget(self.tab_15)
        self.graphicsView_tab_TipAreaFunction_4.setObjectName(u"graphicsView_tab_TipAreaFunction_4")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction_4.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction_4.setUsesScrollButtons(True)
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.gridLayout_44 = QGridLayout(self.tab_20)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE = QTabWidget(self.tab_20)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.gridLayout_45 = QGridLayout(self.tab_21)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE = QCheckBox(self.tab_21)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE")
        sizePolicy7.setHeightForWidth(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE.sizePolicy().hasHeightForWidth())
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE.setSizePolicy(sizePolicy7)

        self.gridLayout_45.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE, 2, 0, 1, 1)

        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE = QGraphicsView(self.tab_21)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE.setSizePolicy(sizePolicy)

        self.gridLayout_45.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabHE, 1, 0, 1, 7)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE = QCheckBox(self.tab_21)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabHE")
        sizePolicy7.setHeightForWidth(self.checkBox_iLHU_inclusive_frame_stiffness_tabHE.sizePolicy().hasHeightForWidth())
        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE.setSizePolicy(sizePolicy7)

        self.gridLayout_45.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabHE, 2, 1, 1, 1)

        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE = QPushButton(self.tab_21)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.setSizePolicy(sizePolicy1)

        self.gridLayout_45.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE, 3, 0, 1, 2)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE = QCheckBox(self.tab_21)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE")

        self.gridLayout_45.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE, 2, 2, 1, 1)

        self.pushButton_Publication_LoadDepthCurve_tabHE = QPushButton(self.tab_21)
        self.pushButton_Publication_LoadDepthCurve_tabHE.setObjectName(u"pushButton_Publication_LoadDepthCurve_tabHE")
        self.pushButton_Publication_LoadDepthCurve_tabHE.setEnabled(False)

        self.gridLayout_45.addWidget(self.pushButton_Publication_LoadDepthCurve_tabHE, 3, 2, 1, 1)

        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.addTab(self.tab_21, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_46 = QGridLayout(self.tab_22)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_4 = QGraphicsView(self.tab_22)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_4.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_4")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_4.setSizePolicy(sizePolicy)

        self.gridLayout_46.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_4, 0, 0, 1, 1)

        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.addTab(self.tab_22, "")

        self.gridLayout_44.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_4.addTab(self.tab_20, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.gridLayout_11 = QGridLayout(self.tab_23)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabWidget_7 = QTabWidget(self.tab_23)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.gridLayout_50 = QGridLayout(self.tab_25)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.graphicsView_H_hc_tabHE = QGraphicsView(self.tab_25)
        self.graphicsView_H_hc_tabHE.setObjectName(u"graphicsView_H_hc_tabHE")
        self.graphicsView_H_hc_tabHE.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_50.addWidget(self.graphicsView_H_hc_tabHE, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.tab_25, "")
        self.tab_26 = QWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.gridLayout_51 = QGridLayout(self.tab_26)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.graphicsView_H_Index_tabHE = QGraphicsView(self.tab_26)
        self.graphicsView_H_Index_tabHE.setObjectName(u"graphicsView_H_Index_tabHE")
        self.graphicsView_H_Index_tabHE.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_51.addWidget(self.graphicsView_H_Index_tabHE, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.tab_26, "")

        self.gridLayout_11.addWidget(self.tabWidget_7, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_4.addTab(self.tab_23, "")
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.gridLayout_47 = QGridLayout(self.tab_24)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.tabWidget_8 = QTabWidget(self.tab_24)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_27 = QWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.gridLayout_53 = QGridLayout(self.tab_27)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.graphicsView_E_hc_tabHE = QGraphicsView(self.tab_27)
        self.graphicsView_E_hc_tabHE.setObjectName(u"graphicsView_E_hc_tabHE")
        self.graphicsView_E_hc_tabHE.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_53.addWidget(self.graphicsView_E_hc_tabHE, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_27, "")
        self.tab_28 = QWidget()
        self.tab_28.setObjectName(u"tab_28")
        self.gridLayout_54 = QGridLayout(self.tab_28)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.graphicsView_E_Index_tabHE = QGraphicsView(self.tab_28)
        self.graphicsView_E_Index_tabHE.setObjectName(u"graphicsView_E_Index_tabHE")
        self.graphicsView_E_Index_tabHE.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_54.addWidget(self.graphicsView_E_Index_tabHE, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_28, "")

        self.gridLayout_47.addWidget(self.tabWidget_8, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_4.addTab(self.tab_24, "")
        self.tab_46 = QWidget()
        self.tab_46.setObjectName(u"tab_46")
        self.gridLayout_115 = QGridLayout(self.tab_46)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.graphicsView_HE_tabHE = QGraphicsView(self.tab_46)
        self.graphicsView_HE_tabHE.setObjectName(u"graphicsView_HE_tabHE")

        self.gridLayout_115.addWidget(self.graphicsView_HE_tabHE, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_4.addTab(self.tab_46, "")

        self.gridLayout_48.addWidget(self.graphicsView_tab_TipAreaFunction_4, 0, 4, 19, 1)

        self.Calculate_tabHE = QPushButton(self.tab_15)
        self.Calculate_tabHE.setObjectName(u"Calculate_tabHE")
        sizePolicy3.setHeightForWidth(self.Calculate_tabHE.sizePolicy().hasHeightForWidth())
        self.Calculate_tabHE.setSizePolicy(sizePolicy3)
        self.Calculate_tabHE.setMinimumSize(QSize(200, 0))
        self.Calculate_tabHE.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_48.addWidget(self.Calculate_tabHE, 7, 3, 1, 1)

        self.pushButton_SelectAll_tabHE = QPushButton(self.tab_15)
        self.pushButton_SelectAll_tabHE.setObjectName(u"pushButton_SelectAll_tabHE")
        self.pushButton_SelectAll_tabHE.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_48.addWidget(self.pushButton_SelectAll_tabHE, 5, 3, 1, 1)

        self.tableWidget_tabHE = QTableWidget(self.tab_15)
        if (self.tableWidget_tabHE.columnCount() < 2):
            self.tableWidget_tabHE.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabHE.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabHE.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        if (self.tableWidget_tabHE.rowCount() < 1):
            self.tableWidget_tabHE.setRowCount(1)
        self.tableWidget_tabHE.setObjectName(u"tableWidget_tabHE")
        sizePolicy12.setHeightForWidth(self.tableWidget_tabHE.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabHE.setSizePolicy(sizePolicy12)
        self.tableWidget_tabHE.setMinimumSize(QSize(200, 0))
        self.tableWidget_tabHE.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_tabHE.setAutoScroll(True)
        self.tableWidget_tabHE.setRowCount(1)
        self.tableWidget_tabHE.horizontalHeader().setVisible(True)
        self.tableWidget_tabHE.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_tabHE.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_tabHE.horizontalHeader().setHighlightSections(True)
        self.tableWidget_tabHE.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_48.addWidget(self.tableWidget_tabHE, 0, 3, 5, 1)

        self.groupBox_47 = QGroupBox(self.tab_15)
        self.groupBox_47.setObjectName(u"groupBox_47")
        sizePolicy9.setHeightForWidth(self.groupBox_47.sizePolicy().hasHeightForWidth())
        self.groupBox_47.setSizePolicy(sizePolicy9)
        self.groupBox_47.setMinimumSize(QSize(224, 0))
        self.groupBox_47.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_97 = QGridLayout(self.groupBox_47)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.label_108 = QLabel(self.groupBox_47)
        self.label_108.setObjectName(u"label_108")
        sizePolicy8.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy8)

        self.gridLayout_97.addWidget(self.label_108, 1, 0, 1, 1)

        self.label_120 = QLabel(self.groupBox_47)
        self.label_120.setObjectName(u"label_120")
        sizePolicy8.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy8)

        self.gridLayout_97.addWidget(self.label_120, 2, 0, 1, 1)

        self.doubleSpinBox_minhc4mean_tabHE = QDoubleSpinBox(self.groupBox_47)
        self.doubleSpinBox_minhc4mean_tabHE.setObjectName(u"doubleSpinBox_minhc4mean_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_minhc4mean_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_minhc4mean_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_minhc4mean_tabHE.setDecimals(3)
        self.doubleSpinBox_minhc4mean_tabHE.setSingleStep(0.001000000000000)
        self.doubleSpinBox_minhc4mean_tabHE.setValue(0.100000000000000)

        self.gridLayout_97.addWidget(self.doubleSpinBox_minhc4mean_tabHE, 1, 1, 1, 1)

        self.doubleSpinBox_maxhc4mean_tabHE = QDoubleSpinBox(self.groupBox_47)
        self.doubleSpinBox_maxhc4mean_tabHE.setObjectName(u"doubleSpinBox_maxhc4mean_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_maxhc4mean_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_maxhc4mean_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_maxhc4mean_tabHE.setDecimals(3)
        self.doubleSpinBox_maxhc4mean_tabHE.setSingleStep(0.001000000000000)
        self.doubleSpinBox_maxhc4mean_tabHE.setValue(2.000000000000000)

        self.gridLayout_97.addWidget(self.doubleSpinBox_maxhc4mean_tabHE, 2, 1, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_47, 4, 1, 2, 1)

        self.groupBox_21 = QGroupBox(self.tab_15)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy8.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy8)
        self.groupBox_21.setMinimumSize(QSize(230, 0))
        self.groupBox_21.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_41 = QGridLayout(self.groupBox_21)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.doubleSpinBox_Rate2findSurface_tabHE = QDoubleSpinBox(self.groupBox_21)
        self.doubleSpinBox_Rate2findSurface_tabHE.setObjectName(u"doubleSpinBox_Rate2findSurface_tabHE")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabHE.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabHE.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabHE.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabHE.setValue(1.000000000000000)

        self.gridLayout_41.addWidget(self.doubleSpinBox_Rate2findSurface_tabHE, 0, 1, 1, 1)

        self.checkBox_UsingRate2findSurface_tabHE = QCheckBox(self.groupBox_21)
        self.checkBox_UsingRate2findSurface_tabHE.setObjectName(u"checkBox_UsingRate2findSurface_tabHE")
        sizePolicy7.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabHE.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabHE.setSizePolicy(sizePolicy7)
        self.checkBox_UsingRate2findSurface_tabHE.setChecked(True)

        self.gridLayout_41.addWidget(self.checkBox_UsingRate2findSurface_tabHE, 0, 0, 1, 1)

        self.spinBox_DataFilterSize_tabHE = QSpinBox(self.groupBox_21)
        self.spinBox_DataFilterSize_tabHE.setObjectName(u"spinBox_DataFilterSize_tabHE")
        sizePolicy2.setHeightForWidth(self.spinBox_DataFilterSize_tabHE.sizePolicy().hasHeightForWidth())
        self.spinBox_DataFilterSize_tabHE.setSizePolicy(sizePolicy2)
        self.spinBox_DataFilterSize_tabHE.setValue(5)

        self.gridLayout_41.addWidget(self.spinBox_DataFilterSize_tabHE, 1, 1, 1, 1)

        self.label_88 = QLabel(self.groupBox_21)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.label_88, 1, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_21, 4, 0, 2, 1)

        self.groupBox_65 = QGroupBox(self.tab_15)
        self.groupBox_65.setObjectName(u"groupBox_65")
        self.groupBox_65.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_117 = QGridLayout(self.groupBox_65)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.spinBox_DecreaseDataDensity_tabHE = QSpinBox(self.groupBox_65)
        self.spinBox_DecreaseDataDensity_tabHE.setObjectName(u"spinBox_DecreaseDataDensity_tabHE")
        self.spinBox_DecreaseDataDensity_tabHE.setMinimum(1)

        self.gridLayout_117.addWidget(self.spinBox_DecreaseDataDensity_tabHE, 0, 1, 1, 1)

        self.label_161 = QLabel(self.groupBox_65)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font)

        self.gridLayout_117.addWidget(self.label_161, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_65, 8, 0, 2, 1)

        self.tabWidget_5.addTab(self.tab_15, "")

        self.gridLayout_27.addWidget(self.tabWidget_5, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_13, "")
        self.tab_analysePopIn = QWidget()
        self.tab_analysePopIn.setObjectName(u"tab_analysePopIn")
        self.gridLayout_89 = QGridLayout(self.tab_analysePopIn)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.tabWidget_10 = QTabWidget(self.tab_analysePopIn)
        self.tabWidget_10.setObjectName(u"tabWidget_10")
        sizePolicy.setHeightForWidth(self.tabWidget_10.sizePolicy().hasHeightForWidth())
        self.tabWidget_10.setSizePolicy(sizePolicy)
        self.tab_35 = QWidget()
        self.tab_35.setObjectName(u"tab_35")
        self.gridLayout_67 = QGridLayout(self.tab_35)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.pushButton_SelectAll_tabPopIn_FrameStiffness = QPushButton(self.tab_35)
        self.pushButton_SelectAll_tabPopIn_FrameStiffness.setObjectName(u"pushButton_SelectAll_tabPopIn_FrameStiffness")
        self.pushButton_SelectAll_tabPopIn_FrameStiffness.setMinimumSize(QSize(200, 0))
        self.pushButton_SelectAll_tabPopIn_FrameStiffness.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_67.addWidget(self.pushButton_SelectAll_tabPopIn_FrameStiffness, 8, 2, 1, 1)

        self.groupBox_33 = QGroupBox(self.tab_35)
        self.groupBox_33.setObjectName(u"groupBox_33")
        sizePolicy1.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy1)
        self.groupBox_33.setMinimumSize(QSize(224, 0))
        self.groupBox_33.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_75 = QGridLayout(self.groupBox_33)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness = QCheckBox(self.groupBox_33)
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.setObjectName(u"checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.setMinimumSize(QSize(0, 0))
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.setChecked(True)

        self.gridLayout_75.addWidget(self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness, 0, 0, 1, 1)

        self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness = QDoubleSpinBox(self.groupBox_33)
        self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness.setObjectName(u"doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness.setValue(1.000000000000000)

        self.gridLayout_75.addWidget(self.doubleSpinBox_Rate2findSurface_tabPopIn_FrameStiffness, 0, 1, 1, 1)

        self.label_101 = QLabel(self.groupBox_33)
        self.label_101.setObjectName(u"label_101")
        sizePolicy9.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy9)
        self.label_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_75.addWidget(self.label_101, 1, 0, 1, 1)

        self.spinBox_DataFilterSize_tabPopIn_FrameStiffness = QSpinBox(self.groupBox_33)
        self.spinBox_DataFilterSize_tabPopIn_FrameStiffness.setObjectName(u"spinBox_DataFilterSize_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.spinBox_DataFilterSize_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.spinBox_DataFilterSize_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.spinBox_DataFilterSize_tabPopIn_FrameStiffness.setValue(5)

        self.gridLayout_75.addWidget(self.spinBox_DataFilterSize_tabPopIn_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_33, 5, 1, 1, 1)

        self.groupBox_31 = QGroupBox(self.tab_35)
        self.groupBox_31.setObjectName(u"groupBox_31")
        sizePolicy1.setHeightForWidth(self.groupBox_31.sizePolicy().hasHeightForWidth())
        self.groupBox_31.setSizePolicy(sizePolicy1)
        self.groupBox_31.setMinimumSize(QSize(230, 0))
        self.groupBox_31.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_73 = QGridLayout(self.groupBox_31)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.label_96 = QLabel(self.groupBox_31)
        self.label_96.setObjectName(u"label_96")
        sizePolicy2.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy2)
        self.label_96.setMaximumSize(QSize(16777215, 16777215))
        self.label_96.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_73.addWidget(self.label_96, 1, 1, 1, 1)

        self.label_97 = QLabel(self.groupBox_31)
        self.label_97.setObjectName(u"label_97")
        sizePolicy1.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy1)

        self.gridLayout_73.addWidget(self.label_97, 2, 1, 1, 1)

        self.comboBox_equipment_tabPopIn_FrameStiffness = QComboBox(self.groupBox_31)
        self.comboBox_equipment_tabPopIn_FrameStiffness.addItem("")
        self.comboBox_equipment_tabPopIn_FrameStiffness.setObjectName(u"comboBox_equipment_tabPopIn_FrameStiffness")
        self.comboBox_equipment_tabPopIn_FrameStiffness.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_73.addWidget(self.comboBox_equipment_tabPopIn_FrameStiffness, 2, 2, 1, 1)

        self.comboBox_method_tabPopIn_FrameStiffness = QComboBox(self.groupBox_31)
        self.comboBox_method_tabPopIn_FrameStiffness.addItem("")
        self.comboBox_method_tabPopIn_FrameStiffness.addItem("")
        self.comboBox_method_tabPopIn_FrameStiffness.addItem("")
        self.comboBox_method_tabPopIn_FrameStiffness.setObjectName(u"comboBox_method_tabPopIn_FrameStiffness")
        self.comboBox_method_tabPopIn_FrameStiffness.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabPopIn_FrameStiffness.setMinimumSize(QSize(120, 0))
        self.comboBox_method_tabPopIn_FrameStiffness.setEditable(False)

        self.gridLayout_73.addWidget(self.comboBox_method_tabPopIn_FrameStiffness, 1, 2, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_31, 5, 0, 1, 1)

        self.tableWidget_tabPopIn_FrameStiffness = QTableWidget(self.tab_35)
        if (self.tableWidget_tabPopIn_FrameStiffness.columnCount() < 2):
            self.tableWidget_tabPopIn_FrameStiffness.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabPopIn_FrameStiffness.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabPopIn_FrameStiffness.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.tableWidget_tabPopIn_FrameStiffness.rowCount() < 1):
            self.tableWidget_tabPopIn_FrameStiffness.setRowCount(1)
        self.tableWidget_tabPopIn_FrameStiffness.setObjectName(u"tableWidget_tabPopIn_FrameStiffness")
        sizePolicy12.setHeightForWidth(self.tableWidget_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy12)
        self.tableWidget_tabPopIn_FrameStiffness.setMinimumSize(QSize(200, 0))
        self.tableWidget_tabPopIn_FrameStiffness.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_tabPopIn_FrameStiffness.setAutoScroll(True)
        self.tableWidget_tabPopIn_FrameStiffness.setRowCount(1)
        self.tableWidget_tabPopIn_FrameStiffness.horizontalHeader().setVisible(True)
        self.tableWidget_tabPopIn_FrameStiffness.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_tabPopIn_FrameStiffness.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_tabPopIn_FrameStiffness.horizontalHeader().setHighlightSections(True)
        self.tableWidget_tabPopIn_FrameStiffness.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_67.addWidget(self.tableWidget_tabPopIn_FrameStiffness, 2, 2, 6, 1)

        self.graphicsView_tab_TipAreaFunction_6 = QTabWidget(self.tab_35)
        self.graphicsView_tab_TipAreaFunction_6.setObjectName(u"graphicsView_tab_TipAreaFunction_6")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction_6.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction_6.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction_6.setUsesScrollButtons(True)
        self.tab_36 = QWidget()
        self.tab_36.setObjectName(u"tab_36")
        self.gridLayout_68 = QGridLayout(self.tab_36)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.tabWidget_11 = QTabWidget(self.tab_36)
        self.tabWidget_11.setObjectName(u"tabWidget_11")
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.gridLayout_69 = QGridLayout(self.tab_37)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness = QCheckBox(self.tab_37)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)

        self.gridLayout_69.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness, 2, 0, 1, 1)

        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness = QGraphicsView(self.tab_37)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness")
        sizePolicy6.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy6)

        self.gridLayout_69.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness, 1, 0, 1, 5)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness = QCheckBox(self.tab_37)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)

        self.gridLayout_69.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness, 2, 1, 1, 1)

        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness = QPushButton(self.tab_37)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy1)

        self.gridLayout_69.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness, 3, 0, 1, 2)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness = QCheckBox(self.tab_37)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness")

        self.gridLayout_69.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness, 2, 2, 1, 1)

        self.tabWidget_11.addTab(self.tab_37, "")
        self.tab_38 = QWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.gridLayout_70 = QGridLayout(self.tab_38)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness = QGraphicsView(self.tab_38)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy)

        self.gridLayout_70.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_38, "")

        self.gridLayout_68.addWidget(self.tabWidget_11, 1, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_6.addTab(self.tab_36, "")
        self.tab_39 = QWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.gridLayout_71 = QGridLayout(self.tab_39)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.label_90 = QLabel(self.tab_39)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_71.addWidget(self.label_90, 1, 2, 1, 1)

        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness = QLineEdit(self.tab_39)
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_FrameStiffness_tabPopIn_FrameStiffness")
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setFrame(True)
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setDragEnabled(False)
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setReadOnly(True)
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setClearButtonEnabled(False)

        self.gridLayout_71.addWidget(self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness, 1, 1, 1, 1)

        self.label_91 = QLabel(self.tab_39)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_71.addWidget(self.label_91, 1, 0, 1, 1)

        self.lineEdit_FrameCompliance_tabPopIn_FrameStiffness = QLineEdit(self.tab_39)
        self.lineEdit_FrameCompliance_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_FrameCompliance_tabPopIn_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_FrameCompliance_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_FrameCompliance_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_FrameCompliance_tabPopIn_FrameStiffness.setReadOnly(True)

        self.gridLayout_71.addWidget(self.lineEdit_FrameCompliance_tabPopIn_FrameStiffness, 1, 3, 1, 1)

        self.graphicsView_tabPopIn_FrameStiffness = QGraphicsView(self.tab_39)
        self.graphicsView_tabPopIn_FrameStiffness.setObjectName(u"graphicsView_tabPopIn_FrameStiffness")
        self.graphicsView_tabPopIn_FrameStiffness.setCacheMode(QGraphicsView.CacheNone)

        self.gridLayout_71.addWidget(self.graphicsView_tabPopIn_FrameStiffness, 3, 0, 1, 6)

        self.graphicsView_tab_TipAreaFunction_6.addTab(self.tab_39, "")

        self.gridLayout_67.addWidget(self.graphicsView_tab_TipAreaFunction_6, 2, 3, 15, 1)

        self.groupBox_58 = QGroupBox(self.tab_35)
        self.groupBox_58.setObjectName(u"groupBox_58")
        sizePolicy1.setHeightForWidth(self.groupBox_58.sizePolicy().hasHeightForWidth())
        self.groupBox_58.setSizePolicy(sizePolicy1)
        self.groupBox_58.setMinimumSize(QSize(460, 0))
        self.groupBox_58.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_107 = QGridLayout(self.groupBox_58)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.groupBox_62 = QGroupBox(self.groupBox_58)
        self.groupBox_62.setObjectName(u"groupBox_62")
        sizePolicy4.setHeightForWidth(self.groupBox_62.sizePolicy().hasHeightForWidth())
        self.groupBox_62.setSizePolicy(sizePolicy4)
        self.groupBox_62.setMinimumSize(QSize(0, 0))
        self.groupBox_62.setMaximumSize(QSize(44000, 16777215))
        self.gridLayout_110 = QGridLayout(self.groupBox_62)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.label_130 = QLabel(self.groupBox_62)
        self.label_130.setObjectName(u"label_130")
        sizePolicy8.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy8)
        self.label_130.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_110.addWidget(self.label_130, 2, 0, 1, 2)

        self.lineEdit_TAF1_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF1_tabPopIn_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF1_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setReadOnly(True)

        self.gridLayout_110.addWidget(self.lineEdit_TAF1_tabPopIn_FrameStiffness, 2, 2, 1, 1)

        self.label_135 = QLabel(self.groupBox_62)
        self.label_135.setObjectName(u"label_135")
        sizePolicy8.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy8)

        self.gridLayout_110.addWidget(self.label_135, 2, 3, 1, 1)

        self.lineEdit_TAF2_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF2_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF2_tabPopIn_FrameStiffness")
        sizePolicy7.setHeightForWidth(self.lineEdit_TAF2_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF2_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy7)
        self.lineEdit_TAF2_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF2_tabPopIn_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF2_tabPopIn_FrameStiffness.setReadOnly(True)

        self.gridLayout_110.addWidget(self.lineEdit_TAF2_tabPopIn_FrameStiffness, 2, 4, 1, 1)

        self.lineEdit_TAF6_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF6_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF6_tabPopIn_FrameStiffness")
        self.lineEdit_TAF6_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_110.addWidget(self.lineEdit_TAF6_tabPopIn_FrameStiffness, 3, 4, 1, 1)

        self.label_136 = QLabel(self.groupBox_62)
        self.label_136.setObjectName(u"label_136")
        sizePolicy9.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy9)
        self.label_136.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_110.addWidget(self.label_136, 0, 0, 1, 3)

        self.label_134 = QLabel(self.groupBox_62)
        self.label_134.setObjectName(u"label_134")
        sizePolicy8.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy8)
        self.label_134.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_110.addWidget(self.label_134, 2, 5, 1, 1)

        self.lineEdit_TAF3_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF3_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF3_tabPopIn_FrameStiffness")
        sizePolicy11.setHeightForWidth(self.lineEdit_TAF3_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TAF3_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy11)
        self.lineEdit_TAF3_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF3_tabPopIn_FrameStiffness.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF3_tabPopIn_FrameStiffness.setReadOnly(True)

        self.gridLayout_110.addWidget(self.lineEdit_TAF3_tabPopIn_FrameStiffness, 2, 6, 1, 1)

        self.label_133 = QLabel(self.groupBox_62)
        self.label_133.setObjectName(u"label_133")
        sizePolicy8.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy8)

        self.gridLayout_110.addWidget(self.label_133, 2, 7, 1, 1)

        self.lineEdit_TAF4_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF4_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF4_tabPopIn_FrameStiffness")
        self.lineEdit_TAF4_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF4_tabPopIn_FrameStiffness.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_TAF4_tabPopIn_FrameStiffness.setReadOnly(True)

        self.gridLayout_110.addWidget(self.lineEdit_TAF4_tabPopIn_FrameStiffness, 2, 8, 1, 1)

        self.label_131 = QLabel(self.groupBox_62)
        self.label_131.setObjectName(u"label_131")
        sizePolicy8.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy8)

        self.gridLayout_110.addWidget(self.label_131, 2, 9, 1, 1)

        self.lineEdit_TAF5_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF5_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF5_tabPopIn_FrameStiffness")
        self.lineEdit_TAF5_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))
        self.lineEdit_TAF5_tabPopIn_FrameStiffness.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_TAF5_tabPopIn_FrameStiffness.setReadOnly(True)

        self.gridLayout_110.addWidget(self.lineEdit_TAF5_tabPopIn_FrameStiffness, 2, 10, 1, 1)

        self.label_132 = QLabel(self.groupBox_62)
        self.label_132.setObjectName(u"label_132")
        sizePolicy8.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy8)

        self.gridLayout_110.addWidget(self.label_132, 2, 11, 1, 1)

        self.label_155 = QLabel(self.groupBox_62)
        self.label_155.setObjectName(u"label_155")

        self.gridLayout_110.addWidget(self.label_155, 3, 5, 1, 1)

        self.lineEdit_TAF7_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF7_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF7_tabPopIn_FrameStiffness")
        self.lineEdit_TAF7_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_110.addWidget(self.lineEdit_TAF7_tabPopIn_FrameStiffness, 3, 6, 1, 1)

        self.label_156 = QLabel(self.groupBox_62)
        self.label_156.setObjectName(u"label_156")

        self.gridLayout_110.addWidget(self.label_156, 3, 7, 1, 1)

        self.lineEdit_TAF8_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF8_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF8_tabPopIn_FrameStiffness")
        self.lineEdit_TAF8_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_110.addWidget(self.lineEdit_TAF8_tabPopIn_FrameStiffness, 3, 8, 1, 1)

        self.label_157 = QLabel(self.groupBox_62)
        self.label_157.setObjectName(u"label_157")

        self.gridLayout_110.addWidget(self.label_157, 3, 9, 1, 1)

        self.lineEdit_TAF9_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TAF9_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TAF9_tabPopIn_FrameStiffness")
        self.lineEdit_TAF9_tabPopIn_FrameStiffness.setMinimumSize(QSize(40, 0))

        self.gridLayout_110.addWidget(self.lineEdit_TAF9_tabPopIn_FrameStiffness, 3, 10, 1, 1)

        self.label_158 = QLabel(self.groupBox_62)
        self.label_158.setObjectName(u"label_158")

        self.gridLayout_110.addWidget(self.label_158, 3, 11, 1, 1)

        self.lineEdit_TipName_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_62)
        self.lineEdit_TipName_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_TipName_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.lineEdit_TipName_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_110.addWidget(self.lineEdit_TipName_tabPopIn_FrameStiffness, 0, 3, 1, 9)

        self.Copy_TAF_tabPopIn_FrameStiffness = QPushButton(self.groupBox_62)
        self.Copy_TAF_tabPopIn_FrameStiffness.setObjectName(u"Copy_TAF_tabPopIn_FrameStiffness")
        sizePolicy3.setHeightForWidth(self.Copy_TAF_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.Copy_TAF_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy3)
        self.Copy_TAF_tabPopIn_FrameStiffness.setMinimumSize(QSize(110, 0))

        self.gridLayout_110.addWidget(self.Copy_TAF_tabPopIn_FrameStiffness, 6, 0, 1, 12)


        self.gridLayout_107.addWidget(self.groupBox_62, 1, 0, 1, 1)

        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness = QComboBox(self.groupBox_58)
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.addItem("")
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.addItem("")
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.setObjectName(u"comboBox_CalculationMethod_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.setEditable(False)

        self.gridLayout_107.addWidget(self.comboBox_CalculationMethod_tabPopIn_FrameStiffness, 0, 0, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_58, 3, 0, 1, 2)

        self.groupBox_34 = QGroupBox(self.tab_35)
        self.groupBox_34.setObjectName(u"groupBox_34")
        sizePolicy9.setHeightForWidth(self.groupBox_34.sizePolicy().hasHeightForWidth())
        self.groupBox_34.setSizePolicy(sizePolicy9)
        self.groupBox_34.setMinimumSize(QSize(460, 0))
        self.groupBox_34.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_76 = QGridLayout(self.groupBox_34)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.lineEdit_path_tabPopIn_FrameStiffness = QLineEdit(self.groupBox_34)
        self.lineEdit_path_tabPopIn_FrameStiffness.setObjectName(u"lineEdit_path_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.lineEdit_path_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)

        self.gridLayout_76.addWidget(self.lineEdit_path_tabPopIn_FrameStiffness, 0, 1, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_34, 2, 0, 1, 2)

        self.groupBox_30 = QGroupBox(self.tab_35)
        self.groupBox_30.setObjectName(u"groupBox_30")
        sizePolicy1.setHeightForWidth(self.groupBox_30.sizePolicy().hasHeightForWidth())
        self.groupBox_30.setSizePolicy(sizePolicy1)
        self.groupBox_30.setMinimumSize(QSize(460, 0))
        self.groupBox_30.setMaximumSize(QSize(440, 16777215))
        self.gridLayout_72 = QGridLayout(self.groupBox_30)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.label_93 = QLabel(self.groupBox_30)
        self.label_93.setObjectName(u"label_93")
        sizePolicy1.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy1)
        self.label_93.setMinimumSize(QSize(0, 0))

        self.gridLayout_72.addWidget(self.label_93, 1, 5, 1, 1)

        self.spinBox_max_size_fluctuation_tabPopIn_FrameStiffness = QSpinBox(self.groupBox_30)
        self.spinBox_max_size_fluctuation_tabPopIn_FrameStiffness.setObjectName(u"spinBox_max_size_fluctuation_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabPopIn_FrameStiffness.setValue(1)

        self.gridLayout_72.addWidget(self.spinBox_max_size_fluctuation_tabPopIn_FrameStiffness, 1, 6, 1, 1)

        self.label_94 = QLabel(self.groupBox_30)
        self.label_94.setObjectName(u"label_94")
        sizePolicy1.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy1)

        self.gridLayout_72.addWidget(self.label_94, 1, 0, 1, 1)

        self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness = QDoubleSpinBox(self.groupBox_30)
        self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness.setObjectName(u"doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness.setSingleStep(0.000100000000000)
        self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness.setValue(0.010000000000000)

        self.gridLayout_72.addWidget(self.doubleSpinBox_relForceRateNoise_tabPopIn_FrameStiffness, 1, 4, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_30, 4, 0, 1, 2)

        self.groupBox_53 = QGroupBox(self.tab_35)
        self.groupBox_53.setObjectName(u"groupBox_53")
        sizePolicy1.setHeightForWidth(self.groupBox_53.sizePolicy().hasHeightForWidth())
        self.groupBox_53.setSizePolicy(sizePolicy1)
        self.groupBox_53.setMinimumSize(QSize(230, 0))
        self.groupBox_53.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_103 = QGridLayout(self.groupBox_53)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness = QDoubleSpinBox(self.groupBox_53)
        self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness.setObjectName(u"doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness.setValue(0.980000000000000)

        self.gridLayout_103.addWidget(self.doubleSpinBox_Start_Pmax_tabPopIn_FrameStiffness, 0, 1, 1, 1)

        self.label_95 = QLabel(self.groupBox_53)
        self.label_95.setObjectName(u"label_95")
        sizePolicy1.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy1)
        self.label_95.setMinimumSize(QSize(110, 0))

        self.gridLayout_103.addWidget(self.label_95, 0, 0, 1, 1)

        self.label_92 = QLabel(self.groupBox_53)
        self.label_92.setObjectName(u"label_92")
        sizePolicy9.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy9)
        self.label_92.setMinimumSize(QSize(0, 0))
        self.label_92.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_103.addWidget(self.label_92, 1, 0, 1, 1)

        self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness = QDoubleSpinBox(self.groupBox_53)
        self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness.setObjectName(u"doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness.setValue(0.500000000000000)

        self.gridLayout_103.addWidget(self.doubleSpinBox_End_Pmax_tabPopIn_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_53, 6, 0, 1, 1)

        self.groupBox_32 = QGroupBox(self.tab_35)
        self.groupBox_32.setObjectName(u"groupBox_32")
        sizePolicy1.setHeightForWidth(self.groupBox_32.sizePolicy().hasHeightForWidth())
        self.groupBox_32.setSizePolicy(sizePolicy1)
        self.groupBox_32.setMinimumSize(QSize(224, 0))
        self.groupBox_32.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_74 = QGridLayout(self.groupBox_32)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness = QDoubleSpinBox(self.groupBox_32)
        self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness.setObjectName(u"doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness.setSingleStep(0.010000000000000)
        self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness.setValue(0.100000000000000)

        self.gridLayout_74.addWidget(self.doubleSpinBox_critDepthStiffness_tabPopIn_FrameStiffness, 0, 1, 1, 1)

        self.label_99 = QLabel(self.groupBox_32)
        self.label_99.setObjectName(u"label_99")
        sizePolicy8.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy8)

        self.gridLayout_74.addWidget(self.label_99, 0, 0, 1, 1)

        self.label_100 = QLabel(self.groupBox_32)
        self.label_100.setObjectName(u"label_100")
        sizePolicy9.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy9)
        self.label_100.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_74.addWidget(self.label_100, 1, 0, 1, 1)

        self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness = QDoubleSpinBox(self.groupBox_32)
        self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness.setObjectName(u"doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness.setMaximum(999.000000000000000)
        self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness.setValue(15.000000000000000)

        self.gridLayout_74.addWidget(self.doubleSpinBox_critForceStiffness_tabPopIn_FrameStiffness, 1, 1, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_32, 6, 1, 1, 1)

        self.progressBar_tabPopIn_FrameStiffness = QProgressBar(self.tab_35)
        self.progressBar_tabPopIn_FrameStiffness.setObjectName(u"progressBar_tabPopIn_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.progressBar_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.progressBar_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy1)
        self.progressBar_tabPopIn_FrameStiffness.setMinimumSize(QSize(224, 0))
        self.progressBar_tabPopIn_FrameStiffness.setMaximumSize(QSize(224, 16777215))
        self.progressBar_tabPopIn_FrameStiffness.setValue(0)

        self.gridLayout_67.addWidget(self.progressBar_tabPopIn_FrameStiffness, 7, 1, 1, 1)

        self.pushButton_Calculate_tabPopIn_FrameStiffness = QPushButton(self.tab_35)
        self.pushButton_Calculate_tabPopIn_FrameStiffness.setObjectName(u"pushButton_Calculate_tabPopIn_FrameStiffness")
        sizePolicy1.setHeightForWidth(self.pushButton_Calculate_tabPopIn_FrameStiffness.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate_tabPopIn_FrameStiffness.setSizePolicy(sizePolicy1)
        self.pushButton_Calculate_tabPopIn_FrameStiffness.setMinimumSize(QSize(224, 0))
        self.pushButton_Calculate_tabPopIn_FrameStiffness.setMaximumSize(QSize(224, 16777215))

        self.gridLayout_67.addWidget(self.pushButton_Calculate_tabPopIn_FrameStiffness, 8, 1, 1, 1)

        self.groupBox_43 = QGroupBox(self.tab_35)
        self.groupBox_43.setObjectName(u"groupBox_43")
        sizePolicy1.setHeightForWidth(self.groupBox_43.sizePolicy().hasHeightForWidth())
        self.groupBox_43.setSizePolicy(sizePolicy1)
        self.groupBox_43.setMinimumSize(QSize(230, 0))
        self.groupBox_43.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_93 = QGridLayout(self.groupBox_43)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness = QCheckBox(self.groupBox_43)
        self.checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness.setObjectName(u"checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness")
        self.checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness.setEnabled(True)
        self.checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness.setChecked(True)

        self.gridLayout_93.addWidget(self.checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness, 0, 0, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_43, 7, 0, 2, 1)

        self.tabWidget_10.addTab(self.tab_35, "")
        self.tab_40 = QWidget()
        self.tab_40.setObjectName(u"tab_40")
        self.gridLayout_77 = QGridLayout(self.tab_40)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.groupBox_39 = QGroupBox(self.tab_40)
        self.groupBox_39.setObjectName(u"groupBox_39")
        sizePolicy1.setHeightForWidth(self.groupBox_39.sizePolicy().hasHeightForWidth())
        self.groupBox_39.setSizePolicy(sizePolicy1)
        self.groupBox_39.setMinimumSize(QSize(460, 0))
        self.groupBox_39.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_87 = QGridLayout(self.groupBox_39)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.doubleSpinBox_Poisson_Tip_tabPopIn = QDoubleSpinBox(self.groupBox_39)
        self.doubleSpinBox_Poisson_Tip_tabPopIn.setObjectName(u"doubleSpinBox_Poisson_Tip_tabPopIn")
        self.doubleSpinBox_Poisson_Tip_tabPopIn.setDecimals(3)
        self.doubleSpinBox_Poisson_Tip_tabPopIn.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_Tip_tabPopIn.setValue(0.070000000000000)

        self.gridLayout_87.addWidget(self.doubleSpinBox_Poisson_Tip_tabPopIn, 1, 3, 1, 1)

        self.label_119 = QLabel(self.groupBox_39)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_87.addWidget(self.label_119, 0, 0, 1, 1)

        self.doubleSpinBox_E_Tip_tabPopIn = QDoubleSpinBox(self.groupBox_39)
        self.doubleSpinBox_E_Tip_tabPopIn.setObjectName(u"doubleSpinBox_E_Tip_tabPopIn")
        self.doubleSpinBox_E_Tip_tabPopIn.setDecimals(3)
        self.doubleSpinBox_E_Tip_tabPopIn.setMaximum(99999.990000000005239)
        self.doubleSpinBox_E_Tip_tabPopIn.setSingleStep(0.001000000000000)
        self.doubleSpinBox_E_Tip_tabPopIn.setValue(1141.000000000000000)

        self.gridLayout_87.addWidget(self.doubleSpinBox_E_Tip_tabPopIn, 1, 1, 1, 1)

        self.label_117 = QLabel(self.groupBox_39)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_87.addWidget(self.label_117, 1, 0, 1, 1)

        self.label_118 = QLabel(self.groupBox_39)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_87.addWidget(self.label_118, 1, 2, 1, 1)

        self.label_104 = QLabel(self.groupBox_39)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_87.addWidget(self.label_104, 2, 0, 1, 1)

        self.doubleSpinBox_TipRadius_tabPopIn = QDoubleSpinBox(self.groupBox_39)
        self.doubleSpinBox_TipRadius_tabPopIn.setObjectName(u"doubleSpinBox_TipRadius_tabPopIn")
        self.doubleSpinBox_TipRadius_tabPopIn.setEnabled(True)
        self.doubleSpinBox_TipRadius_tabPopIn.setDecimals(6)
        self.doubleSpinBox_TipRadius_tabPopIn.setSingleStep(0.000001000000000)
        self.doubleSpinBox_TipRadius_tabPopIn.setValue(0.100000000000000)

        self.gridLayout_87.addWidget(self.doubleSpinBox_TipRadius_tabPopIn, 2, 1, 1, 1)

        self.lineEdit_TipName_tabPopIn = QLineEdit(self.groupBox_39)
        self.lineEdit_TipName_tabPopIn.setObjectName(u"lineEdit_TipName_tabPopIn")
        sizePolicy2.setHeightForWidth(self.lineEdit_TipName_tabPopIn.sizePolicy().hasHeightForWidth())
        self.lineEdit_TipName_tabPopIn.setSizePolicy(sizePolicy2)

        self.gridLayout_87.addWidget(self.lineEdit_TipName_tabPopIn, 0, 1, 1, 3)

        self.Copy_TipRadius_tabPopIn = QPushButton(self.groupBox_39)
        self.Copy_TipRadius_tabPopIn.setObjectName(u"Copy_TipRadius_tabPopIn")

        self.gridLayout_87.addWidget(self.Copy_TipRadius_tabPopIn, 2, 2, 1, 2)


        self.gridLayout_77.addWidget(self.groupBox_39, 1, 0, 1, 2)

        self.groupBox_35 = QGroupBox(self.tab_40)
        self.groupBox_35.setObjectName(u"groupBox_35")
        sizePolicy1.setHeightForWidth(self.groupBox_35.sizePolicy().hasHeightForWidth())
        self.groupBox_35.setSizePolicy(sizePolicy1)
        self.groupBox_35.setMinimumSize(QSize(460, 0))
        self.groupBox_35.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_78 = QGridLayout(self.groupBox_35)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.label_103 = QLabel(self.groupBox_35)
        self.label_103.setObjectName(u"label_103")
        sizePolicy8.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy8)

        self.gridLayout_78.addWidget(self.label_103, 0, 0, 1, 1)

        self.lineEdit_MaterialName_tabPopIn = QLineEdit(self.groupBox_35)
        self.lineEdit_MaterialName_tabPopIn.setObjectName(u"lineEdit_MaterialName_tabPopIn")
        sizePolicy2.setHeightForWidth(self.lineEdit_MaterialName_tabPopIn.sizePolicy().hasHeightForWidth())
        self.lineEdit_MaterialName_tabPopIn.setSizePolicy(sizePolicy2)
        self.lineEdit_MaterialName_tabPopIn.setMinimumSize(QSize(0, 0))

        self.gridLayout_78.addWidget(self.lineEdit_MaterialName_tabPopIn, 0, 1, 1, 1)

        self.label_105 = QLabel(self.groupBox_35)
        self.label_105.setObjectName(u"label_105")
        sizePolicy8.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy8)
        self.label_105.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_78.addWidget(self.label_105, 0, 2, 1, 1)

        self.label_102 = QLabel(self.groupBox_35)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_78.addWidget(self.label_102, 1, 0, 1, 1)

        self.lineEdit_path_tabPopIn = QLineEdit(self.groupBox_35)
        self.lineEdit_path_tabPopIn.setObjectName(u"lineEdit_path_tabPopIn")
        sizePolicy2.setHeightForWidth(self.lineEdit_path_tabPopIn.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_tabPopIn.setSizePolicy(sizePolicy2)

        self.gridLayout_78.addWidget(self.lineEdit_path_tabPopIn, 1, 1, 1, 5)

        self.doubleSpinBox_Poisson_tabPopIn = QDoubleSpinBox(self.groupBox_35)
        self.doubleSpinBox_Poisson_tabPopIn.setObjectName(u"doubleSpinBox_Poisson_tabPopIn")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Poisson_tabPopIn.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Poisson_tabPopIn.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Poisson_tabPopIn.setDecimals(3)
        self.doubleSpinBox_Poisson_tabPopIn.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Poisson_tabPopIn.setValue(0.300000000000000)

        self.gridLayout_78.addWidget(self.doubleSpinBox_Poisson_tabPopIn, 0, 3, 1, 3)


        self.gridLayout_77.addWidget(self.groupBox_35, 0, 0, 1, 2)

        self.groupBox_38 = QGroupBox(self.tab_40)
        self.groupBox_38.setObjectName(u"groupBox_38")
        sizePolicy1.setHeightForWidth(self.groupBox_38.sizePolicy().hasHeightForWidth())
        self.groupBox_38.setSizePolicy(sizePolicy1)
        self.groupBox_38.setMinimumSize(QSize(460, 0))
        self.groupBox_38.setMaximumSize(QSize(460, 16777215))
        self.gridLayout_86 = QGridLayout(self.groupBox_38)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.label_114 = QLabel(self.groupBox_38)
        self.label_114.setObjectName(u"label_114")
        sizePolicy1.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy1)
        self.label_114.setMinimumSize(QSize(128, 0))
        self.label_114.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_86.addWidget(self.label_114, 1, 5, 1, 1)

        self.doubleSpinBox_relForceRateNoise_tabPopIn = QDoubleSpinBox(self.groupBox_38)
        self.doubleSpinBox_relForceRateNoise_tabPopIn.setObjectName(u"doubleSpinBox_relForceRateNoise_tabPopIn")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_relForceRateNoise_tabPopIn.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_relForceRateNoise_tabPopIn.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_relForceRateNoise_tabPopIn.setDecimals(4)
        self.doubleSpinBox_relForceRateNoise_tabPopIn.setSingleStep(0.001000000000000)
        self.doubleSpinBox_relForceRateNoise_tabPopIn.setValue(0.030000000000000)

        self.gridLayout_86.addWidget(self.doubleSpinBox_relForceRateNoise_tabPopIn, 1, 4, 1, 1)

        self.label_115 = QLabel(self.groupBox_38)
        self.label_115.setObjectName(u"label_115")
        sizePolicy1.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy1)

        self.gridLayout_86.addWidget(self.label_115, 1, 1, 1, 1)

        self.spinBox_max_size_fluctuation_tabPopIn = QSpinBox(self.groupBox_38)
        self.spinBox_max_size_fluctuation_tabPopIn.setObjectName(u"spinBox_max_size_fluctuation_tabPopIn")
        sizePolicy2.setHeightForWidth(self.spinBox_max_size_fluctuation_tabPopIn.sizePolicy().hasHeightForWidth())
        self.spinBox_max_size_fluctuation_tabPopIn.setSizePolicy(sizePolicy2)
        self.spinBox_max_size_fluctuation_tabPopIn.setValue(5)

        self.gridLayout_86.addWidget(self.spinBox_max_size_fluctuation_tabPopIn, 1, 6, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_38, 2, 0, 1, 2)

        self.graphicsView_tab_TipAreaFunction_7 = QTabWidget(self.tab_40)
        self.graphicsView_tab_TipAreaFunction_7.setObjectName(u"graphicsView_tab_TipAreaFunction_7")
        sizePolicy.setHeightForWidth(self.graphicsView_tab_TipAreaFunction_7.sizePolicy().hasHeightForWidth())
        self.graphicsView_tab_TipAreaFunction_7.setSizePolicy(sizePolicy)
        self.graphicsView_tab_TipAreaFunction_7.setUsesScrollButtons(True)
        self.tab_41 = QWidget()
        self.tab_41.setObjectName(u"tab_41")
        self.gridLayout_80 = QGridLayout(self.tab_41)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.tabWidget_12 = QTabWidget(self.tab_41)
        self.tabWidget_12.setObjectName(u"tabWidget_12")
        sizePolicy6.setHeightForWidth(self.tabWidget_12.sizePolicy().hasHeightForWidth())
        self.tabWidget_12.setSizePolicy(sizePolicy6)
        self.tab_42 = QWidget()
        self.tab_42.setObjectName(u"tab_42")
        self.gridLayout_81 = QGridLayout(self.tab_42)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn = QGraphicsView(self.tab_42)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setObjectName(u"graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn")
        sizePolicy19 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setSizePolicy(sizePolicy19)
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setMinimumSize(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setMaximumSize(QSize(16777215, 16777215))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setSizeIncrement(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setBaseSize(QSize(0, 0))
        self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_81.addWidget(self.graphicsView_load_depth_tab_inclusive_frame_stiffness_tabPopIn, 1, 0, 1, 5)

        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn = QCheckBox(self.tab_42)
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn.setObjectName(u"checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn")

        self.gridLayout_81.addWidget(self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn, 2, 0, 1, 1)

        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn = QCheckBox(self.tab_42)
        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn.setObjectName(u"checkBox_iLHU_inclusive_frame_stiffness_tabPopIn")

        self.gridLayout_81.addWidget(self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn, 2, 1, 1, 1)

        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn = QPushButton(self.tab_42)
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn.setObjectName(u"pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn.setSizePolicy(sizePolicy1)

        self.gridLayout_81.addWidget(self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn, 3, 0, 1, 2)

        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn = QCheckBox(self.tab_42)
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn.setObjectName(u"checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn")

        self.gridLayout_81.addWidget(self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn, 2, 2, 1, 1)

        self.tabWidget_12.addTab(self.tab_42, "")
        self.tab_43 = QWidget()
        self.tab_43.setObjectName(u"tab_43")
        self.gridLayout_82 = QGridLayout(self.tab_43)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_3 = QGraphicsView(self.tab_43)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_3.setObjectName(u"graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_3")
        sizePolicy.setHeightForWidth(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_3.setSizePolicy(sizePolicy)

        self.gridLayout_82.addWidget(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabTAF_3, 0, 0, 1, 1)

        self.tabWidget_12.addTab(self.tab_43, "")

        self.gridLayout_80.addWidget(self.tabWidget_12, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_7.addTab(self.tab_41, "")
        self.tab_44 = QWidget()
        self.tab_44.setObjectName(u"tab_44")
        self.gridLayout_83 = QGridLayout(self.tab_44)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn = QPushButton(self.tab_44)
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn.setObjectName(u"pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn")
        sizePolicy1.setHeightForWidth(self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn.sizePolicy().hasHeightForWidth())
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn.setSizePolicy(sizePolicy1)

        self.gridLayout_83.addWidget(self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn, 2, 0, 1, 1)

        self.graphicsView_HertzianFitting_tabPopIn = QGraphicsView(self.tab_44)
        self.graphicsView_HertzianFitting_tabPopIn.setObjectName(u"graphicsView_HertzianFitting_tabPopIn")

        self.gridLayout_83.addWidget(self.graphicsView_HertzianFitting_tabPopIn, 1, 0, 1, 2)

        self.graphicsView_tab_TipAreaFunction_7.addTab(self.tab_44, "")
        self.tab_45 = QWidget()
        self.tab_45.setObjectName(u"tab_45")
        self.gridLayout_84 = QGridLayout(self.tab_45)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.label_107 = QLabel(self.tab_45)
        self.label_107.setObjectName(u"label_107")
        sizePolicy8.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy8)

        self.gridLayout_84.addWidget(self.label_107, 0, 2, 1, 1)

        self.label_109 = QLabel(self.tab_45)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_84.addWidget(self.label_109, 0, 0, 1, 1)

        self.graphicsView_E_tabPopIn = QGraphicsView(self.tab_45)
        self.graphicsView_E_tabPopIn.setObjectName(u"graphicsView_E_tabPopIn")
        sizePolicy.setHeightForWidth(self.graphicsView_E_tabPopIn.sizePolicy().hasHeightForWidth())
        self.graphicsView_E_tabPopIn.setSizePolicy(sizePolicy)

        self.gridLayout_84.addWidget(self.graphicsView_E_tabPopIn, 1, 0, 2, 8)

        self.lineEdit_E_errorBar_tabPopIn = QLineEdit(self.tab_45)
        self.lineEdit_E_errorBar_tabPopIn.setObjectName(u"lineEdit_E_errorBar_tabPopIn")
        sizePolicy7.setHeightForWidth(self.lineEdit_E_errorBar_tabPopIn.sizePolicy().hasHeightForWidth())
        self.lineEdit_E_errorBar_tabPopIn.setSizePolicy(sizePolicy7)

        self.gridLayout_84.addWidget(self.lineEdit_E_errorBar_tabPopIn, 0, 3, 1, 1)

        self.lineEdit_E_tabPopIn = QLineEdit(self.tab_45)
        self.lineEdit_E_tabPopIn.setObjectName(u"lineEdit_E_tabPopIn")
        sizePolicy7.setHeightForWidth(self.lineEdit_E_tabPopIn.sizePolicy().hasHeightForWidth())
        self.lineEdit_E_tabPopIn.setSizePolicy(sizePolicy7)
        self.lineEdit_E_tabPopIn.setReadOnly(True)

        self.gridLayout_84.addWidget(self.lineEdit_E_tabPopIn, 0, 1, 1, 1)

        self.graphicsView_tab_TipAreaFunction_7.addTab(self.tab_45, "")
        self.tab_47 = QWidget()
        self.tab_47.setObjectName(u"tab_47")
        self.gridLayout_114 = QGridLayout(self.tab_47)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.graphicsView_PopInLoad_tabPopIn = QGraphicsView(self.tab_47)
        self.graphicsView_PopInLoad_tabPopIn.setObjectName(u"graphicsView_PopInLoad_tabPopIn")

        self.gridLayout_114.addWidget(self.graphicsView_PopInLoad_tabPopIn, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_7.addTab(self.tab_47, "")
        self.tab_34 = QWidget()
        self.tab_34.setObjectName(u"tab_34")
        self.gridLayout_90 = QGridLayout(self.tab_34)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.graphicsView_maxShearStress_tabPopIn = QGraphicsView(self.tab_34)
        self.graphicsView_maxShearStress_tabPopIn.setObjectName(u"graphicsView_maxShearStress_tabPopIn")

        self.gridLayout_90.addWidget(self.graphicsView_maxShearStress_tabPopIn, 0, 0, 1, 1)

        self.graphicsView_tab_TipAreaFunction_7.addTab(self.tab_34, "")

        self.gridLayout_77.addWidget(self.graphicsView_tab_TipAreaFunction_7, 0, 3, 15, 1)

        self.groupBox_40 = QGroupBox(self.tab_40)
        self.groupBox_40.setObjectName(u"groupBox_40")
        sizePolicy1.setHeightForWidth(self.groupBox_40.sizePolicy().hasHeightForWidth())
        self.groupBox_40.setSizePolicy(sizePolicy1)
        self.groupBox_40.setMinimumSize(QSize(224, 0))
        self.groupBox_40.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_88 = QGridLayout(self.groupBox_40)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.lineEdit_FrameCompliance_tabPopIn = QLineEdit(self.groupBox_40)
        self.lineEdit_FrameCompliance_tabPopIn.setObjectName(u"lineEdit_FrameCompliance_tabPopIn")
        self.lineEdit_FrameCompliance_tabPopIn.setReadOnly(True)

        self.gridLayout_88.addWidget(self.lineEdit_FrameCompliance_tabPopIn, 0, 0, 1, 1)

        self.Copy_FrameCompliance_tabPopIn = QPushButton(self.groupBox_40)
        self.Copy_FrameCompliance_tabPopIn.setObjectName(u"Copy_FrameCompliance_tabPopIn")

        self.gridLayout_88.addWidget(self.Copy_FrameCompliance_tabPopIn, 1, 0, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_40, 3, 1, 1, 1)

        self.groupBox_36 = QGroupBox(self.tab_40)
        self.groupBox_36.setObjectName(u"groupBox_36")
        sizePolicy1.setHeightForWidth(self.groupBox_36.sizePolicy().hasHeightForWidth())
        self.groupBox_36.setSizePolicy(sizePolicy1)
        self.groupBox_36.setMinimumSize(QSize(230, 0))
        self.groupBox_36.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_79 = QGridLayout(self.groupBox_36)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.label_106 = QLabel(self.groupBox_36)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_79.addWidget(self.label_106, 1, 1, 1, 1)

        self.doubleSpinBox_Rate2findSurface_tabPopIn = QDoubleSpinBox(self.groupBox_36)
        self.doubleSpinBox_Rate2findSurface_tabPopIn.setObjectName(u"doubleSpinBox_Rate2findSurface_tabPopIn")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Rate2findSurface_tabPopIn.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Rate2findSurface_tabPopIn.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Rate2findSurface_tabPopIn.setDecimals(1)
        self.doubleSpinBox_Rate2findSurface_tabPopIn.setValue(1.000000000000000)

        self.gridLayout_79.addWidget(self.doubleSpinBox_Rate2findSurface_tabPopIn, 0, 2, 1, 1)

        self.spinBox_DataFilterSize_tabPopIn = QSpinBox(self.groupBox_36)
        self.spinBox_DataFilterSize_tabPopIn.setObjectName(u"spinBox_DataFilterSize_tabPopIn")
        sizePolicy2.setHeightForWidth(self.spinBox_DataFilterSize_tabPopIn.sizePolicy().hasHeightForWidth())
        self.spinBox_DataFilterSize_tabPopIn.setSizePolicy(sizePolicy2)
        self.spinBox_DataFilterSize_tabPopIn.setValue(5)

        self.gridLayout_79.addWidget(self.spinBox_DataFilterSize_tabPopIn, 1, 2, 1, 1)

        self.checkBox_UsingRate2findSurface_tabPopIn = QCheckBox(self.groupBox_36)
        self.checkBox_UsingRate2findSurface_tabPopIn.setObjectName(u"checkBox_UsingRate2findSurface_tabPopIn")
        sizePolicy1.setHeightForWidth(self.checkBox_UsingRate2findSurface_tabPopIn.sizePolicy().hasHeightForWidth())
        self.checkBox_UsingRate2findSurface_tabPopIn.setSizePolicy(sizePolicy1)
        self.checkBox_UsingRate2findSurface_tabPopIn.setChecked(True)

        self.gridLayout_79.addWidget(self.checkBox_UsingRate2findSurface_tabPopIn, 0, 1, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_36, 4, 0, 1, 1)

        self.groupBox_37 = QGroupBox(self.tab_40)
        self.groupBox_37.setObjectName(u"groupBox_37")
        sizePolicy1.setHeightForWidth(self.groupBox_37.sizePolicy().hasHeightForWidth())
        self.groupBox_37.setSizePolicy(sizePolicy1)
        self.groupBox_37.setMinimumSize(QSize(230, 0))
        self.groupBox_37.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_85 = QGridLayout(self.groupBox_37)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.label_110 = QLabel(self.groupBox_37)
        self.label_110.setObjectName(u"label_110")
        sizePolicy1.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy1)
        self.label_110.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_85.addWidget(self.label_110, 2, 1, 1, 1)

        self.comboBox_equipment_tabPopIn = QComboBox(self.groupBox_37)
        self.comboBox_equipment_tabPopIn.addItem("")
        self.comboBox_equipment_tabPopIn.setObjectName(u"comboBox_equipment_tabPopIn")
        self.comboBox_equipment_tabPopIn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_equipment_tabPopIn.sizePolicy().hasHeightForWidth())
        self.comboBox_equipment_tabPopIn.setSizePolicy(sizePolicy2)

        self.gridLayout_85.addWidget(self.comboBox_equipment_tabPopIn, 2, 2, 1, 1)

        self.label_111 = QLabel(self.groupBox_37)
        self.label_111.setObjectName(u"label_111")
        sizePolicy16.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy16)
        self.label_111.setMaximumSize(QSize(16777215, 16777215))
        self.label_111.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_85.addWidget(self.label_111, 1, 1, 1, 1)

        self.comboBox_method_tabPopIn = QComboBox(self.groupBox_37)
        self.comboBox_method_tabPopIn.addItem("")
        self.comboBox_method_tabPopIn.addItem("")
        self.comboBox_method_tabPopIn.addItem("")
        self.comboBox_method_tabPopIn.setObjectName(u"comboBox_method_tabPopIn")
        self.comboBox_method_tabPopIn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_method_tabPopIn.sizePolicy().hasHeightForWidth())
        self.comboBox_method_tabPopIn.setSizePolicy(sizePolicy2)
        self.comboBox_method_tabPopIn.setMinimumSize(QSize(120, 0))
        self.comboBox_method_tabPopIn.setEditable(False)

        self.gridLayout_85.addWidget(self.comboBox_method_tabPopIn, 1, 2, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_37, 3, 0, 1, 1)

        self.progressBar_tabPopIn = QProgressBar(self.tab_40)
        self.progressBar_tabPopIn.setObjectName(u"progressBar_tabPopIn")
        sizePolicy1.setHeightForWidth(self.progressBar_tabPopIn.sizePolicy().hasHeightForWidth())
        self.progressBar_tabPopIn.setSizePolicy(sizePolicy1)
        self.progressBar_tabPopIn.setMinimumSize(QSize(224, 0))
        self.progressBar_tabPopIn.setMaximumSize(QSize(224, 16777215))
        self.progressBar_tabPopIn.setValue(0)

        self.gridLayout_77.addWidget(self.progressBar_tabPopIn, 5, 1, 1, 1)

        self.groupBox_54 = QGroupBox(self.tab_40)
        self.groupBox_54.setObjectName(u"groupBox_54")
        sizePolicy1.setHeightForWidth(self.groupBox_54.sizePolicy().hasHeightForWidth())
        self.groupBox_54.setSizePolicy(sizePolicy1)
        self.groupBox_54.setMinimumSize(QSize(224, 0))
        self.groupBox_54.setMaximumSize(QSize(224, 16777215))
        self.gridLayout_104 = QGridLayout(self.groupBox_54)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.doubleSpinBox_End_Pmax_tabPopIn = QDoubleSpinBox(self.groupBox_54)
        self.doubleSpinBox_End_Pmax_tabPopIn.setObjectName(u"doubleSpinBox_End_Pmax_tabPopIn")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_End_Pmax_tabPopIn.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_End_Pmax_tabPopIn.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_End_Pmax_tabPopIn.setSingleStep(0.010000000000000)
        self.doubleSpinBox_End_Pmax_tabPopIn.setValue(0.500000000000000)

        self.gridLayout_104.addWidget(self.doubleSpinBox_End_Pmax_tabPopIn, 1, 1, 1, 1)

        self.label_112 = QLabel(self.groupBox_54)
        self.label_112.setObjectName(u"label_112")
        sizePolicy9.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy9)
        self.label_112.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.label_112, 1, 0, 1, 1)

        self.doubleSpinBox_Start_Pmax_tabPopIn = QDoubleSpinBox(self.groupBox_54)
        self.doubleSpinBox_Start_Pmax_tabPopIn.setObjectName(u"doubleSpinBox_Start_Pmax_tabPopIn")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Start_Pmax_tabPopIn.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Start_Pmax_tabPopIn.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Start_Pmax_tabPopIn.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Start_Pmax_tabPopIn.setValue(0.980000000000000)

        self.gridLayout_104.addWidget(self.doubleSpinBox_Start_Pmax_tabPopIn, 0, 1, 1, 1)

        self.label_113 = QLabel(self.groupBox_54)
        self.label_113.setObjectName(u"label_113")
        sizePolicy1.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy1)
        self.label_113.setMinimumSize(QSize(110, 0))
        self.label_113.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_104.addWidget(self.label_113, 0, 0, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_54, 4, 1, 1, 1)

        self.pushButton_Analyse_tabPopIn = QPushButton(self.tab_40)
        self.pushButton_Analyse_tabPopIn.setObjectName(u"pushButton_Analyse_tabPopIn")
        sizePolicy1.setHeightForWidth(self.pushButton_Analyse_tabPopIn.sizePolicy().hasHeightForWidth())
        self.pushButton_Analyse_tabPopIn.setSizePolicy(sizePolicy1)
        self.pushButton_Analyse_tabPopIn.setMinimumSize(QSize(224, 0))
        self.pushButton_Analyse_tabPopIn.setMaximumSize(QSize(224, 16777215))

        self.gridLayout_77.addWidget(self.pushButton_Analyse_tabPopIn, 6, 1, 1, 1)

        self.groupBox_44 = QGroupBox(self.tab_40)
        self.groupBox_44.setObjectName(u"groupBox_44")
        sizePolicy1.setHeightForWidth(self.groupBox_44.sizePolicy().hasHeightForWidth())
        self.groupBox_44.setSizePolicy(sizePolicy1)
        self.groupBox_44.setMinimumSize(QSize(230, 0))
        self.groupBox_44.setMaximumSize(QSize(230, 16777215))
        self.gridLayout_94 = QGridLayout(self.groupBox_44)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.checkBox_UsingDriftUnloading_tabPopIn = QCheckBox(self.groupBox_44)
        self.checkBox_UsingDriftUnloading_tabPopIn.setObjectName(u"checkBox_UsingDriftUnloading_tabPopIn")

        self.gridLayout_94.addWidget(self.checkBox_UsingDriftUnloading_tabPopIn, 0, 0, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_44, 5, 0, 2, 1)

        self.pushButton_SelectAll_tabPopIn = QPushButton(self.tab_40)
        self.pushButton_SelectAll_tabPopIn.setObjectName(u"pushButton_SelectAll_tabPopIn")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectAll_tabPopIn.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectAll_tabPopIn.setSizePolicy(sizePolicy1)
        self.pushButton_SelectAll_tabPopIn.setMinimumSize(QSize(205, 0))
        self.pushButton_SelectAll_tabPopIn.setMaximumSize(QSize(205, 16777215))

        self.gridLayout_77.addWidget(self.pushButton_SelectAll_tabPopIn, 6, 2, 1, 1)

        self.tableWidget_tabPopIn = QTableWidget(self.tab_40)
        if (self.tableWidget_tabPopIn.columnCount() < 3):
            self.tableWidget_tabPopIn.setColumnCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabPopIn.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabPopIn.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_tabPopIn.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        if (self.tableWidget_tabPopIn.rowCount() < 1):
            self.tableWidget_tabPopIn.setRowCount(1)
        self.tableWidget_tabPopIn.setObjectName(u"tableWidget_tabPopIn")
        sizePolicy12.setHeightForWidth(self.tableWidget_tabPopIn.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabPopIn.setSizePolicy(sizePolicy12)
        self.tableWidget_tabPopIn.setMinimumSize(QSize(205, 0))
        self.tableWidget_tabPopIn.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_tabPopIn.setAutoScroll(True)
        self.tableWidget_tabPopIn.setRowCount(1)
        self.tableWidget_tabPopIn.setColumnCount(3)
        self.tableWidget_tabPopIn.horizontalHeader().setVisible(True)
        self.tableWidget_tabPopIn.horizontalHeader().setMinimumSectionSize(65)
        self.tableWidget_tabPopIn.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_tabPopIn.horizontalHeader().setHighlightSections(True)
        self.tableWidget_tabPopIn.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_77.addWidget(self.tableWidget_tabPopIn, 0, 2, 6, 1)

        self.tabWidget_10.addTab(self.tab_40, "")
        self.graphicsView_tab_TipAreaFunction_7.raise_()
        self.groupBox_35.raise_()
        self.groupBox_38.raise_()
        self.groupBox_37.raise_()
        self.groupBox_40.raise_()
        self.groupBox_39.raise_()
        self.tableWidget_tabPopIn.raise_()
        self.groupBox_54.raise_()
        self.groupBox_36.raise_()
        self.groupBox_44.raise_()
        self.progressBar_tabPopIn.raise_()
        self.pushButton_Analyse_tabPopIn.raise_()
        self.pushButton_SelectAll_tabPopIn.raise_()

        self.gridLayout_89.addWidget(self.tabWidget_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_analysePopIn, "")
        self.tab_48 = QWidget()
        self.tab_48.setObjectName(u"tab_48")
        self.gridLayout_116 = QGridLayout(self.tab_48)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.textEdit_Files_tabClassification = QTextEdit(self.tab_48)
        self.textEdit_Files_tabClassification.setObjectName(u"textEdit_Files_tabClassification")
        sizePolicy.setHeightForWidth(self.textEdit_Files_tabClassification.sizePolicy().hasHeightForWidth())
        self.textEdit_Files_tabClassification.setSizePolicy(sizePolicy)

        self.gridLayout_116.addWidget(self.textEdit_Files_tabClassification, 2, 0, 1, 2)

        self.label_160 = QLabel(self.tab_48)
        self.label_160.setObjectName(u"label_160")

        self.gridLayout_116.addWidget(self.label_160, 6, 0, 1, 1)

        self.label_159 = QLabel(self.tab_48)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setWordWrap(True)

        self.gridLayout_116.addWidget(self.label_159, 1, 0, 1, 2)

        self.graphicsView_HE_tabClassification = QGraphicsView(self.tab_48)
        self.graphicsView_HE_tabClassification.setObjectName(u"graphicsView_HE_tabClassification")
        sizePolicy.setHeightForWidth(self.graphicsView_HE_tabClassification.sizePolicy().hasHeightForWidth())
        self.graphicsView_HE_tabClassification.setSizePolicy(sizePolicy)

        self.gridLayout_116.addWidget(self.graphicsView_HE_tabClassification, 0, 2, 3, 1)

        self.spinBox_NumberClusters_tabClassification = QSpinBox(self.tab_48)
        self.spinBox_NumberClusters_tabClassification.setObjectName(u"spinBox_NumberClusters_tabClassification")

        self.gridLayout_116.addWidget(self.spinBox_NumberClusters_tabClassification, 6, 1, 1, 1)

        self.pushButton_PlotMappingAfterClustering_tabClassification = QPushButton(self.tab_48)
        self.pushButton_PlotMappingAfterClustering_tabClassification.setObjectName(u"pushButton_PlotMappingAfterClustering_tabClassification")
        self.pushButton_PlotMappingAfterClustering_tabClassification.setEnabled(False)

        self.gridLayout_116.addWidget(self.pushButton_PlotMappingAfterClustering_tabClassification, 9, 0, 1, 2)

        self.pushButton_Classify_tabClassification = QPushButton(self.tab_48)
        self.pushButton_Classify_tabClassification.setObjectName(u"pushButton_Classify_tabClassification")

        self.gridLayout_116.addWidget(self.pushButton_Classify_tabClassification, 7, 0, 1, 2)

        self.checkBox_ifPlotElbow_tabClassification = QCheckBox(self.tab_48)
        self.checkBox_ifPlotElbow_tabClassification.setObjectName(u"checkBox_ifPlotElbow_tabClassification")
        self.checkBox_ifPlotElbow_tabClassification.setChecked(True)

        self.gridLayout_116.addWidget(self.checkBox_ifPlotElbow_tabClassification, 5, 0, 1, 1)

        self.pushButton_PlotMappingWithoutClustering_tabClassification = QPushButton(self.tab_48)
        self.pushButton_PlotMappingWithoutClustering_tabClassification.setObjectName(u"pushButton_PlotMappingWithoutClustering_tabClassification")

        self.gridLayout_116.addWidget(self.pushButton_PlotMappingWithoutClustering_tabClassification, 8, 0, 1, 2)

        self.checkBox_ifUsingFoundNumberClusters_tabClassification = QCheckBox(self.tab_48)
        self.checkBox_ifUsingFoundNumberClusters_tabClassification.setObjectName(u"checkBox_ifUsingFoundNumberClusters_tabClassification")
        self.checkBox_ifUsingFoundNumberClusters_tabClassification.setChecked(True)

        self.gridLayout_116.addWidget(self.checkBox_ifUsingFoundNumberClusters_tabClassification, 4, 0, 1, 2)

        self.tableWidget_tabClassification = QTableWidget(self.tab_48)
        if (self.tableWidget_tabClassification.columnCount() < 6):
            self.tableWidget_tabClassification.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_tabClassification.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_tabClassification.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_tabClassification.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_tabClassification.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_tabClassification.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_tabClassification.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.tableWidget_tabClassification.setObjectName(u"tableWidget_tabClassification")
        sizePolicy.setHeightForWidth(self.tableWidget_tabClassification.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabClassification.setSizePolicy(sizePolicy)

        self.gridLayout_116.addWidget(self.tableWidget_tabClassification, 4, 2, 6, 1)

        self.tabWidget.addTab(self.tab_48, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1485, 22))
        self.menuData = QMenu(self.menuBar)
        self.menuData.setObjectName(u"menuData")
        self.menuOpenRecent = QMenu(self.menuData)
        self.menuOpenRecent.setObjectName(u"menuOpenRecent")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuData.menuAction())
        self.menuData.addAction(self.actionNew)
        self.menuData.addAction(self.actionLoad)
        self.menuData.addAction(self.menuOpenRecent.menuAction())
        self.menuData.addAction(self.actionSave)
        self.menuData.addAction(self.actionSaveAs)
        self.menuData.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.comboBox_equipment_tabTAF.setCurrentIndex(0)
        self.comboBox_method_tabTAF.setCurrentIndex(0)
        self.graphicsView_tab_TipAreaFunction.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.graphicsView_tab_TipAreaFunction_2.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.graphicsView_tab_TipAreaFunction_5.setCurrentIndex(2)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(1)
        self.graphicsView_tab_TipAreaFunction_3.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.graphicsView_tab_TipAreaFunction_4.setCurrentIndex(0)
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(1)
        self.tabWidget_8.setCurrentIndex(1)
        self.tabWidget_10.setCurrentIndex(0)
        self.graphicsView_tab_TipAreaFunction_6.setCurrentIndex(1)
        self.tabWidget_11.setCurrentIndex(0)
        self.graphicsView_tab_TipAreaFunction_7.setCurrentIndex(0)
        self.tabWidget_12.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
#if QT_CONFIG(shortcut)
        self.actionExport.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionRecent1.setText(QCoreApplication.translate("MainWindow", u"Recent1", None))
        self.actionAAA.setText(QCoreApplication.translate("MainWindow", u"AAA", None))
        self.groupBox_59.setTitle(QCoreApplication.translate("MainWindow", u"Calculation Method", None))
        self.comboBox_CalculationMethod_tabTAF.setItemText(0, QCoreApplication.translate("MainWindow", u"1. Assume constant Hardness and Modulus ( Eq. (24), Oliver 2004)", None))
        self.comboBox_CalculationMethod_tabTAF.setItemText(1, QCoreApplication.translate("MainWindow", u"2. Assume constant Modulus but neglect Pile-up (Eq. (22), Oliver 2004 )", None))

        self.pushButton_SelectAll_tabTAF.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect All", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.checkBox_UsingRate2findSurface_tabTAF.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.groupBox_48.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabTAF.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Material (Target values)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Material's Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus[GPa]:", None))
        self.lineEdit_path_tabTAF.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example1\\FusedSilica.xlsx", None))
        self.lineEdit_MaterialName_tabTAF.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Equipment", None))
        self.comboBox_equipment_tabTAF.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X (KLA)", None))
        self.comboBox_equipment_tabTAF.setItemText(1, QCoreApplication.translate("MainWindow", u"NanoTest Xtreme (Mico Materials)", None))

        self.comboBox_method_tabTAF.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabTAF.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabTAF.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTAF.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTAF.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTAF.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"inclusive of frame compliance", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"exclusive of frame compliance", None))
        self.graphicsView_tab_TipAreaFunction.setTabText(self.graphicsView_tab_TipAreaFunction.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Frame Stiffness [mN/\u00b5m]", None))
        self.lineEdit_FrameStiffness_tabTAF.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.graphicsView_tab_TipAreaFunction.setTabText(self.graphicsView_tab_TipAreaFunction.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Frame Compliance", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Calibrated Tip Area Function", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/4</span>+</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Ac=", None))
        self.lineEdit_TAF3_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF2_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF4_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF1_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/2</span>+</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span>+</p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">2</span>+</p></body></html>", None))
        self.lineEdit_TAF5_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/8</span>+</p></body></html>", None))
        self.lineEdit_TAF6_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/16</span>+</p></body></html>", None))
        self.lineEdit_TAF7_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/32</span>+</p></body></html>", None))
        self.lineEdit_TAF8_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/64</span>+</p></body></html>", None))
        self.lineEdit_TAF9_tabTAF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/128</span></p></body></html>", None))
        self.graphicsView_tab_TipAreaFunction.setTabText(self.graphicsView_tab_TipAreaFunction.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tip Area Function", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Tip", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus[GPa]:", None))
        self.comboBox_TipType_tabTAF.setItemText(0, QCoreApplication.translate("MainWindow", u"Berkovich", None))
        self.comboBox_TipType_tabTAF.setItemText(1, QCoreApplication.translate("MainWindow", u"Sphere", None))
        self.comboBox_TipType_tabTAF.setItemText(2, QCoreApplication.translate("MainWindow", u"Sphere+Cone", None))

        self.groupBox_63.setTitle(QCoreApplication.translate("MainWindow", u"Geometric Parameters of Cone/ Sphere", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"conical half-included angle [\u00b0]:", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"spherical radius [\u00b5m]:", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Geometry:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Tip's Name:", None))
        self.lineEdit_TipName_tabTAF.setText(QCoreApplication.translate("MainWindow", u"a Berkovich Tip ", None))
        self.groupBox_64.setTitle(QCoreApplication.translate("MainWindow", u"Parametres for Tip Area Function (TAF)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Number of Terms:", None))
        self.checkBox_IfTermsGreaterThanZero_tabTAF.setText(QCoreApplication.translate("MainWindow", u"Terms > 0 (except the first Term of Sphere)", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"min. Depth [\u00b5m]:", None))
        ___qtablewidgetitem = self.tableWidget_tabTAF.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"(use?) Test", None));
        ___qtablewidgetitem1 = self.tableWidget_tabTAF.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        self.OK_path_tabTAF.setText(QCoreApplication.translate("MainWindow", u"Calcultate Frame Compliance and TAF", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Range to calculate Frame Compliance", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"min. Depth [\u00b5m]:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"min. Force [mN]:", None))
        self.groupBox_55.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to Calculate Stiffnes", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calibration), QCoreApplication.translate("MainWindow", u"Tip Area Function", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.pushButton_SelectAll_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect all", None))
        self.groupBox_57.setTitle(QCoreApplication.translate("MainWindow", u"Calculation Method", None))
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"1. Assume constant Hardness and Modulus ( Eq. (24), Oliver 2004)", None))
        self.comboBox_CalculationMethod_tabTipRadius_FrameStiffness.setItemText(1, QCoreApplication.translate("MainWindow", u"2. Assume constant Modulus and neglect Pile-up (Eq. (22), Oliver 2004 )", None))

        self.groupBox_61.setTitle(QCoreApplication.translate("MainWindow", u"Tip Area Function used by method 2.", None))
        self.lineEdit_TAF4_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">2</span>+</p></body></html>", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/2</span>+</p></body></html>", None))
        self.lineEdit_TAF2_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Ac=", None))
        self.lineEdit_TAF3_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF1_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"24.5", None))
        self.lineEdit_TAF5_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Tip Name:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/4</span>+</p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span>+</p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/8</span>+</p></body></html>", None))
        self.lineEdit_TAF9_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF8_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF7_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF6_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/16</span>+</p></body></html>", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/32</span>+</p></body></html>", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/64</span>+</p></body></html>", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/128</span></p></body></html>", None))
        self.Copy_TAF_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Copy from \"Tip Area Function\"", None))
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"inclusive of frame compliance", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"exclusive of frame compliance", None))
        self.graphicsView_tab_TipAreaFunction_2.setTabText(self.graphicsView_tab_TipAreaFunction_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Frame Stiffness [mN/\u00b5m]", None))
        self.lineEdit_FrameStiffness_tabTipRadius_FrameStiffness.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.graphicsView_tab_TipAreaFunction_2.setTabText(self.graphicsView_tab_TipAreaFunction_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Frame Compliance", None))
        ___qtablewidgetitem2 = self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Test Name", None));
        ___qtablewidgetitem3 = self.tableWidget_tabTipRadius_FrameStiffness.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.checkBox_UsingRate2findSurface_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.comboBox_equipment_tabTipRadius_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X", None))

        self.comboBox_method_tabTipRadius_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabTipRadius_FrameStiffness.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabTipRadius_FrameStiffness.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Test for Calculating Frame Compliance", None))
        self.lineEdit_path_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example2\\Tungsten_FrameStiffness.xlsx", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.groupBox_50.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to Calculate Stiffness ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Range to Calculate Frame Compliance", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"min. Depth [\u00b5m]:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"min. Force [mN]:", None))
        self.pushButton_Calculate_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Calculate Frame Compliance", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabTipRadius_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Calculate Frame Compliance", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Tested Material", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Material's Name:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus [GPa]:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.lineEdit_path_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example2\\Tungsten_TipRadius.xlsx", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Tip", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Tip's Name:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus [GPa]:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.lineEdit_TipName_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"a Berkovich Tip", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_30), QCoreApplication.translate("MainWindow", u"inclusive of frame compliance", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_31), QCoreApplication.translate("MainWindow", u"exclusive of frame compliance", None))
        self.graphicsView_tab_TipAreaFunction_5.setTabText(self.graphicsView_tab_TipAreaFunction_5.indexOf(self.tab_29), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.graphicsView_tab_TipAreaFunction_5.setTabText(self.graphicsView_tab_TipAreaFunction_5.indexOf(self.tab_32), QCoreApplication.translate("MainWindow", u"Hertzian fitting", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Tip Radius [\u00b5m]", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"reduced Modulus Er [GPa]", None))
        self.graphicsView_tab_TipAreaFunction_5.setTabText(self.graphicsView_tab_TipAreaFunction_5.indexOf(self.tab_33), QCoreApplication.translate("MainWindow", u"Calculated Tip Radius", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.comboBox_method_tabTipRadius.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabTipRadius.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabTipRadius.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        self.comboBox_equipment_tabTipRadius.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X", None))

        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.groupBox_49.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to calculate stiffnes", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.checkBox_UsingRate2findSurface_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.lineEdit_FrameCompliance_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Copy_FrameCompliance_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Copy the calculated value", None))
        self.pushButton_Calculate_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Calculate Tip Radius", None))
        self.groupBox_46.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        ___qtablewidgetitem4 = self.tableWidget_tabTipRadius.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Test Name", None));
        ___qtablewidgetitem5 = self.tableWidget_tabTipRadius.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        ___qtablewidgetitem6 = self.tableWidget_tabTipRadius.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pop-in?", None));
        self.pushButton_SelectAll_tabTipRadius.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect all", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Calculate Tip Radius", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tip Radius", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"inclusive of frame compliance", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"exclusive of frame compliance", None))
        self.graphicsView_tab_TipAreaFunction_3.setTabText(self.graphicsView_tab_TipAreaFunction_3.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Frame Stiffness [mN/\u00b5m]", None))
        self.lineEdit_FrameStiffness_tabHE_FrameStiffness.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.graphicsView_tab_TipAreaFunction_3.setTabText(self.graphicsView_tab_TipAreaFunction_3.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"Frame Compliance", None))
        self.groupBox_56.setTitle(QCoreApplication.translate("MainWindow", u"Calculation Method", None))
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"1. Assume constant Hardness and Modulus ( Eq. (24), Oliver 2004)", None))
        self.comboBox_CalculationMethod_tabHE_FrameStiffness.setItemText(1, QCoreApplication.translate("MainWindow", u"2. Assume constant Modulus and neglect Pile-up (Eq. (22), Oliver 2004 )", None))

        self.groupBox_60.setTitle(QCoreApplication.translate("MainWindow", u"Tip Area Function used by method 2.", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">2</span>+</p></body></html>", None))
        self.lineEdit_TAF1_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"24.5", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Tip Name:", None))
        self.lineEdit_TAF5_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span>+</p></body></html>", None))
        self.lineEdit_TAF3_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF2_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/2</span>+</p></body></html>", None))
        self.lineEdit_TAF4_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/4</span>+</p></body></html>", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/8</span>+</p></body></html>", None))
        self.lineEdit_TAF6_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF7_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF8_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF9_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/16</span>+</p></body></html>", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/32</span>+</p></body></html>", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/64</span>+</p></body></html>", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/128</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Ac=", None))
        self.Copy_TAF_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Copy from \"Tip Area Function\"", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.comboBox_method_tabHE_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabHE_FrameStiffness.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabHE_FrameStiffness.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        self.comboBox_equipment_tabHE_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X", None))

        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.checkBox_UsingRate2findSurface_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Test for Calculating Frame Compliance", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.lineEdit_path_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example1\\FusedSilica.xlsx", None))
        self.pushButton_SelectAll_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect all", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Range to Calculate Frame Compliance", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"min. Depth [\u00b5m]:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"min. Force [mN]:", None))
        self.groupBox_51.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to Calculate Stiffness", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.pushButton_Calculate_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Calculate Frame Compliance", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabHE_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        ___qtablewidgetitem7 = self.tableWidget_tabHE_FrameStiffness.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Test Name", None));
        ___qtablewidgetitem8 = self.tableWidget_tabHE_FrameStiffness.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Calculate Frame Compliance", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.comboBox_method_tabHE.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabHE.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabHE.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        self.comboBox_equipment_tabHE.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X", None))
        self.comboBox_equipment_tabHE.setItemText(1, QCoreApplication.translate("MainWindow", u"Hysitron", None))
        self.comboBox_equipment_tabHE.setItemText(2, QCoreApplication.translate("MainWindow", u"MicroMaterials", None))

        self.groupBox_52.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to Calculate Stiffnes", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Tested Material", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Material's Name:", None))
        self.lineEdit_path_tabHE.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example1\\FusedSilica.xlsx", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabHE.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Tip", None))
        self.lineEdit_TAF6_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Copy_TAF_tabHE.setText(QCoreApplication.translate("MainWindow", u"Copy from \"Tip Area Function\"", None))
        self.lineEdit_TAF4_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/64</span>+</p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">2</span>+</p></body></html>", None))
        self.lineEdit_TAF8_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/16</span>+</p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/2</span>+</p></body></html>", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/32</span>+</p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span>+</p></body></html>", None))
        self.lineEdit_TAF3_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF7_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF9_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/128</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Ac=", None))
        self.lineEdit_TAF5_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF1_tabHE.setText(QCoreApplication.translate("MainWindow", u"24.5", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/8</span>+</p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus [GPa]:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Tip Name:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/4</span>+</p></body></html>", None))
        self.lineEdit_TAF2_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.lineEdit_FrameCompliance_tabHE.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Copy_FrameCompliance_tabHE.setText(QCoreApplication.translate("MainWindow", u"Copy the calculated value", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabHE.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabHE.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabHE.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.pushButton_Publication_LoadDepthCurve_tabHE.setText(QCoreApplication.translate("MainWindow", u"Publication", None))
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.setTabText(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"inclusive of frame stiffness", None))
        self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.setTabText(self.graphicsView_load_depth_tab_exclusive_frame_stiffness_tabHE.indexOf(self.tab_22), QCoreApplication.translate("MainWindow", u"exclusive of frame stiffness", None))
        self.graphicsView_tab_TipAreaFunction_4.setTabText(self.graphicsView_tab_TipAreaFunction_4.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_25), QCoreApplication.translate("MainWindow", u"Hardness-contact depth", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_26), QCoreApplication.translate("MainWindow", u"Hardness-Indents' number", None))
        self.graphicsView_tab_TipAreaFunction_4.setTabText(self.graphicsView_tab_TipAreaFunction_4.indexOf(self.tab_23), QCoreApplication.translate("MainWindow", u"Hardness", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_27), QCoreApplication.translate("MainWindow", u"Young's Modulus-contact depth", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_28), QCoreApplication.translate("MainWindow", u"Young's Modulus-Indents' number", None))
        self.graphicsView_tab_TipAreaFunction_4.setTabText(self.graphicsView_tab_TipAreaFunction_4.indexOf(self.tab_24), QCoreApplication.translate("MainWindow", u"Young's Modulus", None))
        self.graphicsView_tab_TipAreaFunction_4.setTabText(self.graphicsView_tab_TipAreaFunction_4.indexOf(self.tab_46), QCoreApplication.translate("MainWindow", u"H-E", None))
        self.Calculate_tabHE.setText(QCoreApplication.translate("MainWindow", u"Calculate Hardness and Modulus", None))
        self.pushButton_SelectAll_tabHE.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect all ", None))
        ___qtablewidgetitem9 = self.tableWidget_tabHE.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Test Name", None));
        ___qtablewidgetitem10 = self.tableWidget_tabHE.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        self.groupBox_47.setTitle(QCoreApplication.translate("MainWindow", u"Range for calculating mean value", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>min. h<span style=\" vertical-align:sub;\">c</span> [\u00b5m]:</p></body></html>", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>max. h<span style=\" vertical-align:sub;\">c</span> [\u00b5m]:</p></body></html>", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.checkBox_UsingRate2findSurface_tabHE.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.groupBox_65.setTitle(QCoreApplication.translate("MainWindow", u"Options for Big Data", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Level decreasing Data\n"
"Density (only for Plotting)", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Calculate Hardness and Modulus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Hardness and Young's Modulus", None))
        self.pushButton_SelectAll_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect all", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.checkBox_UsingRate2findSurface_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.comboBox_equipment_tabPopIn_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X", None))

        self.comboBox_method_tabPopIn_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabPopIn_FrameStiffness.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabPopIn_FrameStiffness.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        ___qtablewidgetitem11 = self.tableWidget_tabPopIn_FrameStiffness.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Test Name", None));
        ___qtablewidgetitem12 = self.tableWidget_tabPopIn_FrameStiffness.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_37), QCoreApplication.translate("MainWindow", u"inclusive of frame compliance", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_38), QCoreApplication.translate("MainWindow", u"exclusive of frame compliance", None))
        self.graphicsView_tab_TipAreaFunction_6.setTabText(self.graphicsView_tab_TipAreaFunction_6.indexOf(self.tab_36), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.lineEdit_FrameStiffness_tabPopIn_FrameStiffness.setText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Frame Stiffness [mN/\u00b5m]", None))
        self.graphicsView_tab_TipAreaFunction_6.setTabText(self.graphicsView_tab_TipAreaFunction_6.indexOf(self.tab_39), QCoreApplication.translate("MainWindow", u"Frame Compliance", None))
        self.groupBox_58.setTitle(QCoreApplication.translate("MainWindow", u"Calculation Method", None))
        self.groupBox_62.setTitle(QCoreApplication.translate("MainWindow", u"Tip Area Function used by method 2.", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Ac=", None))
        self.lineEdit_TAF1_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"24.5", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">2</span>+</p></body></html>", None))
        self.lineEdit_TAF2_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_TAF6_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Tip Name:", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span>+</p></body></html>", None))
        self.lineEdit_TAF3_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/2</span>+</p></body></html>", None))
        self.lineEdit_TAF4_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/4</span>+</p></body></html>", None))
        self.lineEdit_TAF5_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/8</span>+</p></body></html>", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/16</span>+</p></body></html>", None))
        self.lineEdit_TAF7_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/32</span>+</p></body></html>", None))
        self.lineEdit_TAF8_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/64</span>+</p></body></html>", None))
        self.lineEdit_TAF9_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">c</span><span style=\" vertical-align:super;\">1/128</span></p></body></html>", None))
        self.Copy_TAF_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Copy from \"Tip Area Function\"", None))
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.setItemText(0, QCoreApplication.translate("MainWindow", u"1. Assume constant Hardness and Modulus ( Eq. (24), Oliver 2004)", None))
        self.comboBox_CalculationMethod_tabPopIn_FrameStiffness.setItemText(1, QCoreApplication.translate("MainWindow", u"2. Assume constant Modulus and neglect Pile-up (Eq. (22), Oliver 2004 )", None))

        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"Test for Calculating Frame Compliance", None))
        self.lineEdit_path_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example2\\Tungsten_FrameStiffness.xlsx", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.groupBox_53.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to Calculate Stiffness", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"Range to Calculate Frame Compliance", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"min. Depth [\u00b5m]:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"min. Force [mN]:", None))
        self.pushButton_Calculate_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Calculate Frame Compliance", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabPopIn_FrameStiffness.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_35), QCoreApplication.translate("MainWindow", u"Calculate Frame Compliance", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"Tip", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Tip's Name:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus [GPa]:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Tip Radius [\u00b5m]:", None))
        self.lineEdit_TipName_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"a Berkovich Tip", None))
        self.Copy_TipRadius_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Copy from \"Tip Radius\"", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"Tested Material", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Material's Name:", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Poisson's ratio:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.lineEdit_path_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Examples\\Example2\\Tungsten_TipRadius.xlsx", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"Identify Loading-Holding-UnloadingStart-UnloadingEnd", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"max. Size of fluctuation:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"when (dP/dt) [mN/s] crosses", None))
        self.checkBox_showFindSurface_tab_inclusive_frame_stiffness_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"show find surface", None))
        self.checkBox_iLHU_inclusive_frame_stiffness_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"show the Indentification of Loading-Holding-UnladingStart-UnladingEnd", None))
        self.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.checkBox_showThermalDrift_tab_inclusive_frame_stiffness_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"show thermal drift", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_42), QCoreApplication.translate("MainWindow", u"inclusive of frame compliance", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_43), QCoreApplication.translate("MainWindow", u"exclusive of frame compliance", None))
        self.graphicsView_tab_TipAreaFunction_7.setTabText(self.graphicsView_tab_TipAreaFunction_7.indexOf(self.tab_41), QCoreApplication.translate("MainWindow", u"Load Depth Curve", None))
        self.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Plot the selected Test (by clicking on the test in the \"List of Tests\")", None))
        self.graphicsView_tab_TipAreaFunction_7.setTabText(self.graphicsView_tab_TipAreaFunction_7.indexOf(self.tab_44), QCoreApplication.translate("MainWindow", u"Hertzian fitting", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"+-", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Young's Modulus [GPa]", None))
        self.graphicsView_tab_TipAreaFunction_7.setTabText(self.graphicsView_tab_TipAreaFunction_7.indexOf(self.tab_45), QCoreApplication.translate("MainWindow", u"Calculated Young's Modulus", None))
        self.graphicsView_tab_TipAreaFunction_7.setTabText(self.graphicsView_tab_TipAreaFunction_7.indexOf(self.tab_47), QCoreApplication.translate("MainWindow", u"Pop-in Load", None))
        self.graphicsView_tab_TipAreaFunction_7.setTabText(self.graphicsView_tab_TipAreaFunction_7.indexOf(self.tab_34), QCoreApplication.translate("MainWindow", u"Max. Shear Stress", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"Frame Compliance [\u00b5m/mN]", None))
        self.lineEdit_FrameCompliance_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Copy_FrameCompliance_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Copy the calculated value", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"Find Surface", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Size of data filter:", None))
        self.checkBox_UsingRate2findSurface_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"when dP/dh [mN/\u00b5m] >", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"Test Parameters", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.comboBox_equipment_tabPopIn.setItemText(0, QCoreApplication.translate("MainWindow", u"G200X", None))

        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.comboBox_method_tabPopIn.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Unloading", None))
        self.comboBox_method_tabPopIn.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi Unloadings", None))
        self.comboBox_method_tabPopIn.setItemText(2, QCoreApplication.translate("MainWindow", u"CSM", None))

        self.groupBox_54.setTitle(QCoreApplication.translate("MainWindow", u"Unloading Range to Calculate Stiffnes", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"End [100% of Pmax]:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Start [100% of Pmax]:", None))
        self.pushButton_Analyse_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Analyse Pop-in Effect", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("MainWindow", u"Correct Thermal Drift", None))
        self.checkBox_UsingDriftUnloading_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Use the collection during unloading", None))
        self.pushButton_SelectAll_tabPopIn.setText(QCoreApplication.translate("MainWindow", u"Select/ Unselect all", None))
        ___qtablewidgetitem13 = self.tableWidget_tabPopIn.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Test Name", None));
        ___qtablewidgetitem14 = self.tableWidget_tabPopIn.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Indentify?", None));
        ___qtablewidgetitem15 = self.tableWidget_tabPopIn.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Pop-in?", None));
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_40), QCoreApplication.translate("MainWindow", u"Analyse Pop-in Effect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analysePopIn), QCoreApplication.translate("MainWindow", u"Analyse Pop-in Effect", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Number of Clusters:", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Type the complete paths of files, which were exported using this GUI, to classify their tests:", None))
        self.pushButton_PlotMappingAfterClustering_tabClassification.setText(QCoreApplication.translate("MainWindow", u"Plot mapping after clustering", None))
        self.pushButton_Classify_tabClassification.setText(QCoreApplication.translate("MainWindow", u"Run K-means Clustering", None))
        self.checkBox_ifPlotElbow_tabClassification.setText(QCoreApplication.translate("MainWindow", u"plot Elbow figure", None))
        self.pushButton_PlotMappingWithoutClustering_tabClassification.setText(QCoreApplication.translate("MainWindow", u"Plot mapping without Clustering", None))
        self.checkBox_ifUsingFoundNumberClusters_tabClassification.setText(QCoreApplication.translate("MainWindow", u"determine N using Elbow Method", None))
        ___qtablewidgetitem16 = self.tableWidget_tabClassification.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"#Cluster ", None));
        ___qtablewidgetitem17 = self.tableWidget_tabClassification.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Number of data", None));
        ___qtablewidgetitem18 = self.tableWidget_tabClassification.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"mean of x", None));
        ___qtablewidgetitem19 = self.tableWidget_tabClassification.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"std of x", None));
        ___qtablewidgetitem20 = self.tableWidget_tabClassification.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"mean of y", None));
        ___qtablewidgetitem21 = self.tableWidget_tabClassification.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"std of y", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_48), QCoreApplication.translate("MainWindow", u"K-means Clustering", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpenRecent.setTitle(QCoreApplication.translate("MainWindow", u"Open Recent", None))
    # retranslateUi

