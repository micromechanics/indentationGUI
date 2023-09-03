""" Graphical user interface to calibrate tip area function """
import numpy as np
from micromechanics import indentation
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from .WaitingUpgrade_of_micromechanics import IndentationXXX
from .load_depth import pick

def click_OK_calibration(self):
  """ Graphical user interface to calibrate tip area function """
  #set Progress Bar
  self.ui.progressBar_tabTAF.setValue(0)
  #get Inputs
  fileName = self.ui.lineEdit_path_tabTAF.text()
  E_target = self.ui.doubleSpinBox_E_tabTAF.value()
  Poisson = self.ui.doubleSpinBox_Poisson_tabTAF.value()
  E_Tip = self.ui.doubleSpinBox_E_Tip_tabTAF.value()
  Poisson_Tip = self.ui.doubleSpinBox_Poisson_Tip_tabTAF.value()
  minhc_Tip = self.ui.doubleSpinBox_minhc_Tip_tabTAF.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabTAF.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabTAF.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabTAF.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabTAF.value()
  number_of_TAFterms = self.ui.spinBox_number_of_TAFterms_tabTAF.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabTAF.isChecked()
  Rate2findSurface = self.ui.doubleSpinBox_Rate2findSurface_tabTAF.value()
  DataFilterSize = self.ui.spinBox_DataFilterSize_tabTAF.value()
  Index_CalculationMethod = self.ui.comboBox_CalculationMethod_tabTAF.currentIndex()
  Index_TipType = self.ui.comboBox_TipType_tabTAF.currentIndex()
  Radius_Sphere = self.ui.doubleSpinBox_idealRadiusSphere_tabTAF.value()
  half_includedAngle_Cone = self.ui.doubleSpinBox_half_includedAngle_tabTAF.value()
  IfTermsGreaterThanZero = self.ui.checkBox_IfTermsGreaterThanZero_tabTAF.isChecked()
  if DataFilterSize%2==0:
    DataFilterSize+=1
  #define Inputs (Model, Output, Surface)
  Model = {
            'nuTip':      Poisson_Tip,
            'modulusTip': E_Tip,                        # GPa from Oliver,Pharr Method paper
            'unloadPMax': unloaPMax,                    # upper end of fitting domain of unloading stiffness: Vendor-specific change
            'unloadPMin': unloaPMin,                    # lower end of fitting domain of unloading stiffness: Vendor-specific change
            'relForceRateNoise': relForceRateNoise,     # threshold of dp/dt use to identify start of loading: Vendor-specific change
            'maxSizeFluctuations': max_size_fluctuation # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
            }
  def guiProgressBar(value, location):
    if location=='convert':
      value = value/3
      self.ui.progressBar_tabTAF.setValue(value)
    if location=='calibrateStiffness':
      value = (value/3 + 1/3) *100
      self.ui.progressBar_tabTAF.setValue(value)
    if location in ('calibration1', 'calibration2'):
      value = (value/3 + 2/3) *100
      self.ui.progressBar_tabTAF.setValue(value)
  Output = {
            'progressBar': guiProgressBar,   # function to use for plotting progress bar
            }
  Surface = {}
  if UsingRate2findSurface:
    Surface = {
              "abs(dp/dh)":Rate2findSurface, "median filter":DataFilterSize
              }
  #Reading Inputs
  self.i_tabTAF = IndentationXXX(fileName=fileName, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  self.i_tabTAF.parameters_for_GUI()
  if IfTermsGreaterThanZero:
    self.i_tabTAF.IfTermsGreaterThanZero = 1
  #show Test method
  Method=self.i_tabTAF.method.value
  self.ui.comboBox_method_tabTAF.setCurrentIndex(Method-1)
  #setting to correct thermal drift
  try:
    correctDrift = self.ui.checkBox_UsingDriftUnloading_tabTAF.isChecked()
  except:
    correctDrift = False
  if correctDrift:
    self.i_tabTAF.model['driftRate'] = True
  else:
    self.i_tabTAF.model['driftRate'] = False
  #changing i.allTestList to calculate using the checked tests
  try:
    OriginalAlltest = list(self.i_tabTAF.allTestList)
  except Exception as e: #pylint: disable=broad-except
    suggestion = 'Check if the Path is completed. \n A correct example: C:\G200X\\20230101\Example.xlsx' #pylint: disable=anomalous-backslash-in-string
    self.show_error(str(e), suggestion)
  for k, theTest in enumerate(OriginalAlltest):
    try:
      IsCheck = self.ui.tableWidget_tabTAF.item(k,0).checkState()
    except:
      pass
    else:
      if IsCheck==Qt.Unchecked:
        self.i_tabTAF.allTestList.remove(theTest)
  #update i_tabTAF
  self.i_tabTAF.restartFile()
  #plot load-depth of test 1
  self.i_tabTAF.output['ax'] = self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTAF
  self.i_tabTAF.output['ax'][0].cla()
  self.i_tabTAF.output['ax'][1].cla()
  self.i_tabTAF.output['ax'][0].set_title(f"{self.i_tabTAF.testName}")
  if self.i_tabTAF.method in (indentation.definitions.Method.ISO, indentation.definitions.Method.MULTI):
    self.i_tabTAF.stiffnessFromUnloading(self.i_tabTAF.p, self.i_tabTAF.h, plot=True, win=self)
  elif self.i_tabTAF.method== indentation.definitions.Method.CSM:
    self.i_tabTAF.output['ax'][0].scatter(self.i_tabTAF.h, self.i_tabTAF.p, s=1)
    self.i_tabTAF.output['ax'][0].axhline(0, linestyle='-.', color='tab:orange', label='zero Load or Depth') #!!!!!!
    self.i_tabTAF.output['ax'][0].axvline(0, linestyle='-.', color='tab:orange') #!!!!!!
    self.i_tabTAF.output['ax'][0].legend()
    self.i_tabTAF.output['ax'][0].set_ylabel(r'force [$\mathrm{mN}$]')
    self.i_tabTAF.output['ax'][1].set_ylabel(r"$\frac{P_{cal}-P_{mea}}{P_{mea}}x100$ [%]")
    self.i_tabTAF.output['ax'][1].set_xlabel(r'depth [$\mathrm{\mu m}$]')
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabTAF.figure.set_tight_layout(True)
  self.i_tabTAF.output['ax'] = [None, None]
  self.static_canvas_load_depth_tab_inclusive_frame_stiffness_tabTAF.draw()
  #calculate frameStiffness and Tip Area Function
  self.i_tabTAF.output['ax'] = self.static_ax_FrameStiffness_tabTAF # ax to plot figure for calculating frame compliance
  self.i_tabTAF.output['ax'][0].cla()
  self.i_tabTAF.output['ax'][1].cla()
  critDepthStiffness=self.ui.doubleSpinBox_critDepthStiffness_tabTAF.value()
  critForceStiffness=self.ui.doubleSpinBox_critForceStiffness_tabTAF.value()
  if Index_TipType==0:
    TipType='Berkovich'
  elif Index_TipType==1:
    TipType='Sphere'
  elif Index_TipType==2:
    TipType='Sphere+Cone'
  if Index_CalculationMethod == 0: # assume constant Hardness and Modulus (Eq.(24), Oliver 2004)
    self.i_tabTAF.restartFile()
    self.i_tabTAF.calibrateStiffness(critDepth=critDepthStiffness, critForce=critForceStiffness, plotStiffness=False, returnData=True)
    frameCompliance = self.i_tabTAF.tip.compliance
    hc, Ac = self.i_tabTAF.calibrateTAF(eTarget=E_target, frameCompliance = frameCompliance, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, plotTip=False, returnArea=True, critDepthTip=minhc_Tip) #pylint: disable=line-too-long
  elif Index_CalculationMethod == 1: # assume constant Modulus but neglect Pile-up (Eq.(22), Oliver 2004)
    self.i_tabTAF.output['ax'] = [None, None]
    self.i_tabTAF.calibrate_TAF_and_FrameStiffness_iterativeMethod(eTarget=E_target, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness, critDepthTip=minhc_Tip) # pylint: disable=line-too-long
    self.i_tabTAF.output['ax'] = self.static_ax_FrameStiffness_tabTAF
    self.i_tabTAF.calibrateStiffness_OneIteration(eTarget=E_target, critDepth=critDepthStiffness, critForce=critForceStiffness, plotStiffness=False)
    hc, Ac = self.i_tabTAF.calibrateTAF(eTarget=E_target, frameCompliance = self.i_tabTAF.tip.compliance, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, plotTip=False, returnArea=True, critDepthTip=minhc_Tip) # pylint: disable=line-too-long
  self.i_tabTAF.model['driftRate'] = False   #reset
  self.static_canvas_FrameStiffness_tabTAF.figure.set_tight_layout(True)
  self.i_tabTAF.output['ax'] = [None, None]
  self.static_canvas_FrameStiffness_tabTAF.draw()
  #plot the calibrated tip area funcitonS
  self.plot_TAF(hc,Ac)
  #listing Test
  self.ui.tableWidget_tabTAF.setRowCount(len(OriginalAlltest))
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in self.i_tabTAF.allTestList:
      qtablewidgetitem.setCheckState(Qt.Checked)
    else:
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    self.ui.tableWidget_tabTAF.setItem(k,0,qtablewidgetitem)
    if theTest in self.i_tabTAF.output['successTest']:
      self.ui.tableWidget_tabTAF.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      self.ui.tableWidget_tabTAF.setItem(k,1,QTableWidgetItem("No"))
  #output: calibrated frame compliance and frame stiffness
  self.ui.lineEdit_FrameCompliance_tabTAF.setText(f"{self.i_tabTAF.tip.compliance:.10f}")
  self.ui.lineEdit_FrameStiffness_tabTAF.setText(f"{(1/self.i_tabTAF.tip.compliance):.10f}")
  #output: terms of the calibrated tip area function
  for j in range(9):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTAF") # pylint: disable = eval-used
    lineEdit.setText("0")
  for j in range(number_of_TAFterms):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTAF") # pylint: disable = eval-used
    lineEdit.setText(f"{self.i_tabTAF.tip.prefactors[j]:.10f}")

def plot_TAF(self,hc,Ac):
  """
  to plot the calibrated tip area function

  Args:
    hc (float): contact depth [µm]
    Ac (float): contact area [µm2]
  """
  ax = self.static_ax_TAF_tabTAF
  ax[0].cla()
  ax[1].cla()
  ax[0].scatter(hc,Ac,color='b',label='data')
  hc_new = np.arange(0,hc.max()*1.05,hc.max()/100)
  Ac_new = self.i_tabTAF.tip.areaFunction(hc_new)
  ax[0].plot(hc_new,Ac_new,color='r',label='fitted Tip Area Function')
  ax[0].legend()
  ax[0].set_ylabel(r"Contact Area $A_{c}$ [µm$^2$]")
  Ac_cal = self.i_tabTAF.tip.areaFunction(hc)
  error = (Ac_cal - Ac) / Ac *100
  ax[1].scatter(hc, error, color='grey',s=5)
  ax[1].axhline(0, linestyle='dashdot', color='tab:orange')
  ax[1].set_ylabel(r"$\frac{{\rm fitted} A_{c}-{\rm meas.} A_{c}}{{\rm meas.} A_{c}}x100$ [%]")
  ax[1].set_xlabel(r"Contact Depth $h_{c}$ [µm]")
  self.static_canvas_TAF_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_TAF_tabTAF.draw()
