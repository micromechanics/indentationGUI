""" Graphical user interface to calibrate tip area function """
import numpy as np
from micromechanics import indentation
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module

def click_OK_calibration(self):
  """ Graphical user interface to calibrate tip area function """
  #set Progress Bar
  self.ui.progressBar_calibration.setValue(0)
  #get Inputs
  fileName = f"{self.ui.lineEdit_path_tabCalibration.text()}"
  E_target = self.ui.doubleSpinBox_E_tabCalibration.value()
  Poisson = self.ui.doubleSpinBox_Poisson_tabCalibration.value()
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabTAF.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabTAF.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabCalibration.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabCalibration.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabCalibration.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabCalibration.value()
  number_of_TAFterms = self.ui.spinBox_number_of_TAFterms.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabTAF.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabTAF.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabTAF.value()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  #define Inputs (Model, Output, Surface)
  Model = {
              'nuTip':      Poisson_Tip,
              'modulusTip': E_Tip,      # GPa from Oliver,Pharr Method paper
              'unloadPMax':unloaPMax,        # upper end of fitting domain of unloading stiffness: Vendor-specific change
              'unloadPMin':unloaPMin,         # lower end of fitting domain of unloading stiffness: Vendor-specific change
              'relForceRateNoise':relForceRateNoise, # threshold of dp/dt use to identify start of loading: Vendor-specific change
              'maxSizeFluctuations': max_size_fluctuation # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
              }
  def guiProgressBar(value, location):
    if location=='load':
      value = value/3
    if location=='calibrateStiffness':
      value = (value/3 + 1/3) *100
    if location in ('calibration1', 'calibration2'):
      value = (value/3 + 2/3) *100
    self.ui.progressBar_calibration.setValue(value)
  Output = {
              'progressBar': guiProgressBar,   # function to use for plotting progress bar
              }
  Surface = {}
  if UsingRate2findSurface:
    Surface = {
                "abs(dp/dh)":Rate2findSurface, "median filter":DataFilterSize
                }
  #Reading Inputs
  self.i_tabTAF = indentation.Indentation(fileName=fileName, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  #show Test method
  Method=self.i_tabTAF.method.value
  self.ui.comboBox_method_tabCalibration.setCurrentIndex(Method-1)
  #plot load-depth of test 1
  self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTAF.cla()
  self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTAF.set_title(f"{self.i_tabTAF.testName}")
  self.i_tabTAF.output['ax'] = self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTAF
  self.i_tabTAF.stiffnessFromUnloading(self.i_tabTAF.p, self.i_tabTAF.h, plot=True)
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabTAF.draw()
  self.i_tabTAF.output['ax'] = None
  #calculate frameStiffness and Tip Area Function
  self.static_ax_tabFrameStiffness.cla()
  self.i_tabTAF.output['ax'] = self.static_ax_tabFrameStiffness
  critDepthStiffness=self.ui.doubleSpinBox_critDepthStiffness_tabCalibration.value()
  critForce=self.ui.doubleSpinBox_critForceStiffness_tabCalibration.value()
  hc, Ac = self.i_tabTAF.calibration(critDepthStiffness=critDepthStiffness, critForce=critForce,plotStiffness=False,numPolynomial=number_of_TAFterms,returnArea=True, eTarget=E_target)
  self.static_canvas_tabFrameStiffness.figure.set_tight_layout(True)
  self.static_canvas_tabFrameStiffness.draw()
  self.i_tabTAF.output['ax'] = None
  #listing Test
  self.ui.tableWidget_tabTAF.setRowCount(0)
  self.ui.tableWidget_tabTAF.setRowCount(len(self.i_tabTAF.allTestList))
  for k, theTest in enumerate(self.i_tabTAF.allTestList):
    self.ui.tableWidget_tabTAF.setItem(k,0,QTableWidgetItem(theTest))
    if theTest in self.i_tabTAF.output['successTest']:
      self.ui.tableWidget_tabTAF.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      self.ui.tableWidget_tabTAF.setItem(k,1,QTableWidgetItem("No"))
  #output: calibrated frame compliance and frame stiffness
  self.ui.lineEdit_FrameCompliance_Calibration.setText(f"{self.i_tabTAF.tip.compliance:.10f}")
  self.ui.lineEdit_FrameStiffness_Calibration.setText(f"{(1/self.i_tabTAF.tip.compliance):.10f}")
  #output: terms of the calibrated tip area function
  for j in range(5):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTAF") # pylint: disable = eval-used
    lineEdit.setText("0")
  for j in range(number_of_TAFterms):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTAF") # pylint: disable = eval-used
    lineEdit.setText(f"{self.i_tabTAF.tip.prefactors[j]:.10f}")
  #plot the calibrated tip area funciton
  self.plot_TAF(hc,Ac)

def plot_TAF(self,hc,Ac):
  """
  to plot the calibrated tip area function

  Args:
    hc (float): contact depth [µm]
    Ac (float): contact area [µm2]
  """
  self.static_ax_tabTipAreaFunction.cla()
  self.static_ax_tabTipAreaFunction.scatter(hc,Ac,color='b',label='data')
  hc_new = np.arange(0,hc.max()*1.05,hc.max()/100)
  Ac_new = self.i_tabTAF.tip.areaFunction(hc_new)
  self.static_ax_tabTipAreaFunction.plot(hc_new,Ac_new,color='r',label='fitted Tip Area Function')
  self.static_ax_tabTipAreaFunction.legend()
  self.static_ax_tabTipAreaFunction.set_xlabel('Contact Depth hc [µm]')
  self.static_ax_tabTipAreaFunction.set_ylabel('Contact Area Ac [µm$^2$]')
  self.static_canvas_tabTipAreaFunction.figure.set_tight_layout(True)
  self.static_canvas_tabTipAreaFunction.draw()
