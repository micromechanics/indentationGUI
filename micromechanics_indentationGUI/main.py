""" Graphical user interface includes all widgets """
import sys
from PySide6.QtGui import QAction, QKeySequence, QShortcut, QIcon # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QFileDialog # pylint: disable=no-name-in-module
from PySide6.QtCore import Qt, QRectF, QCoreApplication # pylint: disable=no-name-in-module
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar) # pylint: disable=no-name-in-module # from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
from .main_window_ui import Ui_MainWindow
from .DialogExport_ui import Ui_DialogExport
from .DialogSaveAs_ui import Ui_DialogSaveAs
from .DialogOpen_ui import Ui_DialogOpen
from .DialogError_ui import Ui_DialogError
from .DialogWait_ui import Ui_DialogWait

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow): #pylint: disable=too-many-public-methods
  """ Graphical user interface of MainWindow """
  from .TipRadius import Calculate_TipRadius, plot_Hertzian_fitting
  from .AnalysePopIn import Analyse_PopIn
  from .CalculateHardnessModulus import Calculate_Hardness_Modulus
  from .CalibrateTAF import click_OK_calibration, plot_TAF
  from .Classification import Classification_HE, PlotMappingWithoutClustering, PlotMappingAfterClustering
  from .FrameStiffness import FrameStiffness
  from .load_depth import plot_load_depth, set_aspectRatio

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
    #new
    self.new()


  def new(self):
    """ initial settings """
    self.ui.setupUi(self)
    #initial the Path for saving
    self.Folder_SAVED = 'type or selcet the path of a folder'
    self.FileName_SAVED = 'give an arbitrary file name (with or without an arbitrary file extension)'
    #intial the list of recently opened and saved files
    self.RecentFiles =[]
    self.RecentFilesNumber=0
    #clicked.connect in tabTAF
    self.ui.OK_path_tabTAF.clicked.connect(self.click_OK_calibration)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness)
    self.ui.pushButton_SelectAll_tabTAF.clicked.connect(self.click_pushButton_SelectAll_tabTAF)
    #clicked.connect in tabTipRadius
    self.ui.pushButton_Calculate_tabTipRadius_FrameStiffness.clicked.connect(self.click_pushButton_Calculate_tabTipRadius_FrameStiffness)
    self.ui.pushButton_Calculate_tabPopIn_FrameStiffness.clicked.connect(self.click_pushButton_Calculate_tabPopIn_FrameStiffness)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness) # pylint: disable=line-too-long
    self.ui.Copy_FrameCompliance_tabTipRadius.clicked.connect(self.Copy_FrameCompliance_tabTipRadius)
    self.ui.Copy_TAF_tabTipRadius_FrameStiffness.clicked.connect(self.Copy_TAF_tabTipRadius_FrameStiffness)
    self.ui.pushButton_Calculate_tabTipRadius.clicked.connect(self.Calculate_TipRadius)
    self.ui.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.clicked.connect(self.click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius)
    self.ui.pushButton_SelectAll_tabTipRadius.clicked.connect(self.click_pushButton_SelectAll_tabTipRadius)
    self.ui.pushButton_SelectAll_tabTipRadius_FrameStiffness.clicked.connect(self.click_pushButton_SelectAll_tabTipRadius_FrameStiffness)
    #clicked.connect in tabHE
    self.ui.pushButton_Calculate_tabHE_FrameStiffness.clicked.connect(self.click_pushButton_Calculate_tabHE_FrameStiffness)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE)
    self.ui.Copy_TAF_tabHE.clicked.connect(self.Copy_TAF)
    self.ui.Copy_FrameCompliance_tabHE.clicked.connect(self.Copy_FrameCompliance_tabHE)
    self.ui.Copy_TAF_tabHE_FrameStiffness.clicked.connect(self.Copy_TAF_tabHE_FrameStiffness)
    self.ui.Calculate_tabHE.clicked.connect(self.click_pushButton_Calculate_Hardness_Modulus)
    self.ui.pushButton_SelectAll_tabHE.clicked.connect(self.click_pushButton_SelectAll_tabHE)
    self.ui.pushButton_SelectAll_tabHE_FrameStiffness.clicked.connect(self.click_pushButton_SelectAll_tabHE_FrameStiffness)
    #clicked.connect in tabPopIn
    self.ui.pushButton_Analyse_tabPopIn.clicked.connect(self.Analyse_PopIn)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness) # pylint: disable=line-too-long
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn)
    self.ui.Copy_TipRadius_tabPopIn.clicked.connect(self.Copy_TipRadius)
    self.ui.Copy_FrameCompliance_tabPopIn.clicked.connect(self.Copy_FrameCompliance_tabPopIn)
    self.ui.Copy_TAF_tabPopIn_FrameStiffness.clicked.connect(self.Copy_TAF_tabPopIn_FrameStiffness)
    self.ui.pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn.clicked.connect(self.click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn)
    self.ui.pushButton_SelectAll_tabPopIn.clicked.connect(self.click_pushButton_SelectAll_tabPopIn)
    self.ui.pushButton_SelectAll_tabPopIn_FrameStiffness.clicked.connect(self.click_pushButton_SelectAll_tabPopIn_FrameStiffness)
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
    #initializing variables for collecting analysed results
    self.tabHE_hc_collect=[]
    self.tabHE_Pmax_collect=[]
    self.tabHE_H_collect=[]
    self.tabHE_E_collect=[]
    self.tabHE_testName_collect=[]
    self.canvas_dict = {}
    self.ax_dict = {}

    #graphicsView
    graphicsView_list = [ 'load_depth_tab_inclusive_frame_stiffness_tabTAF',
                          'FrameStiffness_tabTAF',                                #Framestiffness_TabTAF
                          'TAF_tabTAF',
                          'load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness',
                          'tabTipRadius_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness',
                          'tabPopIn_FrameStiffness',
                          'tabHE_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabHE',
                          'H_hc_tabHE',
                          'H_Index_tabHE',
                          'E_hc_tabHE',
                          'E_Index_tabHE',
                          'HE_tabHE',
                          'load_depth_tab_inclusive_frame_stiffness_tabTipRadius',
                          'HertzianFitting_tabTipRadius',
                          'CalculatedTipRadius_tabTipRadius',
                          'load_depth_tab_inclusive_frame_stiffness_tabPopIn',
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
    self.ui.lineEdit_path_tabTAF.setText(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    self.ui.lineEdit_path_tabTipRadius_FrameStiffness.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_FrameStiffness.xlsx")
    self.ui.lineEdit_path_tabPopIn_FrameStiffness.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_FrameStiffness.xlsx")
    self.ui.lineEdit_path_tabTipRadius.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_TipRadius.xlsx")
    self.ui.lineEdit_path_tabPopIn.setText(fr"{file_path}{slash}Examples{slash}Example2{slash}Tungsten_TipRadius.xlsx")
    self.ui.lineEdit_path_tabHE_FrameStiffness.setText(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")
    self.ui.lineEdit_path_tabHE.setText(fr"{file_path}{slash}Examples{slash}Example1{slash}FusedSilica.xlsx")


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
      exec(f"self.static_ax_{graphicsView} = self.static_canvas_{graphicsView}.figure.subplots(2,1)") #pylint: disable=exec-used
      ax = eval(f"self.static_ax_{graphicsView}") #pylint: disable=eval-used
    elif ('load_depth' in graphicsView) or ('FrameStiffness' in graphicsView)  or (graphicsView in ('TAF_tabTAF')):
      exec(f"self.static_ax_{graphicsView} = self.static_canvas_{graphicsView}.figure.subplots(2,1,sharex=True, gridspec_kw={{'hspace':0, 'height_ratios':[4, 1]}})") #pylint: disable=exec-used
      ax = eval(f"self.static_ax_{graphicsView}") #pylint: disable=eval-used
    else:
      exec(f"self.static_ax_{graphicsView} = self.static_canvas_{graphicsView}.figure.subplots()") #pylint: disable=exec-used
      ax = eval(f"self.static_ax_{graphicsView}") #pylint: disable=eval-used
    self.canvas_dict.update({f"{graphicsView}":canvas})
    self.ax_dict.update({f"{graphicsView}":ax})

  def Copy_TAF(self):
    """ get the calibrated tip are function from the tabTAF """
    self.ui.lineEdit_TipName_tabHE.setText(self.ui.lineEdit_TipName_tabTAF.text())
    self.ui.doubleSpinBox_E_Tip_tabHE.setValue(self.ui.doubleSpinBox_E_Tip_tabTAF.value())
    self.ui.doubleSpinBox_Poisson_Tip_tabHE.setValue(self.ui.doubleSpinBox_Poisson_Tip_tabTAF.value())
    for j in range(9):
      lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabHE") #pylint: disable=eval-used disable=unused-variable
      exec(f"lineEdit.setText(self.ui.lineEdit_TAF{j+1}_tabTAF.text())") #pylint: disable=exec-used

  def Copy_TAF_tabTipRadius_FrameStiffness(self):
    """ get the calibrated tip are function from the tabTAF """
    self.ui.lineEdit_TipName_tabTipRadius_FrameStiffness.setText(self.ui.lineEdit_TipName_tabTAF.text())
    for j in range(9):
      lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTipRadius_FrameStiffness") #pylint: disable=eval-used disable=unused-variable
      exec(f"lineEdit.setText(self.ui.lineEdit_TAF{j+1}_tabTAF.text())") #pylint: disable=exec-used


  def Copy_TAF_tabHE_FrameStiffness(self):
    """ get the calibrated tip are function from the tabTAF """
    self.ui.lineEdit_TipName_tabHE_FrameStiffness.setText(self.ui.lineEdit_TipName_tabTAF.text())
    for j in range(9):
      lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabHE_FrameStiffness") #pylint: disable=eval-used disable=unused-variable
      exec(f"lineEdit.setText(self.ui.lineEdit_TAF{j+1}_tabTAF.text())") #pylint: disable=exec-used


  def Copy_TAF_tabPopIn_FrameStiffness(self):
    """ get the calibrated tip are function from the tabTAF """
    self.ui.lineEdit_TipName_tabPopIn_FrameStiffness.setText(self.ui.lineEdit_TipName_tabTAF.text())
    for j in range(9):
      lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabPopIn_FrameStiffness") #pylint: disable=eval-used disable=unused-variable
      exec(f"lineEdit.setText(self.ui.lineEdit_TAF{j+1}_tabTAF.text())") #pylint: disable=exec-used


  def Copy_TipRadius(self):
    """ get the calibrated tip radius from the tabTipRadius """
    self.ui.lineEdit_TipName_tabPopIn.setText(self.ui.lineEdit_TipName_tabTipRadius.text())
    self.ui.doubleSpinBox_E_Tip_tabPopIn.setValue(self.ui.doubleSpinBox_E_Tip_tabTipRadius.value())
    self.ui.doubleSpinBox_Poisson_Tip_tabPopIn.setValue(self.ui.doubleSpinBox_Poisson_Tip_tabTipRadius.value())
    self.ui.doubleSpinBox_TipRadius_tabPopIn.setValue(float(self.ui.lineEdit_TipRadius_tabTipRadius.text()))


  def Copy_FrameCompliance_tabTipRadius(self):
    """ get the calibrated frame compliance """
    self.ui.lineEdit_FrameCompliance_tabTipRadius.setText(self.ui.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness.text())


  def Copy_FrameCompliance_tabHE(self):
    """ get the calibrated frame compliance """
    self.ui.lineEdit_FrameCompliance_tabHE.setText(self.ui.lineEdit_FrameCompliance_tabHE_FrameStiffness.text())


  def Copy_FrameCompliance_tabPopIn(self):
    """ get the calibrated frame compliance """
    self.ui.lineEdit_FrameCompliance_tabPopIn.setText(self.ui.lineEdit_FrameCompliance_tabPopIn_FrameStiffness.text())


  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness(self):
    """ plot the load-depth curves of the chosen tests """
    self.plot_load_depth(tabName='tabTAF')


  def click_pushButton_Calculate_tabTipRadius_FrameStiffness(self):
    """ calculate the frame stiffness in tabTipRadius """
    self.FrameStiffness(tabName='tabTipRadius_FrameStiffness')


  def click_pushButton_Calculate_tabPopIn_FrameStiffness(self):
    """ calculate the frame stiffness in tabPopIn """
    self.FrameStiffness(tabName='tabPopIn_FrameStiffness')


  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness(self):
    """ plot the load-depth curves of the chosen tests in tabTipRadius for calculating frame stiffness"""
    self.plot_load_depth(tabName='tabTipRadius_FrameStiffness')


  def click_pushButton_Calculate_tabHE_FrameStiffness(self):
    """ calculate the frame stiffness in tabHE """
    self.FrameStiffness(tabName='tabHE_FrameStiffness')


  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness(self):
    """ plot the load-depth curves of the chosen tests in tabHE for calculating frame stiffness """
    self.plot_load_depth(tabName='tabHE_FrameStiffness')

  def click_pushButton_Calculate_Hardness_Modulus(self):
    """ calculate the hardness and modulus in tabHE """
    self.Calculate_Hardness_Modulus()

  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE(self):
    """ plot the load-depth curves of the chosen tests in tabHE """
    self.plot_load_depth(tabName='tabHE')


  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn_FrameStiffness(self):
    """ plot the load-depth curves of the chosen tests in tabPopIn for calculating frame stiffness """
    self.plot_load_depth(tabName='tabPopIn_FrameStiffness')


  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabPopIn(self):
    """ plot the load-depth curves of the chosen tests in tabPopIn """
    self.plot_load_depth(tabName='tabPopIn')


  def click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabPopIn(self):
    """ plot the Hertzian fitting curves of the chosen tests in tabPopIn """
    self.plot_Hertzian_fitting(tabName='tabPopIn')


  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius(self):
    """ plot the load-depth curves of the chosen tests in tabTipRadius """
    self.plot_load_depth(tabName='tabTipRadius')


  def click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius(self):
    """ plot the Hertzian fitting curves of the chosen tests in tabTipRadius """
    self.plot_Hertzian_fitting(tabName='tabTipRadius')

  def click_pushButton_SelectAll(self, tabName): #pylint: disable=no-self-use
    """ select/ unselect all tests in {tabName} """
    State = Qt.Checked
    tableWidget = eval(f"self.ui.tableWidget_{tabName}") #pylint: disable = eval-used
    if tableWidget.item(0,0).checkState() == Qt.Checked:
      State = Qt.Unchecked
    for k in range(tableWidget.rowCount()):
      try:
        tableWidget.item(k,0).setCheckState(State)
      except:
        pass

  def click_pushButton_SelectAll_tabTAF(self):
    """ select/ unselect all tests in tabTAF """
    self.click_pushButton_SelectAll(tabName='tabTAF')

  def click_pushButton_SelectAll_tabTipRadius(self):
    """ select/ unselect all tests in tabTipRadius """
    self.click_pushButton_SelectAll(tabName='tabTipRadius')

  def click_pushButton_SelectAll_tabTipRadius_FrameStiffness(self):
    """ select/ unselect all tests in tabTipRadius_FrameStiffness """
    self.click_pushButton_SelectAll(tabName='tabTipRadius_FrameStiffness')

  def click_pushButton_SelectAll_tabHE(self):
    """ select/ unselect all tests in tabHE """
    self.click_pushButton_SelectAll(tabName='tabHE')

  def click_pushButton_SelectAll_tabHE_FrameStiffness(self):
    """ select/ unselect all tests in tabHE_FrameStiffness """
    self.click_pushButton_SelectAll(tabName='tabHE_FrameStiffness')

  def click_pushButton_SelectAll_tabPopIn(self):
    """ select/ unselect all tests in tabPopIn """
    self.click_pushButton_SelectAll(tabName='tabPopIn')

  def click_pushButton_SelectAll_tabPopIn_FrameStiffness(self):
    """ select/ unselect all tests in tabPopIn_FrameStiffness """
    self.click_pushButton_SelectAll(tabName='tabPopIn_FrameStiffness')

  def click_pushButton_Classify_tabClassification(self):
    """ perform classification """
    self.Classification_HE()

  def click_pushButton_PlotMappingWithoutClustering_tabClassification(self):
    """ plot mapping without clustering """
    self.PlotMappingWithoutClustering()

  def click_pushButton_PlotMappingAfterClustering_tabClassification(self):
    """ plot mapping After clustering """
    self.PlotMappingAfterClustering()

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
      tab_path = window.ui.lineEdit_path_tabHE_FrameStiffness.text()
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
      self.ui.comboBox_ExportFormat.setCurrentIndex(0)
    elif self.ui.comboBox_ExportTab.currentIndex()==1:
      tabName='tabPopIn'
      self.ui.comboBox_ExportFormat.setCurrentIndex(1)
    #set default file name und folder path for {tabName}
    tab_path = eval(f"window.ui.lineEdit_path_{tabName}.text()") # pylint: disable=eval-used
    slash = '\\'
    if '\\' in tab_path:
      slash = '\\'
    elif '/' in tab_path:
      slash = '/'
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
  global window, window_DialogExport, window_DialogSaveAs, window_DialogOpen, window_DialogError, window_DialogWait #pylint: disable=global-variable-undefined
  app = QApplication()
  window = MainWindow()
  window.setWindowTitle("GUI for micromechanics.indentation")
  logo_icon = QIcon()
  logo_icon.addFile(f"{window.file_path}{window.slash}pic{window.slash}logo.png")
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
