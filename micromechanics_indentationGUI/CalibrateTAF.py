#pylint: disable=possibly-used-before-assignment, used-before-assignment

""" Graphical user interface to calibrate tip area function """
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic
from micromechanics import indentation
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QApplication, QTableWidgetItem # pylint: disable=no-name-in-module
from .WaitingUpgrade_of_micromechanics import IndentationXXX
from .Tools4LoadingData import read_file_list, Convert2inGUI
from .load_depth import pick
from .Tools_for_GUI.draggable_smooth_bars import DraggableSmoothBars

def click_OK_calibration(self): #pylint: disable=too-many-locals
  """ Graphical user interface to calibrate tip area function """
  #close opened HDF5 file
  try:
    self.i_tabTAF.datafile.close()
  except:
    pass
  #
  errors=""
  suggestions=""
  #set Progress Bar
  self.ui.progressBar_tabTAF.setValue(0)
  #Reading Inputs
  fileNameList = read_file_list(self.ui.tableWidget_path_tabTAF)
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
  try:
    print(fileNameList)
    fileName = Convert2inGUI(fileNameList)
  except:
    pass
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
    correctDrift_Post = self.ui.checkBox_UsingDriftUnloading_tabTAF.isChecked()
  except:
    correctDrift_Post = False
  try:
    correctDrift_Pre = self.ui.checkBox_UsingDriftPre_tabTAF.isChecked()
  except:
    correctDrift_Pre = False
  if correctDrift_Post and correctDrift_Pre:
    correctDrift = 3
  elif correctDrift_Post:
    correctDrift = 1
  elif correctDrift_Pre:
    correctDrift = 2
  else:
    correctDrift = 0
  i.model['driftRate'] = correctDrift
  Range_correctDrift_Post = self.ui.doubleSpinBox_UsingDriftUnloading_tabTAF.value()
  Range_correctDrift_Pre = self.ui.doubleSpinBox_UsingDriftPre_tabTAF.value()
  i.model['Range_PostDrift'] = Range_correctDrift_Post
  i.model['Range_PreDrift'] = Range_correctDrift_Pre
  #changing i.allTestList to calculate using the checked tests
  try:
    OriginalAlltest = list(i.allTestList)
  except Exception as e: #pylint: disable=broad-except
    suggestion = 'Check if the Path is completed. \n A correct example: C:\G200X\\20230101\Example.xlsx' #pylint: disable=anomalous-backslash-in-string
    errors=f"{errors}\n\n{e}"
    suggestions=f"{suggestions}\n\n{suggestion}"
    self.show_error(str(errors), suggestions)
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
  critMinDepthStiffness=self.ui.doubleSpinBox_critDepthStiffness_tabTAF.value()
  critMaxDepthStiffness=self.ui.doubleSpinBox_critMaxDepthStiffness_tabTAF.value()
  critDepthStiffness = (critMinDepthStiffness,critMaxDepthStiffness)
  critMinForceStiffness=self.ui.doubleSpinBox_critForceStiffness_tabTAF.value()
  critMaxForceStiffness=self.ui.doubleSpinBox_critMaxForceStiffness_tabTAF.value()
  critForceStiffness = (critMinForceStiffness,critMaxForceStiffness)
  if Index_TipType==0:
    TipType='Berkovich'
  elif Index_TipType==1:
    TipType='Sphere'
  elif Index_TipType==2:
    TipType='Sphere+Cone'
  frameCompliance_collect = None
  if Index_CalculationMethod == 0: # assume constant Hardness and Modulus (Eq.(24), Oliver 2004)
    i.restartFile()
    try:
      _, _, frameCompliance_collect = i.calibrateStiffness(critDepths=critDepthStiffness, critForces=critForceStiffness, plotStiffness=False, returnData=True)
    except Exception as e: #pylint: disable=broad-except
      suggestion = 'Remove poor-quality data' #pylint: disable=anomalous-backslash-in-string
      errors=f"{errors}\n\n{e}"
      suggestions=f"{suggestions}\n\n{suggestion}"
      self.show_error(str(errors), suggestions)
    else:
      frameCompliance = i.tip.compliance
    try:
      hc, Ac = i.calibrateTAF(eTarget=E_target, frameCompliance = frameCompliance, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, plotTip=False, returnArea=True, critDepthTip=minhc_Tip, critMaxDepthTip=maxhc_Tip) #pylint: disable=line-too-long
    except Exception as e: #pylint: disable=broad-except
      suggestion = 'Remove poor-quality data' #pylint: disable=anomalous-backslash-in-string
      errors=f"{errors}\n\n{e}"
      suggestions=f"{suggestions}\n\n{suggestion}"
      self.show_error(str(errors), suggestions)
  elif Index_CalculationMethod == 1: # assume constant Modulus but neglect Pile-up (Eq.(22), Oliver 2004)
    i.output['ax'] = [None, None]
    #open waiting dialog
    self.show_wait('Iterative calculation is being performed')
    i.calibrate_TAF_and_FrameStiffness_iterativeMethod(eTarget=E_target, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, critDepthStiffness=critDepthStiffness, critForceStiffness=critForceStiffness, critDepthTip=minhc_Tip,critMaxDepthTip=maxhc_Tip) # pylint: disable=line-too-long
    #close waiting dialog
    self.close_wait()
    i.output['ax'] = self.static_ax_FrameStiffness_tabTAF
    i.calibrateStiffness_OneIteration(eTarget=E_target, critDepths=critDepthStiffness, critForces=critForceStiffness, plotStiffness=False)
    hc, Ac = i.calibrateTAF(eTarget=E_target, frameCompliance = i.tip.compliance, TipType=TipType, Radius_Sphere=Radius_Sphere, half_includedAngel_Cone = half_includedAngle_Cone, numPolynomial=number_of_TAFterms, plotTip=False, returnArea=True, critDepthTip=minhc_Tip, critMaxDepthTip=maxhc_Tip) # pylint: disable=line-too-long
  i.model['driftRate'] = False   #reset
  self.static_canvas_FrameStiffness_tabTAF.figure.set_tight_layout(True)
  i.output['ax'] = [None, None]
  self.static_canvas_FrameStiffness_tabTAF.draw()
  #open waiting dialog
  self.show_wait('GUI is plotting results!')
  #plot the calibrated tip area funcitonS
  DepthStep4UniformDepth = 0.01
  if i.method!=indentation.definitions.Method.CSM: DepthStep4UniformDepth = 0
  try:
    self.plot_TAF(hc,Ac,DepthStep4UniformDepth=DepthStep4UniformDepth)
  except Exception as e: #pylint: disable=broad-except
    suggestion = 'Cannot plot hc-Ac' #pylint: disable=anomalous-backslash-in-string
    errors=f"{errors}\n\n{e}"
    suggestions=f"{suggestions}\n\n{suggestion}"
    self.show_error(str(errors), suggestions)
  try:
    self.plot_Hardness_Modulus_tabTAF(min_hc=minhc_Tip, max_hc=maxhc_Tip)
  except Exception as e: #pylint: disable=broad-except
    suggestion = "Cannot plot hardness and Young's modulus"
    errors=f"{errors}\n\n{e}"
    suggestions=f"{suggestions}\n\n{suggestion}"
    self.show_error(str(errors), suggestions)
  try:
    self.plot_weight_tabTAF()
  except Exception as e: #pylint: disable=broad-except
    suggestion = "Cannot plot TAF weight w"
    errors=f"{errors}\n\n{e}"
    suggestions=f"{suggestions}\n\n{suggestion}"
    self.show_error(str(errors), suggestions)
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
  self.plot_load_depth(tabName='tabTAF',SimplePlot=True)
  #close waiting dialog
  self.close_wait(info='Calculation of Tip Area Function is finished!')

