#pylint: disable=possibly-used-before-assignment, used-before-assignment

""" Graphical user interface to calibrate tip area function """
import numpy as np
from micromechanics import indentation
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module
from .WaitingUpgrade_of_micromechanics import IndentationXXX

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
  maxhc_Tip = self.ui.doubleSpinBox_maxhc_Tip_tabTAF.value()
  unloaPMax = self.ui.doubleSpinBox_Start_Pmax_tabTAF.value()
  unloaPMin = self.ui.doubleSpinBox_End_Pmax_tabTAF.value()
  relForceRateNoise = self.ui.doubleSpinBox_relForceRateNoise_tabTAF.value()
  max_size_fluctuation = self.ui.spinBox_max_size_fluctuation_tabTAF.value()
  number_of_TAFterms = self.ui.spinBox_number_of_TAFterms_tabTAF.value()
  UsingRate2findSurface = self.ui.checkBox_UsingRate2findSurface_tabTAF.isChecked()
  UsingSurfaceIndex = self.ui.checkBox_UsingSurfaceIndex_tabTAF.isChecked()
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
            'maxSizeFluctuations': max_size_fluctuation, # maximum size of small fluctuations that are removed in identifyLoadHoldUnload
            'driftRate': 0
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
  #open waiting dialog
  self.show_wait('GUI is reading the file')
  #Reading Inputs
  self.i_tabTAF = IndentationXXX(fileName=fileName, nuMat= Poisson, surface=Surface, model=Model, output=Output)
  i = self.i_tabTAF
  i.parameters_for_GUI()
  if IfTermsGreaterThanZero:
    i.IfTermsGreaterThanZero = 1
  #initial surfaceIdx
  i.surface['surfaceIdx']={}
  #close waiting dialog
  self.close_wait()
  #show Test method
  Method=i.method.value
  self.ui.comboBox_method_tabTAF.setCurrentIndex(Method-1)
  #setting to correct thermal drift
  try:
    correctDrift = self.ui.checkBox_UsingDriftUnloading_tabTAF.isChecked()
  except:
    correctDrift = False
  if correctDrift:
    i.model['driftRate'] = True
  else:
    i.model['driftRate'] = 0
  #changing i.allTestList to calculate using the checked tests
  try:
    OriginalAlltest = list(i.allTestList)
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
        i.allTestList.remove(theTest)
  #update i_tabTAF
  i.restartFile()
  # searching SurfaceIdx in the table
  if UsingSurfaceIndex:
    for k, theTest in enumerate(OriginalAlltest):
      qtablewidgetitem = self.ui.tableWidget_tabTAF.item(k, 2)
      i.testName=theTest
      if i.vendor == indentation.definitions.Vendor.Agilent:
        i.nextAgilentTest(newTest=False)
        i.nextTest(newTest=False)
      if i.vendor == indentation.definitions.Vendor.Micromaterials:
        i.nextMicromaterialsTest(newTest=False)
        i.nextTest(newTest=False)
      try:
        indexX = int(qtablewidgetitem.text())
        i.surface['surfaceIdx'].update({theTest:indexX})
      except:
        pass
    i.restartFile()
  # save test 1 and set the data in the load depht curve can be picked
  i.output['ax'] = self.static_ax_load_depth_tab_inclusive_frame_stiffness_tabTAF
  i.output['ax'][0].figure.canvas.mpl_connect("pick_event", self.right_click_set_ContactSurface)
  self.indentation_inLoadDepth_tabTAF = i
  i.output['ax'] = [None, None]
  #calculate frameStiffness and Tip Area Function
  i.output['ax'] = self.static_ax_FrameStiffness_tabTAF # ax to plot figure for calculating frame compliance
  i.output['ax'][0].cla()
  i.output['ax'][1].cla()
  critDepthStiffness=self.ui.doubleSpinBox_critDepthStiffness_tabTAF.value()
  critForceStiffness=self.ui.doubleSpinBox_critForceStiffness_tabTAF.value()
  if Index_TipType==0:
    TipType='Berkovich'
  elif Index_TipType==1:
    TipType='Sphere'
  elif Index_TipType==2:
    TipType='Sphere+Cone'
  frameCompliance_collect = None
  if Index_CalculationMethod == 0: # assume constant Hardness and Modulus (Eq.(24), Oliver 2004)
    i.restartFile()
    _, _, frameCompliance_collect = i.calibrateStiffness(critDepth=critDepthStiffness, critForce=critForceStiffness, plotStiffness=False, returnData=True)
    frameCompliance = i.tip.compliance
    hc, Ac = i.calibrateTAF(eTarget=E_target, frameCompliance = frameCompliance, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, plotTip=False, returnArea=True, critDepthTip=minhc_Tip, critMaxDepthTip=maxhc_Tip) #pylint: disable=line-too-long
  elif Index_CalculationMethod == 1: # assume constant Modulus but neglect Pile-up (Eq.(22), Oliver 2004)
    i.output['ax'] = [None, None]
    #open waiting dialog
    self.show_wait('Iterative calculation is being performed')
    i.calibrate_TAF_and_FrameStiffness_iterativeMethod(eTarget=E_target, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness, critDepthTip=minhc_Tip,critMaxDepthTip=maxhc_Tip) # pylint: disable=line-too-long
    #close waiting dialog
    self.close_wait()
    i.output['ax'] = self.static_ax_FrameStiffness_tabTAF
    i.calibrateStiffness_OneIteration(eTarget=E_target, critDepth=critDepthStiffness, critMaxDepth=maxhc_Tip, critForce=critForceStiffness, plotStiffness=False)
    hc, Ac = i.calibrateTAF(eTarget=E_target, frameCompliance = i.tip.compliance, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, plotTip=False, returnArea=True, critDepthTip=minhc_Tip, critMaxDepthTip=maxhc_Tip) # pylint: disable=line-too-long
  i.model['driftRate'] = False   #reset
  self.static_canvas_FrameStiffness_tabTAF.figure.set_tight_layout(True)
  i.output['ax'] = [None, None]
  self.static_canvas_FrameStiffness_tabTAF.draw()
  #open waiting dialog
  self.show_wait('GUI is plotting results!')
  #plot the calibrated tip area funcitonS
  self.plot_TAF(hc,Ac)
  #listing Test
  tableWidget=self.ui.tableWidget_tabTAF
  tableWidget.setRowCount(len(OriginalAlltest))
  k_frameCompliance_collect=0
  for k, theTest in enumerate(OriginalAlltest):
    qtablewidgetitem=QTableWidgetItem(theTest)
    if theTest in i.allTestList:
      try:
        tableWidget.setItem(k,3,QTableWidgetItem(f"{frameCompliance_collect[k_frameCompliance_collect]:.10f}"))
      except:
        tableWidget.setItem(k,3,QTableWidgetItem('None'))
      k_frameCompliance_collect += 1
      qtablewidgetitem.setCheckState(Qt.Checked)
    else:
      tableWidget.setItem(k,3,QTableWidgetItem('None'))
      qtablewidgetitem.setCheckState(Qt.Unchecked)
    tableWidget.setItem(k,0,qtablewidgetitem)
    if theTest in i.output['successTest']:
      tableWidget.setItem(k,1,QTableWidgetItem("Yes"))
    else:
      tableWidget.setItem(k,1,QTableWidgetItem("No"))
  #output: calibrated frame compliance and frame stiffness
  self.ui.lineEdit_FrameCompliance_tabTAF.setText(f"{i.tip.compliance:.10f}")
  self.ui.lineEdit_FrameStiffness_tabTAF.setText(f"{(1/i.tip.compliance):.10f}")
  #output: terms of the calibrated tip area function
  for j in range(9):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTAF") # pylint: disable = eval-used
    lineEdit.setText("0")
  for j in range(number_of_TAFterms):
    lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_tabTAF") # pylint: disable = eval-used
    lineEdit.setText(f"{i.tip.prefactors[j]:.10f}")
  #select the test 1 and run plot load-depth curve
  item = self.ui.tableWidget_tabTAF.item(0, 0)
  self.ui.tableWidget_tabTAF.setCurrentItem(item)
  self.plot_load_depth(tabName='tabTAF')
  #close waiting dialog
  self.close_wait(info='Calculation of Tip Area Function is finished!')
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
  ax[0].plot(hc_new,Ac_new,color='r',label='the fitted Tip Area Function')
  ax[0].set_ylabel(r"Contact Area $A_{c}$ [µm$^2$]")
  if self.ui.checkBox_plotReferenceTAF_tabTAF.isChecked():
    Reference_TAF_terms =[]
    for j in range(9):
      lineEdit = eval(f"self.ui.lineEdit_TAF{j+1}_2_tabTAF") # pylint: disable=eval-used
      Reference_TAF_terms.append(float(lineEdit.text()))
    Ac_reference = (
                    Reference_TAF_terms[0] * (hc_new*1000) ** (2/2**0) + Reference_TAF_terms[1] * (hc_new*1000) ** (2/2**1) +
                    Reference_TAF_terms[2] * (hc_new*1000) ** (2/2**2) + Reference_TAF_terms[3] * (hc_new*1000) ** (2/2**3) +
                    Reference_TAF_terms[4] * (hc_new*1000) ** (2/2**4) + Reference_TAF_terms[5] * (hc_new*1000) ** (2/2**5) +
                    Reference_TAF_terms[6] * (hc_new*1000) ** (2/2**6) + Reference_TAF_terms[7] * (hc_new*1000) ** (2/2**7) +
                    Reference_TAF_terms[8] * (hc_new*1000) ** (2/2**8)
                    )/1.e6 # conversion of unit from nm^2 to um^2
    ax[0].plot(hc_new,Ac_reference,color='gray',linestyle='dashed', label='teh reference Tip Area Function')
  ax[0].legend()
  Ac_cal = self.i_tabTAF.tip.areaFunction(hc)
  error = (Ac_cal - Ac) / Ac *100
  ax[1].scatter(hc, error, color='grey',s=5)
  ax[1].axhline(0, linestyle='dashdot', color='tab:orange')
  ax[1].set_ylabel(r"$\frac{{\rm fitted} A_{c}-{\rm meas.} A_{c}}{{\rm meas.} A_{c}}x100$ [%]")
  ax[1].set_xlabel(r"Contact Depth $h_{c}$ [µm]")
  self.static_canvas_TAF_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_TAF_tabTAF.draw()
