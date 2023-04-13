""" Graphical user interface includes all widgets """
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QVBoxLayout, QFileDialog # pylint: disable=no-name-in-module
import sys
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar) # from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
import numpy as np
from main_window_ui import Ui_MainWindow
from DialogExport_ui import Ui_DialogExport

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  """ Graphical user interface includes all widgets """
  from TipRadius import Calculate_TipRadius, plot_Hertzian_fitting
  from CalculateHardnessModulus import Calculate_Hardness_Modulus
  from CalibrateTAF import click_OK_calibration, plot_TAF
  from FrameStiffness import FrameStiffness
  from load_depth import plot_load_depth
  def __init__(self):
    #global setting
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    #clicked.connect
    self.ui.OK_path_tabCalibration.clicked.connect(self.click_OK_calibration)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness)
    self.ui.pushButton_Calculate_tabTipRadius_FrameStiffness.clicked.connect(self.click_pushButton_Calculate_tabTipRadius_FrameStiffness)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness)
    self.ui.pushButton_Calculate_tabHE_FrameStiffness.clicked.connect(self.click_pushButton_Calculate_tabHE_FrameStiffness)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE)
    self.ui.Copy_TAF_tabHE.clicked.connect(self.Copy_TAF)
    self.ui.Copy_FrameCompliance_tabHE.clicked.connect(self.Copy_FrameCompliance)
    self.ui.Copy_FrameCompliance_tabTipRadius.clicked.connect(self.Copy_FrameCompliance_tabTipRadius)
    self.ui.Calculate_tabHE.clicked.connect(self.Calculate_Hardness_Modulus)
    self.ui.pushButton_Calculate_tabTipRadius.clicked.connect(self.Calculate_TipRadius)
    self.ui.pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius.clicked.connect(self.click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius)
    self.ui.pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius.clicked.connect(self.click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius)
    self.ui.actionExport.triggered.connect(self.show_DialogExport)
    #initializing variables for collecting analysed results
    self.tabHE_hc_collect=[]
    self.tabHE_Pmax_collect=[]
    self.tabHE_H_collect=[]
    self.tabHE_E_collect=[]
    self.tabHE_testName_collect=[]
    #graphicsView
    graphicsView_list = ['load_depth_tab_inclusive_frame_stiffness_tabTAF',  
                          'tabFrameStiffness',                                #Frame_stiffness_TabTAF
                          'tabTipAreaFunction',
                          'load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness',
                          'tabTipRadius_FrameStiffness',
                          'tabHE_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabHE_FrameStiffness',
                          'load_depth_tab_inclusive_frame_stiffness_tabHE',
                          'H_hc_tabHE',
                          'H_Index_tabHE',
                          'E_hc_tabHE',
                          'E_Index_tabHE',
                          'load_depth_tab_inclusive_frame_stiffness_tabTipRadius',
                          'HertzianFitting_tabTipRadius',
                          'CalculatedTipRadius_tabTipRadius',
                          ]
    for graphicsView in graphicsView_list:
        self.matplotlib_canve_ax(graphicsView=graphicsView)        

  def show_DialogExport(self):
    if not window_DialogExport.isVisible():
        window_DialogExport.show()

  def matplotlib_canve_ax(self,graphicsView='load_depth_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness'):
    #graphicsView_load_depth_tab_inclusive_frame_stiffness_TipRadius
    layout = eval('QVBoxLayout(self.ui.graphicsView_%s)'%graphicsView)
    exec('self.static_canvas_%s = FigureCanvas(Figure(figsize=(5, 3)))'%graphicsView)
    exec('layout.addWidget(NavigationToolbar(self.static_canvas_%s, self))'%graphicsView)
    exec('layout.addWidget(self.static_canvas_%s)'%graphicsView)
    exec('self.static_ax_%s = self.static_canvas_%s.figure.subplots()'%(graphicsView,graphicsView))

  def Copy_TAF(self):
    self.ui.lineEdit_TipName_tabHE.setText(self.ui.lineEdit_TipName_tabTAF.text())
    self.ui.doubleSpinBox_E_Tip_tabHE.setValue(self.ui.doubleSpinBox_E_Tip_tabTAF.value())
    self.ui.doubleSpinBox_Poisson_Tip_tabHE.setValue(self.ui.doubleSpinBox_Poisson_Tip_tabTAF.value())
    for j in range(5):
        lineEdit = eval('self.ui.lineEdit_TAF%i_tabHE'%(j+1))
        exec('lineEdit.setText(self.ui.lineEdit_TAF%i_tabTAF.text())'%(j+1))

  def Copy_FrameCompliance(self):
    self.ui.lineEdit_FrameCompliance_tabHE.setText(self.ui.lineEdit_FrameCompliance_tabHE_FrameStiffness.text())

  def Copy_FrameCompliance_tabTipRadius(self):
    self.ui.lineEdit_FrameCompliance_tabTipRadius.setText(self.ui.lineEdit_FrameCompliance_tabTipRadius_FrameStiffness.text())

  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness(self):
    self.plot_load_depth(tabName='tabTAF')

  def click_pushButton_Calculate_tabTipRadius_FrameStiffness(self):
    self.FrameStiffness(tabName='tabTipRadius_FrameStiffness')

  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius_FrameStiffness(self):
    self.plot_load_depth(tabName='tabTipRadius_FrameStiffness')

  def click_pushButton_Calculate_tabHE_FrameStiffness(self):
    self.FrameStiffness(tabName='tabHE_FrameStiffness')

  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE_FrameStiffness(self):
    self.plot_load_depth(tabName='tabHE_FrameStiffness')

  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabHE(self):
    self.plot_load_depth(tabName='tabHE')

  def click_pushButton_plot_chosen_test_tab_inclusive_frame_stiffness_tabTipRadius(self):
    self.plot_load_depth(tabName='tabTipRadius')

  def click_pushButton_plot_Hertzian_fitting_of_chosen_test_tabTipRadius(self):
    self.plot_Hertzian_fitting(tabName='tabTipRadius')


class DialogExport(QDialog):
  from Export import export
  def __init__(self, parent = None):
    super().__init__()
    self.ui = Ui_DialogExport()
    self.ui.setupUi(self)    
    self.ui.pushButton_selectPath.clicked.connect(self.selectPath)
    self.ui.pushButton_OK.clicked.connect(self.go2export)
  def selectPath(self):       
    file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
    self.ui.lineEdit_ExportPath.setText(file)
  def go2export(self):
    self.export(window)   

##############
## Main function
def main():
  """ Main method and entry point for commands """
  global window, window_DialogExport
  app = QApplication()
  window = MainWindow()
  window.setWindowTitle("GUI for micromechanics.indentation")
  window.show()
  window.activateWindow()
  window.raise_()
  window_DialogExport = DialogExport()
  app.exec()
  return

# called by python3 -m micromechanics-IndentationGUI.main
if __name__ == '__main__':
  main()
