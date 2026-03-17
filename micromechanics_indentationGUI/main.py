#pylint: disable=possibly-used-before-assignment, used-before-assignment

""" Graphical user interface includes all widgets """
import sys
import os
import numpy as np
from PySide6.QtGui import QDesktopServices, QAction, QKeySequence, QShortcut, QIcon # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QFileDialog, QTableWidgetItem # pylint: disable=no-name-in-module
from PySide6.QtCore import QUrl, Qt, QObject,QEvent, QTimer, QCoreApplication, QSize # pylint: disable=no-name-in-module
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar) # pylint: disable=no-name-in-module # from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
from .main_window_ui import Ui_MainWindow
from .DialogExport_ui import Ui_DialogExport
from .DialogSaveAs_ui import Ui_DialogSaveAs
from .DialogOpen_ui import Ui_DialogOpen
from .DialogError_ui import Ui_DialogError
from .DialogAbout_ui import Ui_DialogAbout
from .DialogPathList_ui import Ui_DialogPathList
from .DialogTestList_ui import Ui_DialogTestList
from .DialogWait_ui import Ui_DialogWait
from .Tools4LoadingData import read_file_list
from .__init__ import __version__

os.environ['PYGOBJECT_DISABLE_CAIRO'] = '1'

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow): #pylint: disable=too-many-public-methods
  """ Graphical user interface of MainWindow """
  from .TipRadius import Calculate_TipRadius, plot_Hertzian_fitting
  from .AnalysePopIn import Analyse_PopIn
  from .CalculateHardnessModulus import Calculate_Hardness_Modulus
  from .CalculateCreepRate import Calculate_CreepRate
  from .CalibrateTAF import click_OK_calibration, plot_TAF
  from .Classification import Classification_HE, PlotMappingWithoutClustering, PlotMappingAfterClustering
  from .FrameStiffness import FrameStiffness
  from .load_depth import plot_load_depth, set_aspectRatio, setAsContactSurface, right_click_set_ContactSurface
  from .Tools4GUI import addFile_tab, deleteFile_tab, changeFile_tab, click_pushButton_SelectAll, Select_TypedTest
  from .AnalyseCreep import plot_load_depth_time

  def __init__(self):
    #global setting
    super().__init__()
    self.ui = Ui_MainWindow()
    #find file_path and slash
    file_path = __file__[:-8]
    slash = '\\'
    if '\\' in file_path:
      slash = '\\'
    elif '/' in file_path:
      slash = '/'
    self.file_path = file_path
    self.slash = slash
    #intial the list of recently opened and saved files
    self.RecentFiles =[]
    self.RecentFilesNumber=0
    #shortcut to Save
    shortcut_actionSave = QShortcut(QKeySequence("Ctrl+S"), self)
    shortcut_actionSave.activated.connect(self.directSave)
    #icons
    self.icons_path = f"{self.file_path}{self.slash}pic{self.slash}icons{self.slash}"
    #new
    self.new()

  def set_icon(self, button, icon_name, size=24):
    """
    Set an icon on a Qt button using a file from the icons path.

    Parameters
    ----------
    button : QPushButton or QToolButton
      The button widget on which the icon will be set.
    icon_name : str
      Filename of the icon (including extension), located in `self.icons_path`.
    size : int, optional
      Size of the icon in pixels (width and height). Default is 24.
    """
    icon = QIcon(f"{self.icons_path}{icon_name}")
    icon.addFile(f"{self.icons_path}{icon_name}", QSize(size, size))
    button.setIcon(icon)

  def _init_icons(self):
    icon_groups = {
      "open_in_new_24x24.png": [
        self.ui.pushButton_addFileWindow_tabTAF,
        self.ui.pushButton_addFileWindow_tabHE_FrameStiffness,
        self.ui.pushButton_tableWidgetWindow_tabHE_FrameStiffness,
        self.ui.pushButton_addFileWindow_tabHE,
        self.ui.pushButton_tableWidgetWindow_tabHE,
        self.ui.pushButton_addFileWindow_tabCreep,
        self.ui.pushButton_tableWidgetWindow_tabCreep,
        self.ui.pushButton_addFileWindow_tabCreep_FrameStiffness,
        self.ui.pushButton_tableWidgetWindow_tabCreep_FrameStiffness,
        ],
      "add_24x24.png": [
        self.ui.pushButton_addFile_tabTAF,
        self.ui.pushButton_addFile_tabHE_FrameStiffness,
        self.ui.pushButton_addFile_tabHE,
        self.ui.pushButton_addFile_tabCreep,
        self.ui.pushButton_addFile_tabCreep_FrameStiffness,
        ],
      "edit_24x24.png": [
        self.ui.pushButton_changeFile_tabTAF,
        self.ui.pushButton_changeFile_tabHE_FrameStiffness,
        self.ui.pushButton_changeFile_tabHE,
        self.ui.pushButton_changeFile_tabCreep,
        self.ui.pushButton_changeFile_tabCreep_FrameStiffness,
        ],
      "delete_24x24.png": [
        self.ui.pushButton_deleteFile_tabTAF,
        self.ui.pushButton_deleteFile_tabHE_FrameStiffness,
        self.ui.pushButton_deleteFile_tabHE,
        self.ui.pushButton_deleteFile_tabCreep,
        self.ui.pushButton_deleteFile_tabCreep_FrameStiffness,
      ],
    }
    for icon, buttons in icon_groups.items():
      for button in buttons:
        self.set_icon(button, icon)

  def get_current_tab_name(self):
    """ get the name of the current tabWidget """
    current_widget = self.ui.tabAll.currentWidget()
    if '0' in current_widget.objectName():
      current_current_widget = eval(f"self.ui.tabWidget_{current_widget.objectName()[3:-2]}.currentWidget()") #pylint: disable=eval-used
    else:
      current_current_widget = current_widget
    return current_current_widget.objectName()

  def new(self):
    """ initial settings """
    self.ui.setupUi(self)
    #icons
    self._init_icons()
    #initial the Path for saving
    self.Folder_SAVED = 'type or selcet the path of a folder'
    self.FileName_SAVED = 'give an arbitrary file name (with or without an arbitrary file extension)'
    #intial the list of recently opened and saved files
    self.RecentFiles =[]
    self.RecentFilesNumber=0
    #clicked.connect in tabTAF
    self.ui.pushButton_addFile_tabTAF.clicked.connect(lambda: self.addFile_tab(tabName='tabTAF'))
    self.ui.pushButton_deleteFile_tabTAF.clicked.connect(lambda: self.deleteFile_tab(tabName='tabTAF'))
    self.ui.pushButton_changeFile_tabTAF.clicked.connect(lambda: self.changeFile_tab(tabName='tabTAF'))
    self.ui.OK_path_tabTAF.clicked.connect(self.click_OK_calibration)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabTAF'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabTAF', If_inclusive_frameStiffness='exclusive'))
    self.ui.pushButton_SelectAll_tabTAF.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabTAF'))
    #clicked.connect in tabTipRadius
    self.ui.pushButton_Calculate_tabTipRadius_FrameStiffness.clicked.connect(lambda: self.click_pushButton_Calculate(tabName = 'tabTipRadius', what = 'FrameStiffness'))
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabTipRadius_FrameStiffness')) # pylint: disable=line-too-long
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabTipRadius_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabTipRadius_FrameStiffness', If_inclusive_frameStiffness='exclusive')) # pylint: disable=line-too-long
    self.ui.Copy_FrameCompliance_tabTipRadius.clicked.connect(lambda: self.Copy_FrameCompliance(tabName='tabTipRadius'))
    self.ui.Copy_TAF_tabTipRadius_FrameStiffness.clicked.connect(lambda: self.Copy_TAF(tabName='tabTipRadius_FrameStiffness', If_complete=False))
    self.ui.pushButton_Calculate_tabTipRadius.clicked.connect(self.Calculate_TipRadius)
    self.ui.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.clicked.connect(self.click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.clicked.connect(lambda: self.plot_load_depth(tabName='tabTipRadius'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabTipRadius.clicked.connect(lambda: self.plot_load_depth(tabName='tabTipRadius', If_inclusive_frameStiffness='exclusive'))
    self.ui.pushButton_SelectAll_tabTipRadius.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabTipRadius'))
    self.ui.pushButton_SelectAll_tabTipRadius_FrameStiffness.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabTipRadius_FrameStiffness'))
    self.ui.pushButton_select_tabTipRadius.clicked.connect(self.selectFile_tabTipRadius)
    self.ui.pushButton_select_tabTipRadius_FrameStiffness.clicked.connect(self.selectFile_tabTipRadius_FrameStiffness)
    #clicked.connect in tabHE
    self.ui.pushButton_SelectTypedTest_tabHE.clicked.connect(lambda: self.Select_TypedTest(tabName = 'tabHE'))
    self.ui.pushButton_SelectTypedTest_tabHE_FrameStiffness.clicked.connect(lambda: self.Select_TypedTest(tabName = 'tabHE_FrameStiffness'))
    self.ui.pushButton_Calculate_tabHE_FrameStiffness.clicked.connect(lambda: self.click_pushButton_Calculate(tabName='tabHE_FrameStiffness', what = 'FrameStiffness'))
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabHE_FrameStiffness'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabHE_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabHE_FrameStiffness', If_inclusive_frameStiffness='exclusive'))# pylint: disable=line-too-long
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.clicked.connect(lambda: self.plot_load_depth(tabName='tabHE'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabHE.clicked.connect(lambda: self.plot_load_depth(tabName='tabHE', If_inclusive_frameStiffness='exclusive'))
    self.ui.Copy_TAF_tabHE.clicked.connect(lambda: self.Copy_TAF(tabName='tabHE'))
    self.ui.Copy_FrameCompliance_tabHE.clicked.connect(lambda: self.Copy_FrameCompliance(tabName='tabHE'))
    self.ui.Copy_TAF_tabHE_FrameStiffness.clicked.connect(lambda: self.Copy_TAF(tabName='tabHE_FrameStiffness', If_complete=False))
    self.ui.Calculate_tabHE.clicked.connect(lambda: self.click_pushButton_Calculate(tabName = 'tabHE', what = 'Hardness_Modulus'))
    self.ui.pushButton_SelectAll_tabHE.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabHE'))
    self.ui.pushButton_SelectAll_tabHE_FrameStiffness.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabHE_FrameStiffness'))
    self.ui.pushButton_addFile_tabHE.clicked.connect(lambda: self.addFile_tab(tabName='tabHE'))
    self.ui.pushButton_addFile_tabHE_FrameStiffness.clicked.connect(lambda: self.addFile_tab(tabName='tabHE_FrameStiffness'))
    self.ui.pushButton_deleteFile_tabHE.clicked.connect(lambda: self.deleteFile_tab(tabName='tabHE'))
    self.ui.pushButton_deleteFile_tabHE_FrameStiffness.clicked.connect(lambda: self.deleteFile_tab(tabName='tabHE_FrameStiffness'))
    self.ui.pushButton_changeFile_tabHE.clicked.connect(lambda: self.changeFile_tab(tabName='tabHE'))
    self.ui.pushButton_changeFile_tabHE_FrameStiffness.clicked.connect(lambda: self.changeFile_tab(tabName='tabHE_FrameStiffness'))
    #clicked.connect in tabCreep
    self.ui.pushButton_SelectTypedTest_tabCreep.clicked.connect(lambda: self.Select_TypedTest(tabName='tabCreep'))
    self.ui.pushButton_SelectTypedTest_tabCreep_FrameStiffness.clicked.connect(lambda: self.Select_TypedTest(tabName='tabCreep_FrameStiffness'))
    self.ui.pushButton_Calculate_tabCreep_FrameStiffness.clicked.connect(lambda: self.click_pushButton_Calculate(tabName = 'tabCreep_FrameStiffness', what = 'FrameStiffness'))
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabCreep_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabCreep_FrameStiffness'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabCreep_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabCreep_FrameStiffness', If_inclusive_frameStiffness='exclusive'))# pylint: disable=line-too-long
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabCreep.clicked.connect(lambda: self.plot_load_depth(tabName='tabCreep'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabCreep.clicked.connect(lambda: self.plot_load_depth(tabName='tabCreep', If_inclusive_frameStiffness='exclusive'))
    self.ui.pushButton_plot_chosen_test_DepthTime_exclusive_frame_stiffness_tabCreep.clicked.connect(lambda: self.plot_load_depth_time(tabName='tabCreep', If_inclusive_frameStiffness='exclusive'))
    self.ui.Copy_TAF_tabCreep.clicked.connect(lambda: self.Copy_TAF(tabName='tabCreep'))
    self.ui.Copy_FrameCompliance_tabCreep.clicked.connect(lambda: self.Copy_FrameCompliance(tabName='tabCreep'))
    self.ui.Copy_TAF_tabCreep_FrameStiffness.clicked.connect(lambda: self.Copy_TAF(tabName='tabCreep_FrameStiffness', If_complete=False))
    self.ui.Calculate_tabCreep.clicked.connect(lambda: self.click_pushButton_Calculate(tabName = 'tabCreep', what = 'CreepRate'))
    self.ui.pushButton_SelectAll_tabCreep.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabCreep'))
    self.ui.pushButton_SelectAll_tabCreep_FrameStiffness.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabCreep_FrameStiffness'))
    self.ui.pushButton_addFile_tabCreep.clicked.connect(lambda: self.addFile_tab(tabName='tabCreep'))
    self.ui.pushButton_addFile_tabCreep_FrameStiffness.clicked.connect(lambda: self.addFile_tab(tabName='tabCreep_FrameStiffness'))
    self.ui.pushButton_deleteFile_tabCreep.clicked.connect(lambda: self.deleteFile_tab(tabName='tabCreep'))
    self.ui.pushButton_deleteFile_tabCreep_FrameStiffness.clicked.connect(lambda: self.deleteFile_tab(tabName='tabCreep_FrameStiffness'))
    self.ui.pushButton_changeFile_tabCreep.clicked.connect(lambda: self.changeFile_tab(tabName='tabCreep'))
    self.ui.pushButton_changeFile_tabCreep_FrameStiffness.clicked.connect(lambda: self.changeFile_tab(tabName='tabCreep_FrameStiffness'))
    #clicked.connect in tabPopIn
    self.ui.pushButton_Analyse_tabPopIn.clicked.connect(self.Analyse_PopIn)
    self.ui.pushButton_Calculate_tabPopIn_FrameStiffness.clicked.connect(lambda: self.click_pushButton_Calculate(tabName = 'tabPopIn', what = 'FrameStiffness'))
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabPopIn_FrameStiffness')) # pylint: disable=line-too-long
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness.clicked.connect(lambda: self.plot_load_depth(tabName='tabPopIn_FrameStiffness', If_inclusive_frameStiffness='exclusive')) # pylint: disable=line-too-long
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn.clicked.connect(lambda: self.plot_load_depth(tabName='tabPopIn'))
    self.ui.pushButton_plot_chosen_test_tab_exclusive_frame_stiffness_tabPopIn.clicked.connect(lambda: self.plot_load_depth(tabName='tabPopIn', If_inclusive_frameStiffness='exclusive'))
    self.ui.Copy_TipRadius_tabPopIn.clicked.connect(self.Copy_TipRadius)
    self.ui.Copy_FrameCompliance_tabPopIn.clicked.connect(lambda: self.Copy_FrameCompliance(tabName='tabPopIn'))
    self.ui.Copy_TAF_tabPopIn_FrameStiffness.clicked.connect(lambda: self.Copy_TAF(tabName='tabPopIn_FrameStiffness', If_complete=False))
    self.ui.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn.clicked.connect(self.click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn)
    self.ui.pushButton_SelectAll_tabPopIn.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabPopIn'))
    self.ui.pushButton_SelectAll_tabPopIn_FrameStiffness.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName='tabPopIn_FrameStiffness'))
    self.ui.pushButton_select_tabPopIn.clicked.connect(self.selectFile_tabPopIn)
    self.ui.pushButton_select_tabPopIn_FrameStiffness.clicked.connect(self.selectFile_tabPopIn_FrameStiffness)
    #clicked.connect in tabClassification
    self.ui.pushButton_Classify_tabClassification.clicked.connect(self.click_pushButton_Classify_tabClassification)
    self.ui.pushButton_PlotMappingWithoutClustering_tabClassification.clicked.connect(self.click_pushButton_PlotMappingWithoutClustering_tabClassification)
    self.ui.pushButton_PlotMappingAfterClustering_tabClassification.clicked.connect(self.click_pushButton_PlotMappingAfterClustering_tabClassification)
    #clicked.connect to new
    self.ui.actionNew.triggered.connect(self.reNew_windows)
    #clicked.connect in DialogExport
    self.ui.actionExport.triggered.connect(self.show_DialogExport)
    #clicked.connect to DialogSaveAs
    self.ui.actionSaveAs.triggered.connect(self.show_DialogSaveAs)
    #clicked.connect to Save
    self.ui.actionSave.triggered.connect(self.directSave)
    #clicked.connect to DialogOpen
    self.ui.actionLoad.triggered.connect(self.show_DialogOpen)
    #clicked.connect to DialogAbout
    self.ui.actionAbout.triggered.connect(self.show_DialogAbout)
    #clicked.connect to Document
    self.ui.actionDocument.triggered.connect(self.openDocument)
    #clicked.connect to DialogPathList in tabTAF
    self.ui.pushButton_addFileWindow_tabTAF.clicked.connect(lambda: self.show_DialogPathList(tabName='tabTAF'))
    #clicked.connect to DialogPathList in tabHE_FrameStiffness
    self.ui.pushButton_addFileWindow_tabHE_FrameStiffness.clicked.connect(lambda: self.show_DialogPathList(tabName='tabHE_FrameStiffness'))
    #clicked.connect to DialogTestList in tabHE_FrameStiffness
    self.ui.pushButton_tableWidgetWindow_tabHE_FrameStiffness.clicked.connect(lambda: self.show_DialogTestList(tabName='tabHE_FrameStiffness'))
    #clicked.connect to DialogPathList in tabHE
    self.ui.pushButton_addFileWindow_tabHE.clicked.connect(lambda: self.show_DialogPathList(tabName='tabHE'))
    #clicked.connect to DialogTestList in tabHE
    self.ui.pushButton_tableWidgetWindow_tabHE.clicked.connect(lambda: self.show_DialogTestList(tabName='tabHE'))
    #clicked.connect to DialogPathList in tabCreep_FrameStiffness
    self.ui.pushButton_addFileWindow_tabCreep_FrameStiffness.clicked.connect(lambda: self.show_DialogPathList(tabName='tabCreep_FrameStiffness'))
    #clicked.connect to DialogTestList in tabCreep_FrameStiffness
    self.ui.pushButton_tableWidgetWindow_tabCreep_FrameStiffness.clicked.connect(lambda: self.show_DialogTestList(tabName='tabCreep_FrameStiffness'))
    #clicked.connect to DialogPathList in tabCreep
    self.ui.pushButton_addFileWindow_tabCreep.clicked.connect(lambda: self.show_DialogPathList(tabName='tabCreep'))
    #clicked.connect to DialogTestList in tabCreep
    self.ui.pushButton_tableWidgetWindow_tabCreep.clicked.connect(lambda: self.show_DialogTestList(tabName='tabCreep'))

    #initializing variables for collecting analysed results
    self.tabHE_hc_collect=[]
    self.tabHE_Pmax_collect=[]
    self.tabHE_H_collect=[]
    self.tabHE_E_collect=[]
    self.tabHE_testName_collect=[]
    self.tabCreep_hc_collect=[]
    self.tabCreep_Pmax_collect=[]
    self.tabCreep_H_collect=[]
    self.tabCreep_E_collect=[]
    self.tabCreep_testName_collect=[]
    self.canvas_dict = {}
    self.ax_dict = {}

    #graphicsView
    graphicsView_list = [ 'load_depth_tab_inclusive_frame_stiffness_tabTAF',
                          'load_depth_tab_exclusive_frame_stiffness_tabTAF',
                          'FrameStiffness_tabTAF',                                #Framestiffness_TabTAF
                          'TAF_tabTAF',
                          'load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness',
                          'load_depth_tab_exclusive_frame_stiffness_tabTipRadius_FrameStiffness',
                          'tabTipRadius_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness',
                          'load_depth_tab_exclusive_frame_stiffness_tabPopIn_FrameStiffness',
                          'tabPopIn_FrameStiffness',
                          'tabHE_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness',
                          'load_depth_tab_exclusive_frame_stiffness_tabHE_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabHE',
                          'load_depth_tab_exclusive_frame_stiffness_tabHE',
                          'H_hc_tabHE',
                          'H_h_tabHE',
                          'H_Index_tabHE',
                          'E_hc_tabHE',
                          'E_h_tabHE',
                          'HE2_hc_tabHE',
                          'E_Index_tabHE',
                          'HE_tabHE',
                          'tabCreep_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabCreep_FrameStiffness',
                          'load_depth_tab_exclusive_frame_stiffness_tabCreep_FrameStiffness',
                          'load_depth_time_tab_inclusive_frame_stiffness_tabCreep',
                          'load_depth_time_tab_exclusive_frame_stiffness_tabCreep',
                          'load_depth_tab_inclusive_frame_stiffness_tabCreep',
                          'load_depth_tab_exclusive_frame_stiffness_tabCreep',
                          'H_hc_tabCreep',
                          'H_Index_tabCreep',
                          'E_hc_tabCreep',
                          'HE2_hc_tabCreep',
                          'E_Index_tabCreep',
                          'HE_tabCreep',
                          'CreepRate_tabCreep',
                          'load_depth_tab_inclusive_frame_stiffness_tabTipRadius',
                          'load_depth_tab_exclusive_frame_stiffness_tabTipRadius',
                          'HertzianFitting_tabTipRadius',
                          'CalculatedTipRadius_tabTipRadius',
                          'load_depth_tab_inclusive_frame_stiffness_tabPopIn',
                          'load_depth_tab_exclusive_frame_stiffness_tabPopIn',
                          'HertzianFitting_tabPopIn',
                          'E_tabPopIn',
                          'maxShearStress_tabPopIn',
                          'PopInLoad_tabPopIn',
                          'HE_tabClassification',
                          ]
    for graphicsView in graphicsView_list:
      self.matplotlib_canve_ax(graphicsView=graphicsView)
    #define path for Examples
    file_path = self.file_path
    slash = self.slash
    self.ui.lineEdit_path_tabTipRadius_FrameStiffness.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_FrameStiffness.xlsx")
    self.ui.lineEdit_path_tabPopIn_FrameStiffness.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_FrameStiffness.xlsx")
    self.ui.lineEdit_path_tabTipRadius.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_TipRadius.xlsx")
    self.ui.lineEdit_path_tabPopIn.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_TipRadius.xlsx")
    # tabTAF
    theTableWidget = self.ui.tableWidget_path_tabTAF
    qtablewidgetitem = QTableWidgetItem(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    qtablewidgetitem.setCheckState(Qt.Checked)
    theTableWidget.setVerticalHeaderItem(0, QTableWidgetItem(f"Path{int(1)}"))
    theTableWidget.setItem(0, 0, qtablewidgetitem)
    # tabHE
    theTableWidget = self.ui.tableWidget_path_tabHE
    qtablewidgetitem = QTableWidgetItem(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    qtablewidgetitem.setCheckState(Qt.Checked)
    theTableWidget.setVerticalHeaderItem(0, QTableWidgetItem(f"Path{int(1)}"))
    theTableWidget.setItem(0, 0, qtablewidgetitem)
    # tabHE_FrameStiffness
    theTableWidget = self.ui.tableWidget_path_tabHE_FrameStiffness
    qtablewidgetitem = QTableWidgetItem(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    qtablewidgetitem.setCheckState(Qt.Checked)
    theTableWidget.setVerticalHeaderItem(0, QTableWidgetItem(f"Path{int(1)}"))
    theTableWidget.setItem(0, 0, qtablewidgetitem)
    # tabCreep
    theTableWidget = self.ui.tableWidget_path_tabCreep
    qtablewidgetitem = QTableWidgetItem(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    qtablewidgetitem.setCheckState(Qt.Checked)
    theTableWidget.setVerticalHeaderItem(0, QTableWidgetItem(f"Path{int(1)}"))
    theTableWidget.setItem(0, 0, qtablewidgetitem)
    # tabCreep_FrameStiffness
    theTableWidget = self.ui.tableWidget_path_tabCreep_FrameStiffness
    qtablewidgetitem = QTableWidgetItem(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    qtablewidgetitem.setCheckState(Qt.Checked)
    theTableWidget.setVerticalHeaderItem(0, QTableWidgetItem(f"Path{int(1)}"))
    theTableWidget.setItem(0, 0, qtablewidgetitem)

  def show_DialogExport(self): #pylint: disable=no-self-use
    """ showing dialog window for exporting results """
    if window_DialogExport.isVisible():
      window_DialogExport.close()
    window_DialogExport.renewFilePath()
    window_DialogExport.show()


  def show_DialogSaveAs(self): #pylint: disable=no-self-use
    """ showing dialog window for saving file """
    if window_DialogSaveAs.isVisible():
      window_DialogSaveAs.close()
    window_DialogSaveAs.ui.lineEdit_SaveAsFileName.setText(self.FileName_SAVED)
    window_DialogSaveAs.ui.lineEdit_SaveAsFolder.setText(self.Folder_SAVED)
    window_DialogSaveAs.show()


  def show_DialogOpen(self): #pylint: disable=no-self-use
    """ showing dialog window for openning file """
    if window_DialogOpen.isVisible():
      window_DialogOpen.close()
    window_DialogOpen.ui.lineEdit_OpenFileName.setText(self.FileName_SAVED)
    window_DialogOpen.ui.lineEdit_OpenFolder.setText(self.Folder_SAVED)
    window_DialogOpen.show()

  def show_DialogPathList(self, tabName): #pylint: disable=no-self-use
    """ showing window for path list """
    dlg = window_DialogPathList  # your existing QDialog
    theTableWidget = eval(f"self.ui.tableWidget_path_{tabName}") # pylint: disable = eval-used
    dlg.OriginalTableWidget = theTableWidget
    dlg.FilesToDialog_tab()

    if dlg.isVisible():
      dlg.raise_()
      dlg.activateWindow()
      return

    dlg.setParent(self, Qt.Dialog)
    dlg.setWindowModality(Qt.NonModal)
    # dlg.setWindowModality(Qt.ApplicationModal)
    dlg.setWindowFlag(Qt.WindowStaysOnTopHint, True)

    self._flash = RaiseAndFlash(dlg) #pylint: disable=attribute-defined-outside-init
    dlg.installEventFilter(self._flash)
    dlg.finished.connect(lambda *_: dlg.removeEventFilter(self._flash))
    dlg.exec()

  def show_DialogTestList(self, tabName): #pylint: disable=no-self-use
    """ showing window for path list """
    dlg = window_DialogTestList  # your existing QDialog
    theTableWidget = getattr(self.ui, f"tableWidget_{tabName}")
    dlg.OriginalTableWidget = theTableWidget
    dlg.FilesToDialog_tab()
    thePlainTextWidget = getattr(self.ui, f"plainTextEdit_SelectTypedTest_{tabName}")
    dlg.OriginalPlainTextWidget = thePlainTextWidget
    dlg.PlainTextToDialog_tab()

    if dlg.isVisible():
      dlg.raise_()
      dlg.activateWindow()
      return

    dlg.setParent(self, Qt.Dialog)
    dlg.setWindowModality(Qt.NonModal)
    # dlg.setWindowModality(Qt.ApplicationModal)
    dlg.setWindowFlag(Qt.WindowStaysOnTopHint, True)

    self._flash = RaiseAndFlash(dlg) #pylint: disable=attribute-defined-outside-init
    dlg.installEventFilter(self._flash)
    dlg.finished.connect(lambda *_: dlg.removeEventFilter(self._flash))
    dlg.exec()

  def show_DialogAbout(self): #pylint: disable=no-self-use
    """ showing dialog window for About """
    if window_DialogAbout.isVisible():
      window_DialogAbout.close()
    file_path = window.file_path
    slash = window.slash
    file_path_UpdateNote = fr"{file_path}{slash}UpdateNote.txt"
    UpdateNote = open(file_path_UpdateNote, "r", encoding="utf-8").read()
    message_in_about=f"Version: {__version__}\n\n"
    message_in_about=message_in_about + "====================Update Note======================\n\n"
    message_in_about=message_in_about + UpdateNote
    window_DialogAbout.print_about(message_in_about)
    window_DialogAbout.show()

  def openDocument(self): #pylint: disable=no-self-use
    """ open document """
    # Define the URL
    URL = "https://micromechanics.github.io/indentationGUI/"
    url = QUrl(URL)
    # Open the URL in the default web browser
    QDesktopServices.openUrl(url)


  def matplotlib_canve_ax(self,graphicsView): #pylint: disable=no-self-use
    """
    define canvas and ax

    Args:
    graphicsView (string): the name of graphicsView defined in Qtdesigner
    """
    layout = eval(f"QVBoxLayout(self.ui.graphicsView_{graphicsView})") #pylint: disable=eval-used disable=unused-variable
    exec(f"self.static_canvas_{graphicsView} = FigureCanvas(Figure(figsize=(8, 6)))") #pylint: disable=exec-used
    exec(f"layout.addWidget(NavigationToolbar(self.static_canvas_{graphicsView}, self))") #pylint: disable=exec-used
    exec(f"layout.addWidget(self.static_canvas_{graphicsView})") #pylint: disable=exec-used
    canvas = eval(f"self.static_canvas_{graphicsView}") #pylint: disable=eval-used
    if graphicsView in ('CalculatedTipRadius_tabTipRadius'):
      canva = getattr(self,f"static_canvas_{graphicsView}")
      ax = canva.figure.subplots(2,1)
      setattr(self, f"static_ax_{graphicsView}", ax)
    elif 'load_depth_time' in graphicsView:
      canva = getattr(self,f"static_canvas_{graphicsView}")
      ax = canva.figure.subplots(3,1,sharex=True, gridspec_kw={'hspace':0.05, 'height_ratios':[1, 2, 2]})
      setattr(self, f"static_ax_{graphicsView}", ax)
    elif ('load_depth' in graphicsView) or ('FrameStiffness' in graphicsView)  or (graphicsView in ('TAF_tabTAF')):
      canva = getattr(self,f"static_canvas_{graphicsView}")
      ax = canva.figure.subplots(2,1,sharex=True, gridspec_kw={'hspace':0, 'height_ratios':[4, 1]})
      setattr(self, f"static_ax_{graphicsView}", ax)
    elif 'CreepRate' in graphicsView:
      canva = getattr(self,f"static_canvas_{graphicsView}")
      ax = canva.figure.subplots(2,1,sharex=True, sharey=True, gridspec_kw={'hspace':0.05, 'height_ratios':[1, 1]})
      setattr(self, f"static_ax_{graphicsView}", ax)
    else:
      canva = getattr(self,f"static_canvas_{graphicsView}")
      ax = canva.figure.subplots()
      setattr(self, f"static_ax_{graphicsView}", ax)
    self.canvas_dict.update({f"{graphicsView}":canvas})
    self.ax_dict.update({f"{graphicsView}":ax})

  def Copy_FrameCompliance(self,tabName='tabHE'):
    """ get the calibrated frame compliance """
    theLineEdit = getattr(self.ui, f"lineEdit_FrameCompliance_{tabName}")
    theLineEdit_FrameStiffness = getattr(self.ui, f"lineEdit_FrameCompliance_{tabName}_FrameStiffness")
    theLineEdit.setText(theLineEdit_FrameStiffness.text())

  def Copy_TAF(self,tabName='tabHE', If_complete=True):
    """ get the calibrated tip are function from the tabTAF """
    theLineEdit = getattr(self.ui, f"lineEdit_TipName_{tabName}")
    theLineEdit.setText(self.ui.lineEdit_TipName_tabTAF.text())
    if If_complete:
      thedoubleSpinBox_E_Tip = getattr(self.ui, f"doubleSpinBox_E_Tip_{tabName}")
      thedoubleSpinBox_E_Tip.setValue(self.ui.doubleSpinBox_E_Tip_tabTAF.value())
      thedoubleSpinBox_Poisson_Tip = getattr(self.ui, f"doubleSpinBox_Poisson_Tip_{tabName}")
      thedoubleSpinBox_Poisson_Tip.setValue(self.ui.doubleSpinBox_Poisson_Tip_tabTAF.value())
    for j in range(9):
      lineEdit = getattr(self.ui, f"lineEdit_TAF{j+1}_{tabName}")
      theLineEdit_tabTAF = getattr(self.ui, f"lineEdit_TAF{j+1}_tabTAF")
      lineEdit.setText(theLineEdit_tabTAF.text())

  def click_pushButton_Calculate(self,tabName='tabHE_FrameStiffness', what='FrameStiffness'):
    """ calculate the values """
    if what == 'FrameStiffness':
      self.FrameStiffness(tabName=tabName)
    elif what == 'Hardness_Modulus':
      self.Calculate_Hardness_Modulus()
    elif what == 'CreepRate':
      self.Calculate_CreepRate()

  # def selectFile_tabHE_FrameStiffness(self):
  #   """ click "select" Button to select a file path for tabHE_FrameStiffness  """
  #   file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
  #   if file != '':
  #     self.ui.lineEdit_path_tabHE_FrameStiffness.setText(file)

  # def selectFile_tabHE(self):
  #   """ click "select" Button to select a file path for tabHE  """
  #   file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
  #   if file != '':
  #     self.ui.lineEdit_path_tabHE.setText(file)

  def Copy_TipRadius(self):
    """ get the calibrated tip radius from the tabTipRadius """
    self.ui.lineEdit_TipName_tabPopIn.setText(self.ui.lineEdit_TipName_tabTipRadius.text())
    self.ui.doubleSpinBox_E_Tip_tabPopIn.setValue(self.ui.doubleSpinBox_E_Tip_tabTipRadius.value())
    self.ui.doubleSpinBox_Poisson_Tip_tabPopIn.setValue(self.ui.doubleSpinBox_Poisson_Tip_tabTipRadius.value())
    self.ui.doubleSpinBox_TipRadius_tabPopIn.setValue(float(self.ui.lineEdit_TipRadius_tabTipRadius.text()))

  def click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn(self):
    """ plot the Hertzian fitting curves of the chosen tests in tabPopIn """
    self.plot_Hertzian_fitting(tabName='tabPopIn')

  def click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius(self):
    """ plot the Hertzian fitting curves of the chosen tests in tabTipRadius """
    self.plot_Hertzian_fitting(tabName='tabTipRadius')

  def click_pushButton_Classify_tabClassification(self):
    """ perform classification """
    self.Classification_HE()

  def click_pushButton_PlotMappingWithoutClustering_tabClassification(self):
    """ plot mapping without clustering """
    self.PlotMappingWithoutClustering()

  def click_pushButton_PlotMappingAfterClustering_tabClassification(self):
    """ plot mapping After clustering """
    self.PlotMappingAfterClustering()

  def selectFile_tabTAF(self):
    """ click "select" Button to select a file path for tabTAF  """
    file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
    if file != '':
      self.ui.lineEdit_path_tabTAF.setText(file)

  def selectFile_tabTipRadius_FrameStiffness(self):
    """ click "select" Button to select a file path for tabTipRadius_FrameStiffness  """
    file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
    if file != '':
      self.ui.lineEdit_path_tabTipRadius_FrameStiffness.setText(file)

  def selectFile_tabTipRadius(self):
    """ click "select" Button to select a file path for tabTipRadius  """
    file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
    if file != '':
      self.ui.lineEdit_path_tabTipRadius.setText(file)

  def selectFile_tabPopIn_FrameStiffness(self):
    """ click "select" Button to select a file path for tabPopIn_FrameStiffness  """
    file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
    if file != '':
      self.ui.lineEdit_path_tabPopIn_FrameStiffness.setText(file)

  def selectFile_tabPopIn(self):
    """ click "select" Button to select a file path for tabPopIn  """
    file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
    if file != '':
      self.ui.lineEdit_path_tabPopIn.setText(file)

  def directSave(self):
    """ Save the current file directly to its original path """
    window_DialogSaveAs.ui.lineEdit_SaveAsFileName.setText(self.FileName_SAVED)
    window_DialogSaveAs.ui.lineEdit_SaveAsFolder.setText(self.Folder_SAVED)
    window_DialogSaveAs.go2Save()


  def update_OpenRecent(self):
    """ update the list of recently opened files """
    for idex, file_name in enumerate(self.RecentFiles):
      if idex>5:
        break
      if '\n' in file_name:
        file_name = file_name[:-1]
        self.RecentFiles[idex] = self.RecentFiles[idex][:-1]
      if idex+1 >self.RecentFilesNumber:
        actionOpenRecent = QAction(self)
        self.ui.menuOpenRecent.addAction(actionOpenRecent)
        self.RecentFilesNumber += 1
        actionOpenRecent.setObjectName(f"actionOpenRecent{idex}")
        actionOpenRecent.setText(QCoreApplication.translate("MainWindow", file_name, None))
        exec(f"self.ui.actionOpenRecent{idex} = actionOpenRecent") # pylint: disable = exec-used
        exec(f"self.ui.actionOpenRecent{idex}.triggered.connect(window_DialogOpen.openUsingOpenRecent{idex})") # pylint: disable = exec-used
      else:
        actionOpenRecent = eval(f"self.ui.actionOpenRecent{idex}") # pylint: disable = eval-used
        actionOpenRecent.setText(QCoreApplication.translate("MainWindow", file_name, None))


  def reNew_windows(self):
    """ newly perform intial settings """
    #save RecentFiles
    file_RecentFiles = open(f"{self.file_path}{self.slash}RecentFiles.txt",'w', encoding="utf-8") #pylint: disable=consider-using-with
    for idex, RecentFile in enumerate(self.RecentFiles):
      if idex>10:
        break
      if '\n' in RecentFile:
        file_RecentFiles.write(RecentFile)
      else:
        file_RecentFiles.write(RecentFile+'\n')
    file_RecentFiles.close()
    #new
    self.new()
    #read the list of recently opened files
    try:
      file_RecentFiles = open(f"{window.file_path}{window.slash}RecentFiles.txt", 'r', encoding="utf-8") #pylint: disable=consider-using-with
    except:
      print(f"**ERROR: cannot open {window.file_path}{window.slash}RecentFiles.txt")
    else:
      self.RecentFiles = file_RecentFiles.readlines()
      self.update_OpenRecent()
      file_RecentFiles.close()


  def closeEvent(self, event):
    """ close other windiows when the main window is closed """
    #save RecentFiles
    file_RecentFiles = open(f"{self.file_path}{self.slash}RecentFiles.txt",'w', encoding="utf-8") #pylint: disable=consider-using-with
    for idex, RecentFile in enumerate(self.RecentFiles):
      if idex>10:
        break
      if '\n' in RecentFile:
        file_RecentFiles.write(RecentFile)
      else:
        file_RecentFiles.write(RecentFile+'\n')
    file_RecentFiles.close()
    #close all windows
    for theWindow in QApplication.topLevelWidgets():
      theWindow.close()

  def show_error(self, message, suggestion=' '): #pylint: disable=no-self-use
    """ show the dialog showing error and suggestion """
    window_DialogError.print_error(message, suggestion)
    window_DialogError.show()

  def show_About(self, message): #pylint: disable=no-self-use
    """ show the dialog showing About """
    window_DialogError.print_error(message)
    window_DialogError.show()

  def show_wait(self, info=' '): #pylint: disable=no-self-use
    """ show the dialog showing waiting info """
    window_DialogWait.setWindowTitle('Waiting ... ... :)  '+info)
    window_DialogWait.show()

  def close_wait(self, info=False): #pylint: disable=no-self-use
    """ clsoe the dialog showing waiting info """
    if info:
      window_DialogWait.setWindowTitle('Done!')
      window_DialogWait.print_wait(info)
    else:
      window_DialogWait.close()


class DialogExport(QDialog):
  """ Graphical user interface of Dialog used to export calculated results """
  from .Export import export

  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogExport()
    self.ui.setupUi(self)
    if self.ui.comboBox_ExportTab.currentIndex()==0:
      #set default file name und folder path for tabHE
      try:
        tab_path = read_file_list(window.ui.tableWidget_path_tabHE)[0]
      except:
        tab_path = ''
      slash = '\\'
      if '\\' in tab_path:
        slash = '\\'
      elif '/' in tab_path:
        slash = '/'
      Default_File_Name = tab_path[tab_path.rfind(slash)+1:tab_path.rfind('.')] + '_tabHE_output.xlsx'
      Default_Folder_Path = tab_path[:tab_path.rfind(slash)]
      self.ui.lineEdit_ExportFileName.setText(Default_File_Name)
      self.ui.lineEdit_ExportFolder.setText(Default_Folder_Path)
    self.ui.comboBox_ExportTab.currentIndexChanged.connect(self.renewFilePath)
    self.ui.pushButton_selectPath.clicked.connect(self.selectPath)
    self.ui.pushButton_OK.clicked.connect(self.go2export)

  def renewFilePath(self):
    """renew the file path after selecting the tab"""
    if self.ui.comboBox_ExportTab.currentIndex()==0:
      tabName='tabHE'
      self.ui.comboBox_ExportFormat.setCurrentIndex(1)
    elif self.ui.comboBox_ExportTab.currentIndex()==1:
      tabName='tabPopIn'
      self.ui.comboBox_ExportFormat.setCurrentIndex(1)
    elif self.ui.comboBox_ExportTab.currentIndex()==2:
      tabName='tabClassification'
      self.ui.comboBox_ExportFormat.setCurrentIndex(1)
      files_list = (window.ui.textEdit_Files_tabClassification.toPlainText()).split("\n")
    #set default file name und folder path for {tabName}
    if tabName == 'tabClassification':
      tab_path = files_list[0]
    else:
      tab_path = eval(f"window.ui.lineEdit_path_{tabName}.text()") # pylint: disable=eval-used
    slash = '\\'
    if '\\' in tab_path:
      slash = '\\'
    elif '/' in tab_path:
      slash = '/'
    if tabName == 'tabClassification':
      Default_File_Name = tab_path[tab_path.rfind(slash)+1:tab_path.rfind('_tab')] + "_tabKmeansClustering_output.xlsx"
    else:
      Default_File_Name = tab_path[tab_path.rfind(slash)+1:tab_path.rfind('.')] + f"_{tabName}_output.xlsx"
    Default_Folder_Path = tab_path[:tab_path.rfind(slash)]
    self.ui.lineEdit_ExportFileName.setText(Default_File_Name)
    self.ui.lineEdit_ExportFolder.setText(Default_Folder_Path)

  def selectPath(self):
    """ click "select" Button to select a path for exporting  """
    file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
    self.ui.lineEdit_ExportFolder.setText(file)


  def go2export(self):
    """ exporting  """
    self.export(window)
    self.close()

class DialogWait(QDialog):
  """ Graphical user interface of Dialog used to show waiting :) """
  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogWait()
    self.ui.setupUi(self)
    self.ui.pushButton_OK_DialogWait.clicked.connect(self.close)
  def print_wait(self,info=' '):
    """ writing info  """
    self.ui.textBrowser_Info.setText(info)

class DialogError(QDialog):
  """ Graphical user interface of Dialog used to show error """
  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogError()
    self.ui.setupUi(self)
    self.ui.pushButton_OK_DialogError.clicked.connect(self.close)
  def print_error(self, error_message, suggestion=' '):
    """ writing error message and suggestion  """
    self.ui.textBrowser_Error.setText(error_message)
    self.ui.textBrowser_Suggestion.setText(suggestion)

class RaiseAndFlash(QObject):
  """
  Event filter helper to bring a dialog to the foreground and briefly highlight it
  when the user interacts with another window.

  This class monitors window activation changes. If the dialog loses focus and the
  user activates a different (unrelated) window, the dialog is raised, activated,
  and visually highlighted ("flashed") for a short duration.

  Parameters
  ----------
  dlg : QDialog
      The dialog window to monitor and highlight.

  Notes
  -----
  - Uses an event filter to detect when the dialog is deactivated.
  - Avoids flashing if focus moves to a child or popup of the dialog.
  - Flash effect is implemented via a temporary stylesheet change.
  """
  def __init__(self, dlg):
    """
    Initialize the RaiseAndFlash helper.

    Parameters
    ----------
    dlg : QDialog
      The dialog to be monitored and flashed.
    """
    super().__init__(dlg)
    self.dlg = dlg
    self._base_style = dlg.styleSheet()

    self._restore_timer = QTimer(self)
    self._restore_timer.setSingleShot(True)
    self._restore_timer.timeout.connect(self._restore_style)

  def _restore_style(self):
    """
    Restore the dialog's original stylesheet after flashing.
    """
    self.dlg.setStyleSheet(self._base_style)

  def eventFilter(self, obj, event):
    """
    Intercept events to detect when the dialog loses focus.

    Parameters
    ----------
    obj : QObject
        The object receiving the event.
    event : QEvent
        The event being processed.

    Returns
    -------
    bool
        False to allow normal event processing to continue.
    """
    if obj is self.dlg and event.type() == QEvent.Type.WindowDeactivate:
      # Deactivate can be followed immediately by another activation.
      # Check *after* the event loop settles which window is active.
      QTimer.singleShot(0, self._maybe_flash)
    return False

  def _maybe_flash(self):
    # If the currently active window is still the dialog (or belongs to it),
    # do NOT flash (user clicked inside the dialog or its popups).
    aw = QApplication.activeWindow()
    if aw is None:
      return

    # If active window is the dialog itself, no flash
    if aw is self.dlg:
      return

    # If active window is a child/popup belonging to the dialog, no flash
    try:
      if self.dlg.isAncestorOf(aw):
        return
    except Exception:
      pass

    # Otherwise the user activated something outside the dialog -> flash
    self.flash()

  def flash(self):
    """
    Bring the dialog to the foreground and briefly highlight it.

    The dialog is:
    - raised and activated
    - outlined with a temporary border
    - restored to its original style after a short delay
    - optionally triggers a system alert (taskbar highlight)
    """
    self.dlg.raise_()
    self.dlg.activateWindow()
    self.dlg.setStyleSheet(self._base_style + "\nQDialog { border: 3px solid #ffcc00; }")
    self._restore_timer.start(150)
    QApplication.alert(self.dlg, 500)
class DialogPathList(QDialog):
  """ Graphical user interface of Dialog used to show path list """
  from .Tools4GUI import FilesToDialog_tab, FilesToMainWindow_tab, \
    addFile_tab, deleteFile_tab, changeFile_tab,\
    MoveFileUp_tab, MoveFileDown_tab
  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogPathList()
    self.ui.setupUi(self)
    self.OriginalTableWidget = None
    #icons
    self.icons_path = f"{window.file_path}{window.slash}pic{window.slash}icons{window.slash}"
    self._init_icons()
    # click connection
    self.ui.pushButton_addFile.clicked.connect(lambda: self.addFile_tab(tabName=None))
    self.ui.pushButton_changeFile.clicked.connect(lambda: self.changeFile_tab(tabName=None))
    self.ui.pushButton_deleteFile.clicked.connect(lambda: self.deleteFile_tab(tabName=None))
    self.ui.pushButton_MoveFileUp.clicked.connect(lambda: self.MoveFileUp_tab(tabName=None))
    self.ui.pushButton_MoveFileDown.clicked.connect(lambda: self.MoveFileDown_tab(tabName=None))

  def set_icon(self, button, icon_name, size=24):
    """
    Set an icon on a Qt button from the configured icons path.
    """
    icon = QIcon(f"{self.icons_path}{icon_name}")
    icon.addFile(f"{self.icons_path}{icon_name}", QSize(size, size))
    button.setIcon(icon)

  def _init_icons(self):
    self.set_icon(
      self.ui.pushButton_addFile,
      "add_24x24.png"
      )
    self.set_icon(
      self.ui.pushButton_MoveFileUp,
      "edit_arrow_up_24x24.png"
      )
    self.set_icon(
      self.ui.pushButton_changeFile,
      "edit_24x24.png"
      )
    self.set_icon(
      self.ui.pushButton_MoveFileDown,
      "edit_arrow_down_24x24.png"
      )
    self.set_icon(
      self.ui.pushButton_deleteFile,
      "delete_24x24.png"
      )
  def closeEvent(self, event):
    """ transfer the path list back """
    try:
      self.FilesToMainWindow_tab()
    except:
      pass

class DialogTestList(QDialog):
  """ Graphical user interface of Dialog used to show path list """
  from .Tools4GUI import FilesToDialog_tab, FilesToMainWindow_tab, \
    addFile_tab, deleteFile_tab, changeFile_tab,\
    MoveFileUp_tab, MoveFileDown_tab,\
    click_pushButton_SelectAll, Select_TypedTest, PlainTextToDialog_tab, PlainTextToMainWindow_tab
  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogTestList()
    self.ui.setupUi(self)
    self.OriginalTableWidget = None
    self.OriginalPlainTextWidget = None
    # click connection
    self.ui.pushButton_SelectAll.clicked.connect(lambda: self.click_pushButton_SelectAll(tabName=None))
    self.ui.pushButton_SelectTypedTest.clicked.connect(lambda: self.Select_TypedTest(tabName=None))


  def closeEvent(self, event):
    """ transfer the path list back """
    try:
      self.FilesToMainWindow_tab()
      self.PlainTextToMainWindow_tab()
    except:
      pass

class DialogAbout(QDialog):
  """ Graphical user interface of Dialog used to show About """
  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogAbout()
    self.ui.setupUi(self)
  def print_about(self, message):
    """ writing about message  """
    self.ui.textBrowser_About.setText(message)

class DialogSaveAs(QDialog):
  """ Graphical user interface of Dialog used to save file """
  from .Save_and_Load import SAVE

  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogSaveAs()
    self.ui.setupUi(self)
    self.ui.pushButton_selectPath.clicked.connect(self.selectPath)
    self.ui.pushButton_OK.clicked.connect(self.go2Save)


  def selectPath(self):
    """ click "select" Button to select a path for exporting  """
    file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
    self.ui.lineEdit_SaveAsFolder.setText(file)


  def go2Save(self):
    """ saving  """
    self.SAVE(window)
    self.close()


class DialogOpen(QDialog):
  """ Graphical user interface of Dialog used to open file """
  from .Save_and_Load import LOAD

  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogOpen()
    self.ui.setupUi(self)
    self.ui.pushButton_selectPath.clicked.connect(self.selectPath)
    self.ui.pushButton_OK.clicked.connect(self.go2Open)


  def selectPath(self):
    """ click "select" Button to select a folder path for exporting  """
    file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
    slash = '\\'
    if '\\' in file:
      slash = '\\'
    elif '/' in file:
      slash = '/'
    fileName=file[file.rfind(slash)+1:]
    fileFolder=file[0:file.rfind(slash)+1]
    self.ui.lineEdit_OpenFolder.setText(fileFolder)
    self.ui.lineEdit_OpenFileName.setText(fileName)


  def go2Open(self):
    """ openning  """
    self.LOAD(window)
    self.close()

  def openUsingOpenRecent(self,file_name):
    """
    open the file named with file_name
    Args:
    file_name (string): the name of the file to be opened
    """
    idx = file_name.rfind(window.slash)
    if file_name[-1] == '\n':
      FileName = file_name[idx+1:-1]
    else:
      FileName = file_name[idx+1:]
    Folder = file_name[:idx]
    self.ui.lineEdit_OpenFileName.setText(FileName)
    self.ui.lineEdit_OpenFolder.setText(Folder)
    self.go2Open()


  def openUsingOpenRecent0(self):
    """ open the recent file 0  """
    file_name = window.ui.actionOpenRecent0.text()
    self.openUsingOpenRecent(file_name)
  def openUsingOpenRecent1(self):
    """ open the recent file 1  """
    file_name = window.ui.actionOpenRecent1.text()
    self.openUsingOpenRecent(file_name)
  def openUsingOpenRecent2(self):
    """ open the recent file 2  """
    file_name = window.ui.actionOpenRecent2.text()
    self.openUsingOpenRecent(file_name)
  def openUsingOpenRecent3(self):
    """ open the recent file 3  """
    file_name = window.ui.actionOpenRecent3.text()
    self.openUsingOpenRecent(file_name)
  def openUsingOpenRecent4(self):
    """ open the recent file 4  """
    file_name = window.ui.actionOpenRecent4.text()
    self.openUsingOpenRecent(file_name)
  def openUsingOpenRecent5(self):
    """ open the recent file 5  """
    file_name = window.ui.actionOpenRecent5.text()
    self.openUsingOpenRecent(file_name)


##############
## Main function
def main():
  """ Main method and entry point for commands """
  #pylint: disable=global-variable-undefined
  global window, window_DialogExport, window_DialogSaveAs, window_DialogOpen, \
    window_DialogError, window_DialogWait, window_DialogAbout, \
    window_DialogPathList, window_DialogTestList
  app = QApplication(sys.argv)
  window = MainWindow()
  window.setWindowTitle("indentationGUI")
  logo_icon = QIcon()
  logo_path = f"{window.file_path}{window.slash}pic{window.slash}logo{window.slash}"
  logo_icon.addFile(f"{logo_path}logo.png", QSize(1000,1000))
  logo_icon.addFile(f"{logo_path}logo_16x16.png", QSize(16,16))
  logo_icon.addFile(f"{logo_path}logo_24x24.png", QSize(24,24))
  logo_icon.addFile(f"{logo_path}logo_32x32.png", QSize(32,32))
  logo_icon.addFile(f"{logo_path}logo_48x48.png", QSize(48,48))
  logo_icon.addFile(f"{logo_path}logo_256x256.png", QSize(256,256))
  window.setWindowIcon(logo_icon)
  window.show()
  window.activateWindow()
  window.raise_()
  window_DialogExport = DialogExport()
  window_DialogExport.setWindowIcon(logo_icon)
  window_DialogSaveAs = DialogSaveAs()
  window_DialogSaveAs.setWindowIcon(logo_icon)
  window_DialogOpen = DialogOpen()
  window_DialogOpen.setWindowIcon(logo_icon)
  window_DialogError = DialogError()
  window_DialogError.setWindowIcon(logo_icon)
  window_DialogWait = DialogWait()
  window_DialogWait.setWindowIcon(logo_icon)
  window_DialogAbout = DialogAbout()
  window_DialogAbout.setWindowIcon(logo_icon)
  window_DialogPathList = DialogPathList()
  window_DialogPathList.setWindowIcon(logo_icon)
  window_DialogTestList = DialogTestList()
  window_DialogTestList.setWindowIcon(logo_icon)
  #open or create Txt-file of OpenRecent
  try:
    file_RecentFiles = open(f"{window.file_path}{window.slash}RecentFiles.txt", 'r', encoding="utf-8") #pylint: disable=consider-using-with
  except:
    pass
  else:
    window.RecentFiles = file_RecentFiles.readlines()
    window.update_OpenRecent()
    file_RecentFiles.close()
  ret = app.exec()
  sys.exit(ret)

# called by python3 micromechanics_indentationGUI
if __name__ == '__main__':
  main()