def plot_TAF(self,hc,Ac,DepthStep4UniformDepth = 0.01):
  """
  to plot the calibrated tip area function

  Args:
    hc (float): contact depth [µm]
    Ac (float): contact area [µm2]
    DepthStepUniformDepth (float): depth step size to make the Ac-hc data uniform along hc
  """
  ax = self.static_ax_TAF_tabTAF
  ax[0].cla()
  ax[1].cla()
  ax[0].scatter(hc,Ac,color='b',label='data',zorder=1)
  if DepthStep4UniformDepth>0:
    bins_ = int((np.max(hc)-np.min(hc))/DepthStep4UniformDepth)
    Ac_mean, bin_edges, _ = binned_statistic(hc, Ac, statistic="mean", bins=bins_)
    Ac_mean = Ac_mean[:-1]
    bin_edges = bin_edges[:-1]
    hc_bin_center = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    ax[0].scatter(hc_bin_center,Ac_mean,color='orange',label=f"data averaged at intervals of {DepthStep4UniformDepth*1000} nm in hc",zorder=2)
  hc_new = np.arange(0,hc.max()*1.05,hc.max()/100)
  Ac_new = self.i_tabTAF.tip.areaFunction(hc_new)
  ax[0].plot(hc_new,Ac_new,color='r',label='the fitted Tip Area Function',zorder=3)
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
    ax[0].plot(hc_new,Ac_reference,color='gray',linestyle='dashed', label='the reference Tip Area Function',zorder=3)
  ax[0].legend()
  Ac_cal = self.i_tabTAF.tip.areaFunction(hc)
  error = (Ac_cal - Ac) / Ac *100
  ax[1].scatter(hc, error, color='grey',s=5)
  ax[1].set_ylim((-15,15))
  ax[1].axhline(0, linestyle='dashdot', color='tab:orange')
  ax[1].set_ylabel(r"$\frac{{\rm fitted} A_{c}-{\rm meas.} A_{c}}{{\rm meas.} A_{c}}x100$ [%]")
  ax[1].set_xlabel(r"Contact Depth $h_{c}$ [µm]")
  self.static_canvas_TAF_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_TAF_tabTAF.draw()


def plot_Hardness_Modulus_tabTAF(self, min_hc=None, max_hc=None):
  """Plot hardness and modulus in tabTAF using tabHE-style plotting parameters."""
  i = self.i_tabTAF
  ax_H_hc = self.static_ax_H_hc_tabTAF
  ax_H_h = self.static_ax_H_h_tabTAF
  ax_E_hc = self.static_ax_E_hc_tabTAF
  ax_E_h = self.static_ax_E_h_tabTAF
  ax_H_hc.cla()
  ax_H_h.cla()
  ax_E_hc.cla()
  ax_E_h.cla()
  hc_collect = []
  H_collect = []
  E_collect = []
  H4ylim_collect = []
  E4ylim_collect = []
  Hmean_collect = []
  Hstd_collect = []
  H4mean_collect = []
  Emean_collect = []
  Estd_collect = []
  E4mean_collect = []
  marker4mean = np.array([], dtype=int)
  decrease_data_density = 1
  i.restartFile()
  while True:
    i.analyse()
    QApplication.processEvents()
    hc_collect.append(i.hc)
    H_collect.append(i.hardness)
    E_collect.append(i.modulus)
    marker4ylim = np.where(i.hc > 0.05)[0]
    if len(marker4ylim) == 0:
      marker4ylim = np.arange(len(i.hc))
    H4ylim_collect.append(i.hardness[marker4ylim])
    E4ylim_collect.append(i.modulus[marker4ylim])
    if min_hc is None or max_hc is None or max_hc <= min_hc:
      marker4mean = np.arange(len(i.hc))
    else:
      marker4mean = np.where((i.hc >= min_hc) & (i.hc <= max_hc))[0]
      if len(marker4mean) == 0:
        marker4mean = np.arange(len(i.hc))
    Hmean_collect.append(np.mean(i.hardness[marker4mean]))
    H4mean_collect.append(i.hardness[marker4mean])
    Emean_collect.append(np.mean(i.modulus[marker4mean]))
    E4mean_collect.append(i.modulus[marker4mean])
    if len(i.hardness[marker4mean]) > 1:
      Hstd_collect.append(np.std(i.hardness[marker4mean], ddof=1))
      Estd_collect.append(np.std(i.modulus[marker4mean], ddof=1))
    else:
      Hstd_collect.append(0)
      Estd_collect.append(0)
    if i.method == indentation.definitions.Method.CSM:
      ax_H_hc.plot(i.hc[::decrease_data_density], i.hardness[::decrease_data_density], '-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
      ax_H_h.plot(i.h[i.valid][::decrease_data_density], i.hardness[::decrease_data_density], '-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
      ax_E_hc.plot(i.hc[::decrease_data_density], i.modulus[::decrease_data_density], '-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
      ax_E_h.plot(i.h[i.valid][::decrease_data_density], i.modulus[::decrease_data_density], '-', linewidth=1, alpha=0.8, picker=True, label=i.testName)
    else:
      ax_H_hc.plot(i.hc[::decrease_data_density], i.hardness[::decrease_data_density], '.-', linewidth=1, picker=True, label=i.testName)
      ax_H_h.plot(i.h[i.valid][::decrease_data_density], i.hardness[::decrease_data_density], '.-', linewidth=1, picker=True, label=i.testName)
      ax_E_hc.plot(i.hc[::decrease_data_density], i.modulus[::decrease_data_density], '.-', linewidth=1, picker=True, label=i.testName)
      ax_E_h.plot(i.h[i.valid][::decrease_data_density], i.modulus[::decrease_data_density], '.-', linewidth=1, picker=True, label=i.testName)
    if not i.testList:
      break
    i.nextTest()
  # if hc_collect and len(marker4mean) > 0:
  #   ax_H_hc.axvline(i.hc[marker4mean][0], color='gray', linestyle='dashed', label='min./max. hc for calculating mean values')
  #   ax_E_hc.axvline(i.hc[marker4mean][0], color='gray', linestyle='dashed', label='min./max. hc for calculating mean values')
  #   if np.max(hc_collect[0])*1.1 > i.hc[marker4mean][-1]:
  #     ax_H_hc.axvline(i.hc[marker4mean][-1], color='gray', linestyle='dashed')
  #     ax_E_hc.axvline(i.hc[marker4mean][-1], color='gray', linestyle='dashed')
  try:
    H4ylim_all = np.hstack(H4ylim_collect)
    E4ylim_all = np.hstack(E4ylim_collect)
    Hstd_limited = min(np.std(H4ylim_all, ddof=1), 1)
    Estd_limited = min(np.std(E4ylim_all, ddof=1), 10)
    Hmean_ylim = np.mean(H4ylim_all)
    Emean_ylim = np.mean(E4ylim_all)
    ax_H_hc.set_ylim(Hmean_ylim-Hstd_limited*20, Hmean_ylim+Hstd_limited*20)
    ax_H_h.set_ylim(Hmean_ylim-Hstd_limited*20, Hmean_ylim+Hstd_limited*20)
    ax_E_hc.set_ylim(Emean_ylim-Estd_limited*20, Emean_ylim+Estd_limited*20)
    ax_E_h.set_ylim(Emean_ylim-Estd_limited*20, Emean_ylim+Estd_limited*20)
  except Exception:
    pass
  if len(H_collect) < 10:
    ax_H_hc.legend()
    ax_E_hc.legend()
  self.static_canvas_H_hc_tabTAF.figure.canvas.mpl_connect("pick_event", pick)
  self.static_canvas_E_hc_tabTAF.figure.canvas.mpl_connect("pick_event", pick)
  ax_H_hc.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_H_hc.set_xlabel('Contact depth [µm]')
  ax_H_hc.set_ylabel('Hardness [GPa]')
  ax_H_h.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_H_h.set_xlabel('Depth [µm]')
  ax_H_h.set_ylabel('Hardness [GPa]')
  ax_E_hc.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_E_hc.set_xlabel('Contact depth [µm]')
  ax_E_hc.set_ylabel("Young's Modulus [GPa]")
  ax_E_h.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  ax_E_h.set_xlabel('Depth [µm]')
  ax_E_h.set_ylabel("Young's Modulus [GPa]")
  self.static_canvas_H_hc_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_H_h_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_E_hc_tabTAF.figure.set_tight_layout(True)
  self.static_canvas_E_h_tabTAF.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_H_hc)
  self.set_aspectRatio(ax=ax_H_h)
  self.set_aspectRatio(ax=ax_E_hc)
  self.set_aspectRatio(ax=ax_E_h)
  self.static_canvas_H_hc_tabTAF.draw()
  self.static_canvas_H_h_tabTAF.draw()
  self.static_canvas_E_hc_tabTAF.draw()
  self.static_canvas_E_h_tabTAF.draw()
  i.restartFile()


def plot_weight_tabTAF(self):
  """Plot the TAF fitting weight w in an interactive draggable view."""
  i = self.i_tabTAF
  ax = self.static_ax_w_tabTAF
  ax.cla()
  weight_data = getattr(i, 'taf_weight_data', None)
  if not weight_data:
    ax.text(0.5, 0.5, 'No TAF weight data available', ha='center', va='center', transform=ax.transAxes)
    self.static_canvas_w_tabTAF.draw()
    return
  hc = np.asarray(weight_data.get('hc', []), dtype=float)
  w = np.asarray(weight_data.get('w', []), dtype=float)
  if len(hc) == 0 or len(w) == 0:
    ax.text(0.5, 0.5, 'No TAF weight data available', ha='center', va='center', transform=ax.transAxes)
    self.static_canvas_w_tabTAF.draw()
    return
  previous_editor = getattr(self, 'taf_weight_editor', None)
  if previous_editor is not None:
    previous_editor.disconnect()
  self.taf_weight_editor = DraggableSmoothBars(
    ax=ax,
    x_values=hc,
    heights=w,
    influence_width=max((np.max(hc) - np.min(hc)) / 10.0, 1e-6),
    title='TAF fitting weight w',
    x_label='Contact depth for fit [µm]',
    y_label='Weight w',
  )
  ax.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.7)
  self.static_canvas_w_tabTAF.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax)
  self.static_canvas_w_tabTAF.draw()
  self.taf_weight_editor.original_position = ax.get_position().frozen()
  toolbar = getattr(self, 'static_toolbar_w_tabTAF', None)
  if toolbar is not None:
    toolbar._taf_weight_editor = self.taf_weight_editor
    toolbar._taf_weight_canvas = self.static_canvas_w_tabTAF
    if not getattr(toolbar, '_taf_weight_home_installed', False):
      original_home = toolbar.home
      def _taf_weight_home(*args, **kwargs):
        editor = getattr(toolbar, '_taf_weight_editor', None)
        canvas = getattr(toolbar, '_taf_weight_canvas', None)
        if editor is None or canvas is None:
          return original_home(*args, **kwargs)
        callbacks = getattr(editor.ax, 'callbacks', None)
        x_callbacks = None
        y_callbacks = None
        if callbacks is not None and hasattr(callbacks, 'callbacks'):
          x_callbacks = list(callbacks.callbacks.get('xlim_changed', {}).items())
          y_callbacks = list(callbacks.callbacks.get('ylim_changed', {}).items())
          for cid, _ in x_callbacks:
            editor.ax.callbacks.disconnect(cid)
          for cid, _ in y_callbacks:
            editor.ax.callbacks.disconnect(cid)
        try:
          editor.ax.set_aspect('auto')
          editor.ax.set_position(editor.original_position, which='both')
          editor.ax.set_xlim(editor.original_xlim)
          editor.ax.set_ylim(editor.original_ylim)
          editor.ax.set_aspect(abs((editor.original_xlim[1]-editor.original_xlim[0])/(editor.original_ylim[0]-editor.original_ylim[1]))*0.618)
        finally:
          if x_callbacks is not None:
            for cid, func in x_callbacks:
              editor.ax.callbacks.connect('xlim_changed', func)
          if y_callbacks is not None:
            for cid, func in y_callbacks:
              editor.ax.callbacks.connect('ylim_changed', func)
        canvas.draw_idle()
      toolbar.home = _taf_weight_home
      toolbar._taf_weight_home_installed = True
